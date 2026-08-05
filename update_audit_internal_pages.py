#!/usr/bin/env python3
# Script untuk mengupdate konten halaman audit internal ISO

iso_standards = {
    '27001': {
        'title': 'Sistem Manajemen Keamanan Informasi',
        'breadcrumb': 'Audit Internal ISO/IEC 27001',
        'benefits': ['Melindungi Aset<br>Informasi', 'Mengidentifikasi Ancaman<br>Keamanan', 'Meningkatkan Keamanan<br>Informasi'],
        'description': 'Jasa Audit Internal ISO/IEC 27001:2022 adalah layanan profesional yang membantu organisasi melakukan evaluasi sistematis terhadap efektivitas penerapan Sistem Manajemen Keamanan Informasi, melindungi kerahasiaan, integritas, dan ketersediaan informasi, serta mengidentifikasi risiko keamanan informasi.',
        'benefit_title': 'Manfaat Audit Internal ISO 27001',
        'benefit_items': [
            ('Evaluasi Keamanan Informasi', 'Mendapatkan penilaian independen terhadap efektivitas sistem keamanan informasi'),
            ('Identifikasi Kerentanan', 'Mendeteksi kerentanan dan ancaman keamanan informasi secara sistematis'),
            ('Manajemen Risiko Informasi', 'Mengevaluasi efektivitas pengelolaan risiko keamanan informasi'),
            ('Kepatuhan Regulasi', 'Memastikan kepatuhan terhadap regulasi perlindungan data dan privasi'),
            ('Perlindungan Aset Digital', 'Meningkatkan perlindungan terhadap aset informasi organisasi'),
            ('Persiapan Audit Eksternal', 'Meningkatkan kesiapan menghadapi audit sertifikasi ISO 27001')
        ],
        'process_steps': [
            ('Persiapan Audit', 'Kami melakukan persiapan audit dengan mempelajari dokumentasi sistem keamanan informasi, assessment risiko, kebijakan keamanan, dan menyusun checklist audit sesuai ISO 27001:2022.'),
            ('Opening Meeting', 'Tim auditor melakukan pembukaan audit dengan menjelaskan tujuan, ruang lingkup, metodologi, dan jadwal audit keamanan informasi kepada auditee serta menjawab pertanyaan terkait proses audit.'),
            ('Pelaksanaan Audit', 'Auditor melakukan verifikasi implementasi kontrol keamanan informasi melalui review kebijakan, prosedur, technical controls, dan wawancara untuk menilai kesesuaian dengan Annex A ISO 27001:2022.'),
            ('Closing Meeting', 'Tim auditor mempresentasikan temuan audit, membahas ketidaksesuaian dan observasi terkait keamanan informasi, serta memberikan kesempatan diskusi dan klarifikasi kepada auditee.'),
            ('Laporan Audit', 'Kami menyusun laporan audit lengkap berisi temuan ketidaksesuaian, evaluasi efektivitas kontrol keamanan, assessment risiko informasi, dan rekomendasi perbaikan sistem.'),
            ('Konsultasi Tindak Lanjut', 'Kami memberikan konsultasi untuk membantu organisasi dalam menyusun action plan perbaikan keamanan informasi, monitoring implementasi, dan persiapan audit sertifikasi eksternal.')
        ],
        'scope': ['Konteks Organisasi', 'Kepemimpinan & Komitmen', 'Penilaian Risiko Informasi', 'Kontrol Keamanan Annex A', 'Kebijakan Keamanan Informasi', 'Manajemen Akses', 'Keamanan Operasional', 'Keamanan Komunikasi', 'Peningkatan Berkelanjutan'],
        'scope_footer': 'Audit internal mencakup seluruh klausul ISO 27001:2022 dan 93 kontrol Annex A termasuk evaluasi efektivitas kontrol keamanan informasi dan manajemen risiko.',
        'cta_title': 'Keamanan Informasi',
        'cta_description': 'Konsultasikan kebutuhan audit internal ISO 27001 Anda bersama tim auditor keamanan informasi berpengalaman INOVASS. Kami siap membantu organisasi Anda melindungi aset informasi.'
    },
    '22301': {
        'title': 'Sistem Manajemen Keberlangsungan Bisnis (BCMS)',
        'breadcrumb': 'Audit Internal ISO 22301',
        'benefits': ['Memastikan Kelangsungan<br>Bisnis', 'Mengidentifikasi Risiko<br>Gangguan', 'Meningkatkan Ketahanan<br>Organisasi'],
        'description': 'Jasa Audit Internal ISO 22301:2019 adalah layanan profesional yang membantu organisasi melakukan evaluasi sistematis terhadap efektivitas penerapan Sistem Manajemen Keberlangsungan Bisnis (BCMS), memastikan kelangsungan operasi saat terjadi gangguan, dan meningkatkan ketahanan organisasi.',
        'benefit_title': 'Manfaat Audit Internal ISO 22301',
        'benefit_items': [
            ('Evaluasi BCMS', 'Mendapatkan penilaian independen terhadap efektivitas sistem keberlangsungan bisnis'),
            ('Identifikasi Risiko Gangguan', 'Mendeteksi potensi gangguan yang dapat menghentikan operasi bisnis'),
            ('Verifikasi BIA & Strategi', 'Memverifikasi Business Impact Analysis dan strategi pemulihan'),
            ('Kesiapan Tanggap Darurat', 'Mengevaluasi kesiapan organisasi menghadapi situasi darurat'),
            ('Ketahanan Organisasi', 'Meningkatkan kemampuan organisasi untuk pulih dari gangguan'),
            ('Persiapan Audit Eksternal', 'Meningkatkan kesiapan menghadapi audit sertifikasi ISO 22301')
        ],
        'process_steps': [
            ('Persiapan Audit', 'Kami melakukan persiapan audit dengan mempelajari dokumentasi BCMS, Business Impact Analysis (BIA), rencana keberlangsungan bisnis, dan menyusun checklist audit sesuai ISO 22301:2019.'),
            ('Opening Meeting', 'Tim auditor melakukan pembukaan audit dengan menjelaskan tujuan, ruang lingkup, metodologi, dan jadwal audit BCMS kepada auditee serta menjawab pertanyaan terkait proses audit.'),
            ('Pelaksanaan Audit', 'Auditor melakukan verifikasi implementasi BCMS melalui review BIA, strategi keberlangsungan, prosedur pemulihan, dan uji coba rencana untuk menilai kesesuaian dengan ISO 22301:2019.'),
            ('Closing Meeting', 'Tim auditor mempresentasikan temuan audit, membahas ketidaksesuaian dan observasi terkait keberlangsungan bisnis, serta memberikan kesempatan diskusi dan klarifikasi kepada auditee.'),
            ('Laporan Audit', 'Kami menyusun laporan audit lengkap berisi temuan ketidaksesuaian, evaluasi efektivitas BIA dan strategi pemulihan, serta rekomendasi perbaikan sistem keberlangsungan bisnis.'),
            ('Konsultasi Tindak Lanjut', 'Kami memberikan konsultasi untuk membantu organisasi dalam menyusun action plan perbaikan BCMS, monitoring implementasi, dan persiapan audit sertifikasi eksternal.')
        ],
        'scope': ['Konteks Organisasi', 'Kepemimpinan & Komitmen', 'Business Impact Analysis', 'Strategi Keberlangsungan', 'Rencana Pemulihan', 'Tanggap Darurat', 'Testing & Exercise', 'Review & Maintenance', 'Peningkatan Berkelanjutan'],
        'scope_footer': 'Audit internal mencakup seluruh klausul ISO 22301:2019 termasuk evaluasi BIA, strategi keberlangsungan, dan rencana pemulihan bisnis.',
        'cta_title': 'Keberlangsungan Bisnis',
        'cta_description': 'Konsultasikan kebutuhan audit internal ISO 22301 Anda bersama tim auditor BCMS berpengalaman INOVASS. Kami siap membantu organisasi Anda meningkatkan ketahanan bisnis.'
    },
    '37001': {
        'title': 'Sistem Manajemen Anti Penyuapan',
        'breadcrumb': 'Audit Internal ISO 37001',
        'benefits': ['Mencegah Praktik<br>Penyuapan', 'Meningkatkan Integritas<br>Organisasi', 'Kepatuhan Anti<br>Korupsi'],
