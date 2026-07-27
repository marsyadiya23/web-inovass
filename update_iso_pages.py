#!/usr/bin/env python3
"""
Script to update content for 6 ISO standard pages
"""

import re

# Define content for each ISO standard
iso_standards = {
    "37001": {
        "title": "Jasa Konsultasi Sertifikasi ISO 37001 – Sistem Manajemen Anti Penyuapan",
        "year": "2016",
        "breadcrumb": "ISO 37001",
        "benefit_highlights": [
            "Mencegah dan Mendeteksi<br>Praktik Suap",
            "Meningkatkan Integritas dan<br>Kepercayaan Publik",
            "Memperkuat Tata Kelola yang<br>Bersih dan Transparan"
        ],
        "definition": "ISO 37001:2016 adalah standar internasional untuk Sistem Manajemen Anti Penyuapan yang membantu organisasi mencegah, mendeteksi, dan menangani praktik suap melalui kebijakan, prosedur, dan kontrol yang efektif dalam budaya organisasi yang berintegritas tinggi.",
        "benefits": [
            ("Mencegah Praktik Suap dan Korupsi", "Meminimalkan risiko tindakan penyuapan melalui sistem pencegahan dan kontrol yang efektif"),
            ("Meningkatkan Reputasi dan Kepercayaan", "Memperkuat citra organisasi sebagai entitas yang berkomitmen terhadap integritas dan transparansi"),
            ("Memenuhi Persyaratan Hukum", "Membantu kepatuhan terhadap peraturan anti korupsi nasional dan internasional"),
            ("Meningkatkan Tata Kelola Perusahaan", "Memperkuat sistem pengendalian internal dan transparansi dalam proses bisnis"),
            ("Mengurangi Risiko Hukum dan Keuangan", "Menurunkan potensi sanksi, denda, dan kerugian akibat tindakan penyuapan"),
            ("Membuka Peluang Bisnis Global", "Memenuhi persyaratan tender dan kerja sama dengan mitra bisnis internasional")
        ],
        "process_step2": "Tim kami memberikan pelatihan persyaratan ISO 37001:2016, mendampingi penyusunan kebijakan anti suap, due diligence, dan implementasi sistem manajemen anti penyuapan di seluruh proses organisasi.",
        "target_title": "Siapa yang Membutuhkan ISO 37001?",
        "target_desc": "ISO 37001:2016 dapat diterapkan oleh berbagai jenis organisasi yang ingin mencegah dan menangani risiko penyuapan serta memperkuat tata kelola yang bersih.",
        "targets": [
            "BUMN dan Lembaga Pemerintahan",
            "Perusahaan Konstruksi",
            "Perusahaan Energi dan Tambang",
            "Lembaga Keuangan dan Perbankan",
            "Perusahaan Pengadaan Barang/Jasa",
            "Perusahaan Farmasi dan Kesehatan",
            "Konsultan dan Jasa Profesional",
            "Organisasi Internasional",
            "Perusahaan Logistik dan Distribusi"
        ],
        "target_footer": "Standar ini cocok untuk organisasi yang berinteraksi dengan pihak ketiga, pemerintah, atau beroperasi di lingkungan berisiko tinggi terhadap praktik suap."
    },
    "37301": {
        "title": "Jasa Konsultasi Sertifikasi ISO 37301 – Sistem Manajemen Kepatuhan",
        "year": "2021",
        "breadcrumb": "ISO 37301",
        "benefit_highlights": [
            "Memastikan Kepatuhan terhadap<br>Peraturan dan Regulasi",
            "Mengurangi Risiko Hukum<br>dan Sanksi",
            "Memperkuat Budaya Kepatuhan<br>di Organisasi"
        ],
        "definition": "ISO 37301:2021 adalah standar internasional untuk Sistem Manajemen Kepatuhan yang membantu organisasi memastikan kepatuhan terhadap peraturan perundang-undangan, standar industri, dan komitmen internal melalui sistem manajemen yang terstruktur dan efektif.",
        "benefits": [
            ("Meningkatkan Kepatuhan Regulasi", "Memastikan organisasi mematuhi peraturan perundang-undangan dan standar yang berlaku"),
            ("Mengurangi Risiko Hukum", "Meminimalkan potensi sanksi, denda, dan tuntutan hukum akibat ketidakpatuhan"),
            ("Memperkuat Tata Kelola Perusahaan", "Meningkatkan transparansi dan akuntabilitas dalam proses bisnis"),
            ("Meningkatkan Reputasi Organisasi", "Membangun kepercayaan stakeholder melalui komitmen kepatuhan yang nyata"),
            ("Efisiensi Operasional", "Mengintegrasikan kepatuhan dalam proses bisnis secara sistematis"),
            ("Mendukung Pengambilan Keputusan", "Menyediakan informasi kepatuhan yang akurat untuk manajemen")
        ],
        "process_step2": "Tim kami memberikan pelatihan persyaratan ISO 37301:2021, mendampingi penyusunan register kepatuhan, analisis risiko kepatuhan, dan implementasi sistem manajemen kepatuhan di seluruh proses organisasi.",
        "target_title": "Siapa yang Membutuhkan ISO 37301?",
        "target_desc": "ISO 37301:2021 dapat diterapkan oleh berbagai jenis organisasi yang ingin memastikan kepatuhan terhadap peraturan dan memperkuat tata kelola.",
        "targets": [
            "Lembaga Keuangan dan Perbankan",
            "Perusahaan Farmasi dan Kesehatan",
            "Perusahaan Energi dan Tambang",
            "Lembaga Pemerintahan",
            "Perusahaan Manufaktur",
            "Industri Telekomunikasi",
            "Perusahaan Asuransi",
            "Organisasi Nirlaba",
            "Perusahaan Konstruksi"
        ],
        "target_footer": "Standar ini cocok untuk organisasi yang beroperasi dalam lingkungan regulasi yang ketat atau memiliki komitmen kepatuhan yang tinggi."
    },
    "50001": {
        "title": "Jasa Konsultasi Sertifikasi ISO 50001 – Sistem Manajemen Energi",
        "year": "2018",
        "breadcrumb": "ISO 50001",
        "benefit_highlights": [
            "Meningkatkan Efisiensi<br>Penggunaan Energi",
            "Mengurangi Biaya Operasional<br>dan Emisi",
            "Mendukung Kebijakan Energi<br>Berkelanjutan"
        ],
        "definition": "ISO 50001:2018 adalah standar internasional untuk Sistem Manajemen Energi yang membantu organisasi meningkatkan kinerja energi, mengurangi konsumsi energi, dan menurunkan emisi gas rumah kaca melalui pendekatan sistematis dan berkelanjutan.",
        "benefits": [
            ("Mengurangi Biaya Energi", "Mengoptimalkan penggunaan energi sehingga mengurangi biaya operasional"),
            ("Meningkatkan Efisiensi Energi", "Mengidentifikasi dan menerapkan peluang penghematan energi secara berkelanjutan"),
            ("Mengurangi Emisi Gas Rumah Kaca", "Menurunkan jejak karbon dan dampak lingkungan dari penggunaan energi"),
            ("Memenuhi Persyaratan Regulasi", "Membantu kepatuhan terhadap peraturan energi dan lingkungan yang berlaku"),
            ("Meningkatkan Reputasi Perusahaan", "Menunjukkan komitmen terhadap keberlanjutan dan tanggung jawab lingkungan"),
            ("Meningkatkan Daya Saing", "Memperoleh keunggulan kompetitif melalui efisiensi operasional")
        ],
        "process_step2": "Tim kami memberikan pelatihan persyaratan ISO 50001:2018, mendampingi penyusunan kebijakan energi, tinjauan energi, dan implementasi sistem manajemen energi di seluruh proses organisasi.",
        "target_title": "Siapa yang Membutuhkan ISO 50001?",
        "target_desc": "ISO 50001:2018 dapat diterapkan oleh berbagai jenis organisasi yang ingin meningkatkan efisiensi energi dan mengurangi biaya operasional.",
        "targets": [
            "Perusahaan Manufaktur",
            "Perusahaan Energi dan Utilitas",
            "Gedung Komersial dan Perkantoran",
            "Rumah Sakit dan Fasilitas Kesehatan",
            "Hotel dan Perhotelan",
            "Perguruan Tinggi dan Kampus",
            "Pusat Perbelanjaan",
            "Industri Pangan dan Minuman",
            "Fasilitas Transportasi"
        ],
        "target_footer": "Standar ini cocok untuk organisasi dengan konsumsi energi signifikan yang ingin meningkatkan efisiensi dan mengurangi dampak lingkungan."
    },
    "55001": {
        "title": "Jasa Konsultasi Sertifikasi ISO 55001 – Sistem Manajemen Aset",
        "year": "2014",
        "breadcrumb": "ISO 55001",
        "benefit_highlights": [
            "Mengoptimalkan Nilai dan<br>Kinerja Aset",
            "Mengurangi Biaya Pemeliharaan<br>dan Operasional",
            "Meningkatkan Pengambilan Keputusan<br>Berbasis Risiko"
        ],
        "definition": "ISO 55001:2014 adalah standar internasional untuk Sistem Manajemen Aset yang membantu organisasi mengoptimalkan pengelolaan aset fisik, meningkatkan nilai aset, mengurangi risiko, dan memastikan kinerja aset yang berkelanjutan sepanjang siklus hidupnya.",
        "benefits": [
            ("Meningkatkan Nilai Aset", "Mengoptimalkan pengelolaan aset untuk memberikan nilai maksimal bagi organisasi"),
            ("Mengurangi Biaya Operasional", "Menurunkan biaya pemeliharaan dan operasional melalui pengelolaan aset yang efisien"),
            ("Meningkatkan Kinerja Aset", "Memastikan aset beroperasi dengan optimal sepanjang siklus hidupnya"),
            ("Mengurangi Risiko Kegagalan Aset", "Menerapkan pemeliharaan preventif dan prediktif untuk mengurangi downtime"),
            ("Meningkatkan Pengambilan Keputusan", "Menyediakan data dan informasi yang akurat untuk keputusan investasi aset"),
            ("Memenuhi Persyaratan Regulasi", "Membantu kepatuhan terhadap peraturan pengelolaan aset yang berlaku")
        ],
        "process_step2": "Tim kami memberikan pelatihan persyaratan ISO 55001:2014, mendampingi penyusunan strategi aset, rencana pengelolaan aset (Asset Management Plan), dan implementasi sistem manajemen aset di seluruh organisasi.",
        "target_title": "Siapa yang Membutuhkan ISO 55001?",
        "target_desc": "ISO 55001:2014 dapat diterapkan oleh berbagai jenis organisasi yang memiliki aset fisik signifikan dan ingin mengoptimalkan pengelolaannya.",
        "targets": [
            "Perusahaan Utilitas (Listrik, Air, Gas)",
            "Industri Minyak dan Gas",
            "Transportasi dan Logistik",
            "Perusahaan Manufaktur",
            "Infrastruktur dan Konstruksi",
            "Telekomunikasi",
            "Rumah Sakit dan Fasilitas Kesehatan",
            "Lembaga Pemerintahan",
            "Real Estate dan Property"
        ],
        "target_footer": "Standar ini cocok untuk organisasi yang memiliki aset fisik bernilai tinggi dan ingin meningkatkan efisiensi pengelolaannya."
    },
    "21001": {
        "title": "Jasa Konsultasi Sertifikasi ISO 21001 – Sistem Manajemen Organisasi Pendidikan",
        "year": "2018",
        "breadcrumb": "ISO 21001",
        "benefit_highlights": [
            "Meningkatkan Mutu Pendidikan<br>dan Pembelajaran",
            "Meningkatkan Kepuasan Peserta<br>Didik dan Stakeholder",
            "Mendukung Akreditasi dan<br>Pengakuan Internasional"
        ],
        "definition": "ISO 21001:2018 adalah standar internasional untuk Sistem Manajemen Organisasi Pendidikan yang membantu lembaga pendidikan meningkatkan mutu pembelajaran, kepuasan peserta didik, dan efektivitas pengelolaan melalui pendekatan yang berfokus pada kebutuhan peserta didik dan stakeholder lainnya.",
        "benefits": [
            ("Meningkatkan Mutu Pembelajaran", "Memastikan proses pendidikan dan pembelajaran yang berkualitas dan efektif"),
            ("Meningkatkan Kepuasan Peserta Didik", "Memenuhi kebutuhan dan ekspektasi peserta didik serta stakeholder"),
            ("Mendukung Akreditasi", "Memenuhi persyaratan akreditasi nasional dan internasional"),
            ("Meningkatkan Reputasi Institusi", "Memperkuat citra lembaga pendidikan di tingkat nasional dan internasional"),
            ("Meningkatkan Efisiensi Operasional", "Mengoptimalkan proses pengelolaan pendidikan yang terstruktur"),
            ("Mendukung Perbaikan Berkelanjutan", "Menerapkan budaya evaluasi dan peningkatan mutu secara konsisten")
        ],
        "process_step2": "Tim kami memberikan pelatihan persyaratan ISO 21001:2018, mendampingi penyusunan kurikulum, proses pembelajaran, dan implementasi sistem manajemen pendidikan di seluruh proses organisasi pendidikan.",
        "target_title": "Siapa yang Membutuhkan ISO 21001?",
        "target_desc": "ISO 21001:2018 dapat diterapkan oleh berbagai jenis organisasi pendidikan yang ingin meningkatkan mutu pembelajaran dan kepuasan stakeholder.",
        "targets": [
            "Perguruan Tinggi dan Universitas",
            "Sekolah Menengah dan Dasar",
            "Lembaga Pelatihan Vokasional",
            "Akademi dan Institut",
            "Lembaga Kursus dan Pelatihan",
            "Pesantren dan Madrasah",
            "Sekolah Internasional",
            "Pusat Pendidikan Anak Usia Dini",
            "Lembaga Pendidikan Online"
        ],
        "target_footer": "Standar ini cocok untuk organisasi pendidikan yang berkomitmen terhadap mutu pembelajaran dan kepuasan peserta didik."
    },
    "13485": {
        "title": "Jasa Konsultasi Sertifikasi ISO 13485 – Sistem Manajemen Mutu Alat Kesehatan",
        "year": "2016",
        "breadcrumb": "ISO 13485",
        "benefit_highlights": [
            "Memastikan Keamanan dan<br>Efektivitas Alat Kesehatan",
            "Memenuhi Persyaratan Regulasi<br>Global",
            "Meningkatkan Kepercayaan Pasar<br>dan Pelanggan"
        ],
        "definition": "ISO 13485:2016 adalah standar internasional untuk Sistem Manajemen Mutu Alat Kesehatan yang membantu organisasi memenuhi persyaratan regulasi, memastikan keamanan dan efektivitas produk, serta meningkatkan kepercayaan pasar melalui sistem manajemen mutu yang konsisten.",
        "benefits": [
            ("Memenuhi Persyaratan Regulasi", "Membantu kepatuhan terhadap regulasi alat kesehatan nasional dan internasional"),
            ("Meningkatkan Keamanan Produk", "Memastikan alat kesehatan aman dan efektif untuk digunakan"),
            ("Membuka Akses Pasar Global", "Memenuhi persyaratan untuk ekspor ke berbagai negara"),
            ("Meningkatkan Kepercayaan Pelanggan", "Memperkuat reputasi sebagai produsen alat kesehatan yang berkualitas"),
            ("Mengurangi Risiko Produk Cacat", "Menerapkan kontrol mutu yang ketat sepanjang proses produksi"),
            ("Mendukung Vigilans dan Keamanan", "Memastikan sistem pemantauan pasca-pasar yang efektif")
        ],
        "process_step2": "Tim kami memberikan pelatihan persyaratan ISO 13485:2016, mendampingi penyusunan dokumentasi alat kesehatan, manajemen risiko, dan implementasi sistem manajemen mutu alat kesehatan di seluruh proses organisasi.",
        "target_title": "Siapa yang Membutuhkan ISO 13485?",
        "target_desc": "ISO 13485:2016 dapat diterapkan oleh berbagai jenis organisasi yang terlibat dalam siklus hidup alat kesehatan.",
        "targets": [
            "Produsen Alat Kesehatan",
            "Distributor Alat Kesehatan",
            "Perusahaan Perakitan dan Packing",
            "Laboratorium Pengujian",
            "Produsen Komponen Alat Kesehatan",
            "Sterilisasi dan Jasa Teknis",
            "Perusahaan Instalasi Alat Kesehatan",
            "Konsultan Regulasi Alat Kesehatan",
            "Importir Alat Kesehatan"
        ],
        "target_footer": "Standar ini cocok untuk organisasi yang memproduksi, mendistribusikan, atau menyediakan layanan terkait alat kesehatan."
    }
}

def update_iso_page(iso_number, data):
    """Update a single ISO page with new content"""
    filename = f"layanan-detail-iso-{iso_number}.html"
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update title tag
        content = re.sub(
            r'<title>.*?</title>',
            f'<title>{data["title"]} — INOVASS</title>',
            content
        )
        
        # Update breadcrumb
        content = re.sub(
            r'<span class="breadcrumb-current"[^>]*>.*?</span>',
            f'<span class="breadcrumb-current" style="color: #00e0a0 !important;">{data["breadcrumb"]}</span>',
            content
        )
        
        # Update page title
        content = re.sub(
            r'<h1 class="detail-page-title"[^>]*>.*?</h1>',
            f'<h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important; font-weight: 700 !important;">{data["title"]}</h1>',
            content
        )
        
        # Update benefit highlights title
        content = re.sub(
            r'<h2 class="benefit-highlight-title">Dengan ISO .*? Organisasi Anda Dapat:</h2>',
            f'<h2 class="benefit-highlight-title">Dengan ISO {iso_number}:{data["year"]} Organisasi Anda Dapat:</h2>',
            content
        )
        
        # Update benefit highlight cards
        benefit_cards = '\n          '.join([
            f'<div class="benefit-highlight-card">\n            <p>{benefit}</p>\n          </div>'
            for benefit in data["benefit_highlights"]
        ])
        content = re.sub(
            r'(<div class="benefit-highlight-grid">)(.*?)(</div>\s*</div>\s*<!-- PENGERTIAN)',
            f'\\1\n          {benefit_cards}\n        \\3',
            content,
            flags=re.DOTALL
        )
        
        # Update pengertian title
        content = re.sub(
            r'<h2 class="iso-content-title">Pengertian ISO.*?</h2>',
            f'<h2 class="iso-content-title">Pengertian ISO {iso_number}:{data["year"]}</h2>',
            content
        )
        
        # Update pengertian description
        content = re.sub(
            r'(<p class="iso-content-desc">)\s*<strong>ISO .*?</strong>.*?(</p>)',
            f'\\1\n            <strong>ISO {iso_number}:{data["year"]}</strong> {data["definition"]}\n          \\2',
            content,
            flags=re.DOTALL
        )
        
        # Update manfaat implementasi title
        content = re.sub(
            r'<h2 class="iso-benefit-section-title">Manfaat Implementasi ISO.*?</h2>',
            f'<h2 class="iso-benefit-section-title">Manfaat Implementasi ISO {iso_number}</h2>',
            content
        )
        
        # Update benefit cards
        benefit_cards_html = '\n          '.join([
            f'<div class="iso-benefit-modern-card">\n            <h3>{title}</h3>\n            <p>{desc}</p>\n          </div>'
            for title, desc in data["benefits"]
        ])
        content = re.sub(
            r'(<div class="iso-benefits-modern-grid">)(.*?)(</div>\s*</div>\s*<!-- CTA)',
            f'\\1\n          {benefit_cards_html}\n        \\3',
            content,
            flags=re.DOTALL
        )
        
        # Update process title
        content = re.sub(
            r'<h2 class="iso-process-title">Proses Sertifikasi ISO.*?</h2>',
            f'<h2 class="iso-process-title">Proses Sertifikasi ISO {iso_number}:{data["year"]}</h2>',
            content
        )
        
        # Update process step 1 (Konsultasi)
        content = re.sub(
            r'(<h3>Konsultasi & Perencanaan</h3>\s*<p>).*?(</p>\s*</div>\s*<div class="process-step-number">1</div>)',
            f'\\1Kami melakukan assessment awal untuk menilai kesiapan organisasi dalam menerapkan Sistem Manajemen ISO {iso_number}:{data["year"]}, mengidentifikasi gap terhadap persyaratan standar, dan menyusun roadmap implementasi yang sesuai dengan kebutuhan organisasi.\\2',
            content,
            flags=re.DOTALL
        )
        
        # Update process step 2 (Pelatihan)
        content = re.sub(
            r'(<h3>Pelatihan & Implementasi</h3>\s*<p>).*?(</p>\s*</div>\s*<div class="process-step-number">2</div>)',
            f'\\1{data["process_step2"]}\\2',
            content,
            flags=re.DOTALL
        )
        
        # Update process step 3 (Audit Internal)
        content = re.sub(
            r'(<h3>Audit Internal & Tinjauan Manajemen</h3>\s*<p>).*?(</p>\s*</div>\s*<div class="process-step-number">3</div>)',
            f'\\1Organisasi melaksanakan audit internal dan tinjauan manajemen untuk memastikan sistem telah diterapkan secara efektif dan siap menghadapi audit sertifikasi.\\2',
            content,
            flags=re.DOTALL
        )
        
        # Update process step 5 (Penerbitan)
        content = re.sub(
            r'(<h3>Penerbitan Sertifikat</h3>\s*<p>).*?(</p>\s*</div>\s*<div class="process-step-number">5</div>)',
            f'\\1Setelah proses audit selesai dan seluruh ketidaksesuaian (jika ada) telah ditindaklanjuti, lembaga sertifikasi menerbitkan Sertifikat ISO {iso_number}:{data["year"]} yang berlaku selama tiga tahun.\\2',
            content,
            flags=re.DOTALL
        )
        
        # Update target title
        content = re.sub(
            r'<h2 class="iso-target-section-title"[^>]*>Siapa yang .*?</h2>',
            f'<h2 class="iso-target-section-title" style="margin-bottom: 3rem;">{data["target_title"]}</h2>',
            content
        )
        
        # Update target description
        content = re.sub(
            r'(<p class="iso-target-description">).*?(</p>)',
            f'\\1\n          {data["target_desc"]}\n        \\2',
            content,
            flags=re.DOTALL
        )
        
        # Update target cards
        target_cards_html = '\n          '.join([
            f'<div class="iso-target-card"><h4>{target}</h4></div>'
            for target in data["targets"]
        ])
        content = re.sub(
            r'(<div class="iso-target-grid">)(.*?)(</div>\s*<p class="iso-target-footer">)',
            f'\\1\n          {target_cards_html}\n        \\3',
            content,
            flags=re.DOTALL
        )
        
        # Update target footer
        content = re.sub(
            r'(<p class="iso-target-footer">).*?(</p>)',
            f'\\1\n          {data["target_footer"]}\n        \\2',
            content,
            flags=re.DOTALL
        )
        
        # Write updated content
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Updated {filename}")
        return True
        
    except Exception as e:
        print(f"✗ Error updating {filename}: {e}")
        return False

# Update all 6 ISO pages
print("Updating ISO standard pages...")
print("=" * 50)

for iso_num, data in iso_standards.items():
    update_iso_page(iso_num, data)

print("=" * 50)
print("Update complete!")
