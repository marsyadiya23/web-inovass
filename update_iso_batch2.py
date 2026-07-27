#!/usr/bin/env python3
"""Script to update 7 new ISO standard pages"""
import re

iso_standards = {
    "39001": {
        "title": "Jasa Konsultasi Sertifikasi ISO 39001 – Sistem Manajemen Keselamatan Lalu Lintas Jalan",
        "year": "2012",
        "breadcrumb": "ISO 39001",
        "benefit_highlights": [
            "Mengurangi Kecelakaan Lalu Lintas<br>dan Korban Jiwa",
            "Meningkatkan Keselamatan Pengemudi<br>dan Pengguna Jalan",
            "Memenuhi Komitmen Keselamatan<br>Berkelanjutan"
        ],
        "definition": "ISO 39001:2012 adalah standar internasional untuk Sistem Manajemen Keselamatan Lalu Lintas Jalan yang membantu organisasi mengurangi risiko kematian dan cedera serius akibat kecelakaan lalu lintas melalui pendekatan sistematis dalam pengelolaan keselamatan jalan.",
        "benefits": [
            ("Mengurangi Angka Kecelakaan", "Menurunkan insiden kecelakaan lalu lintas dan korban jiwa melalui sistem manajemen yang efektif"),
            ("Meningkatkan Keselamatan Karyawan", "Melindungi pengemudi dan karyawan yang menggunakan jalan dalam aktivitas kerja"),
            ("Memenuhi Persyaratan Hukum", "Membantu kepatuhan terhadap peraturan keselamatan lalu lintas yang berlaku"),
            ("Mengurangi Biaya Operasional", "Menurunkan biaya akibat kecelakaan, kerusakan kendaraan, dan klaim asuransi"),
            ("Meningkatkan Reputasi Perusahaan", "Menunjukkan komitmen terhadap keselamatan dan tanggung jawab sosial"),
            ("Meningkatkan Budaya Keselamatan", "Membangun kesadaran dan perilaku aman di kalangan pengemudi dan karyawan")
        ],
        "process_step2": "Tim kami memberikan pelatihan persyaratan ISO 39001:2012, mendampingi penyusunan kebijakan keselamatan jalan, risk assessment, dan implementasi sistem manajemen keselamatan lalu lintas di seluruh proses organisasi.",
        "target_title": "Siapa yang Membutuhkan ISO 39001?",
        "target_desc": "ISO 39001:2012 dapat diterapkan oleh berbagai jenis organisasi yang memiliki risiko keselamatan lalu lintas dalam operasionalnya.",
        "targets": [
            "Perusahaan Transportasi dan Logistik",
            "Perusahaan Angkutan Umum",
            "Perusahaan Rental Kendaraan",
            "Organisasi dengan Armada Kendaraan",
            "Lembaga Pemerintahan Transportasi",
            "Perusahaan Konstruksi",
            "Perusahaan Kurir dan Ekspedisi",
            "Perusahaan Pertambangan",
            "Industri Minyak dan Gas"
        ],
        "target_footer": "Standar ini cocok untuk organisasi yang memiliki armada kendaraan atau karyawan yang sering menggunakan jalan dalam aktivitas kerja."
    },
    "10002": {
        "title": "Jasa Konsultasi Sertifikasi ISO 10002 – Sistem Manajemen Penanganan Keluhan Pelanggan",
        "year": "2018",
        "breadcrumb": "ISO 10002",
        "benefit_highlights": [
            "Meningkatkan Kepuasan dan<br>Loyalitas Pelanggan",
            "Menangani Keluhan Secara<br>Efektif dan Transparan",
            "Mengubah Keluhan Menjadi<br>Peluang Perbaikan"
        ],
        "definition": "ISO 10002:2018 adalah standar internasional untuk Sistem Manajemen Penanganan Keluhan Pelanggan yang membantu organisasi menangani keluhan secara efektif, meningkatkan kepuasan pelanggan, dan mengubah keluhan menjadi peluang perbaikan berkelanjutan.",
        "benefits": [
            ("Meningkatkan Kepuasan Pelanggan", "Menangani keluhan dengan cepat dan efektif sehingga meningkatkan kepercayaan pelanggan"),
            ("Meningkatkan Loyalitas Pelanggan", "Mengubah pelanggan yang tidak puas menjadi pelanggan yang loyal"),
            ("Memperbaiki Produk dan Layanan", "Mengidentifikasi akar masalah dari keluhan untuk perbaikan berkelanjutan"),
            ("Meningkatkan Reputasi Perusahaan", "Menunjukkan komitmen terhadap kepuasan dan kepentingan pelanggan"),
            ("Mengurangi Risiko Hukum", "Menurunkan potensi tuntutan hukum akibat penanganan keluhan yang tidak tepat"),
            ("Meningkatkan Efisiensi Operasional", "Menerapkan proses penanganan keluhan yang terstruktur dan sistematis")
        ],
        "process_step2": "Tim kami memberikan pelatihan persyaratan ISO 10002:2018, mendampingi penyusunan prosedur penanganan keluhan, customer feedback mechanism, dan implementasi sistem manajemen keluhan di seluruh proses organisasi.",
        "target_title": "Siapa yang Membutuhkan ISO 10002?",
        "target_desc": "ISO 10002:2018 dapat diterapkan oleh berbagai jenis organisasi yang ingin meningkatkan penanganan keluhan pelanggan.",
        "targets": [
            "Perusahaan Jasa Keuangan",
            "Rumah Sakit dan Klinik",
            "Hotel dan Perhotelan",
            "Maskapai Penerbangan",
            "Perusahaan Telekomunikasi",
            "Retail dan E-commerce",
            "Perusahaan Asuransi",
            "Lembaga Pendidikan",
            "Layanan Publik"
        ],
        "target_footer": "Standar ini cocok untuk organisasi yang menerima keluhan pelanggan dan ingin meningkatkan proses penanganannya."
    },
    "30301": {
        "title": "Jasa Konsultasi Sertifikasi ISO 30301 – Sistem Manajemen Pengelolaan Arsip",
        "year": "2019",
        "breadcrumb": "ISO 30301",
        "benefit_highlights": [
            "Mengelola Arsip Secara<br>Sistematis dan Aman",
            "Memastikan Akses dan<br>Penemuan Kembali yang Cepat",
            "Memenuhi Persyaratan Hukum<br>dan Regulasi"
        ],
        "definition": "ISO 30301:2019 adalah standar internasional untuk Sistem Manajemen Pengelolaan Arsip yang membantu organisasi mengelola arsip secara sistematis, memastikan integritas informasi, dan memenuhi persyaratan hukum serta regulasi terkait pengelolaan dokumen.",
        "benefits": [
            ("Meningkatkan Pengelolaan Informasi", "Mengelola arsip dan dokumen secara terstruktur dan mudah diakses"),
            ("Memastikan Keamanan Arsip", "Melindungi arsip dari kerusakan, kehilangan, atau akses tidak sah"),
            ("Memenuhi Persyaratan Hukum", "Membantu kepatuhan terhadap regulasi pengelolaan arsip dan dokumen"),
            ("Meningkatkan Efisiensi Operasional", "Mempercepat pencarian dan penemuan kembali dokumen yang dibutuhkan"),
            ("Mendukung Audit dan Akuntabilitas", "Menyediakan jejak audit yang jelas untuk transparansi dan akuntabilitas"),
            ("Mengurangi Risiko Kehilangan Data", "Menerapkan sistem backup dan preservasi arsip yang efektif")
        ],
        "process_step2": "Tim kami memberikan pelatihan persyaratan ISO 30301:2019, mendampingi penyusunan kebijakan pengelolaan arsip, klasifikasi dokumen, dan implementasi sistem manajemen arsip di seluruh proses organisasi.",
        "target_title": "Siapa yang Membutuhkan ISO 30301?",
        "target_desc": "ISO 30301:2019 dapat diterapkan oleh berbagai jenis organisasi yang memiliki kebutuhan pengelolaan arsip yang sistematis.",
        "targets": [
            "Lembaga Pemerintahan",
            "Lembaga Keuangan dan Perbankan",
            "Rumah Sakit dan Fasilitas Kesehatan",
            "Lembaga Pendidikan",
            "Perusahaan Hukum",
            "Arsip Nasional dan Daerah",
            "Perusahaan Asuransi",
            "Perpustakaan dan Museum",
            "Perusahaan Konsultan"
        ],
        "target_footer": "Standar ini cocok untuk organisasi yang mengelola dokumen penting dan memiliki kewajiban penyimpanan arsip jangka panjang."
    },
    "20000-1": {
        "title": "Jasa Konsultasi Sertifikasi ISO/IEC 20000-1 – Sistem Manajemen Layanan Teknologi Informasi",
        "year": "2018",
        "breadcrumb": "ISO/IEC 20000-1",
        "benefit_highlights": [
            "Meningkatkan Kualitas Layanan<br>Teknologi Informasi",
            "Memastikan Ketersediaan dan<br>Keandalan Layanan IT",
            "Mendukung Transformasi Digital<br>yang Efektif"
        ],
        "definition": "ISO/IEC 20000-1:2018 adalah standar internasional untuk Sistem Manajemen Layanan Teknologi Informasi yang membantu organisasi menyediakan layanan IT berkualitas, meningkatkan kepuasan pengguna, dan memastikan ketersediaan serta keandalan layanan IT.",
        "benefits": [
            ("Meningkatkan Kualitas Layanan IT", "Memastikan layanan teknologi informasi yang konsisten dan berkualitas tinggi"),
            ("Meningkatkan Kepuasan Pengguna", "Memenuhi kebutuhan dan ekspektasi pengguna layanan IT"),
            ("Mengurangi Downtime Sistem", "Meningkatkan ketersediaan dan keandalan infrastruktur IT"),
            ("Meningkatkan Efisiensi Operasional IT", "Mengoptimalkan proses pengelolaan layanan IT"),
            ("Mendukung Bisnis yang Berkelanjutan", "Memastikan layanan IT mendukung tujuan bisnis organisasi"),
            ("Memenuhi Persyaratan Kontrak", "Membantu memenuhi Service Level Agreement (SLA) dengan klien")
        ],
        "process_step2": "Tim kami memberikan pelatihan persyaratan ISO/IEC 20000-1:2018, mendampingi penyusunan katalog layanan, Service Level Agreement (SLA), dan implementasi sistem manajemen layanan IT di seluruh proses organisasi.",
        "target_title": "Siapa yang Membutuhkan ISO/IEC 20000-1?",
        "target_desc": "ISO/IEC 20000-1:2018 dapat diterapkan oleh berbagai jenis organisasi yang menyediakan layanan teknologi informasi.",
        "targets": [
            "Perusahaan IT dan Software",
            "Data Center dan Cloud Provider",
            "Perusahaan Telekomunikasi",
            "IT Service Provider",
            "Lembaga Keuangan",
            "Rumah Sakit dan Healthcare IT",
            "Lembaga Pendidikan",
            "Departemen IT Internal",
            "Managed Service Provider (MSP)"
        ],
        "target_footer": "Standar ini cocok untuk organisasi yang menyediakan layanan IT internal maupun eksternal dan ingin meningkatkan kualitas layanannya."
    },
    "35001": {
        "title": "Jasa Konsultasi Sertifikasi ISO 35001 – Sistem Manajemen Biorisiko Laboratorium",
        "year": "2019",
        "breadcrumb": "ISO 35001",
        "benefit_highlights": [
            "Mengelola Biorisiko Secara<br>Sistematis dan Aman",
            "Melindungi Pekerja dan<br>Lingkungan dari Bahaya Biologis",
            "Memenuhi Persyaratan Biosafety<br>dan Biosecurity"
        ],
        "definition": "ISO 35001:2019 adalah standar internasional untuk Sistem Manajemen Biorisiko Laboratorium yang membantu organisasi mengidentifikasi, menilai, dan mengendalikan risiko biologis di laboratorium untuk melindungi pekerja, masyarakat, dan lingkungan.",
        "benefits": [
            ("Meningkatkan Keamanan Laboratorium", "Mengurangi risiko paparan agen biologis berbahaya bagi pekerja laboratorium"),
            ("Melindungi Kesehatan Publik", "Mencegah penyebaran agen biologis ke masyarakat dan lingkungan"),
            ("Memenuhi Persyaratan Regulasi", "Membantu kepatuhan terhadap peraturan biosafety dan biosecurity"),
            ("Meningkatkan Kepercayaan Stakeholder", "Menunjukkan komitmen terhadap pengelolaan biorisiko yang bertanggung jawab"),
            ("Mengurangi Insiden Kecelakaan", "Menurunkan kejadian paparan, tumpahan, atau kontaminasi biologis"),
            ("Meningkatkan Budaya Keselamatan", "Membangun kesadaran dan perilaku aman dalam penanganan bahan biologis")
        ],
        "process_step2": "Tim kami memberikan pelatihan persyaratan ISO 35001:2019, mendampingi penyusunan bio risk assessment, protokol biosafety, dan implementasi sistem manajemen biorisiko di seluruh proses laboratorium.",
        "target_title": "Siapa yang Membutuhkan ISO 35001?",
        "target_desc": "ISO 35001:2019 dapat diterapkan oleh berbagai jenis organisasi yang menangani bahan biologis berbahaya.",
        "targets": [
            "Laboratorium Mikrobiologi",
            "Rumah Sakit dan Laboratorium Klinik",
            "Lembaga Penelitian Biomedis",
            "Perusahaan Bioteknologi",
            "Laboratorium Veteriner",
            "Laboratorium Pangan dan Lingkungan",
            "Lembaga Kesehatan Masyarakat",
            "Universitas dan Institusi Pendidikan",
            "Industri Farmasi dan Vaksin"
        ],
        "target_footer": "Standar ini cocok untuk organisasi yang bekerja dengan agen biologis dan memiliki risiko biorisiko dalam operasionalnya."
    },
    "ims": {
        "title": "Jasa Konsultasi Integrated Management System (IMS) ISO/IEC/SNI",
        "year": "",
        "breadcrumb": "IMS ISO/IEC/SNI",
        "benefit_highlights": [
            "Mengintegrasikan Berbagai<br>Sistem Manajemen",
            "Meningkatkan Efisiensi dan<br>Mengurangi Duplikasi",
            "Memperkuat Pengelolaan Risiko<br>Secara Holistik"
        ],
        "definition": "Integrated Management System (IMS) adalah pendekatan terintegrasi yang menggabungkan beberapa standar sistem manajemen (seperti ISO 9001, ISO 14001, ISO 45001, dll) ke dalam satu sistem manajemen yang kohesif, efisien, dan efektif untuk meningkatkan kinerja organisasi secara menyeluruh.",
        "benefits": [
            ("Mengurangi Duplikasi Proses", "Mengintegrasikan proses yang tumpang tindih dari berbagai standar"),
            ("Meningkatkan Efisiensi Operasional", "Mengurangi beban administrasi dan biaya operasional sistem manajemen"),
            ("Pengelolaan Risiko yang Holistik", "Mengelola risiko mutu, lingkungan, K3, dan lainnya secara terintegrasi"),
            ("Audit yang Lebih Efisien", "Melakukan audit terintegrasi untuk berbagai standar sekaligus"),
            ("Meningkatkan Kinerja Organisasi", "Memperkuat sinergi antar fungsi dan meningkatkan efektivitas sistem"),
            ("Kemudahan Pengelolaan Dokumen", "Mengelola dokumentasi berbagai standar dalam satu sistem terpadu")
        ],
        "process_step2": "Tim kami memberikan pelatihan integrasi sistem manajemen, mendampingi penyusunan dokumentasi terintegrasi, gap analysis multi-standar, dan implementasi IMS di seluruh proses organisasi.",
        "target_title": "Siapa yang Membutuhkan IMS?",
        "target_desc": "IMS dapat diterapkan oleh organisasi yang telah atau akan menerapkan beberapa standar sistem manajemen secara bersamaan.",
        "targets": [
            "Perusahaan Manufaktur",
            "Perusahaan Konstruksi",
            "Lembaga Kesehatan",
            "Perusahaan Energi dan Tambang",
            "Perusahaan Jasa dan Konsultan",
            "Lembaga Pendidikan",
            "Perusahaan Teknologi Informasi",
            "Lembaga Pemerintahan",
            "Organisasi Multi-Sertifikasi"
        ],
        "target_footer": "IMS cocok untuk organisasi yang ingin mengoptimalkan pengelolaan berbagai sistem manajemen dalam satu kerangka kerja yang efisien."
    },
    "lainnya": {
        "title": "Jasa Konsultasi Sertifikasi Sistem Manajemen ISO/IEC/SNI Lainnya",
        "year": "",
        "breadcrumb": "ISO/IEC/SNI Lainnya",
        "benefit_highlights": [
            "Dukungan untuk Berbagai<br>Standar ISO/IEC/SNI",
            "Konsultasi yang Disesuaikan<br>dengan Kebutuhan Spesifik",
            "Pengalaman Luas di Berbagai<br>Sektor Industri"
        ],
        "definition": "Kami menyediakan jasa konsultasi untuk berbagai standar sistem manajemen ISO/IEC/SNI lainnya yang belum tercantum secara spesifik, dengan pendekatan yang disesuaikan dengan kebutuhan unik organisasi Anda di berbagai sektor industri.",
        "benefits": [
            ("Dukungan Multi-Standar", "Menyediakan konsultasi untuk berbagai standar ISO/IEC/SNI yang beragam"),
            ("Konsultasi yang Fleksibel", "Menyesuaikan pendekatan dengan kebutuhan dan karakteristik organisasi"),
            ("Konsultan Berpengalaman", "Didukung oleh tim konsultan dengan keahlian di berbagai standar"),
            ("Meningkatkan Daya Saing", "Membantu organisasi memenuhi persyaratan tender dan pasar global"),
            ("Memenuhi Persyaratan Regulasi", "Membantu kepatuhan terhadap peraturan industri yang berlaku"),
            ("Perbaikan Berkelanjutan", "Mendorong budaya peningkatan kinerja organisasi secara konsisten")
        ],
        "process_step2": "Tim kami memberikan pelatihan persyaratan standar yang relevan, mendampingi penyusunan dokumentasi sistem manajemen, dan implementasi standar sesuai kebutuhan spesifik organisasi Anda.",
        "target_title": "Standar ISO/IEC/SNI yang Kami Layani",
        "target_desc": "Kami menyediakan konsultasi untuk berbagai standar sistem manajemen sesuai kebutuhan industri Anda.",
        "targets": [
            "ISO 31000 - Manajemen Risiko",
            "ISO 28000 - Supply Chain Security",
            "ISO 41001 - Facility Management",
            "ISO 56002 - Innovation Management",
            "ISO 26000 - Social Responsibility",
            "SNI 19-17025 - Laboratorium",
            "ISO 15189 - Laboratorium Medik",
            "Dan Standar ISO/IEC/SNI Lainnya",
            "Konsultasikan Kebutuhan Anda"
        ],
        "target_footer": "Hubungi kami untuk mendiskusikan kebutuhan sertifikasi standar ISO/IEC/SNI spesifik yang Anda butuhkan."
    }
}

def update_iso_page(filename, iso_num, data):
    """Update ISO page with new content"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update title
        content = re.sub(r'<title>.*?</title>', f'<title>{data["title"]} — INOVASS</title>', content)
        
        # Update breadcrumb
        content = re.sub(r'<span class="breadcrumb-current"[^>]*>.*?</span>',
                        f'<span class="breadcrumb-current" style="color: #00e0a0 !important;">{data["breadcrumb"]}</span>', content)
        
        # Update page title
        content = re.sub(r'<h1 class="detail-page-title"[^>]*>.*?</h1>',
                        f'<h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important; font-weight: 700 !important;">{data["title"]}</h1>', content)
        
        # Update benefit highlights title
        year_text = f" {iso_num}:{data['year']}" if data['year'] else f" {iso_num}"
        if iso_num == "ims":
            year_text = " IMS"
        elif iso_num == "lainnya":
            year_text = " ISO/IEC/SNI"
        
        content = re.sub(r'<h2 class="benefit-highlight-title">Dengan ISO .*? Organisasi Anda Dapat:</h2>',
                        f'<h2 class="benefit-highlight-title">Dengan{year_text} Organisasi Anda Dapat:</h2>', content)
        
        # Update benefit highlight cards
        benefit_cards = '\n          '.join([f'<div class="benefit-highlight-card">\n            <p>{b}</p>\n          </div>' for b in data["benefit_highlights"]])
        content = re.sub(r'(<div class="benefit-highlight-grid">)(.*?)(</div>\s*</div>\s*<!-- PENGERTIAN)',
                        f'\\1\n          {benefit_cards}\n        \\3', content, flags=re.DOTALL)
        
        # Update pengertian title
        title_text = f"ISO {iso_num}:{data['year']}" if data['year'] else data['breadcrumb']
        content = re.sub(r'<h2 class="iso-content-title">Pengertian ISO.*?</h2>',
                        f'<h2 class="iso-content-title">Pengertian {title_text}</h2>', content)
        
        # Update pengertian description
        strong_text = f"<strong>{title_text}</strong>" if data['year'] or iso_num in ['ims', 'lainnya'] else f"<strong>{data['breadcrumb']}</strong>"
        content = re.sub(r'(<p class="iso-content-desc">)\s*<strong>ISO.*?</strong>.*?(</p>)',
                        f'\\1\n            {strong_text} {data["definition"]}\n          \\2', content, flags=re.DOTALL)
        
        # Update manfaat title
        manfaat_title = f"Manfaat Implementasi {data['breadcrumb']}" if iso_num in ['ims', 'lainnya'] else f"Manfaat Implementasi ISO {iso_num}"
        content = re.sub(r'<h2 class="iso-benefit-section-title">Manfaat Implementasi ISO.*?</h2>',
                        f'<h2 class="iso-benefit-section-title">{manfaat_title}</h2>', content)
        
        # Update benefit cards
        benefit_cards_html = '\n          '.join([f'<div class="iso-benefit-modern-card">\n            <h3>{t}</h3>\n            <p>{d}</p>\n          </div>' for t, d in data["benefits"]])
        content = re.sub(r'(<div class="iso-benefits-modern-grid">)(.*?)(</div>\s*</div>\s*<!-- CTA)',
                        f'\\1\n          {benefit_cards_html}\n        \\3', content, flags=re.DOTALL)
        
        # Update process title
        process_title = f"Proses Sertifikasi {title_text}" if data['year'] else f"Proses {data['breadcrumb']}"
        content = re.sub(r'<h2 class="iso-process-title">Proses Sertifikasi ISO.*?</h2>',
                        f'<h2 class="iso-process-title">{process_title}</h2>', content)
        
        # Update process step 1
        step1_text = f"menerapkan {data['breadcrumb']}" if iso_num in ['ims', 'lainnya'] else f"menerapkan Sistem Manajemen {title_text}"
        content = re.sub(r'(<h3>Konsultasi & Perencanaan</h3>\s*<p>).*?(</p>)',
                        f'\\1Kami melakukan assessment awal untuk menilai kesiapan organisasi dalam {step1_text}, mengidentifikasi gap terhadap persyaratan standar, dan menyusun roadmap implementasi yang sesuai dengan kebutuhan organisasi.\\2', content, flags=re.DOTALL)
        
        # Update process step 2
        content = re.sub(r'(<h3>Pelatihan & Implementasi</h3>\s*<p>).*?(</p>)',
                        f'\\1{data["process_step2"]}\\2', content, flags=re.DOTALL)
        
        # Update process step 3
        content = re.sub(r'(<h3>Audit Internal & Tinjauan Manajemen</h3>\s*<p>).*?(</p>)',
                        f'\\1Organisasi melaksanakan audit internal dan tinjauan manajemen untuk memastikan sistem telah diterapkan secara efektif dan siap menghadapi audit sertifikasi.\\2', content, flags=re.DOTALL)
        
        # Update process step 5
        cert_text = f"Sertifikat {title_text}" if data['year'] else f"Sertifikat {data['breadcrumb']}"
        content = re.sub(r'(<h3>Penerbitan Sertifikat</h3>\s*<p>).*?(</p>)',
                        f'\\1Setelah proses audit selesai dan seluruh ketidaksesuaian (jika ada) telah ditindaklanjuti, lembaga sertifikasi menerbitkan {cert_text} yang berlaku selama tiga tahun.\\2', content, flags=re.DOTALL)
        
        # Update target title
        content = re.sub(r'<h2 class="iso-target-section-title"[^>]*>Siapa yang .*?</h2>',
                        f'<h2 class="iso-target-section-title" style="margin-bottom: 3rem;">{data["target_title"]}</h2>', content)
        
        # Update target description
        content = re.sub(r'(<p class="iso-target-description">).*?(</p>)',
                        f'\\1\n          {data["target_desc"]}\n        \\2', content, flags=re.DOTALL)
        
        # Update target cards
        target_cards_html = '\n          '.join([f'<div class="iso-target-card"><h4>{t}</h4></div>' for t in data["targets"]])
        content = re.sub(r'(<div class="iso-target-grid">)(.*?)(</div>\s*<p class="iso-target-footer">)',
                        f'\\1\n          {target_cards_html}\n        \\3', content, flags=re.DOTALL)
        
        # Update target footer
        content = re.sub(r'(<p class="iso-target-footer">).*?(</p>)',
                        f'\\1\n          {data["target_footer"]}\n        \\2', content, flags=re.DOTALL)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Updated {filename}")
        return True
        
    except Exception as e:
        print(f"✗ Error updating {filename}: {e}")
        return False

# File mappings
file_mappings = {
    "39001": "layanan-detail-iso-39001.html",
    "10002": "layanan-detail-iso-10002.html",
    "30301": "layanan-detail-iso-30301.html",
    "20000-1": "layanan-detail-iso-20000-1.html",
    "35001": "layanan-detail-iso-35001.html",
    "ims": "layanan-detail-ims.html",
    "lainnya": "layanan-detail-iso-lainnya.html"
}

print("Updating 7 new ISO standard pages...")
print("=" * 50)

for iso_num, filename in file_mappings.items():
    data = iso_standards[iso_num]
    update_iso_page(filename, iso_num, data)

print("=" * 50)
print("Update complete!")
