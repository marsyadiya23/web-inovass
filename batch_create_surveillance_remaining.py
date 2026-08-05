#!/usr/bin/env python3
"""
Script to create 11 remaining surveillance pages based on ISO 9001 template
"""

import re
import shutil

# Define all 11 standards with their specific content
standards_data = {
    '50001': {
        'number': '50001',
        'year': '2018',
        'full_title': 'ISO 50001',
        'system_name': 'Sistem Manajemen Energi',
        'breadcrumb': 'Konsultasi Surveillance ISO 50001',
        'benefits': ['Mempertahankan<br>Sertifikasi EnMS', 'Efisiensi Energi<br>Berkelanjutan', 'Performa Energi<br>Meningkat'],
        'definition': 'Jasa Konsultasi Persiapan Audit Surveillance ISO 50001:2018 adalah layanan profesional yang membantu organisasi mempersiapkan audit surveillance untuk mempertahankan sertifikasi sistem manajemen energi, memastikan peningkatan efisiensi energi berkelanjutan, dan mendemonstrasikan kinerja energi yang optimal.',
        'benefit_items': [
            ('Mempertahankan Sertifikasi EnMS', 'Memastikan organisasi tetap memenuhi persyaratan ISO 50001 dan mempertahankan validitas sertifikat sistem manajemen energi.'),
            ('Efisiensi Energi Berkelanjutan', 'Menjaga konsistensi program penghematan energi dan memastikan pencapaian target efisiensi energi organisasi.'),
            ('Continuous Improvement Energi', 'Mengidentifikasi peluang perbaikan dalam pengelolaan energi dan meningkatkan kinerja energi secara berkelanjutan.'),
            ('Compliance Peraturan Energi', 'Memastikan kepatuhan berkelanjutan terhadap peraturan dan regulasi terkait penggunaan dan konservasi energi.'),
            ('Monitoring Kinerja Energi', 'Melakukan evaluasi berkala terhadap Energy Performance Indicators (EnPI) dan efektivitas kontrol operasional energi.'),
            ('Kesiapan Audit Surveillance', 'Mempersiapkan dokumentasi, evidence, dan tim organisasi untuk menghadapi audit surveillance dari lembaga sertifikasi.')
        ],
        'process_steps': [
            ('Pre-Surveillance Assessment', 'Kami melakukan evaluasi kesiapan organisasi menghadapi audit surveillance dengan mereview dokumentasi EnMS, energy baseline, EnPI, dan perubahan sejak sertifikasi awal.'),
            ('Gap Analysis Energi', 'Tim konsultan mengidentifikasi gap antara kondisi aktual dengan persyaratan ISO 50001:2018, termasuk evaluasi significant energy uses (SEUs) dan action plans.'),
            ('Corrective Actions Support', 'Kami membantu organisasi menindaklanjuti temuan audit sebelumnya, menyusun corrective actions, dan memastikan efektivitas perbaikan yang telah dilakukan.'),
            ('Evidence Preparation', 'Konsultan membantu menyiapkan bukti objektif kepatuhan ISO 50001, termasuk energy review, monitoring data, dan management review records.'),
            ('Mock Audit Surveillance', 'Melakukan simulasi audit surveillance untuk menguji kesiapan organisasi, mengidentifikasi potensi ketidaksesuaian, dan memberikan feedback perbaikan.'),
            ('Post-Surveillance Support', 'Memberikan pendampingan pasca audit surveillance untuk menindaklanjuti temuan auditor dan memastikan continuous improvement sistem manajemen energi.')
        ],
        'scope_items': [
            'Konteks & Ruang Lingkup EnMS', 'Kepemimpinan & Komitmen Energi', 'Energy Policy & Objectives', 'Energy Planning & Baseline', 
            'Significant Energy Uses (SEUs)', 'Energy Performance Indicators', 'Operational Control Energi', 'Monitoring & Measurement Energi', 
            'Management Review & Improvement'
        ],
        'cta_title': 'Persiapan Audit Surveillance Energi',
        'cta_desc': 'Konsultasikan persiapan audit surveillance ISO 50001 Anda bersama tim konsultan energi berpengalaman INOVASS. Kami siap membantu organisasi Anda mempertahankan sertifikasi sistem manajemen energi.'
    }
}

# Template file
template_file = 'layanan-detail-konsultasi-surveillance-iso-9001.html'

# Read template
with open(template_file, 'r', encoding='utf-8') as f:
    template_content = f.read()

# Process only ISO 50001 for now
for iso_num, data in standards_data.items():
    print(f"Creating page for ISO {iso_num}...")
    
    content = template_content
    
    # Replace title
    content = re.sub(
        r'<title>.*?</title>',
        f'<title>Jasa Konsultasi Persiapan Audit Surveillance {data["full_title"]} – {data["system_name"]} — INOVASS</title>',
        content
    )
    
    # Replace breadcrumb
    content = re.sub(
        r'<span class="breadcrumb-current"[^>]*>Konsultasi Surveillance ISO/SNI 9001</span>',
        f'<span class="breadcrumb-current" style="color: #00e0a0 !important;">{data["breadcrumb"]}</span>',
        content
    )
    
    # Replace main title
    content = re.sub(
        r'<h1 class="detail-page-title"[^>]*>Jasa Konsultasi Persiapan Audit Surveillance ISO/SNI 9001[^<]*</h1>',
        f'<h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important; font-weight: 700 !important;">Jasa Konsultasi Persiapan Audit Surveillance {data["full_title"]} – {data["system_name"]}</h1>',
        content
    )
    
    # Save output
    output_file = f'layanan-detail-konsultasi-surveillance-iso-{iso_num}.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Created: {output_file}")

print("\nCompleted!")
