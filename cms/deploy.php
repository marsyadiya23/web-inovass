<?php

/*
 * Dijalankan cron di server (cPanel tanpa SSH) setelah CI meng-upload release.zip + deploy-pending.
 *   1) ekstrak release.zip ke folder ini (/home/{user}/inovass); .env & isi storage/ tidak ada di zip
 *   2) salin public/ ke ../public_html/inovass/public (document root subdomain, harus di dalam public_html)
 *   3) migrate + optimize
 * Cara pasang cron: docs/PANDUAN-DEPLOY.md bagian 3.8.
 */

$app = __DIR__;
$publicDst = dirname($app).'/public_html/inovass/public';
$log = fn (string $m) => print('['.date('c').'] '.$m.PHP_EOL);

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

foreach (['migrate --force', 'optimize'] as $cmd) {
    passthru(escapeshellarg(PHP_BINARY).' '.escapeshellarg("$app/artisan").' '.$cmd, $code);
    if ($code !== 0) {
        $log("gagal: artisan $cmd");
        exit($code);
    }
}
$log('deploy selesai');
