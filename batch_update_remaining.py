#!/usr/bin/env python3
# Script untuk update 10 halaman audit internal ISO tersisa

import re

iso_data = {
    '55001': {
        'title': 'ISO 55001 – Sistem Manajemen Aset',
        'year': '2014',
        'benefits': ['Mengoptimalkan Nilai<br>Aset', 'Meningkatkan ROI<br>Aset', 'Mengurangi Risiko<br>Aset'],
        'description': 'Jasa Audit Internal ISO 55001:2014 adalah layanan profesional yang membantu organisasi melakukan evaluasi sistematis terhadap efektivitas penerapan Sistem Manajemen Aset, mengoptimalkan nilai aset sepanjang lifecycle, meningkatkan ROI aset, dan mengurangi risiko kegagalan aset organisasi.',
        'cta': 'Manajemen Aset',
        'cta_desc': 'Konsultasikan kebutuhan audit internal ISO 55001 Anda bersama tim auditor manajemen aset berpengalaman INOVASS. Kami siap membantu organisasi Anda mengoptimalkan nilai aset.',
        'scope': ['Konteks Organisasi', 'Kepemimpinan & Komitmen', 'Asset Management Policy', 'Asset Lifecycle Management', 'Asset Performance', 'Risk Management Aset', 'Asset Portfolio Optimization', 'Monitoring & Review', 'Peningkatan Berkelanjutan']
    },
    '21001': {
        'title': 'ISO 21001 – Sistem Manajemen Organisasi Pendidikan',
        'year': '2018',
        'benefits': ['Meningkatkan Kualitas<br>Pendidikan', 'Kepuasan Peserta<br>Didik', 'Akreditasi & Reputasi<br>Institusi'],
        'description': 'Jasa Audit Internal ISO 21001:2018 adalah layanan profesional yang membantu organisasi pendidikan melakukan evaluasi sistematis terhadap efektivitas penerapan Sistem Manajemen Organisasi Pendidikan (EOMS), meningkatkan kualitas pembelajaran, kepuasan peserta didik, dan reputasi institusi pendidikan.',
        'cta': 'Kualitas Pendidikan',
        'cta_desc': 'Konsultasikan kebutuhan audit internal ISO 21001 Anda bersama tim auditor pendidikan berpengalaman INOVASS. Kami siap membantu institusi Anda meningkatkan kualitas pembelajaran.',
        'scope': ['Konteks Organisasi', 'Kepemimpinan Pendidikan', 'Kebutuhan Peserta Didik', 'Kurikulum & Pembelajaran', 'Kompetensi Pendidik', 'Fasilitas Pembelajaran', 'Kepuasan Stakeholder', 'Evaluasi Pembelajaran', 'Peningkatan Berkelanjutan']
    },
    '13485': {
        'title': 'ISO 13485 – Sistem Manajemen Mutu Alat Kesehatan',
        'year': '2016',
        'benefits': ['Keamanan Alat<br>Kesehatan', 'Kepatuhan Regulasi<br>Medis', 'Kualitas Produk<br>Medis'],
        'description': 'Jasa Audit Internal ISO 13485:2016 adalah layanan profesional yang membantu organisasi manufaktur alat kesehatan melakukan evaluasi sistematis terhadap efektivitas penerapan Sistem Manajemen Mutu Alat Kesehatan, memastikan keamanan dan efektivitas produk medis, serta kepatuhan terhadap regulasi kesehatan.',
        'cta': 'Mutu Alat Kesehatan',
        'cta_desc': 'Konsultasikan kebutuhan audit internal ISO 13485 Anda bersama tim auditor alat kesehatan berpengalaman INOVASS. Kami siap membantu organisasi Anda memastikan keamanan produk medis.',
        'scope': ['Konteks Organisasi', 'Tanggung Jawab Manajemen', 'Manajemen Risiko Medis', 'Desain & Pengembangan', 'Kontrol Produksi', 'Validasi Proses', 'Ketertelusuran Produk', 'Post-Market Surveillance', 'Peningkatan Berkelanjutan']
    },
    '39001': {
        'title': 'ISO 39001 – Sistem Manajemen Keselamatan Lalu Lintas Jalan',
        'year': '2012',
        'benefits': ['Mengurangi Kecelakaan<br>Lalu Lintas', 'Keselamatan Pengguna<br>Jalan', 'Kepatuhan Regulasi<br>Transportasi'],
        'description': 'Jasa Audit Internal ISO 39001:2012 adalah layanan profesional yang membantu organisasi transportasi melakukan evaluasi sistematis terhadap efektivitas penerapan Sistem Manajemen Keselamatan Lalu Lintas Jalan (RTS-MS), mengurangi kecelakaan lalu lintas, dan meningkatkan keselamatan pengguna jalan.',
        'cta': 'Keselamatan Lalu Lintas',
        'cta_desc': 'Konsultasikan kebutuhan audit internal ISO 39001 Anda bersama tim auditor keselamatan transportasi berpengalaman INOVASS. Kami siap membantu organisasi Anda mengurangi kecelakaan lalu lintas.',
        'scope': ['Konteks Organisasi', 'Kepemimpinan & Komitmen', 'Road Traffic Safety Performance', 'Risk Management Lalu Lintas', 'Safety Action Plans', 'Driver Safety Management', 'Vehicle Safety', 'Emergency Response', 'Peningkatan Berkelanjutan']
    },
    '10002': {
        'title': 'ISO 10002 – Sistem Manajemen Penanganan Keluhan Pelanggan',
        'year': '2018',
        'benefits': ['Kepuasan Pelanggan<br>Meningkat', 'Penanganan Keluhan<br>Efektif', 'Loyalitas Pelanggan<br>Tinggi'],
        'description': 'Jasa Audit Internal ISO 10002:2018 adalah layanan profesional yang membantu organisasi melakukan evaluasi sistematis terhadap efektivitas penerapan Sistem Manajemen Penanganan Keluhan Pelanggan, meningkatkan kepuasan pelanggan, menangani keluhan secara efektif, dan membangun loyalitas pelanggan.',
        'cta': 'Penanganan Keluhan Pelanggan',
        'cta_desc': 'Konsultasikan kebutuhan audit internal ISO 10002 Anda bersama tim auditor customer service berpengalaman INOVASS. Kami siap membantu organisasi Anda meningkatkan kepuasan pelanggan.',
        'scope': ['Konteks Organisasi', 'Kepemimpinan & Komitmen', 'Kebijakan Penanganan Keluhan', 'Proses Penerimaan Keluhan', 'Investigasi & Resolusi', 'Komunikasi dengan Pelanggan', 'Monitoring & Tracking', 'Analisis Keluhan', 'Peningkatan Berkelanjutan']
    },
    '30301': {
        'title': 'ISO 30301 – Sistem Manajemen Pengelolaan Arsip',
        'year': '2019',
        'benefits': ['Pengelolaan Arsip<br>Efektif', 'Kepatuhan Regulasi<br>Arsip', 'Akses Informasi<br>Cepat'],
        'description': 'Jasa Audit Internal ISO 30301:2019 adalah layanan profesional yang membantu organisasi melakukan evaluasi sistematis terhadap efektivitas penerapan Sistem Manajemen Pengelolaan Arsip (MSR), memastikan pengelolaan dokumen dan arsip yang efektif, kepatuhan regulasi, dan kemudahan akses informasi.',
        'cta': 'Pengelolaan Arsip',
        'cta_desc': 'Konsultasikan kebutuhan audit internal ISO 30301 Anda bersama tim auditor manajemen arsip berpengalaman INOVASS. Kami siap membantu organisasi Anda mengelola arsip secara efektif.',
        'scope': ['Konteks Organisasi', 'Kepemimpinan & Komitmen', 'Records Management Policy', 'Klasifikasi & Penamaan', 'Retensi & Disposal', 'Keamanan Arsip', 'Akses & Retrieval', 'Preservasi Jangka Panjang', 'Peningkatan Berkelanjutan']
    },
    '20000-1': {
        'title': 'ISO/IEC 20000-1 – Sistem Manajemen Layanan Teknologi Informasi',
        'year': '2018',
        'benefits': ['Kualitas Layanan<br>IT Meningkat', 'Kepatuhan IT<br>Governance', 'Kepuasan Pengguna<br>IT'],
        'description': 'Jasa Audit Internal ISO/IEC 20000-1:2018 adalah layanan profesional yang membantu organisasi IT melakukan evaluasi sistematis terhadap efektivitas penerapan Sistem Manajemen Layanan Teknologi Informasi (IT Service Management), meningkatkan kualitas layanan IT, dan kepuasan pengguna layanan IT.',
        'cta': 'Layanan Teknologi Informasi',
        'cta_desc': 'Konsultasikan kebutuhan audit internal ISO 20000-1 Anda bersama tim auditor IT service management berpengalaman INOVASS. Kami siap membantu organisasi Anda meningkatkan kualitas layanan IT.',
        'scope': ['Konteks Organisasi', 'Kepemimpinan & Komitmen', 'Service Portfolio Management', 'Service Level Management', 'Incident & Problem Management', 'Change Management', 'Service Desk', 'IT Security Management', 'Peningkatan Berkelanjutan']
    },
    '35001': {
        'title': 'ISO 35001 – Sistem Manajemen Biorisiko Laboratorium',
        'year': '2019',
        'benefits': ['Keamanan Biorisiko<br>Laboratorium', 'Kepatuhan Biosafety<br>Biosecurity', 'Perlindungan Personel<br>Lab'],
        'description': 'Jasa Audit Internal ISO 35001:2019 adalah layanan profesional yang membantu laboratorium melakukan evaluasi sistematis terhadap efektivitas penerapan Sistem Manajemen Biorisiko, memastikan keamanan biologis (biosafety) dan keamanan biologis (biosecurity), serta melindungi personel dan lingkungan.',
        'cta': 'Biorisiko Laboratorium',
        'cta_desc': 'Konsultasikan kebutuhan audit internal ISO 35001 Anda bersama tim auditor biosafety berpengalaman INOVASS. Kami siap membantu laboratorium Anda mengelola biorisiko secara efektif.',
        'scope': ['Konteks Organisasi', 'Kepemimpinan & Komitmen', 'Biosafety Risk Assessment', 'Biosecurity Risk Assessment', 'Containment & Engineering Controls', 'PPE & Work Practices', 'Emergency Response Biohazard', 'Training & Competence', 'Peningkatan Berkelanjutan']
    },
    'ims': {
        'title': 'Integrated Management System (IMS) ISO/IEC/SNI',
        'year': '',
        'benefits': ['Efisiensi Sistem<br>Manajemen', 'Integrasi Multi<br>Standar', 'Optimalisasi Sumber<br>Daya'],
        'description': 'Jasa Audit Internal Integrated Management System (IMS) ISO/IEC/SNI adalah layanan profesional yang membantu organisasi melakukan evaluasi sistematis terhadap efektivitas penerapan sistem manajemen terintegrasi (multiple standards), meningkatkan efisiensi, mengurangi duplikasi, dan mengoptimalkan sumber daya organisasi.',
        'cta': 'Integrated Management System',
        'cta_desc': 'Konsultasikan kebutuhan audit internal IMS Anda bersama tim auditor multi-standar berpengalaman INOVASS. Kami siap membantu organisasi Anda mengintegrasikan multiple standards secara efektif.',
        'scope': ['Konteks Organisasi Terintegrasi', 'Kepemimpinan Multi-Standar', 'Risk-Based Thinking', 'Integrated Documentation', 'Unified Objectives', 'Common Processes', 'Integrated Monitoring', 'Management Review Terintegrasi', 'Peningkatan Berkelanjutan']
    },
    'lainnya': {
        'title': 'Sistem Manajemen ISO/IEC/SNI Lainnya',
        'year': '',
        'benefits': ['Audit Sesuai<br>Kebutuhan', 'Fleksibilitas<br>Standar', 'Solusi Custom<br>Audit'],
        'description': 'Jasa Audit Internal Sistem Manajemen ISO/IEC/SNI Lainnya adalah layanan profesional yang membantu organisasi melakukan evaluasi sistematis terhadap efektivitas penerapan sistem manajemen berbagai standar ISO/IEC/SNI lainnya sesuai kebutuhan spesifik organisasi dan industri.',
        'cta': 'Sistem Manajemen Organisasi',
        'cta_desc': 'Konsultasikan kebutuhan audit internal sistem manajemen Anda bersama tim auditor berpengalaman INOVASS. Kami siap membantu organisasi Anda dengan berbagai standar ISO/IEC/SNI.',
        'scope': ['Konteks Organisasi', 'Kepemimpinan & Komitmen', 'Perencanaan Sistem', 'Dukungan & Sumber Daya', 'Operasi & Kontrol', 'Evaluasi Kinerja', 'Monitoring & Measurement', 'Audit Internal', 'Peningkatan Berkelanjutan']
    }
}

def update_file(iso_num, data):
    filename = f'layanan-detail-audit-internal-iso-{iso_num}.html'
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        year_text = f':{data["year"]}' if data["year"] else ''
        
        # Update title
        content = re.sub(
            r'<title>.*?</title>',
            f'<title>Jasa Audit Internal {data["title"]} — INOVASS</title>',
            content
        )
        
        # Update breadcrumb
        breadcrumb_text = data["title"].split(" – ")[0]
        content = re.sub(
            r'<span class="breadcrumb-current"[^>]*>.*?</span>',
            f'<span class="breadcrumb-current" style="color: #00e0a0 !important;">Audit Internal {breadcrumb_text}</span>',
            content
        )
        
        # Update H1
        content = re.sub(
            r'(<h1 class="detail-page-title"[^>]*>).*?(</h1>)',
            f'\\1Jasa Audit Internal {data["title"]}\\2',
            content
        )
        
        # Update benefit title
        content = re.sub(
            r'(<h2 class="benefit-highlight-title">)Dengan Jasa Audit Internal.*?(<)',
            f'\\1Dengan Jasa Audit Internal {data["title"].split(" – ")[0]}{year_text} Organisasi Anda Dapat:\\2',
            content
        )
        
        # Update pengertian title
        content = re.sub(
            r'(<h2 class="iso-content-title">)Pengertian Jasa Audit Internal.*?(</h2>)',
            f'\\1Pengertian Jasa Audit Internal {data["title"].split(" – ")[0]}{year_text}\\2',
            content
        )
        
        # Update description
        content = re.sub(
            r'(<p class="iso-content-desc">\s*).*?(?=\s*</p>)',
            f'\\1{data["description"]}',
            content,
            flags=re.DOTALL
        )
        
        # Update CTA
        content = re.sub(
            r'(<h2>Siap Meningkatkan <em>).*?(</em>)',
            f'\\1{data["cta"]}\\2',
            content
        )
        
        content = re.sub(
            r'(<section class="page-cta">.*?<p>).*?(?=</p>)',
            f'\\1{data["cta_desc"]}',
            content,
            flags=re.DOTALL
        )
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f'✅ Updated {filename}')
        return True
        
    except Exception as e:
        print(f'❌ Error updating {filename}: {e}')
        return False

# Update all files
success_count = 0
for iso_num, data in iso_data.items():
    if update_file(iso_num, data):
        success_count += 1

print(f'\n🎉 Successfully updated {success_count}/{len(iso_data)} files!')
