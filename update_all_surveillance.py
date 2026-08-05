#!/usr/bin/env python3
"""Update all 11 surveillance pages with specific content"""
import re

def update_file(filename, data):
    """Update a surveillance file with specific data"""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update title tag
    content = re.sub(
        r'<title>.*?</title>',
        f'<title>Jasa Konsultasi Persiapan Audit Surveillance {data["title"]} – {data["system"]} — INOVASS</title>',
        content, flags=re.DOTALL
    )
    
    # Update breadcrumb
    content = re.sub(
        r'<span class="breadcrumb-current"[^>]*>Konsultasi Surveillance ISO/SNI 9001</span>',
        f'<span class="breadcrumb-current" style="color: #00e0a0 !important;">{data["breadcrumb"]}</span>',
        content
    )
    
    # Update main page title (h1)
    content = re.sub(
        r'<h1 class="detail-page-title"[^>]*>Jasa Konsultasi Persiapan Audit Surveillance ISO/SNI 9001[^<]*</h1>',
        f'<h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important; font-weight: 700 !important;">{data["full_title"]}</h1>',
        content
    )
    
    # Update benefit highlight title
    content = re.sub(
        r'<h2 class="benefit-highlight-title">Dengan Jasa Konsultasi Persiapan Audit Surveillance ISO/SNI 9001:2015[^<]*</h2>',
        f'<h2 class="benefit-highlight-title">{data["benefit_title"]}</h2>',
        content
    )
    
    # Update benefit cards (3 cards)
    benefit_pattern = r'<div class="benefit-highlight-card">\s*<p>([^<]*)</p>\s*</div>'
    matches = list(re.finditer(benefit_pattern, content))
    if len(matches) >= 3 and len(data['benefits_short']) == 3:
        for i, match in enumerate(matches[:3]):
            content = content.replace(
                match.group(0),
                f'<div class="benefit-highlight-card">\n            <p>{data["benefits_short"][i]}</p>\n          </div>'
            )
    
    # Update pengertian title
    content = re.sub(
        r'<h2 class="iso-content-title">Pengertian Jasa Konsultasi Persiapan Audit Surveillance ISO/SNI 9001:2015</h2>',
        f'<h2 class="iso-content-title">{data["pengertian_title"]}</h2>',
        content
    )
    
    # Update pengertian description
    content = re.sub(
        r'<p class="iso-content-desc">\s*Jasa Konsultasi Persiapan Audit Surveillance ISO/SNI 9001:2015[^<]*</p>',
        f'<p class="iso-content-desc">\n            {data["definition"]}\n          </p>',
        content, flags=re.DOTALL
    )
    
    # Update process title
    content = re.sub(
        r'<h2 class="iso-process-title">Proses Konsultasi Persiapan Audit Surveillance ISO/SNI 9001:2015</h2>',
        f'<h2 class="iso-process-title">{data["process_title"]}</h2>',
        content
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ Updated: {filename}")

# Data for all 11 standards
STANDARDS = {
    'iso-50001': {
        'title': 'ISO 50001', 'system': 'Sistem Manajemen Energi',
        'breadcrumb': 'Konsultasi Surveillance ISO 50001',
        'full_title': 'Jasa Konsultasi Persiapan Audit Surveillance ISO 50001 – Sistem Manajemen Energi',
        'benefit_title': 'Dengan Jasa Konsultasi Persiapan Audit Surveillance ISO 50001:2018 Organisasi Anda Dapat:',
        'benefits_short': ['Mempertahankan<br>Sertifikasi EnMS', 'Efisiensi Energi<br>Berkelanjutan', 'Performa Energi<br>Meningkat'],
        'pengertian_title': 'Pengertian Jasa Konsultasi Persiapan Audit Surveillance ISO 50001:2018',
        'definition': 'Jasa Konsultasi Persiapan Audit Surveillance ISO 50001:2018 adalah layanan profesional yang membantu organisasi mempersiapkan audit surveillance untuk mempertahankan sertifikasi sistem manajemen energi, memastikan peningkatan efisiensi energi berkelanjutan, dan mendemonstrasikan kinerja energi yang optimal.',
        'process_title': 'Proses Konsultasi Persiapan Audit Surveillance ISO 50001:2018'
    },
    'iso-55001': {
        'title': 'ISO 55001', 'system': 'Sistem Manajemen Aset',
        'breadcrumb': 'Konsultasi Surveillance ISO 55001',
        'full_title': 'Jasa Konsultasi Persiapan Audit Surveillance ISO 55001 – Sistem Manajemen Aset',
        'benefit_title': 'Dengan Jasa Konsultasi Persiapan Audit Surveillance ISO 55001:2024 Organisasi Anda Dapat:',
        'benefits_short': ['Mempertahankan<br>Sertifikasi AMS', 'Nilai Aset<br>Optimal', 'ROI Aset<br>Meningkat'],
        'pengertian_title': 'Pengertian Jasa Konsultasi Persiapan Audit Surveillance ISO 55001:2024',
        'definition': 'Jasa Konsultasi Persiapan Audit Surveillance ISO 55001:2024 adalah layanan profesional yang membantu organisasi mempersiapkan audit surveillance untuk mempertahankan sertifikasi sistem manajemen aset, memastikan optimalisasi nilai aset berkelanjutan, dan mendemonstrasikan peningkatan return on investment aset.',
        'process_title': 'Proses Konsultasi Persiapan Audit Surveillance ISO 55001:2024'
    },
