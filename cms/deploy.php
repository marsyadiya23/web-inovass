<?php

/*
 * Dijalankan cron di server (cPanel tanpa SSH) setelah CI meng-upload release.zip + deploy-pending.
 *   1) ekstrak release.zip ke folder ini (/home/{user}/inovass); .env & isi storage/ tidak ada di zip
 *   2) salin public/ ke ../public_html/inovass/public (document root subdomain, harus di dalam public_html)
 *   3) migrate + optimize (Laravel dijalankan di proses ini: hosting sering memblokir passthru/exec)
 * Cara pasang cron: docs/PANDUAN-DEPLOY.md bagian 3.8.
 */

$app = __DIR__;
$publicDst = dirname($app).'/public_html/inovass/public';
$log = fn (string $m) => print('['.date('c').'] '.$m.PHP_EOL);

// Error apa pun harus tertulis di deploy.log (display_errors di CLI cPanel biasanya mati).
ini_set('display_errors', '1');
error_reporting(E_ALL);

try {
    $zip = new ZipArchive;
    if (! is_file("$app/release.zip") || $zip->open("$app/release.zip", ZipArchive::CHECKCONS) !== true) {
        $log('release.zip hilang atau rusak (upload belum selesai?), dicoba lagi menit berikutnya');
        exit(1);
    }
    if (! $zip->extractTo($app)) {
        $log('gagal mengekstrak release.zip');
        exit(1);
    }
    $zip->close();
    $log('ekstrak OK');

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
    $log('public/ disalin ke '.$publicDst);

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
    $log('deploy selesai');
} catch (Throwable $e) {
    $log('ERROR '.get_class($e).': '.$e->getMessage().' ('.basename($e->getFile()).':'.$e->getLine().')');
    exit(1);
}
