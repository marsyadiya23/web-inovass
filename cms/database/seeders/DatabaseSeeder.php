<?php

namespace Database\Seeders;

use App\Models\PageContent;
use App\Models\User;
use Illuminate\Database\Seeder;

class DatabaseSeeder extends Seeder
{
    public function run(): void
    {
        User::updateOrCreate(
            ['email' => env('ADMIN_EMAIL', 'admin@inovass.com')], // email admin = penerima notifikasi pendaftar
            ['name' => 'Admin INOVASS', 'password' => bcrypt(env('ADMIN_PASSWORD', 'inovass123'))],
        );

        PageContent::put('settings', [
            'site_name' => 'INOVASS',
            'tagline' => 'Inovasi untuk Masa Depan',
            'description' => 'Perusahaan konsultan ISO dan pengembangan solusi digital yang membantu organisasi meningkatkan mutu, efisiensi, dan daya saing.',
            'logo' => null, // kosong = logo bawaan assets/img/logo.png; isian upload admin disimpan di public/uploads
            'address' => "Jl. Danau Melahayu No. 23A\nPesona Telaga Cibinong\nKel. Harapan Jaya, Kec. Cibinong,\nKab. Bogor",
            'phone' => '+62-813-1117-3707',
            'whatsapp' => '6281311173707',
            'show_prices' => false, // harga pelatihan disembunyikan di website; konfirmasi biaya oleh admin
            'email' => 'inovass.adm@gmail.com',
            'socials' => [
                ['platform' => 'instagram', 'url' => ''],
                ['platform' => 'linkedin', 'url' => ''],
                ['platform' => 'youtube', 'url' => ''],
            ],
            'copyright' => '© {tahun} INOVASS. Hak cipta dilindungi undang-undang.',
        ]);

        // Seeder per area konten. Dicek dulu agar urutan pengerjaan tidak saling mengunci.
        foreach (['HomeSeeder', 'PagesSeeder', 'LayananSeeder', 'CollectionsSeeder', 'TrainingSeeder'] as $seeder) {
            if (class_exists($class = __NAMESPACE__.'\\'.$seeder)) {
                $this->call($class);
            }
        }
    }
}
