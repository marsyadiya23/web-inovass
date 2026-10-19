<?php

namespace Database\Seeders;

use App\Models\PageContent;
use Illuminate\Database\Seeder;

/** Konten Beranda (PageContent 'home'), teks asli dari inovass.com. */
class HomeSeeder extends Seeder
{
    public function run(): void
    {
        $card = fn ($icon, $title, $text) => compact('icon', 'title', 'text');

        PageContent::put('home', [
            'meta_description' => 'INOVASS — konsultan ISO, pelatihan, akreditasi, dan solusi digital. Kami wujudkan ide dan peluang menjadi inovasi nyata yang berdampak dan berkelanjutan.',
            'hero' => [
                'eyebrow' => 'Innovate To Elevate',
                'title' => 'The Maker of Innovation',
                'title_em' => 'to be Comes True',
                'description' => 'Kami wujudkan ide dan peluang menjadi inovasi nyata yang berdampak dan berkelanjutan',
                'image' => 'legacy/wallpaper 3.png',
                'button_label' => 'Explore Now',
                'button_url' => '#tentang',
            ],
            'about' => [
                'eyebrow' => 'TENTANG KAMI',
                'title' => 'Mitra Konsultasi ISO dan Transformasi Digital',
                'title_em' => 'untuk Organisasi yang Terus Bertumbuh',
                'text' => 'INOVASS menghadirkan layanan konsultasi ISO, pelatihan, audit, pengembangan sistem, dan solusi digital untuk membantu organisasi meningkatkan kinerja, memastikan kepatuhan, serta mempercepat transformasi menuju standar kelas dunia.',
                'button_label' => 'Pelajari Lebih Lanjut →',
                'button_url' => '/tentang.html',
                'stats' => [
                    ['number' => 20, 'suffix' => '+', 'label' => 'Tahun Pengalaman'],
                    ['number' => 200, 'suffix' => '+', 'label' => 'Organisasi'],
                    ['number' => 500, 'suffix' => '+', 'label' => 'Program Pelatihan'],
                    ['number' => 10000, 'suffix' => '+', 'label' => 'Peserta'],
                ],
                'values' => [
                    ['icon' => 'legacy/image1.png', 'title' => 'Inovasi Berkelanjutan', 'text' => 'Mendorong organisasi beradaptasi melalui solusi ISO dan transformasi digital yang inovatif.'],
                    ['icon' => 'legacy/image2.png', 'title' => 'Kemitraan Strategis', 'text' => 'Menjadi mitra terpercaya yang mendampingi pertumbuhan organisasi dari perencanaan hingga implementasi.'],
                    ['icon' => 'legacy/image3.png', 'title' => 'Implementasi Efektif', 'text' => 'Setiap solusi dijalankan dengan pendekatan terstruktur, transparan, dan berorientasi pada hasil yang terukur.'],
                    ['icon' => 'legacy/image4.png', 'title' => 'Nilai Jangka Panjang', 'text' => 'Menciptakan peningkatan kinerja, kepatuhan, dan daya saing yang memberikan manfaat berkelanjutan bagi organisasi.'],
                ],
            ],
            'clients' => ['label' => 'Telah mendampingi berbagai perusahaan'],
            'services' => [
                'eyebrow' => 'LAYANAN KAMI',
                'title' => 'Solusi Lengkap untuk',
                'title_em' => 'Pertumbuhan Organisasi',
                'button_label' => 'Lihat Semua Layanan',
                'button_url' => '/layanan/sertifikasi-organisasi/index.html',
                'cards' => [
                    ['title' => 'Konsultasi & Sertifikasi ISO', 'text' => 'Pendampingan implementasi, penyusunan dokumen, audit internal, hingga persiapan sertifikasi ISO.', 'image' => 'legacy/Konsultasi & Sertifikasi ISO.jpeg', 'url' => '/layanan/sertifikasi-organisasi/index.html', 'link_label' => 'Pelajari Layanan →'],
                    ['title' => 'Konsultasi Akreditasi', 'text' => 'Pendampingan akreditasi laboratorium, lembaga inspeksi, LSP, dan LSPro sesuai standar yang berlaku.', 'image' => 'legacy/Konsultasi Akreditasi.jpeg', 'url' => '/layanan/akreditasi-organisasi/index.html', 'link_label' => 'Pelajari Layanan →'],
                    ['title' => 'Pelatihan Profesional', 'text' => 'Program Public Training, In House Training, Executive Training, dan Private Training berbasis standar ISO.', 'image' => 'legacy/Pelatihan Profesional.jpeg', 'url' => '/layanan/pelatihan-sertifikasi/index.html', 'link_label' => 'Pelajari Layanan →'],
                    ['title' => 'Sertifikasi Kompetensi', 'text' => 'Program sertifikasi kompetensi personel pada bidang mutu, K3, lingkungan, laboratorium, dan bidang terkait.', 'image' => 'legacy/Sertifikasi Kompetensi.jpeg', 'url' => '/layanan/pelatihan-akreditasi/index.html', 'link_label' => 'Pelajari Layanan →'],
                ],
            ],
            'products' => [
                'eyebrow' => 'PRODUK KAMI',
                'title' => 'Solusi Digital',
                'title_em' => 'Berbasis Teknologi',
                'subtitle' => 'Aplikasi dan platform yang kami kembangkan untuk mendukung pengelolaan sistem manajemen secara modern dan efisien.',
            ],
            'training' => [
                'eyebrow' => 'BIDANG PELATIHAN',
                'title' => 'Pelatihan untuk',
                'title_em' => 'Berbagai Bidang',
                'button_label' => 'Lihat Semua Pelatihan',
                'button_url' => '/layanan/pelatihan-sertifikasi/index.html',
                'cards' => [
                    $card('mutu', 'Sistem Manajemen Mutu', 'ISO 9001 dan penerapan QMS untuk berbagai sektor industri'),
                    $card('k3', 'Keselamatan & Kesehatan Kerja', 'ISO 45001 dan SMK3 untuk lingkungan kerja yang aman'),
                    $card('lingkungan', 'Manajemen Lingkungan', 'ISO 14001 untuk pengelolaan dampak lingkungan organisasi'),
                    $card('lab', 'Laboratorium & Pengujian', 'ISO/IEC 17025 untuk akreditasi laboratorium pengujian'),
                    $card('keamanan', 'Keamanan Informasi', 'ISO 27001 untuk perlindungan aset informasi organisasi'),
                    $card('energi', 'Manajemen Energi', 'ISO 50001 untuk efisiensi dan kinerja energi organisasi'),
                ],
            ],
            'why' => [
                'eyebrow' => 'KEUNGGULAN KAMI',
                'title' => 'Mengapa Memilih',
                'title_em' => 'INOVASS?',
                'description' => 'Dengan pengalaman lebih dari 20 tahun, INOVASS telah membuktikan komitmen dalam mendampingi ratusan organisasi meraih standar internasional.',
                'cards' => [
                    $card('orang', 'Konsultan Berpengalaman', 'Tim konsultan bersertifikasi internasional dengan rekam jejak lebih dari 20 tahun'),
                    $card('daftar', 'Pendekatan Terstruktur', 'Metodologi kerja yang sistematis dari analisis hingga implementasi dan sertifikasi'),
                    $card('grid', 'Solusi Terintegrasi', 'Layanan lengkap dari konsultasi, pelatihan, audit, hingga pengembangan sistem digital'),
                    $card('jaringan', 'Jaringan Luas', 'Didukung jaringan mitra lembaga sertifikasi dan akreditasi terpercaya di Indonesia'),
                ],
            ],
            'process' => [
                'eyebrow' => 'BAGAIMANA KAMI BEKERJA',
                'title' => 'Proses Kerja Kami',
                'steps' => [
                    ['title' => 'Konsultasi Awal', 'text' => 'Identifikasi kebutuhan, ruang lingkup, dan tujuan organisasi'],
                    ['title' => 'Gap Analysis', 'text' => 'Penilaian kesenjangan antara kondisi saat ini dan persyaratan standar'],
                    ['title' => 'Implementasi', 'text' => 'Pendampingan penyusunan sistem, dokumentasi, dan pelatihan tim'],
                    ['title' => 'Sertifikasi', 'text' => 'Pendampingan audit sertifikasi hingga organisasi meraih sertifikat'],
                ],
            ],
            'news' => ['eyebrow' => 'BERITA & INSIGHT', 'title' => 'Update Terbaru dari INOVASS'],
            'testimonials' => ['eyebrow' => 'TESTIMONI', 'title' => 'Apa Kata Klien Kami'],
            'faq' => ['eyebrow' => 'FAQ', 'title' => 'Pertanyaan yang Sering Diajukan'],
            'cta' => [
                'title' => 'Mulai Perjalanan Sertifikasi Anda',
                'title_em' => 'Bersama INOVASS',
                'text' => 'Konsultasikan kebutuhan organisasi Anda secara gratis. Tim ahli kami siap membantu merancang solusi yang tepat.',
                'primary_label' => 'Konsultasi Gratis',
                'primary_url' => '/kontak.html',
                'secondary_label' => 'Lihat Layanan Kami',
                'secondary_url' => '/layanan/sertifikasi-organisasi/index.html',
            ],
        ]);
    }
}
