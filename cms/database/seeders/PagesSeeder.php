<?php

namespace Database\Seeders;

use App\Models\PageContent;
use App\Models\Product;
use Illuminate\Database\Seeder;

/** Konten asli tentang.html, produk.html, kontak.html + produk InoSys & InoLab. */
class PagesSeeder extends Seeder
{
    public function run(): void
    {
        PageContent::put('tentang', [
            'hero_title' => 'Tentang',
            'hero_em' => 'Kami',
            'hero_desc' => 'Inovass hadir sebagai mitra strategis yang mengubah tantangan organisasi menjadi peluang melalui solusi konsultasi, inovasi, dan penerapan standar internasional yang berkelanjutan',
            'hero_image' => 'legacy/hero tentang kami.png',
            'profile_title' => 'Mitra Strategis',
            'profile_em' => 'untuk Standar Internasional',
            'profile_text' => "INOVASS adalah lembaga konsultan yang berdedikasi dalam memberikan layanan konsultasi, sertifikasi ISO, akreditasi, pelatihan profesional, dan pengembangan solusi digital untuk berbagai sektor industri di Indonesia dengan menempatkan keunggulan dan kepatuhan pada standar Nasional maupun Internasional.\nKami memiliki komitmen yang kuat untuk memastikan bahwa sistem manajemen organisasi memenuhi standar kualitas terbaik. Tim kami yang berpengalaman siap mendampingi organisasi Anda mencapai standar kelas dunia melalui pendekatan terstruktur dan terukur.",
            'profile_image' => 'legacy/investment-valuable.jpeg',
            'stats' => [
                ['number' => '20+', 'label' => 'Tahun Pengalaman'],
                ['number' => '200+', 'label' => 'Organisasi'],
                ['number' => '10.000+', 'label' => 'Peserta Pelatihan'],
            ],
            'visi_title' => 'Visi dan Misi',
            'visi_em' => 'INOVASS',
            'visi' => 'Menjadi lembaga konsultan terkemuka dan terpercaya di Indonesia, yang membantu organisasi mencapai tingkat kualitas layanan, produk, dan sistem manajemen yang dapat bersaing di tingkat Nasional maupun Internasional.',
            'misi' => [
                'Menyediakan layanan konsultasi ISO dan akreditasi dengan pendekatan terstruktur dan terukur',
                'Mengembangkan kompetensi SDM melalui program pelatihan dan sertifikasi profesional',
                'Memberikan solusi digital inovatif untuk meningkatkan efisiensi sistem manajemen',
                'Membangun kemitraan jangka panjang yang berkelanjutan dengan setiap klien',
                'Memastikan kepatuhan standar internasional melalui audit dan pendampingan berkualitas',
            ],
            'visi_image' => 'legacy/layanan kami.jpeg',
            'why_title' => 'Mengapa Memilih',
            'why_em' => 'INOVASS?',
            'why_items' => [
                ['icon' => 'users', 'title' => 'Konsultan Berpengalaman', 'text' => 'Tim konsultan bersertifikasi internasional dengan rekam jejak lebih dari 20 tahun di bidang sistem manajemen dan akreditasi.'],
                ['icon' => 'activity', 'title' => 'Pendekatan Terstruktur', 'text' => 'Metodologi kerja yang sistematis dari analisis kesenjangan, implementasi, hingga sertifikasi dan pemeliharaan berkelanjutan.'],
                ['icon' => 'grid', 'title' => 'Solusi Terintegrasi', 'text' => 'Layanan lengkap dari konsultasi ISO, pelatihan, audit, akreditasi, hingga pengembangan sistem digital manajemen.'],
                ['icon' => 'clock', 'title' => 'Komitmen Jangka Panjang', 'text' => 'Kami tidak hanya membantu organisasi mendapatkan sertifikasi, tetapi juga mendampingi implementasi berkelanjutan.'],
                ['icon' => 'file', 'title' => 'Dokumentasi Lengkap', 'text' => 'Penyusunan dokumen sistem manajemen yang komprehensif dan sesuai dengan persyaratan standar internasional.'],
                ['icon' => 'shield', 'title' => 'Jaringan Luas', 'text' => 'Didukung jaringan mitra lembaga sertifikasi dan akreditasi terpercaya di Indonesia maupun internasional.'],
            ],
            'clients_title' => 'Telah Melayani & Berkolaborasi',
            'clients_em' => 'Dengan',
            'cta_title' => 'Bergabunglah dengan',
            'cta_em' => 'perjalanan kami.',
            'cta_text' => 'Tertarik bekerja sama atau bergabung dengan tim INOVASS? Mari berbicara.',
            'cta_button' => 'Hubungi Kami',
        ]);

        PageContent::put('produk', [
            'hero_title' => 'Produk',
            'hero_em' => 'Kami',
            'hero_desc' => 'Platform digital yang dirancang untuk mendukung implementasi standar ISO, pengelolaan pelatihan, dokumen, audit, dan sistem manajemen organisasi secara modern dan terintegrasi',
            'hero_image' => 'legacy/hero produk kami.png',
            'section_title' => 'Solusi Digital INOVASS',
            'cta_title' => 'Butuh solusi',
            'cta_em' => 'yang lebih spesifik?',
            'cta_text' => 'Kami juga menyediakan layanan custom sesuai kebutuhan bisnis Anda.',
            'cta_button' => 'Diskusikan Kebutuhan Anda',
        ]);

        PageContent::put('kontak', [
            'hero_title' => 'Hubungi',
            'hero_em' => 'Kami',
            'hero_desc' => 'Ada pertanyaan atau proyek yang ingin dibahas? Tim kami siap membantu Anda',
            'hero_image' => 'legacy/hero produk kami.png',
            'title' => 'Mari Wujudkan Solusi Bersama',
            'intro' => 'Terima kasih atas ketertarikan Anda kepada INOVASS. Silakan hubungi kami untuk konsultasi, pertanyaan, atau kebutuhan layanan Anda. Tim kami siap membantu.',
            'subjects' => ['Konsultasi ISO', 'Akreditasi Laboratorium', 'Pelatihan', 'Sertifikasi Kompetensi', 'Produk Digital', 'Lainnya'],
            'map_url' => 'https://www.google.com/maps/embed?pb=!1m17!1m12!1m3!1d3964.432233214819!2d106.83294699999999!3d-6.466800999999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m2!1m1!2zNsKwMjgnMDAuNSJTIDEwNsKwNDknNTguNiJF!5e0!3m2!1sen!2sid!4v1784904375351!5m2!1sen!2sid',
        ]);

        // Situs lama: beranda menyebut InoSys/InoLab, halaman produk menyebut DCS/LMS (tombol "Konsultasikan DCS/LMS").
        // Digabung: nama = InoSys/InoLab, tagline = DCS/LMS, deskripsi dari halaman produk.
        $products = [
            [
                'slug' => 'inosys',
                'name' => 'InoSys',
                'tagline' => 'Document Control System (DCS)',
                'description' => 'Platform digital yang dirancang untuk mengelola dokumen ISO, SOP, kebijakan, instruksi kerja, dan formulir secara terpusat dengan kontrol revisi, persetujuan digital, serta distribusi dokumen yang aman dan terdokumentasi',
                'features' => ['Pengelolaan dokumen terpusat', 'Kontrol revisi & persetujuan digital', 'Audit internal & monitoring ketidaksesuaian', 'Pelaporan sistem manajemen ISO secara real-time'],
                'image' => 'legacy/dcs.png',
                'button_label' => 'Konsultasikan InoSys',
                'sort' => 1,
            ],
            [
                'slug' => 'inolab',
                'name' => 'InoLab',
                'tagline' => 'Learning Management System (LMS)',
                'description' => 'Platform digital yang dirancang untuk mendukung pelatihan ISO, K3, laboratorium, dan pengembangan kompetensi SDM melalui pengelolaan kelas, materi, ujian, sertifikat digital, serta pelaporan hasil pelatihan secara terpusat dan terdokumentasi',
                'features' => ['Pengelolaan kelas & materi pelatihan', 'Ujian & sertifikat digital', 'Pengelolaan dokumen akreditasi laboratorium', 'Pelaporan hasil pelatihan terpusat'],
                'image' => 'legacy/lms.png',
                'button_label' => 'Konsultasikan InoLab',
                'sort' => 2,
            ],
        ];

        foreach ($products as $p) {
            Product::updateOrCreate(['slug' => $p['slug']], $p + ['is_published' => true]);
        }
    }
}
