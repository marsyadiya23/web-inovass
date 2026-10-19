<?php

namespace Database\Seeders;

use App\Models\Article;
use App\Models\Client;
use App\Models\Faq;
use App\Models\Testimonial;
use Illuminate\Database\Seeder;

/** Klien, testimoni, FAQ, dan berita dari situs statis lama (index.html / tentang.html). */
class CollectionsSeeder extends Seeder
{
    public function run(): void
    {
        // Urutan = urutan marquee asli (baris 1 lalu baris 2), logo duplikat untuk loop sudah dibuang.
        $clients = [
            ['PT Pertamina (Persero)', 'pertamina-3b5a0-3404_250-t598_26.png'],
            ['Institut Teknologi Bandung', 'Logo_Institut_Teknologi_Bandung 1.png'],
            ['Universitas Sumatera Utara', '1200px-Logo_of_North_Sumatra_University.png'],
            ['Universitas Brawijaya', '1200px-Logo_Universitas_Brawijaya 1.png'],
            ['Universitas Airlangga', 'Logo-Branding-UNAIR-biru.png'],
            ['Universitas Jenderal Soedirman', 'Logo_Unsoed.png'],
            ['IPB University', 'Bogor_Agricultural_University_(IPB)_symbol.png'],
            ['Universitas Hasanuddin', 'Logo-Resmi-Unhas-1 1.png'],
            ['Institut Teknologi Sumatera', 'Logo_ITERA.png'],
            ['Universitas Islam Indonesia', 'Logo-UII-Biru.png'],
            ['Universitas Negeri Malang', 'Lambang-UM.png'],
            ['Universitas Katolik Parahyangan', 'UNPAR_LOGO 1.png'],
            ['PT Wijaya Karya Beton Tbk', 'Wika_beton 1.png'],
            ['PT Charoen Pokphand Jaya Farm', 'PT-Charoen-Pokphand-Jaya-Farm-.png'],
            ['PT Kaltim Prima Coal', 'pt-kaltim-prima-coal-logo-F822D4E08A-seeklogo.png'],
            ['Balitbangkes Kementerian Kesehatan', 'Logo_Balitbangkes.png'],
            ['Universitas Mercu Buana', 'logo_baru_umb 1.png'],
            ['Universitas Islam Riau', 'Logo_UIR.png'],
            ['Lembaga Biologi Molekuler Eijkman', 'Lembaga-Biomolekuler-Eijkman-Update.png'],
            ['Pusat Penelitian Kelapa Sawit', 'PPKS-385x385.png'],
            ['PT Sucofindo', '2862274-pt-sangata-sucofindo-kantor-cabang-bontang-kalimantan-timur.png'],
            ['Balai Besar Laboratorium Kesehatan Jakarta', 'logo-bblk.png'],
            ['Universitas Teuku Umar', 'Logo_Universitas_Teuku_Umar.png'],
            ['Universitas Muhammadiyah Jakarta', 'Lambang_Resmi_UMJ.png'],
            ['UIN Walisongo Semarang', 'Logo-UIN-Walisongo-Warna-PNG.png'],
            ['Universitas Semarang', 'lambang-universitas-semarang.png'],
            ['Universitas Muhammadiyah Semarang', 'logo-unimus.png'],
            ['Universitas Sebelas Maret', 'Logo-UNS-New-04-1.png'],
            ['Universitas Atma Jaya Yogyakarta', 'UAJY_LOGOGRAM.png'],
            ['Universitas Muhammadiyah Gorontalo', 'Universitas-Muhammadiyah-Gorontalo.png'],
            ['Poltekkes Kemenkes Jakarta II', 'Politeknik_Kesehatan_Jakarta_II.png'],
            ['Poltekkes Kemenkes Tanjungkarang', 'Poltekkes_Tjk.png'],
            ['Poltekkes Kemenkes Pontianak', 'Logo-Poltekkes-Pontianak.png'],
            ['Poltekkes Kemenkes Tasikmalaya', 'logo-poltekkkes-Asli-225x300.png'],
            ['Dinas Ketahanan Pangan, Kelautan, dan Pertanian Provinsi DKI Jakarta', 'dinas_ketahanan_pangan_kelautan_dan_pertanian_provinsi_dki_jakarta_cover.png'],
            ['Pemerintah Provinsi Kalimantan Selatan', 'kalsel 1.png'],
            ['SMK Migas Cepu', 'SMK_Migas_Cepu.png'],
            ['PT Clariant Indonesia', 'pt-clariant-indonesia-195.png'],
            ['PT Caltest Engineering', 'pt caltest engineerings.png'],
            ['PT Mintec Abadi', 'Logo_2021-09-03cdfc8389e7bc7d8917bced414d5266961234567890.png'],
            ['Merpati', 'merpati-logo-landscape.png'],
            ['PDAM Tirta Musi Palembang', 'Tarif-PDAM-Tirta-Musi-Palembang-Naik-2022.png'],
            ['Pratita', 'logo-pratita.png'],
            ['Yayasan Almarisah Madani', 'YAYASAN-ALMARISAH-MADANI.png'],
        ];
        foreach ($clients as $i => [$name, $file]) {
            Client::updateOrCreate(['logo' => "legacy/client/{$file}"], ['name' => $name, 'sort' => $i + 1, 'is_published' => true]);
        }

        $testimonials = [
            ['Dr. Ahmad Fauzi', 'Direktur', 'RS Medika Utama', 'INOVASS mendampingi kami dengan sangat profesional. Proses sertifikasi ISO 9001 berjalan lancar dan tepat waktu.'],
            ['Ir. Sari Dewi', 'Kepala Lab', 'BBLK Jakarta', 'Tim konsultan INOVASS sangat kompeten dan responsif. Mereka benar-benar memahami kebutuhan laboratorium kami.'],
            ['Budi Santoso', 'HRD Manager', 'PT Energi Nusantara', 'Pelatihan yang diberikan sangat aplikatif. Peserta langsung dapat mengimplementasikan materi di tempat kerja.'],
            ['Prof. Hendra Wijaya', 'Dekan Fakultas Teknik', 'UNS', 'Pendampingan INOVASS membantu kami memahami gap analysis dengan jelas dan solusi yang terstruktur.'],
            ['Maya Putri', 'Manajer Mutu', 'PT Caltest', 'Dengan bantuan INOVASS, kami berhasil meraih akreditasi KAN untuk laboratorium pengujian kami.'],
        ];
        foreach ($testimonials as $i => [$name, $position, $org, $quote]) {
            Testimonial::updateOrCreate(['name' => $name], [
                'position' => $position, 'organization' => $org, 'quote' => $quote,
                'rating' => 5, 'sort' => $i + 1, 'is_published' => true,
            ]);
        }

        $faqs = [
            ['Berapa lama proses sertifikasi ISO?', 'Durasi bervariasi tergantung kesiapan organisasi, umumnya 3–6 bulan untuk ISO 9001. INOVASS menyesuaikan timeline dengan kondisi dan kebutuhan setiap klien.'],
            ['Apakah INOVASS melayani instansi pemerintah?', 'Ya, INOVASS telah mendampingi berbagai instansi pemerintah, kementerian, dan lembaga negara dalam penerapan standar ISO dan sistem manajemen.'],
            ['Pelatihan apa saja yang tersedia?', 'Kami menyediakan pelatihan untuk berbagai standar ISO, pelatihan auditor internal, awareness training, dan program pelatihan khusus sesuai kebutuhan organisasi.'],
            ['Apakah layanan konsultasi tersedia secara online?', 'Ya, INOVASS menyediakan layanan konsultasi hybrid — tatap muka maupun online — untuk memastikan fleksibilitas dan kenyamanan klien di seluruh Indonesia.'],
            ['Bagaimana cara memulai kerja sama dengan INOVASS?', 'Hubungi kami melalui formulir kontak atau langsung WhatsApp. Tim kami akan merespons dalam 1x24 jam untuk menjadwalkan konsultasi awal gratis.'],
            ['Apakah ada garansi keberhasilan sertifikasi?', 'Kami berkomitmen memberikan pendampingan terbaik. Tingkat keberhasilan klien kami mencapai 98% berdasarkan rekam jejak selama lebih dari 20 tahun.'],
        ];
        foreach ($faqs as $i => [$q, $a]) {
            Faq::updateOrCreate(['question' => $q], ['answer' => "<p>{$a}</p>", 'sort' => $i + 1, 'is_published' => true]);
        }

        $articles = [
            [
                'title' => 'Memahami Revisi ISO 9001:2025 dan Dampaknya bagi Organisasi',
                'slug' => 'memahami-revisi-iso-9001-2025',
                'category' => 'Berita',
                'published_at' => '2025-06-12 09:00:00',
                'excerpt' => 'Standar ISO 9001 mengalami pembaruan signifikan. Pahami perubahan utama dan langkah persiapan yang perlu dilakukan.',
                'body' => <<<'HTML'
<p>ISO 9001 adalah standar sistem manajemen mutu yang paling banyak digunakan di dunia. Seperti standar ISO lainnya, ISO 9001 ditinjau secara berkala oleh komite teknis ISO/TC 176 agar tetap relevan dengan perkembangan praktik bisnis, teknologi, dan harapan pelanggan. Versi yang berlaku saat ini adalah ISO 9001:2015, yang pada tahun 2024 telah dilengkapi amandemen terkait pertimbangan perubahan iklim dalam konteks organisasi.</p>
<p>Proses revisi menuju edisi berikutnya sedang berjalan. Struktur dasar yang mengikuti Harmonized Structure ISO diperkirakan tetap dipertahankan, sehingga prinsip-prinsip utama seperti pendekatan proses, pemikiran berbasis risiko, dan siklus Plan-Do-Check-Act tetap menjadi fondasi. Perubahan yang dibahas lebih banyak menyangkut penajaman persyaratan dan penjelasan, bukan perombakan total.</p>
<p>Bagi organisasi yang sudah tersertifikasi, langkah persiapan yang bijak adalah memastikan sistem yang ada berjalan efektif: konteks organisasi dan isu internal-eksternal diperbarui, risiko dan peluang ditinjau secara rutin, serta audit internal dan tinjauan manajemen dilaksanakan dengan sungguh-sungguh. Setelah edisi baru resmi terbit, lembaga sertifikasi akan menetapkan masa transisi sehingga organisasi memiliki waktu untuk menyesuaikan diri.</p>
<p>INOVASS memantau perkembangan revisi ini dan siap membantu organisasi melakukan gap analysis terhadap persyaratan baru ketika standar tersebut diterbitkan.</p>
HTML,
            ],
            [
                'title' => '5 Kesalahan Umum dalam Audit Internal ISO yang Harus Dihindari',
                'slug' => '5-kesalahan-umum-audit-internal-iso',
                'category' => 'Insight',
                'published_at' => '2025-06-05 09:00:00',
                'excerpt' => 'Audit internal yang efektif adalah kunci keberhasilan sistem manajemen. Kenali kesalahan yang sering terjadi.',
                'body' => <<<'HTML'
<p>Audit internal merupakan persyaratan wajib dalam standar sistem manajemen ISO dan menjadi alat utama organisasi untuk menilai apakah sistemnya berjalan sesuai rencana. Sayangnya, audit internal sering diperlakukan sebagai formalitas menjelang audit sertifikasi. Berikut beberapa kesalahan yang sering ditemui.</p>
<ol>
<li><strong>Program audit tidak berbasis risiko.</strong> Semua proses diaudit dengan porsi yang sama, padahal proses yang kritis atau sering bermasalah seharusnya mendapat perhatian lebih.</li>
<li><strong>Auditor tidak independen.</strong> Auditor memeriksa pekerjaannya sendiri sehingga temuan menjadi bias atau terlewat.</li>
<li><strong>Hanya memeriksa dokumen.</strong> Audit berhenti pada kelengkapan prosedur dan formulir tanpa menelusuri bukti penerapan di lapangan.</li>
<li><strong>Temuan ditulis tidak jelas.</strong> Ketidaksesuaian tidak merujuk pada persyaratan dan bukti objektif, sehingga sulit ditindaklanjuti.</li>
<li><strong>Tindak lanjut tidak dipantau.</strong> Koreksi dilakukan sebatas gejala tanpa analisis akar masalah, dan efektivitas tindakan korektif tidak diverifikasi.</li>
</ol>
<p>Panduan ISO 19011 tentang audit sistem manajemen dapat menjadi rujukan untuk membangun program audit yang lebih baik. Pelatihan auditor internal yang tepat juga membantu tim memahami teknik wawancara, pengambilan sampel, dan penulisan temuan yang bernilai bagi manajemen.</p>
HTML,
            ],
            [
                'title' => 'Digitalisasi Sistem Manajemen ISO: Tren dan Peluang di 2025',
                'slug' => 'digitalisasi-sistem-manajemen-iso-2025',
                'category' => 'Insight',
                'published_at' => '2025-05-28 09:00:00',
                'excerpt' => 'Transformasi digital membuka peluang baru dalam pengelolaan sistem manajemen yang lebih efisien dan terukur.',
                'body' => <<<'HTML'
<p>Banyak organisasi masih mengelola sistem manajemen ISO dengan dokumen kertas atau berkas yang tersebar di berbagai folder. Cara ini rawan menimbulkan masalah: versi dokumen yang tidak terkendali, catatan yang sulit ditelusuri, dan persiapan audit yang memakan waktu.</p>
<p>Digitalisasi menawarkan cara yang lebih tertib. Sistem pengendalian dokumen elektronik membantu memastikan hanya versi terbaru yang beredar, lengkap dengan riwayat revisi dan persetujuan. Pencatatan ketidaksesuaian, tindakan korektif, dan hasil audit dalam satu sistem memudahkan manajemen memantau status dan tren secara langsung.</p>
<p>Meski demikian, digitalisasi bukan tujuan akhir. Aplikasi hanya alat; efektivitas sistem manajemen tetap ditentukan oleh proses yang dirancang dengan baik, kompetensi personel, dan komitmen pimpinan. Organisasi sebaiknya memulai dari proses yang paling banyak menyita waktu, seperti pengendalian dokumen atau pengelolaan temuan audit, lalu memperluasnya secara bertahap.</p>
<p>INOVASS mengembangkan solusi digital seperti InoSys untuk membantu organisasi mengelola sistem manajemen secara lebih efisien dan terukur.</p>
HTML,
            ],
        ];
        foreach ($articles as $a) {
            Article::updateOrCreate(['slug' => $a['slug']], $a + ['cover' => 'legacy/wallpaper 3.png', 'is_published' => true]);
        }
    }
}
