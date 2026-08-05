#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Batch customize all pemeliharaan pages
"""

def customize_file(filename, data):
    """Customize a single file with provided data"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Apply all replacements
        for old, new in data['replacements']:
            content = content.replace(old, new)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"❌ Error in {filename}: {e}")
        return False

# Data untuk 10 halaman yang perlu dikustomisasi
pages_data = [
    {
        'filename': 'layanan-detail-pemeliharaan-iso-55001.html',
        'replacements': [
            # Title & Breadcrumb
            ('Pemeliharaan ISO/SNI 9001', 'Pemeliharaan ISO 55001'),
            ('<title>Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001 – Sistem Manajemen Mutu — INOVASS</title>',
             '<title>Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 55001 – Sistem Manajemen Aset — INOVASS</title>'),
            ('<h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important; font-weight: 700 !important;">Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001 – Sistem Manajemen Mutu</h1>',
             '<h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important; font-weight: 700 !important;">Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 55001 – Sistem Manajemen Aset</h1>'),
            
            # Benefit Highlights
            ('<h2 class="benefit-highlight-title">Dengan Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015 Organisasi Anda Dapat:</h2>',
             '<h2 class="benefit-highlight-title">Dengan Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 55001:2024 Organisasi Anda Dapat:</h2>'),
            ('<p>Memastikan Kesesuaian<br>Berkelanjutan</p>',
             '<p>Optimasi Nilai<br>Aset</p>'),
            ('<p>Menjaga Efektivitas<br>Sistem</p>',
             '<p>Lifecycle Cost<br>Management</p>'),
            ('<p>Mempertahankan<br>Sertifikasi</p>',
             '<p>Asset Performance<br>Maksimal</p>'),
            
            # Pengertian
            ('<h2 class="iso-content-title">Pengertian Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015</h2>',
             '<h2 class="iso-content-title">Pengertian Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 55001:2024</h2>'),
            ('Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015 adalah layanan profesional yang membantu organisasi memelihara, memonitor, dan meningkatkan efektivitas sistem manajemen mutu secara berkelanjutan untuk mempertahankan sertifikasi dan performa organisasi.',
             'Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 55001:2024 adalah layanan profesional yang membantu organisasi memelihara, memonitor, dan meningkatkan efektivitas sistem manajemen aset secara berkelanjutan untuk mempertahankan sertifikasi dan optimalisasi nilai aset organisasi.'),
            
            # Benefits Section Title
            ('<h2 class="iso-benefit-section-title">Manfaat Konsultasi Pemeliharaan Sistem Manajemen ISO 9001</h2>',
             '<h2 class="iso-benefit-section-title">Manfaat Konsultasi Pemeliharaan Sistem Manajemen ISO 55001</h2>'),
            
            # 6 Benefit Cards
            ('<h3>Pemeliharaan Dokumentasi</h3>\n            <p>Membantu update dan pemeliharaan dokumentasi sistem sesuai perubahan proses bisnis</p>',
             '<h3>Asset Register Update</h3>\n            <p>Membantu update asset register dan lifecycle information sesuai perubahan portfolio aset</p>'),
            ('<h3>Monitoring Berkelanjutan</h3>\n            <p>Monitoring efektivitas sistem secara rutin untuk memastikan kesesuaian berkelanjutan</p>',
             '<h3>Performance Monitoring</h3>\n            <p>Monitoring kinerja aset secara rutin untuk memastikan pencapaian asset objectives</p>'),
            ('<h3>Improvement Support</h3>\n            <p>Dukungan dalam implementasi peningkatan berkelanjutan dan corrective actions</p>',
             '<h3>Risk-Based Maintenance</h3>\n            <p>Dukungan dalam pengelolaan maintenance strategy berbasis risiko dan criticality</p>'),
            ('<h3>Compliance Assurance</h3>\n            <p>Memastikan compliance berkelanjutan terhadap persyaratan ISO 9001:2015</p>',
             '<h3>Compliance AMS</h3>\n            <p>Memastikan compliance berkelanjutan terhadap persyaratan ISO 55001:2024</p>'),
            ('<h3>Performance Review</h3>\n            <p>Review berkala terhadap KPI dan performance indicators sistem manajemen mutu</p>',
             '<h3>Asset Performance Review</h3>\n            <p>Review berkala terhadap asset performance indicators dan lifecycle costs</p>'),
            ('<h3>Readiness Audit</h3>\n            <p>Menjaga kesiapan organisasi untuk audit surveillance dan recertification</p>',
             '<h3>Certification Readiness</h3>\n            <p>Menjaga kesiapan organisasi untuk audit surveillance dan recertification</p>'),
        ]
    }
]

print("="*70)
print("BATCH CUSTOMIZATION - Pemeliharaan Pages")
print("="*70)
print()

success_count = 0
for page_data in pages_data:
    filename = page_data['filename']
    print(f"Processing: {filename}...")
    if customize_file(filename, page_data):
        success_count += 1
        print(f"✅ Successfully customized: {filename}")
    print()

print("="*70)
print(f"Completed: {success_count}/{len(pages_data)} files successfully customized")
print("="*70)
