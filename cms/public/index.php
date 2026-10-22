<?php

use Illuminate\Foundation\Application;
use Illuminate\Http\Request;

define('LARAVEL_START', microtime(true));

// Folder aplikasi: lokal = satu tingkat di atas public/. Di cPanel, public/ ada di
// public_html/inovass/public dan aplikasinya di /home/{user}/inovass (di luar folder publik).
$base = is_file(__DIR__.'/../vendor/autoload.php') ? __DIR__.'/..' : __DIR__.'/../../../inovass';

// Determine if the application is in maintenance mode...
if (file_exists($maintenance = $base.'/storage/framework/maintenance.php')) {
    require $maintenance;
}

// Register the Composer autoloader...
require $base.'/vendor/autoload.php';

// Bootstrap Laravel and handle the request...
/** @var Application $app */
$app = require_once $base.'/bootstrap/app.php';
$app->usePublicPath(__DIR__); // upload admin (public/uploads) harus jatuh di folder yang dilayani web

$app->handleRequest(Request::capture());
