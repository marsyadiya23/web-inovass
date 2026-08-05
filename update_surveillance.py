#!/usr/bin/env python3
import re

iso_data = {
    '9001': {
        'title': 'ISO/SNI 9001 – Sistem Manajemen Mutu',
        'year': '2015',
        'benefits': ['Mempertahankan<br>Sertifikasi', 'Kesiapan Audit<br>Surveillance', 'Continuous Improvement<br>Terjaga'],
        'description': 'Jasa Konsultasi Persiapan Audit Surveillance ISO/SNI 9001:2015 adalah layanan profesional yang membantu organisasi mempersiapkan audit surveillance (pengawasan) untuk mempertahankan sertifikasi, memastikan kesesuaian berkelanjutan dengan persyaratan standar, dan menunjukkan peningkatan berkelanjutan sistem manajemen mutu.',
        'benefit_title': 'Manfaat Konsultasi Persiapan Audit Surveillance ISO 9001',
        'benefit_items': [
            ('Kesiapan Audit Surveillance', 'Mempersiapkan organisasi menghadapi audit surveillance dengan confidence'),
            ('Gap Analysis Pre-Surveillance', 'Mengidentifikasi gap dan ketidaksesuaian sebelum audit surveillance'),
            ('Perbaikan Proaktif', 'Melakukan perbaikan sistem sebelum audit surveillance dilakukan'),
            ('Pemeliharaan Sertifikasi', 'Mempertahankan status sertifikasi ISO 9001 organisasi'),
            ('Evidence Preparation', 'Menyiapkan bukti objektif dan dokumentasi untuk audit surveillance'),
            ('Continuous Improvement Support', 'Memastikan peningkatan berkelanjutan terlihat oleh auditor')
        ],
        'cta': 'Persiapan Audit Surveillance',
        'cta_desc': 'Konsultasikan persiapan audit surveillance ISO 9001 Anda bersama tim konsultan berpengalaman INOVASS. Kami siap membantu organisasi Anda mempertahankan sertifikasi.',
        'scope': ['Review Sistem Manajemen', 'Gap Analysis', 'Corrective Actions Review', 'Management Review', 'Internal Audit Results', 'Customer Satisfaction', 'Process Performance', 'Continual Improvement', 'Evidence Preparation']
    },
    '14001': {
        'title': 'ISO/SNI 14001 – Sistem Manajemen Lingkungan',
        'year': '2015',
        'benefits': ['Mempertahankan<br>Sertifikasi', 'Kepatuhan Lingkungan<br>Terjaga', 'Kinerja Lingkungan<br>Meningkat'],
        'description': 'Jasa Konsultasi Persiapan Audit Surveillance ISO/SNI 14001:2015 adalah layanan profesional yang membantu organisasi mempersiapkan audit surveillance untuk mempertahankan sertifikasi lingkungan, memastikan kepatuhan berkelanjutan terhadap aspek lingkungan, dan mendemonstrasikan peningkatan kinerja lingkungan.',
        'cta': 'Persiapan Audit Surveillance Lingkungan',
        'cta_desc': 'Konsultasikan persiapan audit surveillance ISO 14001 Anda bersama tim konsultan lingkungan berpengalaman INOVASS. Kami siap membantu organisasi Anda mempertahankan sertifikasi lingkungan.',
        'scope': ['Review Aspek Lingkungan', 'Kepatuhan Regulasi', 'Environmental Performance', 'Corrective Actions', 'Environmental Objectives', 'Waste & Emission Data', 'Emergency Preparedness', 'Interested Parties', 'Evidence Preparation']
    },
    '45001': {
        'title': 'ISO 45001 – Sistem Manajemen Keselamatan dan Kesehatan Kerja (SMK3)',
        'year': '2018',
        'benefits': ['Mempertahankan<br>Sertifikasi SMK3', 'Keselamatan Kerja<br>Terjaga', 'Zero Accident<br>Maintenance'],
        'description': 'Jasa Konsultasi Persiapan Audit Surveillance ISO 45001:2018 adalah layanan profesional yang membantu organisasi mempersiapkan audit surveillance SMK3 untuk mempertahankan sertifikasi, memastikan keselamatan kerja berkelanjutan, dan mendemonstrasikan pencegahan kecelakaan kerja yang efektif.',
        'cta': 'Persiapan Audit Surveillance K3',
        'cta_desc': 'Konsultasikan persiapan audit surveillance ISO 45001 Anda bersama tim konsultan K3 berpengalaman INOVASS. Kami siap membantu organisasi Anda mempertahankan sertifikasi SMK3.',
        'scope': ['Review HIRARC', 'Incident Investigation', 'OH&S Performance', 'Worker Consultation', 'Corrective Actions K3', 'Training Records', 'PPE Management', 'Emergency Drill Results', 'Evidence Preparation']
    },
    '22000': {
        'title': 'ISO 22000 – Sistem Manajemen Keamanan Pangan',
        'year': '2018',
        'benefits': ['Mempertahankan<br>Sertifikasi Pangan', 'Keamanan Pangan<br>Konsisten', 'HACCP Compliance<br>Terjaga'],
        'description': 'Jasa Konsultasi Persiapan Audit Surveillance ISO 22000:2018 adalah layanan profesional yang membantu organisasi pangan mempersiapkan audit surveillance untuk mempertahankan sertifikasi keamanan pangan, memastikan HACCP compliance berkelanjutan, dan mendemonstrasikan keamanan produk pangan.',
        'cta': 'Persiapan Audit Surveillance Keamanan Pangan',
        'cta_desc': 'Konsultasikan persiapan audit surveillance ISO 22000 Anda bersama tim konsultan keamanan pangan berpengalaman INOVASS. Kami siap membantu organisasi Anda mempertahankan sertifikasi.',
        'scope': ['Review HACCP Plan', 'PRPs Implementation', 'Verification Results', 'Corrective Actions', 'Food Safety Performance', 'Traceability Records', 'Supplier Management', 'Customer Complaints', 'Evidence Preparation']
    },
    '27001': {
        'title': 'ISO/IEC 27001 – Sistem Manajemen Keamanan Informasi',
        'year': '2022',
        'benefits': ['Mempertahankan<br>Sertifikasi ISMS', 'Keamanan Informasi<br>Terjaga', 'Cyber Security<br>Maintained'],
        'description': 'Jasa Konsultasi Persiapan Audit Surveillance ISO/IEC 27001:2022 adalah layanan profesional yang membantu organisasi mempersiapkan audit surveillance ISMS untuk mempertahankan sertifikasi keamanan informasi, memastikan proteksi aset informasi berkelanjutan, dan mendemonstrasikan efektivitas kontrol keamanan.',
        'cta': 'Persiapan Audit Surveillance Keamanan Informasi',
        'cta_desc': 'Konsultasikan persiapan audit surveillance ISO 27001 Anda bersama tim konsultan keamanan informasi berpengalaman INOVASS. Kami siap membantu organisasi Anda mempertahankan sertifikasi ISMS.',
        'scope': ['Review Risk Assessment', 'Annex A Controls', 'Security Incidents', 'Corrective Actions', 'SoA Updates', 'Access Control Review', 'Vulnerability Management', 'Security Awareness', 'Evidence Preparation']
    },
    '22301': {
        'title': 'ISO 22301 – Sistem Manajemen Keberlangsungan Bisnis (BCMS)',
        'year': '2019',
        'benefits': ['Mempertahankan<br>Sertifikasi BCMS', 'Business Continuity<br>Maintained', 'Resilience<br>Demonstrated'],
        'description': 'Jasa Konsultasi Persiapan Audit Surveillance ISO 22301:2019 adalah layanan profesional yang membantu organisasi mempersiapkan audit surveillance BCMS untuk mempertahankan sertifikasi keberlangsungan bisnis, memastikan kesiapan continuity plan, dan mendemonstrasikan ketahanan organisasi.',
        'cta': 'Persiapan Audit Surveillance BCMS',
        'cta_desc': 'Konsultasikan persiapan audit surveillance ISO 22301 Anda bersama tim konsultan BCMS berpengalaman INOVASS. Kami siap membantu organisasi Anda mempertahankan sertifikasi keberlangsungan bisnis.',
        'scope': ['Review BIA', 'BC Plans Updates', 'Exercise & Testing Results', 'Corrective Actions', 'Recovery Strategies', 'Communication Plans', 'Supplier Continuity', 'Lessons Learned', 'Evidence Preparation']
    },
    '37001': {
        'title': 'ISO 37001 – Sistem Manajemen Anti Penyuapan',
        'year': '2016',
        'benefits': ['Mempertahankan<br>Sertifikasi ABMS', 'Anti-Bribery<br>Compliance', 'Integrity<br>Maintained'],
        'description': 'Jasa Konsultasi Persiapan Audit Surveillance ISO 37001:2016 adalah layanan profesional yang membantu organisasi mempersiapkan audit surveillance anti penyuapan untuk mempertahankan sertifikasi, memastikan compliance berkelanjutan, dan mendemonstrasikan efektivitas kontrol anti penyuapan.',
        'cta': 'Persiapan Audit Surveillance Anti Penyuapan',
        'cta_desc': 'Konsultasikan persiapan audit surveillance ISO 37001 Anda bersama tim konsultan anti penyuapan berpengalaman INOVASS. Kami siap membantu organisasi Anda mempertahankan sertifikasi.',
        'scope': ['Review Risk Assessment', 'Due Diligence Records', 'Bribery Incidents', 'Corrective Actions', 'Gifts & Hospitality', 'Whistleblowing Reports', 'Training Records', 'Third Party Management', 'Evidence Preparation']
    },
    '37301': {
        'title': 'ISO 37301 – Sistem Manajemen Kepatuhan',
        'year': '2021',
        'benefits': ['Mempertahankan<br>Sertifikasi CMS', 'Regulatory Compliance<br>Maintained', 'Legal Risk<br>Mitigated'],
        'description': 'Jasa Konsultasi Persiapan Audit Surveillance ISO 37301:2021 adalah layanan profesional yang membantu organisasi mempersiapkan audit surveillance kepatuhan untuk mempertahankan sertifikasi, memastikan compliance obligation terpenuhi, dan mendemonstrasikan efektivitas sistem manajemen kepatuhan.',
        'cta': 'Persiapan Audit Surveillance Kepatuhan',
        'cta_desc': 'Konsultasikan persiapan audit surveillance ISO 37301 Anda bersama tim konsultan kepatuhan berpengalaman INOVASS. Kami siap membantu organisasi Anda mempertahankan sertifikasi.',
        'scope': ['Compliance Obligation Review', 'Regulatory Updates', 'Compliance Testing', 'Corrective Actions', 'Legal Register', 'Compliance Training', 'Non-Compliance Reports', 'Regulatory Changes', 'Evidence Preparation']
    }
}

def update_file(iso_num, data):
    filename = f'layanan-detail-konsultasi-surveillance-iso-{iso_num}.html'
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        year_text = f':{data["year"]}'
        
        # Update title
        content = re.sub(
            r'<title>.*?</title>',
            f'<title>Jasa Konsultasi Persiapan Audit Surveillance {data["title"]} — INOVASS</title>',
            content
        )
        
        # Update breadcrumb - change to surveillance
        breadcrumb_text = data["title"].split(" – ")[0]
        content = re.sub(
            r'<span class="breadcrumb-current"[^>]*>.*?</span>',
            f'<span class="breadcrumb-current" style="color: #00e0a0 !important;">Konsultasi Surveillance {breadcrumb_text}</span>',
            content
        )
        
        # Update H1
        content = re.sub(
            r'(<h1 class="detail-page-title"[^>]*>).*?(</h1>)',
            f'\\1Jasa Konsultasi Persiapan Audit Surveillance {data["title"]}\\2',
            content
        )
        
        # Update benefit title
        content = re.sub(
            r'(<h2 class="benefit-highlight-title">).*?(<)',
            f'\\1Dengan Jasa Konsultasi Persiapan Audit Surveillance {data["title"].split(" – ")[0]}{year_text} Organisasi Anda Dapat:\\2',
            content
        )
        
        # Update pengertian title
        content = re.sub(
            r'(<h2 class="iso-content-title">).*?(</h2>)',
            f'\\1Pengertian Jasa Konsultasi Persiapan Audit Surveillance {data["title"].split(" – ")[0]}{year_text}\\2',
            content
        )
        
        # Update description
        content = re.sub(
            r'(<p class="iso-content-desc">\s*).*?(?=\s*</p>)',
            f'\\1{data["description"]}',
            content,
            flags=re.DOTALL
        )
        
        # Update benefit section title
        content = re.sub(
            r'(<h2 class="iso-benefit-section-title">).*?(</h2>)',
            f'\\1Manfaat Konsultasi Persiapan Audit Surveillance {data["title"].split(" – ")[0].replace("ISO/SNI", "ISO").replace("ISO/IEC", "ISO")}\\2',
            content
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
        
        # Update process title to "Persiapan"
        content = re.sub(
            r'(<h2 class="iso-process-title">).*?(</h2>)',
            f'\\1Proses Konsultasi Persiapan Audit Surveillance {data["title"].split(" – ")[0]}{year_text}\\2',
            content
        )
        
        # Update target section title
        content = re.sub(
            r'(<h2 class="iso-target-section-title"[^>]*>).*?(</h2>)',
            f'\\1Fokus Persiapan Audit Surveillance {data["title"].split(" – ")[0].replace("ISO/SNI", "ISO").replace("ISO/IEC", "ISO")}\\2',
            content
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

print(f'\n🎉 Successfully updated {success_count}/{len(iso_data)} surveillance files!')
