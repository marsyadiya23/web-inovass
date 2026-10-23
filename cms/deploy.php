<?php

/*
 * Dijalankan cron di server (cPanel tanpa SSH) bila ada file deploy-pending (di-upload CI paling akhir).
 * FTP Rumahweb ±5 detik per file, jadi CI meng-upload satu zip per situs, dan skrip ini yang membukanya:
 *   site.zip    (situs statis, dari public/ repo) -> ../public_html
 *   release.zip (CMS Laravel, dari cms/)          -> folder ini, lalu public/ disalin ke
 *               ../public_html/inovass/public, lalu migrate + optimize
 * Zip dihapus setelah berhasil. Zip rusak/setengah ter-upload -> exit 1, cron mencoba lagi menit berikutnya.
 * Cara pasang cron: docs/PANDUAN-DEPLOY.md bagian 3.8.
 */

$app = __DIR__;
$publicHtml = dirname($app).'/public_html';
$log = fn (string $m) => print('['.date('c').'] '.$m.PHP_EOL);

// Error apa pun harus tertulis di deploy.log (display_errors di CLI cPanel biasanya mati).
ini_set('display_errors', '1');
error_reporting(E_ALL);

$extract = function (string $zipFile, string $to) use ($log): void {
    $zip = new ZipArchive;
    if ($zip->open($zipFile, ZipArchive::CHECKCONS) !== true) {
        $log(basename($zipFile).' rusak (upload belum selesai?), dicoba lagi menit berikutnya');
        exit(1);
    }
    if (! $zip->extractTo($to)) {
        $log('gagal mengekstrak '.basename($zipFile));
        exit(1);
    }
    $zip->close();
};

try {
    if (! is_file("$app/site.zip") && ! is_file("$app/release.zip")) {
        $log('tidak ada zip baru, tidak ada yang dikerjakan');
        exit(0);
    }

    if (is_file("$app/site.zip")) {
        $extract("$app/site.zip", $publicHtml);
        unlink("$app/site.zip");
        $log('situs statis diekstrak ke '.$publicHtml);
    }

    if (is_file("$app/release.zip")) {
        $extract("$app/release.zip", $app);
        $log('CMS diekstrak');

        $publicDst = "$publicHtml/inovass/public";
        is_dir($publicDst) || mkdir($publicDst, 0755, true);
        $files = new RecursiveIteratorIterator(
            new RecursiveDirectoryIterator("$app/public", FilesystemIterator::SKIP_DOTS),
            RecursiveIteratorIterator::SELF_FIRST,
        );
        foreach ($files as $f) {
            $to = $publicDst.'/'.$files->getSubPathname();
            if ($f->isDir()) {
                is_dir($to) || mkdir($to, 0755, true);
            } elseif (! copy($f->getPathname(), $to)) {
                $log("gagal menyalin ke $to");
                exit(1);
            }
        }
        $log('public/ CMS disalin ke '.$publicDst);

        // Laravel dijalankan di proses ini: hosting memblokir passthru/exec
        require "$app/vendor/autoload.php";
        $kernel = (require "$app/bootstrap/app.php")->make(Illuminate\Contracts\Console\Kernel::class);
        foreach (['migrate' => ['--force' => true], 'optimize' => []] as $cmd => $args) {
            $code = $kernel->call($cmd, $args);
            echo $kernel->output();
            if ($code !== 0) {
                $log("gagal: artisan $cmd (kode $code)");
                exit($code);
            }
        }
        unlink("$app/release.zip");
    }

    $log('deploy selesai');
} catch (Throwable $e) {
    $log('ERROR '.get_class($e).': '.$e->getMessage().' ('.basename($e->getFile()).':'.$e->getLine().')');
    exit(1);
}
