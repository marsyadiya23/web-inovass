#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Complete Customization Script for 9 Remaining Pemeliharaan Pages
This script will customize all content from ISO 9001 template to specific ISO standards
"""

def customize_file(filename, replacements):
    """Apply all replacements to a file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        replaced_count = 0
        for old, new in replacements:
            if old in content:
                content = content.replace(old, new)
                replaced_count += 1
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ {filename}: {replaced_count}/{len(replacements)} replacements applied")
        return True
    except Exception as e:
        print(f"❌ Error in {filename}: {e}")
        return False

# =============================================================================
# DATA FOR ALL 9 FILES
# =============================================================================

files_data = {
    # =========================================================================
    # 1. ISO 21001 - Educational Organizations Management System
    # =========================================================================
    'layanan-detail-pemeliharaan-iso-21001.html': [
        # Title & Breadcrumb
        ('Pemeliharaan ISO/SNI 9001', 'Pemeliharaan ISO 21001'),
        ('<title>Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001 – Sistem Manajemen Mutu — INOVASS</title>',
         '<title>Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 21001 – Sistem Manajemen Organisasi Pendidikan — INOVASS</title>'),
        ('<h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important; font-weight: 700 !important;">Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001 – Sistem Manajemen Mutu</h1>',
         '<h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important; font-weight: 700 !important;">Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 21001 – Sistem Manajemen Organisasi Pendidikan</h1>'),
        
        # Benefit Highlights
        ('<h2 class="benefit-highlight-title">Dengan Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015 Organisasi Anda Dapat:</h2>',
         '<h2 class="benefit-highlight-title">Dengan Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 21001:2025 Organisasi Anda Dapat:</h2>'),
        ('<p>Memastikan Kesesuaian<br>Berkelanjutan</p>',
         '<p>Mutu Pembelajaran<br>Berkelanjutan</p>'),
        ('<p>Menjaga Efektivitas<br>Sistem</p>',
         '<p>Kepuasan<br>Peserta Didik</p>'),
        ('<p>Mempertahankan<br>Sertifikasi</p>',
         '<p>Akreditasi<br>Terjaga</p>'),
        
        # Pengertian
        ('<h2 class="iso-content-title">Pengertian Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015</h2>',
         '<h2 class="iso-content-title">Pengertian Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 21001:2025</h2>'),
        ('Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015 adalah layanan profesional yang membantu organisasi memelihara, memonitor, dan meningkatkan efektivitas sistem manajemen mutu secara berkelanjutan untuk mempertahankan sertifikasi dan performa organisasi.',
         'Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 21001:2025 adalah layanan profesional yang membantu organisasi pendidikan memelihara, memonitor, dan meningkatkan efektivitas sistem manajemen pendidikan secara berkelanjutan untuk mempertahankan sertifikasi dan mutu pendidikan.'),
        
        # Benefits Section Title
        ('<h2 class="iso-benefit-section-title">Manfaat Konsultasi Pemeliharaan Sistem Manajemen ISO 9001</h2>',
         '<h2 class="iso-benefit-section-title">Manfaat Konsultasi Pemeliharaan Sistem Manajemen ISO 21001</h2>'),
        
        # 6 Benefit Cards
        ('<h3>Pemeliharaan Dokumentasi</h3>\n            <p>Membantu update dan pemeliharaan dokumentasi sistem sesuai perubahan proses bisnis</p>',
         '<h3>Curriculum Maintenance</h3>\n            <p>Membantu update kurikulum dan learning outcomes sesuai perkembangan kebutuhan learners</p>'),
        ('<h3>Monitoring Berkelanjutan</h3>\n            <p>Monitoring efektivitas sistem secara rutin untuk memastikan kesesuaian berkelanjutan</p>',
         '<h3>Learning Monitoring</h3>\n            <p>Monitoring efektivitas pembelajaran secara rutin untuk memastikan pencapaian learning objectives</p>'),
        ('<h3>Improvement Support</h3>\n            <p>Dukungan dalam implementasi peningkatan berkelanjutan dan corrective actions</p>',
         '<h3>Stakeholder Engagement</h3>\n            <p>Dukungan dalam pengelolaan engagement dengan learners, educators, dan stakeholders</p>'),
        ('<h3>Compliance Assurance</h3>\n            <p>Memastikan compliance berkelanjutan terhadap persyaratan ISO 9001:2015</p>',
         '<h3>Compliance EOMS</h3>\n            <p>Memastikan compliance berkelanjutan terhadap persyaratan ISO 21001:2025</p>'),
        ('<h3>Performance Review</h3>\n            <p>Review berkala terhadap KPI dan performance indicators sistem manajemen mutu</p>',
         '<h3>Educational Performance</h3>\n            <p>Review berkala terhadap educational KPIs dan learner satisfaction</p>'),
        ('<h3>Readiness Audit</h3>\n            <p>Menjaga kesiapan organisasi untuk audit surveillance dan recertification</p>',
         '<h3>Accreditation Readiness</h3>\n            <p>Menjaga kesiapan organisasi untuk audit surveillance dan recertification</p>'),
        
        # Process Section
        ('<h2 class="iso-process-title">Proses Konsultasi Pemeliharaan Sistem Manajemen Mutu ISO/SNI 9001:2015</h2>',
         '<h2 class="iso-process-title">Proses Konsultasi Pemeliharaan Sistem Manajemen Organisasi Pendidikan ISO 21001:2025</h2>'),
        
        # Process Steps
        ('<h3>Assessment Sistem Berjalan</h3>\n              <p>Kami melakukan evaluasi komprehensif terhadap implementasi sistem manajemen mutu, meninjau efektivitas proses QMS, dan mengidentifikasi area yang memerlukan perbaikan atau peningkatan.</p>',
         '<h3>Assessment Sistem Berjalan</h3>\n              <p>Kami melakukan evaluasi komprehensif terhadap implementasi sistem manajemen pendidikan, meninjau efektivitas pembelajaran dan learner satisfaction, serta mengidentifikasi area yang memerlukan perbaikan dalam delivery pendidikan.</p>'),
        ('<h3>Gap Analysis & Review</h3>\n              <p>Tim konsultan melakukan analisis kesenjangan antara praktik saat ini dengan persyaratan ISO 9001:2015, meninjau hasil audit internal, dan mengidentifikasi potensi ketidaksesuaian atau area improvement.</p>',
         '<h3>Gap Analysis & Review</h3>\n              <p>Tim konsultan melakukan analisis kesenjangan antara praktik saat ini dengan persyaratan ISO 21001:2025, meninjau learning outcomes dan stakeholder needs, serta mengidentifikasi gap dalam educational quality atau area improvement.</p>'),
        ('<h3>Update Dokumentasi QMS</h3>\n              <p>Kami membantu organisasi memperbarui dokumen sistem manajemen mutu termasuk prosedur, instruksi kerja, dan formulir sesuai dengan perubahan proses bisnis, regulasi terbaru, dan best practice.</p>',
         '<h3>Update Dokumentasi EOMS</h3>\n              <p>Kami membantu organisasi memperbarui dokumen sistem manajemen pendidikan termasuk kurikulum, learning plans, assessment methods, dan educational resources sesuai dengan perkembangan pedagogi dan teknologi pembelajaran terkini.</p>'),
        ('<h3>Improvement Planning</h3>\n              <p>Tim konsultan membantu menyusun rencana perbaikan dan peningkatan berkelanjutan, mengembangkan action plan untuk mengatasi temuan gap analysis, dan menetapkan target improvement yang terukur.</p>',
         '<h3>Improvement Planning</h3>\n              <p>Tim konsultan membantu menyusun rencana peningkatan mutu pendidikan, mengembangkan action plan untuk mengatasi temuan gap analysis dan learner feedback, serta menetapkan target educational excellence yang terukur.</p>'),
        ('<h3>Implementation Support</h3>\n              <p>Konsultan memberikan pendampingan dalam implementasi perbaikan, pelatihan refreshment untuk personel kunci, dan fasilitasi management review untuk memastikan komitmen top management terhadap pemeliharaan QMS.</p>',
         '<h3>Implementation Support</h3>\n              <p>Konsultan memberikan pendampingan dalam implementasi educational improvements, pelatihan pedagogis untuk educators, dan fasilitasi management review untuk memastikan komitmen top management terhadap pemeliharaan EOMS.</p>'),
        ('<h3>Monitoring & Follow-up</h3>\n              <p>Kami melakukan monitoring berkelanjutan terhadap efektivitas pemeliharaan sistem, evaluasi pencapaian KPI mutu, dan memberikan dukungan konsultasi untuk memastikan kesiapan menghadapi audit surveillance atau recertification.</p>',
         '<h3>Monitoring & Follow-up</h3>\n              <p>Kami melakukan monitoring berkelanjutan terhadap mutu pembelajaran, evaluasi learner outcomes dan satisfaction, dan memberikan dukungan konsultasi untuk memastikan kesiapan menghadapi audit surveillance atau recertification.</p>'),
        
        # Fokus Section
        ('<h2 class="iso-target-section-title" style="margin-bottom: 3rem;">Fokus Pemeliharaan Sistem Manajemen ISO 9001</h2>',
         '<h2 class="iso-target-section-title" style="margin-bottom: 3rem;">Fokus Pemeliharaan Sistem Manajemen ISO 21001</h2>'),
        
        # Fokus Items (9 cards)
        ('<div class="iso-target-card"><h4>Document Control</h4></div>',
         '<div class="iso-target-card"><h4>Learner-Centered Approach</h4></div>'),
        ('<div class="iso-target-card"><h4>Records Management</h4></div>',
         '<div class="iso-target-card"><h4>Learning Outcomes</h4></div>'),
        ('<div class="iso-target-card"><h4>Process Monitoring</h4></div>',
         '<div class="iso-target-card"><h4>Curriculum Development</h4></div>'),
        ('<div class="iso-target-card"><h4>KPI & Performance Tracking</h4></div>',
         '<div class="iso-target-card"><h4>Assessment Methods</h4></div>'),
        ('<div class="iso-target-card"><h4>Internal Audit Program</h4></div>',
         '<div class="iso-target-card"><h4>Educator Competence</h4></div>'),
        ('<div class="iso-target-card"><h4>Management Review</h4></div>',
         '<div class="iso-target-card"><h4>Learning Resources</h4></div>'),
        ('<div class="iso-target-card"><h4>Corrective Actions</h4></div>',
         '<div class="iso-target-card"><h4>Stakeholder Satisfaction</h4></div>'),
        ('<div class="iso-target-card"><h4>Customer Satisfaction</h4></div>',
         '<div class="iso-target-card"><h4>Educational Performance</h4></div>'),
        ('<div class="iso-target-card"><h4>Continuous Improvement</h4></div>',
         '<div class="iso-target-card"><h4>Continuous Improvement EOMS</h4></div>'),
    ],

    # =========================================================================
    # 2. ISO 13485 - Medical Devices Quality Management System
    # =========================================================================
    'layanan-detail-pemeliharaan-iso-13485.html': [
        # Title & Breadcrumb
        ('Pemeliharaan ISO/SNI 9001', 'Pemeliharaan ISO 13485'),
        ('<title>Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001 – Sistem Manajemen Mutu — INOVASS</title>',
         '<title>Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 13485 – Sistem Manajemen Mutu Alat Kesehatan — INOVASS</title>'),
        ('<h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important; font-weight: 700 !important;">Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001 – Sistem Manajemen Mutu</h1>',
         '<h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important; font-weight: 700 !important;">Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 13485 – Sistem Manajemen Mutu Alat Kesehatan</h1>'),
        
        # Benefit Highlights
        ('<h2 class="benefit-highlight-title">Dengan Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015 Organisasi Anda Dapat:</h2>',
         '<h2 class="benefit-highlight-title">Dengan Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 13485:2016 Organisasi Anda Dapat:</h2>'),
        ('<p>Memastikan Kesesuaian<br>Berkelanjutan</p>',
         '<p>Keamanan Produk<br>Medis</p>'),
        ('<p>Menjaga Efektivitas<br>Sistem</p>',
         '<p>Compliance<br>Regulasi</p>'),
        ('<p>Mempertahankan<br>Sertifikasi</p>',
         '<p>Market Access<br>Global</p>'),
        
        # Pengertian
        ('<h2 class="iso-content-title">Pengertian Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015</h2>',
         '<h2 class="iso-content-title">Pengertian Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 13485:2016</h2>'),
        ('Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015 adalah layanan profesional yang membantu organisasi memelihara, memonitor, dan meningkatkan efektivitas sistem manajemen mutu secara berkelanjutan untuk mempertahankan sertifikasi dan performa organisasi.',
         'Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 13485:2016 adalah layanan profesional yang membantu organisasi manufaktur alat kesehatan memelihara, memonitor, dan meningkatkan efektivitas sistem manajemen mutu medical devices secara berkelanjutan untuk mempertahankan sertifikasi dan compliance regulasi.'),
        
        # Benefits Section Title
        ('<h2 class="iso-benefit-section-title">Manfaat Konsultasi Pemeliharaan Sistem Manajemen ISO 9001</h2>',
         '<h2 class="iso-benefit-section-title">Manfaat Konsultasi Pemeliharaan Sistem Manajemen ISO 13485</h2>'),
        
        # 6 Benefit Cards
        ('<h3>Pemeliharaan Dokumentasi</h3>\n            <p>Membantu update dan pemeliharaan dokumentasi sistem sesuai perubahan proses bisnis</p>',
         '<h3>DMR Maintenance</h3>\n            <p>Membantu update Device Master Record dan design history file sesuai perubahan produk</p>'),
        ('<h3>Monitoring Berkelanjutan</h3>\n            <p>Monitoring efektivitas sistem secara rutin untuk memastikan kesesuaian berkelanjutan</p>',
         '<h3>Post-Market Surveillance</h3>\n            <p>Monitoring post-market performance alat kesehatan untuk memastikan safety dan effectiveness</p>'),
        ('<h3>Improvement Support</h3>\n            <p>Dukungan dalam implementasi peningkatan berkelanjutan dan corrective actions</p>',
         '<h3>CAPA Management</h3>\n            <p>Dukungan dalam pengelolaan Corrective and Preventive Actions untuk medical devices</p>'),
        ('<h3>Compliance Assurance</h3>\n            <p>Memastikan compliance berkelanjutan terhadap persyaratan ISO 9001:2015</p>',
         '<h3>Regulatory Compliance</h3>\n            <p>Memastikan compliance berkelanjutan terhadap ISO 13485:2016 dan regulasi medical devices</p>'),
        ('<h3>Performance Review</h3>\n            <p>Review berkala terhadap KPI dan performance indicators sistem manajemen mutu</p>',
         '<h3>Quality Performance</h3>\n            <p>Review berkala terhadap quality metrics dan post-market data</p>'),
        ('<h3>Readiness Audit</h3>\n            <p>Menjaga kesiapan organisasi untuk audit surveillance dan recertification</p>',
         '<h3>Certification Readiness</h3>\n            <p>Menjaga kesiapan organisasi untuk audit surveillance dan regulatory inspections</p>'),
        
        # Process Section
        ('<h2 class="iso-process-title">Proses Konsultasi Pemeliharaan Sistem Manajemen Mutu ISO/SNI 9001:2015</h2>',
         '<h2 class="iso-process-title">Proses Konsultasi Pemeliharaan Sistem Manajemen Mutu Alat Kesehatan ISO 13485:2016</h2>'),
        
        # Process Steps
        ('<h3>Assessment Sistem Berjalan</h3>\n              <p>Kami melakukan evaluasi komprehensif terhadap implementasi sistem manajemen mutu, meninjau efektivitas proses QMS, dan mengidentifikasi area yang memerlukan perbaikan atau peningkatan.</p>',
         '<h3>Assessment Sistem Berjalan</h3>\n              <p>Kami melakukan evaluasi komprehensif terhadap implementasi sistem manajemen mutu medical devices, meninjau efektivitas design controls dan risk management, serta mengidentifikasi area yang memerlukan perbaikan dalam quality system.</p>'),
        ('<h3>Gap Analysis & Review</h3>\n              <p>Tim konsultan melakukan analisis kesenjangan antara praktik saat ini dengan persyaratan ISO 9001:2015, meninjau hasil audit internal, dan mengidentifikasi potensi ketidaksesuaian atau area improvement.</p>',
         '<h3>Gap Analysis & Review</h3>\n              <p>Tim konsultan melakukan analisis kesenjangan antara praktik saat ini dengan persyaratan ISO 13485:2016 dan regulasi medical devices, meninjau DHF dan complaint handling, serta mengidentifikasi potensi non-conformance atau area improvement.</p>'),
        ('<h3>Update Dokumentasi QMS</h3>\n              <p>Kami membantu organisasi memperbarui dokumen sistem manajemen mutu termasuk prosedur, instruksi kerja, dan formulir sesuai dengan perubahan proses bisnis, regulasi terbaru, dan best practice.</p>',
         '<h3>Update Dokumentasi MDQMS</h3>\n              <p>Kami membantu organisasi memperbarui dokumen sistem mutu alat kesehatan termasuk DMR, design controls, risk management files, dan validation protocols sesuai dengan perubahan produk dan regulasi medical devices terkini.</p>'),
        ('<h3>Improvement Planning</h3>\n              <p>Tim konsultan membantu menyusun rencana perbaikan dan peningkatan berkelanjutan, mengembangkan action plan untuk mengatasi temuan gap analysis, dan menetapkan target improvement yang terukur.</p>',
         '<h3>Improvement Planning</h3>\n              <p>Tim konsultan membantu menyusun rencana peningkatan quality system, mengembangkan action plan untuk mengatasi temuan gap analysis dan CAPA, serta menetapkan target quality performance yang terukur.</p>'),
        ('<h3>Implementation Support</h3>\n              <p>Konsultan memberikan pendampingan dalam implementasi perbaikan, pelatihan refreshment untuk personel kunci, dan fasilitasi management review untuk memastikan komitmen top management terhadap pemeliharaan QMS.</p>',
         '<h3>Implementation Support</h3>\n              <p>Konsultan memberikan pendampingan dalam implementasi quality improvements, pelatihan GMP untuk personel manufacturing, dan fasilitasi management review untuk memastikan komitmen top management terhadap pemeliharaan MDQMS.</p>'),
        ('<h3>Monitoring & Follow-up</h3>\n              <p>Kami melakukan monitoring berkelanjutan terhadap efektivitas pemeliharaan sistem, evaluasi pencapaian KPI mutu, dan memberikan dukungan konsultasi untuk memastikan kesiapan menghadapi audit surveillance atau recertification.</p>',
         '<h3>Monitoring & Follow-up</h3>\n              <p>Kami melakukan monitoring berkelanjutan terhadap quality metrics dan post-market surveillance data, evaluasi adverse events, dan memberikan dukungan konsultasi untuk memastikan kesiapan menghadapi audit surveillance atau regulatory inspections.</p>'),
        
        # Fokus Section
        ('<h2 class="iso-target-section-title" style="margin-bottom: 3rem;">Fokus Pemeliharaan Sistem Manajemen ISO 9001</h2>',
         '<h2 class="iso-target-section-title" style="margin-bottom: 3rem;">Fokus Pemeliharaan Sistem Manajemen ISO 13485</h2>'),
        
        # Fokus Items (9 cards)
        ('<div class="iso-target-card"><h4>Document Control</h4></div>',
         '<div class="iso-target-card"><h4>Design Controls</h4></div>'),
        ('<div class="iso-target-card"><h4>Records Management</h4></div>',
         '<div class="iso-target-card"><h4>Risk Management (ISO 14971)</h4></div>'),
        ('<div class="iso-target-card"><h4>Process Monitoring</h4></div>',
         '<div class="iso-target-card"><h4>DHF & DMR</h4></div>'),
        ('<div class="iso-target-card"><h4>KPI & Performance Tracking</h4></div>',
         '<div class="iso-target-card"><h4>Validation & Verification</h4></div>'),
        ('<div class="iso-target-card"><h4>Internal Audit Program</h4></div>',
         '<div class="iso-target-card"><h4>Post-Market Surveillance</h4></div>'),
        ('<div class="iso-target-card"><h4>Management Review</h4></div>',
         '<div class="iso-target-card"><h4>Complaint Handling</h4></div>'),
        ('<div class="iso-target-card"><h4>Corrective Actions</h4></div>',
         '<div class="iso-target-card"><h4>CAPA System</h4></div>'),
        ('<div class="iso-target-card"><h4>Customer Satisfaction</h4></div>',
         '<div class="iso-target-card"><h4>Regulatory Compliance</h4></div>'),
        ('<div class="iso-target-card"><h4>Continuous Improvement</h4></div>',
         '<div class="iso-target-card"><h4>Continuous Improvement MDQMS</h4></div>'),
    ],

    # =========================================================================
    # 3. ISO 39001 - Road Traffic Safety Management System
    # =========================================================================
    'layanan-detail-pemeliharaan-iso-39001.html': [
        ('Pemeliharaan ISO/SNI 9001', 'Pemeliharaan ISO 39001'),
        ('<title>Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001 – Sistem Manajemen Mutu — INOVASS</title>',
         '<title>Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 39001 – Sistem Manajemen Keselamatan Lalu Lintas Jalan — INOVASS</title>'),
        ('<h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important; font-weight: 700 !important;">Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001 – Sistem Manajemen Mutu</h1>',
         '<h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important; font-weight: 700 !important;">Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 39001 – Sistem Manajemen Keselamatan Lalu Lintas Jalan</h1>'),
        ('<h2 class="benefit-highlight-title">Dengan Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015 Organisasi Anda Dapat:</h2>',
         '<h2 class="benefit-highlight-title">Dengan Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 39001:2012 Organisasi Anda Dapat:</h2>'),
        ('<p>Memastikan Kesesuaian<br>Berkelanjutan</p>', '<p>Zero Road<br>Fatalities</p>'),
        ('<p>Menjaga Efektivitas<br>Sistem</p>', '<p>Keselamatan<br>Berkendara</p>'),
        ('<p>Mempertahankan<br>Sertifikasi</p>', '<p>Compliance<br>RTS</p>'),
        ('<h2 class="iso-content-title">Pengertian Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015</h2>',
         '<h2 class="iso-content-title">Pengertian Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 39001:2012</h2>'),
        ('Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015 adalah layanan profesional yang membantu organisasi memelihara, memonitor, dan meningkatkan efektivitas sistem manajemen mutu secara berkelanjutan untuk mempertahankan sertifikasi dan performa organisasi.',
         'Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 39001:2012 adalah layanan profesional yang membantu organisasi memelihara, memonitor, dan meningkatkan efektivitas sistem manajemen keselamatan lalu lintas jalan secara berkelanjutan untuk mempertahankan sertifikasi dan mengurangi risiko kecelakaan lalu lintas.'),
        ('<h2 class="iso-benefit-section-title">Manfaat Konsultasi Pemeliharaan Sistem Manajemen ISO 9001</h2>',
         '<h2 class="iso-benefit-section-title">Manfaat Konsultasi Pemeliharaan Sistem Manajemen ISO 39001</h2>'),
        ('<h3>Pemeliharaan Dokumentasi</h3>\n            <p>Membantu update dan pemeliharaan dokumentasi sistem sesuai perubahan proses bisnis</p>',
         '<h3>RTS Performance Monitoring</h3>\n            <p>Membantu monitoring Road Traffic Safety performance dan incident analysis</p>'),
        ('<h3>Monitoring Berkelanjutan</h3>\n            <p>Monitoring efektivitas sistem secara rutin untuk memastikan kesesuaian berkelanjutan</p>',
         '<h3>Risk Mitigation</h3>\n            <p>Monitoring risk factors dan implementasi kontrol keselamatan berkendara</p>'),
        ('<h3>Improvement Support</h3>\n            <p>Dukungan dalam implementasi peningkatan berkelanjutan dan corrective actions</p>',
         '<h3>Driver Management</h3>\n            <p>Dukungan dalam pengelolaan driver competence dan behavior monitoring</p>'),
        ('<h3>Compliance Assurance</h3>\n            <p>Memastikan compliance berkelanjutan terhadap persyaratan ISO 9001:2015</p>',
         '<h3>Compliance RTS</h3>\n            <p>Memastikan compliance berkelanjutan terhadap persyaratan ISO 39001:2012</p>'),
        ('<h3>Performance Review</h3>\n            <p>Review berkala terhadap KPI dan performance indicators sistem manajemen mutu</p>',
         '<h3>Safety Performance</h3>\n            <p>Review berkala terhadap RTS KPIs dan accident/incident statistics</p>'),
        ('<h3>Readiness Audit</h3>\n            <p>Menjaga kesiapan organisasi untuk audit surveillance dan recertification</p>',
         '<h3>Certification Readiness</h3>\n            <p>Menjaga kesiapan organisasi untuk audit surveillance dan recertification</p>'),
        ('<h2 class="iso-process-title">Proses Konsultasi Pemeliharaan Sistem Manajemen Mutu ISO/SNI 9001:2015</h2>',
         '<h2 class="iso-process-title">Proses Konsultasi Pemeliharaan Sistem Manajemen Keselamatan Lalu Lintas Jalan ISO 39001:2012</h2>'),
        ('<h3>Assessment Sistem Berjalan</h3>\n              <p>Kami melakukan evaluasi komprehensif terhadap implementasi sistem manajemen mutu, meninjau efektivitas proses QMS, dan mengidentifikasi area yang memerlukan perbaikan atau peningkatan.</p>',
         '<h3>Assessment Sistem Berjalan</h3>\n              <p>Kami melakukan evaluasi komprehensif terhadap implementasi sistem manajemen RTS, meninjau efektivitas road safety performance dan exposure controls, serta mengidentifikasi area yang memerlukan perbaikan dalam manajemen keselamatan berkendara.</p>'),
        ('<h3>Gap Analysis & Review</h3>\n              <p>Tim konsultan melakukan analisis kesenjangan antara praktik saat ini dengan persyaratan ISO 9001:2015, meninjau hasil audit internal, dan mengidentifikasi potensi ketidaksesuaian atau area improvement.</p>',
         '<h3>Gap Analysis & Review</h3>\n              <p>Tim konsultan melakukan analisis kesenjangan antara praktik saat ini dengan persyaratan ISO 39001:2012, meninjau incident data dan risk factors, serta mengidentifikasi potensi unsafe conditions atau area improvement dalam RTSMS.</p>'),
        ('<h3>Update Dokumentasi QMS</h3>\n              <p>Kami membantu organisasi memperbarui dokumen sistem manajemen mutu termasuk prosedur, instruksi kerja, dan formulir sesuai dengan perubahan proses bisnis, regulasi terbaru, dan best practice.</p>',
         '<h3>Update Dokumentasi RTSMS</h3>\n              <p>Kami membantu organisasi memperbarui dokumen sistem manajemen RTS termasuk road safety policy, risk assessment, driver procedures, dan emergency response plans sesuai dengan perubahan operasional dan regulasi lalu lintas terkini.</p>'),
        ('<h3>Improvement Planning</h3>\n              <p>Tim konsultan membantu menyusun rencana perbaikan dan peningkatan berkelanjutan, mengembangkan action plan untuk mengatasi temuan gap analysis, dan menetapkan target improvement yang terukur.</p>',
         '<h3>Improvement Planning</h3>\n              <p>Tim konsultan membantu menyusun rencana peningkatan road safety performance, mengembangkan action plan untuk mengatasi temuan gap analysis dan incident investigations, serta menetapkan target zero fatalities yang terukur.</p>'),
        ('<h3>Implementation Support</h3>\n              <p>Konsultan memberikan pendampingan dalam implementasi perbaikan, pelatihan refreshment untuk personel kunci, dan fasilitasi management review untuk memastikan komitmen top management terhadap pemeliharaan QMS.</p>',
         '<h3>Implementation Support</h3>\n              <p>Konsultan memberikan pendampingan dalam implementasi safety improvements, pelatihan defensive driving untuk drivers, dan fasilitasi management review untuk memastikan komitmen top management terhadap pemeliharaan RTSMS.</p>'),
        ('<h3>Monitoring & Follow-up</h3>\n              <p>Kami melakukan monitoring berkelanjutan terhadap efektivitas pemeliharaan sistem, evaluasi pencapaian KPI mutu, dan memberikan dukungan konsultasi untuk memastikan kesiapan menghadapi audit surveillance atau recertification.</p>',
         '<h3>Monitoring & Follow-up</h3>\n              <p>Kami melakukan monitoring berkelanjutan terhadap RTS performance, evaluasi accident/incident trends dan near miss reporting, dan memberikan dukungan konsultasi untuk memastikan kesiapan menghadapi audit surveillance atau recertification.</p>'),
        ('<h2 class="iso-target-section-title" style="margin-bottom: 3rem;">Fokus Pemeliharaan Sistem Manajemen ISO 9001</h2>',
         '<h2 class="iso-target-section-title" style="margin-bottom: 3rem;">Fokus Pemeliharaan Sistem Manajemen ISO 39001</h2>'),
        ('<div class="iso-target-card"><h4>Document Control</h4></div>', '<div class="iso-target-card"><h4>RTS Policy & Objectives</h4></div>'),
        ('<div class="iso-target-card"><h4>Records Management</h4></div>', '<div class="iso-target-card"><h4>Risk Factor Analysis</h4></div>'),
        ('<div class="iso-target-card"><h4>Process Monitoring</h4></div>', '<div class="iso-target-card"><h4>Exposure Control</h4></div>'),
        ('<div class="iso-target-card"><h4>KPI & Performance Tracking</h4></div>', '<div class="iso-target-card"><h4>Driver Competence</h4></div>'),
        ('<div class="iso-target-card"><h4>Internal Audit Program</h4></div>', '<div class="iso-target-card"><h4>Vehicle Safety</h4></div>'),
        ('<div class="iso-target-card"><h4>Management Review</h4></div>', '<div class="iso-target-card"><h4>Incident Investigation</h4></div>'),
        ('<div class="iso-target-card"><h4>Corrective Actions</h4></div>', '<div class="iso-target-card"><h4>Emergency Response</h4></div>'),
        ('<div class="iso-target-card"><h4>Customer Satisfaction</h4></div>', '<div class="iso-target-card"><h4>Performance Monitoring RTS</h4></div>'),
        ('<div class="iso-target-card"><h4>Continuous Improvement</h4></div>', '<div class="iso-target-card"><h4>Continuous Improvement RTSMS</h4></div>'),
    ],

    # =========================================================================
    # 4. ISO 10002 - Customer Complaints Handling Management System
    # =========================================================================
    'layanan-detail-pemeliharaan-iso-10002.html': [
        ('Pemeliharaan ISO/SNI 9001', 'Pemeliharaan ISO 10002'),
        ('<title>Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001 – Sistem Manajemen Mutu — INOVASS</title>',
         '<title>Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 10002 – Sistem Manajemen Penanganan Keluhan Pelanggan — INOVASS</title>'),
        ('<h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important; font-weight: 700 !important;">Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001 – Sistem Manajemen Mutu</h1>',
         '<h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important; font-weight: 700 !important;">Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 10002 – Sistem Manajemen Penanganan Keluhan Pelanggan</h1>'),
        ('<h2 class="benefit-highlight-title">Dengan Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015 Organisasi Anda Dapat:</h2>',
         '<h2 class="benefit-highlight-title">Dengan Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 10002:2018 Organisasi Anda Dapat:</h2>'),
        ('<p>Memastikan Kesesuaian<br>Berkelanjutan</p>', '<p>Kepuasan<br>Pelanggan</p>'),
        ('<p>Menjaga Efektivitas<br>Sistem</p>', '<p>Complaint Resolution<br>Efektif</p>'),
        ('<p>Mempertahankan<br>Sertifikasi</p>', '<p>Customer<br>Loyalty</p>'),
        ('<h2 class="iso-content-title">Pengertian Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015</h2>',
         '<h2 class="iso-content-title">Pengertian Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 10002:2018</h2>'),
        ('Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015 adalah layanan profesional yang membantu organisasi memelihara, memonitor, dan meningkatkan efektivitas sistem manajemen mutu secara berkelanjutan untuk mempertahankan sertifikasi dan performa organisasi.',
         'Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 10002:2018 adalah layanan profesional yang membantu organisasi memelihara, memonitor, dan meningkatkan efektivitas sistem penanganan keluhan pelanggan secara berkelanjutan untuk mempertahankan sertifikasi dan meningkatkan kepuasan pelanggan.'),
        ('<h2 class="iso-benefit-section-title">Manfaat Konsultasi Pemeliharaan Sistem Manajemen ISO 9001</h2>',
         '<h2 class="iso-benefit-section-title">Manfaat Konsultasi Pemeliharaan Sistem Manajemen ISO 10002</h2>'),
        ('<h3>Pemeliharaan Dokumentasi</h3>\n            <p>Membantu update dan pemeliharaan dokumentasi sistem sesuai perubahan proses bisnis</p>',
         '<h3>Complaint Process</h3>\n            <p>Membantu maintenance proses penanganan keluhan yang efektif dan customer-friendly</p>'),
        ('<h3>Monitoring Berkelanjutan</h3>\n            <p>Monitoring efektivitas sistem secara rutin untuk memastikan kesesuaian berkelanjutan</p>',
         '<h3>Response Monitoring</h3>\n            <p>Monitoring response time dan complaint resolution rate secara berkelanjutan</p>'),
        ('<h3>Improvement Support</h3>\n            <p>Dukungan dalam implementasi peningkatan berkelanjutan dan corrective actions</p>',
         '<h3>Root Cause Analysis</h3>\n            <p>Dukungan dalam analisis akar masalah keluhan dan preventive actions</p>'),
        ('<h3>Compliance Assurance</h3>\n            <p>Memastikan compliance berkelanjutan terhadap persyaratan ISO 9001:2015</p>',
         '<h3>Compliance CHMS</h3>\n            <p>Memastikan compliance berkelanjutan terhadap persyaratan ISO 10002:2018</p>'),
        ('<h3>Performance Review</h3>\n            <p>Review berkala terhadap KPI dan performance indicators sistem manajemen mutu</p>',
         '<h3>Satisfaction Review</h3>\n            <p>Review berkala terhadap customer satisfaction dan complaint trends</p>'),
        ('<h2 class="iso-process-title">Proses Konsultasi Pemeliharaan Sistem Manajemen Mutu ISO/SNI 9001:2015</h2>',
         '<h2 class="iso-process-title">Proses Konsultasi Pemeliharaan Sistem Manajemen Penanganan Keluhan ISO 10002:2018</h2>'),
        ('<h3>Assessment Sistem Berjalan</h3>\n              <p>Kami melakukan evaluasi komprehensif terhadap implementasi sistem manajemen mutu, meninjau efektivitas proses QMS, dan mengidentifikasi area yang memerlukan perbaikan atau peningkatan.</p>',
         '<h3>Assessment Sistem Berjalan</h3>\n              <p>Kami melakukan evaluasi komprehensif terhadap implementasi sistem penanganan keluhan, meninjau efektivitas complaint handling process dan customer satisfaction, serta mengidentifikasi area yang memerlukan perbaikan dalam complaint management.</p>'),
        ('<h3>Gap Analysis & Review</h3>\n              <p>Tim konsultan melakukan analisis kesenjangan antara praktik saat ini dengan persyaratan ISO 9001:2015, meninjau hasil audit internal, dan mengidentifikasi potensi ketidaksesuaian atau area improvement.</p>',
         '<h3>Gap Analysis & Review</h3>\n              <p>Tim konsultan melakukan analisis kesenjangan antara praktik saat ini dengan persyaratan ISO 10002:2018, meninjau complaint data dan resolution effectiveness, serta mengidentifikasi bottleneck dalam complaint process atau area improvement.</p>'),
        ('<h3>Update Dokumentasi QMS</h3>\n              <p>Kami membantu organisasi memperbarui dokumen sistem manajemen mutu termasuk prosedur, instruksi kerja, dan formulir sesuai dengan perubahan proses bisnis, regulasi terbaru, dan best practice.</p>',
         '<h3>Update Dokumentasi CHMS</h3>\n              <p>Kami membantu organisasi memperbarui dokumen sistem penanganan keluhan termasuk complaint handling procedures, escalation matrix, dan customer communication protocols sesuai dengan perubahan kebutuhan pelanggan dan teknologi CRM terkini.</p>'),
        ('<h3>Improvement Planning</h3>\n              <p>Tim konsultan membantu menyusun rencana perbaikan dan peningkatan berkelanjutan, mengembangkan action plan untuk mengatasi temuan gap analysis, dan menetapkan target improvement yang terukur.</p>',
         '<h3>Improvement Planning</h3>\n              <p>Tim konsultan membantu menyusun rencana peningkatan complaint handling effectiveness, mengembangkan action plan untuk mengatasi temuan gap analysis dan recurring complaints, serta menetapkan target complaint resolution yang terukur.</p>'),
        ('<h3>Implementation Support</h3>\n              <p>Konsultan memberikan pendampingan dalam implementasi perbaikan, pelatihan refreshment untuk personel kunci, dan fasilitasi management review untuk memastikan komitmen top management terhadap pemeliharaan QMS.</p>',
         '<h3>Implementation Support</h3>\n              <p>Konsultan memberikan pendampingan dalam implementasi complaint handling improvements, pelatihan customer service skills untuk personel, dan fasilitasi management review untuk memastikan komitmen top management terhadap pemeliharaan CHMS.</p>'),
        ('<h3>Monitoring & Follow-up</h3>\n              <p>Kami melakukan monitoring berkelanjutan terhadap efektivitas pemeliharaan sistem, evaluasi pencapaian KPI mutu, dan memberikan dukungan konsultasi untuk memastikan kesiapan menghadapi audit surveillance atau recertification.</p>',
         '<h3>Monitoring & Follow-up</h3>\n              <p>Kami melakukan monitoring berkelanjutan terhadap complaint handling performance, evaluasi customer satisfaction dan complaint trends, dan memberikan dukungan konsultasi untuk memastikan kesiapan menghadapi audit surveillance atau recertification.</p>'),
        ('<h2 class="iso-target-section-title" style="margin-bottom: 3rem;">Fokus Pemeliharaan Sistem Manajemen ISO 9001</h2>',
         '<h2 class="iso-target-section-title" style="margin-bottom: 3rem;">Fokus Pemeliharaan Sistem Manajemen ISO 10002</h2>'),
        ('<div class="iso-target-card"><h4>Document Control</h4></div>', '<div class="iso-target-card"><h4>Complaint Handling Process</h4></div>'),
        ('<div class="iso-target-card"><h4>Records Management</h4></div>', '<div class="iso-target-card"><h4>Response Time Management</h4></div>'),
        ('<div class="iso-target-card"><h4>Process Monitoring</h4></div>', '<div class="iso-target-card"><h4>Complaint Recording</h4></div>'),
        ('<div class="iso-target-card"><h4>KPI & Performance Tracking</h4></div>', '<div class="iso-target-card"><h4>Resolution Tracking</h4></div>'),
        ('<div class="iso-target-card"><h4>Internal Audit Program</h4></div>', '<div class="iso-target-card"><h4>Root Cause Analysis</h4></div>'),
        ('<div class="iso-target-card"><h4>Management Review</h4></div>', '<div class="iso-target-card"><h4>Customer Communication</h4></div>'),
        ('<div class="iso-target-card"><h4>Corrective Actions</h4></div>', '<div class="iso-target-card"><h4>Preventive Actions</h4></div>'),
        ('<div class="iso-target-card"><h4>Customer Satisfaction</h4></div>', '<div class="iso-target-card"><h4>Satisfaction Monitoring</h4></div>'),
        ('<div class="iso-target-card"><h4>Continuous Improvement</h4></div>', '<div class="iso-target-card"><h4>Continuous Improvement CHMS</h4></div>'),
    ],

    # =========================================================================
    # 5. ISO 30301 - Records Management System
    # =========================================================================
    'layanan-detail-pemeliharaan-iso-30301.html': [
        ('Pemeliharaan ISO/SNI 9001', 'Pemeliharaan ISO 30301'),
        ('<title>Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001 – Sistem Manajemen Mutu — INOVASS</title>',
         '<title>Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 30301 – Sistem Manajemen Pengelolaan Arsip — INOVASS</title>'),
        ('<h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important; font-weight: 700 !important;">Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001 – Sistem Manajemen Mutu</h1>',
         '<h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important; font-weight: 700 !important;">Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 30301 – Sistem Manajemen Pengelolaan Arsip</h1>'),
        ('<h2 class="benefit-highlight-title">Dengan Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015 Organisasi Anda Dapat:</h2>',
         '<h2 class="benefit-highlight-title">Dengan Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 30301:2019 Organisasi Anda Dapat:</h2>'),
        ('<p>Memastikan Kesesuaian<br>Berkelanjutan</p>', '<p>Pengelolaan Arsip<br>Terstruktur</p>'),
        ('<p>Menjaga Efektivitas<br>Sistem</p>', '<p>Compliance<br>Regulasi</p>'),
        ('<p>Mempertahankan<br>Sertifikasi</p>', '<p>Information<br>Governance</p>'),
        ('<h2 class="iso-content-title">Pengertian Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015</h2>',
         '<h2 class="iso-content-title">Pengertian Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 30301:2019</h2>'),
        ('Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015 adalah layanan profesional yang membantu organisasi memelihara, memonitor, dan meningkatkan efektivitas sistem manajemen mutu secara berkelanjutan untuk mempertahankan sertifikasi dan performa organisasi.',
         'Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 30301:2019 adalah layanan profesional yang membantu organisasi memelihara, memonitor, dan meningkatkan efektivitas sistem manajemen pengelolaan arsip secara berkelanjutan untuk mempertahankan sertifikasi dan information governance organisasi.'),
        ('<h2 class="iso-benefit-section-title">Manfaat Konsultasi Pemeliharaan Sistem Manajemen ISO 9001</h2>',
         '<h2 class="iso-benefit-section-title">Manfaat Konsultasi Pemeliharaan Sistem Manajemen ISO 30301</h2>'),
        ('<h3>Pemeliharaan Dokumentasi</h3>\n            <p>Membantu update dan pemeliharaan dokumentasi sistem sesuai perubahan proses bisnis</p>',
         '<h3>Records Classification</h3>\n            <p>Membantu update records classification scheme dan retention schedule</p>'),
        ('<h3>Monitoring Berkelanjutan</h3>\n            <p>Monitoring efektivitas sistem secara rutin untuk memastikan kesesuaian berkelanjutan</p>',
         '<h3>Archives Monitoring</h3>\n            <p>Monitoring efektivitas pengelolaan arsip untuk memastikan compliance dan accessibility</p>'),
        ('<h3>Improvement Support</h3>\n            <p>Dukungan dalam implementasi peningkatan berkelanjutan dan corrective actions</p>',
         '<h3>Digital Preservation</h3>\n            <p>Dukungan dalam implementasi digital preservation dan migration strategies</p>'),
        ('<h3>Compliance Assurance</h3>\n            <p>Memastikan compliance berkelanjutan terhadap persyaratan ISO 9001:2015</p>',
         '<h3>Compliance MSR</h3>\n            <p>Memastikan compliance berkelanjutan terhadap persyaratan ISO 30301:2019</p>'),
        ('<h3>Performance Review</h3>\n            <p>Review berkala terhadap KPI dan performance indicators sistem manajemen mutu</p>',
         '<h3>Records Performance</h3>\n            <p>Review berkala terhadap records management performance dan retention compliance</p>'),
        ('<h2 class="iso-process-title">Proses Konsultasi Pemeliharaan Sistem Manajemen Mutu ISO/SNI 9001:2015</h2>',
         '<h2 class="iso-process-title">Proses Konsultasi Pemeliharaan Sistem Manajemen Pengelolaan Arsip ISO 30301:2019</h2>'),
        ('<h3>Assessment Sistem Berjalan</h3>\n              <p>Kami melakukan evaluasi komprehensif terhadap implementasi sistem manajemen mutu, meninjau efektivitas proses QMS, dan mengidentifikasi area yang memerlukan perbaikan atau peningkatan.</p>',
         '<h3>Assessment Sistem Berjalan</h3>\n              <p>Kami melakukan evaluasi komprehensif terhadap implementasi sistem manajemen arsip, meninjau efektivitas records lifecycle management, dan mengidentifikasi area yang memerlukan perbaikan dalam pengelolaan arsip.</p>'),
        ('<h3>Gap Analysis & Review</h3>\n              <p>Tim konsultan melakukan analisis kesenjangan antara praktik saat ini dengan persyaratan ISO 9001:2015, meninjau hasil audit internal, dan mengidentifikasi potensi ketidaksesuaian atau area improvement.</p>',
         '<h3>Gap Analysis & Review</h3>\n              <p>Tim konsultan melakukan analisis kesenjangan antara praktik saat ini dengan persyaratan ISO 30301:2019, meninjau classification scheme dan retention compliance, serta mengidentifikasi gaps dalam records management.</p>'),
        ('<h3>Update Dokumentasi QMS</h3>\n              <p>Kami membantu organisasi memperbarui dokumen sistem manajemen mutu termasuk prosedur, instruksi kerja, dan formulir sesuai dengan perubahan proses bisnis, regulasi terbaru, dan best practice.</p>',
         '<h3>Update Dokumentasi MSR</h3>\n              <p>Kami membantu organisasi memperbarui dokumen sistem manajemen arsip termasuk classification scheme, retention schedule, dan disposal procedures sesuai dengan perubahan regulasi dan teknologi arsip terkini.</p>'),
        ('<h3>Improvement Planning</h3>\n              <p>Tim konsultan membantu menyusun rencana perbaikan dan peningkatan berkelanjutan, mengembangkan action plan untuk mengatasi temuan gap analysis, dan menetapkan target improvement yang terukur.</p>',
         '<h3>Improvement Planning</h3>\n              <p>Tim konsultan membantu menyusun rencana peningkatan records management, mengembangkan action plan untuk mengatasi temuan gap analysis dan compliance issues, serta menetapkan target information governance yang terukur.</p>'),
        ('<h3>Implementation Support</h3>\n              <p>Konsultan memberikan pendampingan dalam implementasi perbaikan, pelatihan refreshment untuk personel kunci, dan fasilitasi management review untuk memastikan komitmen top management terhadap pemeliharaan QMS.</p>',
         '<h3>Implementation Support</h3>\n              <p>Konsultan memberikan pendampingan dalam implementasi records improvements, pelatihan records management untuk personel, dan fasilitasi management review untuk memastikan komitmen top management terhadap pemeliharaan MSR.</p>'),
        ('<h3>Monitoring & Follow-up</h3>\n              <p>Kami melakukan monitoring berkelanjutan terhadap efektivitas pemeliharaan sistem, evaluasi pencapaian KPI mutu, dan memberikan dukungan konsultasi untuk memastikan kesiapan menghadapi audit surveillance atau recertification.</p>',
         '<h3>Monitoring & Follow-up</h3>\n              <p>Kami melakukan monitoring berkelanjutan terhadap records management performance, evaluasi retention compliance dan accessibility, dan memberikan dukungan konsultasi untuk memastikan kesiapan menghadapi audit surveillance atau recertification.</p>'),
        ('<h2 class="iso-target-section-title" style="margin-bottom: 3rem;">Fokus Pemeliharaan Sistem Manajemen ISO 9001</h2>',
         '<h2 class="iso-target-section-title" style="margin-bottom: 3rem;">Fokus Pemeliharaan Sistem Manajemen ISO 30301</h2>'),
        ('<div class="iso-target-card"><h4>Document Control</h4></div>', '<div class="iso-target-card"><h4>Records Classification</h4></div>'),
        ('<div class="iso-target-card"><h4>Records Management</h4></div>', '<div class="iso-target-card"><h4>Retention Schedule</h4></div>'),
        ('<div class="iso-target-card"><h4>Process Monitoring</h4></div>', '<div class="iso-target-card"><h4>Lifecycle Management</h4></div>'),
        ('<div class="iso-target-card"><h4>KPI & Performance Tracking</h4></div>', '<div class="iso-target-card"><h4>Disposal Procedures</h4></div>'),
        ('<div class="iso-target-card"><h4>Internal Audit Program</h4></div>', '<div class="iso-target-card"><h4>Access Controls</h4></div>'),
        ('<div class="iso-target-card"><h4>Management Review</h4></div>', '<div class="iso-target-card"><h4>Digital Preservation</h4></div>'),
        ('<div class="iso-target-card"><h4>Corrective Actions</h4></div>', '<div class="iso-target-card"><h4>Compliance Monitoring</h4></div>'),
        ('<div class="iso-target-card"><h4>Customer Satisfaction</h4></div>', '<div class="iso-target-card"><h4>Information Governance</h4></div>'),
        ('<div class="iso-target-card"><h4>Continuous Improvement</h4></div>', '<div class="iso-target-card"><h4>Continuous Improvement MSR</h4></div>'),
    ],

    # =========================================================================
    # 6. ISO/IEC 20000-1 - IT Service Management System
    # =========================================================================
    'layanan-detail-pemeliharaan-iso-20000-1.html': [
        ('Pemeliharaan ISO/SNI 9001', 'Pemeliharaan ISO/IEC 20000-1'),
        ('<title>Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001 – Sistem Manajemen Mutu — INOVASS</title>',
         '<title>Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/IEC 20000-1 – Sistem Manajemen Layanan Teknologi Informasi — INOVASS</title>'),
        ('<h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important; font-weight: 700 !important;">Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001 – Sistem Manajemen Mutu</h1>',
         '<h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important; font-weight: 700 !important;">Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/IEC 20000-1 – Sistem Manajemen Layanan Teknologi Informasi</h1>'),
        ('<h2 class="benefit-highlight-title">Dengan Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015 Organisasi Anda Dapat:</h2>',
         '<h2 class="benefit-highlight-title">Dengan Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/IEC 20000-1:2018 Organisasi Anda Dapat:</h2>'),
        ('<p>Memastikan Kesesuaian<br>Berkelanjutan</p>', '<p>Service Quality<br>Excellence</p>'),
        ('<p>Menjaga Efektivitas<br>Sistem</p>', '<p>IT Service<br>Reliability</p>'),
        ('<p>Mempertahankan<br>Sertifikasi</p>', '<p>Customer<br>Satisfaction IT</p>'),
        ('<h2 class="iso-content-title">Pengertian Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015</h2>',
         '<h2 class="iso-content-title">Pengertian Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/IEC 20000-1:2018</h2>'),
        ('Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015 adalah layanan profesional yang membantu organisasi memelihara, memonitor, dan meningkatkan efektivitas sistem manajemen mutu secara berkelanjutan untuk mempertahankan sertifikasi dan performa organisasi.',
         'Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/IEC 20000-1:2018 adalah layanan profesional yang membantu organisasi memelihara, memonitor, dan meningkatkan efektivitas sistem manajemen layanan TI secara berkelanjutan untuk mempertahankan sertifikasi dan service delivery excellence.'),
        ('<h2 class="iso-benefit-section-title">Manfaat Konsultasi Pemeliharaan Sistem Manajemen ISO 9001</h2>',
         '<h2 class="iso-benefit-section-title">Manfaat Konsultasi Pemeliharaan Sistem Manajemen ISO/IEC 20000-1</h2>'),
        ('<h3>Pemeliharaan Dokumentasi</h3>\n            <p>Membantu update dan pemeliharaan dokumentasi sistem sesuai perubahan proses bisnis</p>',
         '<h3>Service Catalog Update</h3>\n            <p>Membantu update service catalog dan SLA sesuai perubahan kebutuhan bisnis</p>'),
        ('<h3>Monitoring Berkelanjutan</h3>\n            <p>Monitoring efektivitas sistem secara rutin untuk memastikan kesesuaian berkelanjutan</p>',
         '<h3>Service Monitoring</h3>\n            <p>Monitoring service performance dan SLA compliance secara real-time</p>'),
        ('<h3>Improvement Support</h3>\n            <p>Dukungan dalam implementasi peningkatan berkelanjutan dan corrective actions</p>',
         '<h3>Service Improvement</h3>\n            <p>Dukungan dalam implementasi continual service improvement dan automation</p>'),
        ('<h3>Compliance Assurance</h3>\n            <p>Memastikan compliance berkelanjutan terhadap persyaratan ISO 9001:2015</p>',
         '<h3>Compliance SMS</h3>\n            <p>Memastikan compliance berkelanjutan terhadap persyaratan ISO/IEC 20000-1:2018</p>'),
        ('<h3>Performance Review</h3>\n            <p>Review berkala terhadap KPI dan performance indicators sistem manajemen mutu</p>',
         '<h3>Service Performance</h3>\n            <p>Review berkala terhadap service KPIs dan customer satisfaction metrics</p>'),
        ('<h2 class="iso-process-title">Proses Konsultasi Pemeliharaan Sistem Manajemen Mutu ISO/SNI 9001:2015</h2>',
         '<h2 class="iso-process-title">Proses Konsultasi Pemeliharaan Sistem Manajemen Layanan TI ISO/IEC 20000-1:2018</h2>'),
        ('<h3>Assessment Sistem Berjalan</h3>\n              <p>Kami melakukan evaluasi komprehensif terhadap implementasi sistem manajemen mutu, meninjau efektivitas proses QMS, dan mengidentifikasi area yang memerlukan perbaikan atau peningkatan.</p>',
         '<h3>Assessment Sistem Berjalan</h3>\n              <p>Kami melakukan evaluasi komprehensif terhadap implementasi sistem manajemen layanan TI, meninjau efektivitas service delivery dan ITIL processes, serta mengidentifikasi area yang memerlukan perbaikan dalam IT service management.</p>'),
        ('<h3>Gap Analysis & Review</h3>\n              <p>Tim konsultan melakukan analisis kesenjangan antara praktik saat ini dengan persyaratan ISO 9001:2015, meninjau hasil audit internal, dan mengidentifikasi potensi ketidaksesuaian atau area improvement.</p>',
         '<h3>Gap Analysis & Review</h3>\n              <p>Tim konsultan melakukan analisis kesenjangan antara praktik saat ini dengan persyaratan ISO/IEC 20000-1:2018, meninjau SLA performance dan incident management, serta mengidentifikasi service gaps atau area improvement.</p>'),
        ('<h3>Update Dokumentasi QMS</h3>\n              <p>Kami membantu organisasi memperbarui dokumen sistem manajemen mutu termasuk prosedur, instruksi kerja, dan formulir sesuai dengan perubahan proses bisnis, regulasi terbaru, dan best practice.</p>',
         '<h3>Update Dokumentasi SMS</h3>\n              <p>Kami membantu organisasi memperbarui dokumen sistem manajemen layanan TI termasuk service catalog, SLA, dan operational procedures sesuai dengan perubahan teknologi dan ITIL best practices terkini.</p>'),
        ('<h3>Improvement Planning</h3>\n              <p>Tim konsultan membantu menyusun rencana perbaikan dan peningkatan berkelanjutan, mengembangkan action plan untuk mengatasi temuan gap analysis, dan menetapkan target improvement yang terukur.</p>',
         '<h3>Improvement Planning</h3>\n              <p>Tim konsultan membantu menyusun rencana service improvement, mengembangkan action plan untuk mengatasi temuan gap analysis dan SLA breaches, serta menetapkan target service excellence yang terukur.</p>'),
        ('<h3>Implementation Support</h3>\n              <p>Konsultan memberikan pendampingan dalam implementasi perbaikan, pelatihan refreshment untuk personel kunci, dan fasilitasi management review untuk memastikan komitmen top management terhadap pemeliharaan QMS.</p>',
         '<h3>Implementation Support</h3>\n              <p>Konsultan memberikan pendampingan dalam implementasi service improvements, pelatihan ITIL untuk IT teams, dan fasilitasi management review untuk memastikan komitmen top management terhadap pemeliharaan SMS.</p>'),
        ('<h3>Monitoring & Follow-up</h3>\n              <p>Kami melakukan monitoring berkelanjutan terhadap efektivitas pemeliharaan sistem, evaluasi pencapaian KPI mutu, dan memberikan dukungan konsultasi untuk memastikan kesiapan menghadapi audit surveillance atau recertification.</p>',
         '<h3>Monitoring & Follow-up</h3>\n              <p>Kami melakukan monitoring berkelanjutan terhadap service performance, evaluasi SLA compliance dan customer satisfaction, dan memberikan dukungan konsultasi untuk memastikan kesiapan menghadapi audit surveillance atau recertification.</p>'),
        ('<h2 class="iso-target-section-title" style="margin-bottom: 3rem;">Fokus Pemeliharaan Sistem Manajemen ISO 9001</h2>',
         '<h2 class="iso-target-section-title" style="margin-bottom: 3rem;">Fokus Pemeliharaan Sistem Manajemen ISO/IEC 20000-1</h2>'),
        ('<div class="iso-target-card"><h4>Document Control</h4></div>', '<div class="iso-target-card"><h4>Service Catalog</h4></div>'),
        ('<div class="iso-target-card"><h4>Records Management</h4></div>', '<div class="iso-target-card"><h4>SLA Management</h4></div>'),
        ('<div class="iso-target-card"><h4>Process Monitoring</h4></div>', '<div class="iso-target-card"><h4>Incident Management</h4></div>'),
        ('<div class="iso-target-card"><h4>KPI & Performance Tracking</h4></div>', '<div class="iso-target-card"><h4>Problem Management</h4></div>'),
        ('<div class="iso-target-card"><h4>Internal Audit Program</h4></div>', '<div class="iso-target-card"><h4>Change Management</h4></div>'),
        ('<div class="iso-target-card"><h4>Management Review</h4></div>', '<div class="iso-target-card"><h4>Release Management</h4></div>'),
        ('<div class="iso-target-card"><h4>Corrective Actions</h4></div>', '<div class="iso-target-card"><h4>Service Continuity</h4></div>'),
        ('<div class="iso-target-card"><h4>Customer Satisfaction</h4></div>', '<div class="iso-target-card"><h4>Service Performance</h4></div>'),
        ('<div class="iso-target-card"><h4>Continuous Improvement</h4></div>', '<div class="iso-target-card"><h4>Continual Service Improvement</h4></div>'),
    ],

    # =========================================================================
    # 7. ISO 35001 - Biorisk Management for Laboratories
    # =========================================================================
    'layanan-detail-pemeliharaan-iso-35001.html': [
        ('Pemeliharaan ISO/SNI 9001', 'Pemeliharaan ISO 35001'),
        ('<title>Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001 – Sistem Manajemen Mutu — INOVASS</title>',
         '<title>Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 35001 – Sistem Manajemen Biorisiko Laboratorium — INOVASS</title>'),
        ('<h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important; font-weight: 700 !important;">Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001 – Sistem Manajemen Mutu</h1>',
         '<h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important; font-weight: 700 !important;">Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 35001 – Sistem Manajemen Biorisiko Laboratorium</h1>'),
        ('<h2 class="benefit-highlight-title">Dengan Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015 Organisasi Anda Dapat:</h2>',
         '<h2 class="benefit-highlight-title">Dengan Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 35001:2019 Organisasi Anda Dapat:</h2>'),
        ('<p>Memastikan Kesesuaian<br>Berkelanjutan</p>', '<p>Keamanan<br>Laboratorium</p>'),
        ('<p>Menjaga Efektivitas<br>Sistem</p>', '<p>Biorisk<br>Mitigation</p>'),
        ('<p>Mempertahankan<br>Sertifikasi</p>', '<p>Laboratory<br>Safety</p>'),
        ('<h2 class="iso-content-title">Pengertian Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015</h2>',
         '<h2 class="iso-content-title">Pengertian Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 35001:2019</h2>'),
        ('Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015 adalah layanan profesional yang membantu organisasi memelihara, memonitor, dan meningkatkan efektivitas sistem manajemen mutu secara berkelanjutan untuk mempertahankan sertifikasi dan performa organisasi.',
         'Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 35001:2019 adalah layanan profesional yang membantu laboratorium memelihara, memonitor, dan meningkatkan efektivitas sistem manajemen biorisiko secara berkelanjutan untuk mempertahankan sertifikasi dan keamanan laboratorium.'),
        ('<h2 class="iso-benefit-section-title">Manfaat Konsultasi Pemeliharaan Sistem Manajemen ISO 9001</h2>',
         '<h2 class="iso-benefit-section-title">Manfaat Konsultasi Pemeliharaan Sistem Manajemen ISO 35001</h2>'),
        ('<h3>Pemeliharaan Dokumentasi</h3>\n            <p>Membantu update dan pemeliharaan dokumentasi sistem sesuai perubahan proses bisnis</p>',
         '<h3>Biorisk Assessment Update</h3>\n            <p>Membantu update biorisk assessment dan control measures sesuai perubahan aktivitas lab</p>'),
        ('<h3>Monitoring Berkelanjutan</h3>\n            <p>Monitoring efektivitas sistem secara rutin untuk memastikan kesesuaian berkelanjutan</p>',
         '<h3>Safety Monitoring</h3>\n            <p>Monitoring lab safety performance dan biosafety compliance secara berkelanjutan</p>'),
        ('<h3>Improvement Support</h3>\n            <p>Dukungan dalam implementasi peningkatan berkelanjutan dan corrective actions</p>',
         '<h3>Biorisk Control</h3>\n            <p>Dukungan dalam implementasi biorisk control measures dan biosecurity protocols</p>'),
        ('<h3>Compliance Assurance</h3>\n            <p>Memastikan compliance berkelanjutan terhadap persyaratan ISO 9001:2015</p>',
         '<h3>Compliance BRMS</h3>\n            <p>Memastikan compliance berkelanjutan terhadap persyaratan ISO 35001:2019</p>'),
        ('<h3>Performance Review</h3>\n            <p>Review berkala terhadap KPI dan performance indicators sistem manajemen mutu</p>',
         '<h3>Safety Performance</h3>\n            <p>Review berkala terhadap laboratory safety KPIs dan incident statistics</p>'),
        ('<h2 class="iso-process-title">Proses Konsultasi Pemeliharaan Sistem Manajemen Mutu ISO/SNI 9001:2015</h2>',
         '<h2 class="iso-process-title">Proses Konsultasi Pemeliharaan Sistem Manajemen Biorisiko Laboratorium ISO 35001:2019</h2>'),
        ('<h3>Assessment Sistem Berjalan</h3>\n              <p>Kami melakukan evaluasi komprehensif terhadap implementasi sistem manajemen mutu, meninjau efektivitas proses QMS, dan mengidentifikasi area yang memerlukan perbaikan atau peningkatan.</p>',
         '<h3>Assessment Sistem Berjalan</h3>\n              <p>Kami melakukan evaluasi komprehensif terhadap implementasi sistem manajemen biorisiko, meninjau efektivitas control measures dan biosafety protocols, serta mengidentifikasi area yang memerlukan perbaikan dalam lab safety.</p>'),
        ('<h3>Gap Analysis & Review</h3>\n              <p>Tim konsultan melakukan analisis kesenjangan antara praktik saat ini dengan persyaratan ISO 9001:2015, meninjau hasil audit internal, dan mengidentifikasi potensi ketidaksesuaian atau area improvement.</p>',
         '<h3>Gap Analysis & Review</h3>\n              <p>Tim konsultan melakukan analisis kesenjangan antara praktik saat ini dengan persyaratan ISO 35001:2019, meninjau biorisk assessment dan incident data, serta mengidentifikasi potential hazards atau area improvement dalam BRMS.</p>'),
        ('<h3>Update Dokumentasi QMS</h3>\n              <p>Kami membantu organisasi memperbarui dokumen sistem manajemen mutu termasuk prosedur, instruksi kerja, dan formulir sesuai dengan perubahan proses bisnis, regulasi terbaru, dan best practice.</p>',
         '<h3>Update Dokumentasi BRMS</h3>\n              <p>Kami membantu laboratorium memperbarui dokumen sistem manajemen biorisiko termasuk biorisk register, SOPs, dan emergency procedures sesuai dengan perubahan aktivitas lab dan regulasi biosafety terkini.</p>'),
        ('<h3>Improvement Planning</h3>\n              <p>Tim konsultan membantu menyusun rencana perbaikan dan peningkatan berkelanjutan, mengembangkan action plan untuk mengatasi temuan gap analysis, dan menetapkan target improvement yang terukur.</p>',
         '<h3>Improvement Planning</h3>\n              <p>Tim konsultan membantu menyusun rencana peningkatan laboratory safety, mengembangkan action plan untuk mengatasi temuan gap analysis dan incident findings, serta menetapkan target zero incidents yang terukur.</p>'),
        ('<h3>Implementation Support</h3>\n              <p>Konsultan memberikan pendampingan dalam implementasi perbaikan, pelatihan refreshment untuk personel kunci, dan fasilitasi management review untuk memastikan komitmen top management terhadap pemeliharaan QMS.</p>',
         '<h3>Implementation Support</h3>\n              <p>Konsultan memberikan pendampingan dalam implementasi safety improvements, pelatihan biosafety untuk laboratory staff, dan fasilitasi management review untuk memastikan komitmen top management terhadap pemeliharaan BRMS.</p>'),
        ('<h3>Monitoring & Follow-up</h3>\n              <p>Kami melakukan monitoring berkelanjutan terhadap efektivitas pemeliharaan sistem, evaluasi pencapaian KPI mutu, dan memberikan dukungan konsultasi untuk memastikan kesiapan menghadapi audit surveillance atau recertification.</p>',
         '<h3>Monitoring & Follow-up</h3>\n              <p>Kami melakukan monitoring berkelanjutan terhadap lab safety performance, evaluasi biosafety compliance dan incident trends, dan memberikan dukungan konsultasi untuk memastikan kesiapan menghadapi audit surveillance atau recertification.</p>'),
        ('<h2 class="iso-target-section-title" style="margin-bottom: 3rem;">Fokus Pemeliharaan Sistem Manajemen ISO 9001</h2>',
         '<h2 class="iso-target-section-title" style="margin-bottom: 3rem;">Fokus Pemeliharaan Sistem Manajemen ISO 35001</h2>'),
        ('<div class="iso-target-card"><h4>Document Control</h4></div>', '<div class="iso-target-card"><h4>Biorisk Assessment</h4></div>'),
        ('<div class="iso-target-card"><h4>Records Management</h4></div>', '<div class="iso-target-card"><h4>Biosafety Protocols</h4></div>'),
        ('<div class="iso-target-card"><h4>Process Monitoring</h4></div>', '<div class="iso-target-card"><h4>Biosecurity Measures</h4></div>'),
        ('<div class="iso-target-card"><h4>KPI & Performance Tracking</h4></div>', '<div class="iso-target-card"><h4>Containment Control</h4></div>'),
        ('<div class="iso-target-card"><h4>Internal Audit Program</h4></div>', '<div class="iso-target-card"><h4>Incident Management</h4></div>'),
        ('<div class="iso-target-card"><h4>Management Review</h4></div>', '<div class="iso-target-card"><h4>Emergency Response</h4></div>'),
        ('<div class="iso-target-card"><h4>Corrective Actions</h4></div>', '<div class="iso-target-card"><h4>PPE Management</h4></div>'),
        ('<div class="iso-target-card"><h4>Customer Satisfaction</h4></div>', '<div class="iso-target-card"><h4>Laboratory Safety</h4></div>'),
        ('<div class="iso-target-card"><h4>Continuous Improvement</h4></div>', '<div class="iso-target-card"><h4>Continuous Improvement BRMS</h4></div>'),
    ],

    # =========================================================================
    # 8. IMS - Integrated Management System
    # =========================================================================
    'layanan-detail-pemeliharaan-ims.html': [
        ('Pemeliharaan ISO/SNI 9001', 'Pemeliharaan IMS'),
        ('<title>Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001 – Sistem Manajemen Mutu — INOVASS</title>',
         '<title>Jasa Konsultasi Pemeliharaan Integrated Management System (IMS) ISO/IEC/SNI — INOVASS</title>'),
        ('<h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important; font-weight: 700 !important;">Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001 – Sistem Manajemen Mutu</h1>',
         '<h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important; font-weight: 700 !important;">Jasa Konsultasi Pemeliharaan Integrated Management System (IMS) ISO/IEC/SNI</h1>'),
        ('<h2 class="benefit-highlight-title">Dengan Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015 Organisasi Anda Dapat:</h2>',
         '<h2 class="benefit-highlight-title">Dengan Jasa Konsultasi Pemeliharaan Integrated Management System (IMS) Organisasi Anda Dapat:</h2>'),
        ('<p>Memastikan Kesesuaian<br>Berkelanjutan</p>', '<p>Sistem Terintegrasi<br>Efisien</p>'),
        ('<p>Menjaga Efektivitas<br>Sistem</p>', '<p>Eliminasi<br>Duplikasi</p>'),
        ('<p>Mempertahankan<br>Sertifikasi</p>', '<p>Multi-Standard<br>Compliance</p>'),
        ('<h2 class="iso-content-title">Pengertian Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015</h2>',
         '<h2 class="iso-content-title">Pengertian Jasa Konsultasi Pemeliharaan Integrated Management System (IMS)</h2>'),
        ('Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015 adalah layanan profesional yang membantu organisasi memelihara, memonitor, dan meningkatkan efektivitas sistem manajemen mutu secara berkelanjutan untuk mempertahankan sertifikasi dan performa organisasi.',
         'Jasa Konsultasi Pemeliharaan Integrated Management System (IMS) adalah layanan profesional yang membantu organisasi memelihara, memonitor, dan meningkatkan efektivitas sistem manajemen terintegrasi (kombinasi multiple ISO standards) secara berkelanjutan untuk mempertahankan multi-certification dan operational excellence.'),
        ('<h2 class="iso-benefit-section-title">Manfaat Konsultasi Pemeliharaan Sistem Manajemen ISO 9001</h2>',
         '<h2 class="iso-benefit-section-title">Manfaat Konsultasi Pemeliharaan Integrated Management System (IMS)</h2>'),
        ('<h3>Pemeliharaan Dokumentasi</h3>\n            <p>Membantu update dan pemeliharaan dokumentasi sistem sesuai perubahan proses bisnis</p>',
         '<h3>Integrated Documentation</h3>\n            <p>Membantu update dokumentasi terintegrasi untuk multiple standards secara efisien</p>'),
        ('<h3>Monitoring Berkelanjutan</h3>\n            <p>Monitoring efektivitas sistem secara rutin untuk memastikan kesesuaian berkelanjutan</p>',
         '<h3>Holistic Monitoring</h3>\n            <p>Monitoring efektivitas IMS secara holistik untuk memastikan compliance multi-standard</p>'),
        ('<h3>Improvement Support</h3>\n            <p>Dukungan dalam implementasi peningkatan berkelanjutan dan corrective actions</p>',
         '<h3>Synergy Optimization</h3>\n            <p>Dukungan dalam optimasi sinergi antar standards dan eliminasi redundancy</p>'),
        ('<h3>Compliance Assurance</h3>\n            <p>Memastikan compliance berkelanjutan terhadap persyaratan ISO 9001:2015</p>',
         '<h3>Multi-Compliance</h3>\n            <p>Memastikan compliance berkelanjutan terhadap multiple ISO/IEC/SNI standards</p>'),
        ('<h3>Performance Review</h3>\n            <p>Review berkala terhadap KPI dan performance indicators sistem manajemen mutu</p>',
         '<h3>Integrated Performance</h3>\n            <p>Review berkala terhadap integrated KPIs dan overall system performance</p>'),
        ('<h2 class="iso-process-title">Proses Konsultasi Pemeliharaan Sistem Manajemen Mutu ISO/SNI 9001:2015</h2>',
         '<h2 class="iso-process-title">Proses Konsultasi Pemeliharaan Integrated Management System (IMS)</h2>'),
        ('<h3>Assessment Sistem Berjalan</h3>\n              <p>Kami melakukan evaluasi komprehensif terhadap implementasi sistem manajemen mutu, meninjau efektivitas proses QMS, dan mengidentifikasi area yang memerlukan perbaikan atau peningkatan.</p>',
         '<h3>Assessment Sistem Berjalan</h3>\n              <p>Kami melakukan evaluasi komprehensif terhadap implementasi IMS, meninjau efektivitas integrasi multiple standards dan synergy effectiveness, serta mengidentifikasi area yang memerlukan perbaikan dalam integrated system.</p>'),
        ('<h3>Gap Analysis & Review</h3>\n              <p>Tim konsultan melakukan analisis kesenjangan antara praktik saat ini dengan persyaratan ISO 9001:2015, meninjau hasil audit internal, dan mengidentifikasi potensi ketidaksesuaian atau area improvement.</p>',
         '<h3>Gap Analysis & Review</h3>\n              <p>Tim konsultan melakukan analisis kesenjangan antara praktik saat ini dengan persyaratan multiple standards, meninjau integration effectiveness dan redundancies, serta mengidentifikasi optimization opportunities dalam IMS.</p>'),
        ('<h3>Update Dokumentasi QMS</h3>\n              <p>Kami membantu organisasi memperbarui dokumen sistem manajemen mutu termasuk prosedur, instruksi kerja, dan formulir sesuai dengan perubahan proses bisnis, regulasi terbaru, dan best practice.</p>',
         '<h3>Update Dokumentasi IMS</h3>\n              <p>Kami membantu organisasi memperbarui dokumentasi terintegrasi termasuk common procedures, integrated processes, dan consolidated forms sesuai dengan perubahan requirements dan integration best practices.</p>'),
        ('<h3>Improvement Planning</h3>\n              <p>Tim konsultan membantu menyusun rencana perbaikan dan peningkatan berkelanjutan, mengembangkan action plan untuk mengatasi temuan gap analysis, dan menetapkan target improvement yang terukur.</p>',
         '<h3>Improvement Planning</h3>\n              <p>Tim konsultan membantu menyusun rencana peningkatan IMS, mengembangkan action plan untuk mengatasi temuan gap analysis dan integration gaps, serta menetapkan target synergy optimization yang terukur.</p>'),
        ('<h3>Implementation Support</h3>\n              <p>Konsultan memberikan pendampingan dalam implementasi perbaikan, pelatihan refreshment untuk personel kunci, dan fasilitasi management review untuk memastikan komitmen top management terhadap pemeliharaan QMS.</p>',
         '<h3>Implementation Support</h3>\n              <p>Konsultan memberikan pendampingan dalam implementasi IMS improvements, pelatihan integrated approach untuk teams, dan fasilitasi integrated management review untuk memastikan komitmen top management terhadap pemeliharaan IMS.</p>'),
        ('<h3>Monitoring & Follow-up</h3>\n              <p>Kami melakukan monitoring berkelanjutan terhadap efektivitas pemeliharaan sistem, evaluasi pencapaian KPI mutu, dan memberikan dukungan konsultasi untuk memastikan kesiapan menghadapi audit surveillance atau recertification.</p>',
         '<h3>Monitoring & Follow-up</h3>\n              <p>Kami melakukan monitoring berkelanjutan terhadap IMS effectiveness, evaluasi integrated performance dan multi-standard compliance, dan memberikan dukungan konsultasi untuk memastikan kesiapan menghadapi multiple audits surveillance atau recertification.</p>'),
        ('<h2 class="iso-target-section-title" style="margin-bottom: 3rem;">Fokus Pemeliharaan Sistem Manajemen ISO 9001</h2>',
         '<h2 class="iso-target-section-title" style="margin-bottom: 3rem;">Fokus Pemeliharaan Integrated Management System (IMS)</h2>'),
        ('<div class="iso-target-card"><h4>Document Control</h4></div>', '<div class="iso-target-card"><h4>Integrated Documentation</h4></div>'),
        ('<div class="iso-target-card"><h4>Records Management</h4></div>', '<div class="iso-target-card"><h4>Common Processes</h4></div>'),
        ('<div class="iso-target-card"><h4>Process Monitoring</h4></div>', '<div class="iso-target-card"><h4>Synergy Management</h4></div>'),
        ('<div class="iso-target-card"><h4>KPI & Performance Tracking</h4></div>', '<div class="iso-target-card"><h4>Integrated Audits</h4></div>'),
        ('<div class="iso-target-card"><h4>Internal Audit Program</h4></div>', '<div class="iso-target-card"><h4>Multi-Standard Compliance</h4></div>'),
        ('<div class="iso-target-card"><h4>Management Review</h4></div>', '<div class="iso-target-card"><h4>Integrated Management Review</h4></div>'),
        ('<div class="iso-target-card"><h4>Corrective Actions</h4></div>', '<div class="iso-target-card"><h4>Holistic Risk Management</h4></div>'),
        ('<div class="iso-target-card"><h4>Customer Satisfaction</h4></div>', '<div class="iso-target-card"><h4>Stakeholder Satisfaction</h4></div>'),
        ('<div class="iso-target-card"><h4>Continuous Improvement</h4></div>', '<div class="iso-target-card"><h4>Continuous IMS Improvement</h4></div>'),
    ],

    # =========================================================================
    # 9. Lainnya - Other ISO/IEC/SNI Standards
    # =========================================================================
    'layanan-detail-pemeliharaan-lainnya.html': [
        ('Pemeliharaan ISO/SNI 9001', 'Pemeliharaan ISO/IEC/SNI Lainnya'),
        ('<title>Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001 – Sistem Manajemen Mutu — INOVASS</title>',
         '<title>Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/IEC/SNI Lainnya — INOVASS</title>'),
        ('<h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important; font-weight: 700 !important;">Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001 – Sistem Manajemen Mutu</h1>',
         '<h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important; font-weight: 700 !important;">Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/IEC/SNI Lainnya</h1>'),
        ('<h2 class="benefit-highlight-title">Dengan Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015 Organisasi Anda Dapat:</h2>',
         '<h2 class="benefit-highlight-title">Dengan Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/IEC/SNI Lainnya Organisasi Anda Dapat:</h2>'),
        ('<p>Memastikan Kesesuaian<br>Berkelanjutan</p>', '<p>Flexibility<br>Standards</p>'),
        ('<p>Menjaga Efektivitas<br>Sistem</p>', '<p>Customized<br>Support</p>'),
        ('<p>Mempertahankan<br>Sertifikasi</p>', '<p>Multi-Industry<br>Compliance</p>'),
        ('<h2 class="iso-content-title">Pengertian Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015</h2>',
         '<h2 class="iso-content-title">Pengertian Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/IEC/SNI Lainnya</h2>'),
        ('Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015 adalah layanan profesional yang membantu organisasi memelihara, memonitor, dan meningkatkan efektivitas sistem manajemen mutu secara berkelanjutan untuk mempertahankan sertifikasi dan performa organisasi.',
         'Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/IEC/SNI Lainnya adalah layanan profesional yang membantu organisasi memelihara, memonitor, dan meningkatkan efektivitas berbagai sistem manajemen standar ISO/IEC/SNI lainnya secara berkelanjutan untuk mempertahankan sertifikasi dan compliance requirements sesuai kebutuhan industri spesifik.'),
        ('<h2 class="iso-benefit-section-title">Manfaat Konsultasi Pemeliharaan Sistem Manajemen ISO 9001</h2>',
         '<h2 class="iso-benefit-section-title">Manfaat Konsultasi Pemeliharaan Sistem Manajemen ISO/IEC/SNI Lainnya</h2>'),
        ('<h3>Pemeliharaan Dokumentasi</h3>\n            <p>Membantu update dan pemeliharaan dokumentasi sistem sesuai perubahan proses bisnis</p>',
         '<h3>Flexible Documentation</h3>\n            <p>Membantu update dan pemeliharaan dokumentasi untuk various standards sesuai kebutuhan spesifik</p>'),
        ('<h3>Monitoring Berkelanjutan</h3>\n            <p>Monitoring efektivitas sistem secara rutin untuk memastikan kesesuaian berkelanjutan</p>',
         '<h3>Customized Monitoring</h3>\n            <p>Monitoring efektivitas sistem secara customized untuk memastikan compliance specific standards</p>'),
        ('<h3>Improvement Support</h3>\n            <p>Dukungan dalam implementasi peningkatan berkelanjutan dan corrective actions</p>',
         '<h3>Tailored Improvement</h3>\n            <p>Dukungan dalam implementasi peningkatan yang disesuaikan dengan unique requirements</p>'),
        ('<h3>Compliance Assurance</h3>\n            <p>Memastikan compliance berkelanjutan terhadap persyaratan ISO 9001:2015</p>',
         '<h3>Multi-Standard Compliance</h3>\n            <p>Memastikan compliance berkelanjutan terhadap various ISO/IEC/SNI standards requirements</p>'),
        ('<h3>Performance Review</h3>\n            <p>Review berkala terhadap KPI dan performance indicators sistem manajemen mutu</p>',
         '<h3>Flexible Performance Review</h3>\n            <p>Review berkala terhadap KPIs sesuai dengan specific standards requirements</p>'),
        ('<h2 class="iso-process-title">Proses Konsultasi Pemeliharaan Sistem Manajemen Mutu ISO/SNI 9001:2015</h2>',
         '<h2 class="iso-process-title">Proses Konsultasi Pemeliharaan Sistem Manajemen ISO/IEC/SNI Lainnya</h2>'),
        ('<h3>Assessment Sistem Berjalan</h3>\n              <p>Kami melakukan evaluasi komprehensif terhadap implementasi sistem manajemen mutu, meninjau efektivitas proses QMS, dan mengidentifikasi area yang memerlukan perbaikan atau peningkatan.</p>',
         '<h3>Assessment Sistem Berjalan</h3>\n              <p>Kami melakukan evaluasi komprehensif terhadap implementasi sistem manajemen sesuai standard yang diterapkan, meninjau efektivitas processes, dan mengidentifikasi area yang memerlukan perbaikan atau enhancement.</p>'),
        ('<h3>Gap Analysis & Review</h3>\n              <p>Tim konsultan melakukan analisis kesenjangan antara praktik saat ini dengan persyaratan ISO 9001:2015, meninjau hasil audit internal, dan mengidentifikasi potensi ketidaksesuaian atau area improvement.</p>',
         '<h3>Gap Analysis & Review</h3>\n              <p>Tim konsultan melakukan analisis kesenjangan antara praktik saat ini dengan persyaratan specific standards, meninjau compliance status, dan mengidentifikasi gaps atau improvement opportunities.</p>'),
        ('<h3>Update Dokumentasi QMS</h3>\n              <p>Kami membantu organisasi memperbarui dokumen sistem manajemen mutu termasuk prosedur, instruksi kerja, dan formulir sesuai dengan perubahan proses bisnis, regulasi terbaru, dan best practice.</p>',
         '<h3>Update Dokumentasi MS</h3>\n              <p>Kami membantu organisasi memperbarui dokumentasi sistem manajemen sesuai dengan perubahan requirements, industry best practices, dan regulatory updates yang relevan.</p>'),
        ('<h3>Improvement Planning</h3>\n              <p>Tim konsultan membantu menyusun rencana perbaikan dan peningkatan berkelanjutan, mengembangkan action plan untuk mengatasi temuan gap analysis, dan menetapkan target improvement yang terukur.</p>',
         '<h3>Improvement Planning</h3>\n              <p>Tim konsultan membantu menyusun rencana perbaikan customized, mengembangkan action plan untuk mengatasi temuan gap analysis, dan menetapkan target improvement sesuai standard requirements.</p>'),
        ('<h3>Implementation Support</h3>\n              <p>Konsultan memberikan pendampingan dalam implementasi perbaikan, pelatihan refreshment untuk personel kunci, dan fasilitasi management review untuk memastikan komitmen top management terhadap pemeliharaan QMS.</p>',
         '<h3>Implementation Support</h3>\n              <p>Konsultan memberikan pendampingan dalam implementasi improvements, pelatihan tailored untuk personel, dan fasilitasi management review untuk memastikan komitmen top management terhadap pemeliharaan MS.</p>'),
        ('<h3>Monitoring & Follow-up</h3>\n              <p>Kami melakukan monitoring berkelanjutan terhadap efektivitas pemeliharaan sistem, evaluasi pencapaian KPI mutu, dan memberikan dukungan konsultasi untuk memastikan kesiapan menghadapi audit surveillance atau recertification.</p>',
         '<h3>Monitoring & Follow-up</h3>\n              <p>Kami melakukan monitoring berkelanjutan terhadap system effectiveness, evaluasi pencapaian KPIs sesuai standards, dan memberikan dukungan konsultasi untuk memastikan kesiapan menghadapi audit surveillance atau recertification.</p>'),
        ('<h2 class="iso-target-section-title" style="margin-bottom: 3rem;">Fokus Pemeliharaan Sistem Manajemen ISO 9001</h2>',
         '<h2 class="iso-target-section-title" style="margin-bottom: 3rem;">Fokus Pemeliharaan Sistem Manajemen ISO/IEC/SNI Lainnya</h2>'),
        ('<div class="iso-target-card"><h4>Document Control</h4></div>', '<div class="iso-target-card"><h4>Flexible Documentation</h4></div>'),
        ('<div class="iso-target-card"><h4>Records Management</h4></div>', '<div class="iso-target-card"><h4>Customized Processes</h4></div>'),
        ('<div class="iso-target-card"><h4>Process Monitoring</h4></div>', '<div class="iso-target-card"><h4>Tailored Monitoring</h4></div>'),
        ('<div class="iso-target-card"><h4>KPI & Performance Tracking</h4></div>', '<div class="iso-target-card"><h4>Standard-Specific KPIs</h4></div>'),
        ('<div class="iso-target-card"><h4>Internal Audit Program</h4></div>', '<div class="iso-target-card"><h4>Customized Audits</h4></div>'),
        ('<div class="iso-target-card"><h4>Management Review</h4></div>', '<div class="iso-target-card"><h4>Flexible Management Review</h4></div>'),
        ('<div class="iso-target-card"><h4>Corrective Actions</h4></div>', '<div class="iso-target-card"><h4>Tailored Actions</h4></div>'),
        ('<div class="iso-target-card"><h4>Customer Satisfaction</h4></div>', '<div class="iso-target-card"><h4>Stakeholder Satisfaction</h4></div>'),
        ('<div class="iso-target-card"><h4>Continuous Improvement</h4></div>', '<div class="iso-target-card"><h4>Continuous MS Improvement</h4></div>'),
    ],
}


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("="*80)
    print("COMPLETE CUSTOMIZATION SCRIPT - Pemeliharaan Pages")
    print("="*80)
    print(f"\nThis script will customize {len(files_data)} files")
    print("Please wait...\n")
    
    success_count = 0
    failed_files = []
    
    for filename, replacements in files_data.items():
        print(f"\nProcessing: {filename}")
        print(f"Total replacements to apply: {len(replacements)}")
        print("-" * 80)
        
        if customize_file(filename, replacements):
            success_count += 1
        else:
            failed_files.append(filename)
    
    print("\n" + "="*80)
    print("CUSTOMIZATION COMPLETE")
    print("="*80)
    print(f"\n✅ Successfully customized: {success_count}/{len(files_data)} files")
    
    if failed_files:
        print(f"\n❌ Failed files:")
        for f in failed_files:
            print(f"   - {f}")
    else:
        print("\n🎉 All files successfully customized!")
    
    print("\n" + "="*80)
