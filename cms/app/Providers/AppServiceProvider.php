<?php

namespace App\Providers;

use Illuminate\Mail\Markdown;
use Illuminate\Support\ServiceProvider;

class AppServiceProvider extends ServiceProvider
{
    /**
     * Register any application services.
     */
    public function register(): void
    {
        //
    }

    /**
     * Bootstrap any application services.
     */
    public function boot(): void
    {
        // Isian formulir pendaftaran publik masuk ke email (nama, instansi, pesan). Tanpa ini, "[teks](https://...)"
        // menjadi tautan aktif di email resmi INOVASS ke alamat pilihan penyerang (phishing). Format **tebal** tetap jalan.
        Markdown::withSecuredEncoding();
    }
}
