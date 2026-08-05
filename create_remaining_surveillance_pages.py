#!/usr/bin/env python3
# Script to create remaining surveillance pages

import os

# ISO Standards data
standards = {
    '50001': {
        'title': 'Jasa Konsultasi Persiapan Audit Surveillance ISO 50001 – Sistem Manajemen Energi',
        'short_title': 'ISO 50001',
        'system': 'Sistem Manajemen Energi',
        'breadcrumb': 'Konsultasi Surveillance ISO 50001',
        'year': '2018',
        'benefits': ['Mempertahankan<br>Sertifikasi EnMS', 'Efisiensi Energi<br>Berkelanjutan', 'Performa Energi<br>Meningkat'],
        'description': 'Jasa Konsultasi Persiapan Audit Surveillance ISO 50001:2018 adalah layanan profesional yang membantu organisasi mempersiapkan audit surveillance untuk mempertahankan sertifikasi sistem manajemen energi, memastikan peningkatan efisiensi energi berkelanjutan, dan mendemonstrasikan kinerja energi yang optimal.',
        'benefits_detail': [
            ('Mempertahankan Sertifikasi EnMS', 'Memastikan organisasi tetap memenuhi persyaratan ISO 50001 dan mempertahankan validitas sertifikat sistem manajemen energi.'),
            ('Efisiensi Energi Berkelanjutan', 'Menjaga konsistensi program penghematan energi dan memastikan pencapaian target efisiensi energi organisasi.'),
            ('Continuous Improvement Energi', 'Mengidentifikasi peluang perbaikan dalam pengelolaan energi dan meningkatkan kinerja energi secara berkelanjutan.'),
            ('Compliance Peraturan Energi', 'Memastikan kepatuhan berkelanjutan terhadap peraturan dan regulasi terkait penggunaan dan konservasi energi.'),
            ('Monitoring Kinerja Energi', 'Melakukan evaluasi berkala terhadap Energy Performance Indicators (EnPI) dan efektivitas kontrol operasional energi.'),
            ('Kesiapan Audit Surveillance', 'Mempersiapkan dokumentasi, evidence, dan tim organisasi untuk menghadapi audit surveillance dari lembaga sertifikasi.')
        ],
        'process': [
            ('Pre-Surveillance Assessment', 'Kami melakukan evaluasi kesiapan organisasi menghadapi audit surveillance dengan mereview dokumentasi EnMS, energy baseline, EnPI, dan perubahan sejak sertifikasi awal.'),
            ('Gap Analysis Energi', 'Tim konsultan mengidentifikasi gap antara kondisi aktual dengan persyaratan ISO 50001:2018, termasuk evaluasi significant energy uses (SEUs) dan action plans.'),
            ('Corrective Actions Support', 'Kami membantu organisasi menindaklanjuti temuan audit sebelumnya, menyusun corrective actions, dan memastikan efektivitas perbaikan yang telah dilakukan.'),
            ('Evidence Preparation', 'Konsultan membantu menyiapkan bukti objektif kepatuhan ISO 50001, termasuk energy review, monitoring data, dan management review records.'),
            ('Mock Audit Surveillance', 'Melakukan simulasi audit surveillance untuk menguji kesiapan organisasi, mengidentifikasi potensi ketidaksesuaian, dan memberikan feedback perbaikan.'),
            ('Post-Surveillance Support', 'Memberikan pendampingan pasca audit surveillance untuk menindaklanjuti temuan auditor dan memastikan continuous improvement sistem manajemen energi.')
        ],
        'scope': [
            'Konteks & Ruang Lingkup EnMS', 'Kepemimpinan & Komitmen Energi', 'Energy Policy & Objectives', 'Energy Planning & Baseline', 
            'Significant Energy Uses (SEUs)', 'Energy Performance Indicators', 'Operational Control Energi', 'Monitoring & Measurement Energi', 
            'Management Review & Improvement'
        ],
        'cta_title': 'Persiapan Audit Surveillance Energi',
        'cta_desc': 'Konsultasikan persiapan audit surveillance ISO 50001 Anda bersama tim konsultan energi berpengalaman INOVASS. Kami siap membantu organisasi Anda mempertahankan sertifikasi sistem manajemen energi.'
    },
    '55001': {
        'title': 'Jasa Konsultasi Persiapan Audit Surveillance ISO 55001 – Sistem Manajemen Aset',
        'short_title': 'ISO 55001',
        'system': 'Sistem Manajemen Aset',
        'breadcrumb': 'Konsultasi Surveillance ISO 55001',
        'year': '2024',
        'benefits': ['Mempertahankan<br>Sertifikasi AMS', 'Nilai Aset<br>Optimal', 'ROI Aset<br>Meningkat'],
        'description': 'Jasa Konsultasi Persiapan Audit Surveillance ISO 55001:2024 adalah layanan profesional yang membantu organisasi mempersiapkan audit surveillance untuk mempertahankan sertifikasi sistem manajemen aset, memastikan optimalisasi nilai aset berkelanjutan, dan mendemonstrasikan peningkatan return on investment aset.',
        'benefits_detail': [
            ('Mempertahankan Sertifikasi AMS', 'Memastikan organisasi tetap memenuhi persyaratan ISO 55001 dan mempertahankan validitas sertifikat sistem manajemen aset.'),
            ('Optimalisasi Nilai Aset', 'Menjaga konsistensi program pengelolaan aset dan memastikan pencapaian target nilai optimal sepanjang lifecycle aset.'),
            ('Continuous Improvement Aset', 'Mengidentifikasi peluang perbaikan dalam manajemen aset dan meningkatkan kinerja aset secara berkelanjutan.'),
            ('Risk Management Aset', 'Memastikan efektivitas identifikasi dan mitigasi risiko kegagalan aset serta optimalisasi keandalan aset organisasi.'),
            ('Monitoring Kinerja Aset', 'Melakukan evaluasi berkala terhadap asset performance indicators dan efektivitas maintenance strategies.'),
            ('Kesiapan Audit Surveillance', 'Mempersiapkan dokumentasi SAMP, asset register, dan tim organisasi untuk menghadapi audit surveillance dari lembaga sertifikasi.')
        ],
        'process': [
            ('Pre-Surveillance Assessment', 'Kami melakukan evaluasi kesiapan organisasi menghadapi audit surveillance dengan mereview dokumentasi AMS, Strategic Asset Management Plan (SAMP), dan perubahan sejak sertifikasi awal.'),
            ('Gap Analysis Aset', 'Tim konsultan mengidentifikasi gap antara kondisi aktual dengan persyaratan ISO 55001:2024, termasuk evaluasi asset register, lifecycle plans, dan risk assessments.'),
            ('Corrective Actions Support', 'Kami membantu organisasi menindaklanjuti temuan audit sebelumnya, menyusun corrective actions untuk kegagalan aset, dan memastikan efektivitas perbaikan.'),
            ('Evidence Preparation', 'Konsultan membantu menyiapkan bukti objektif kepatuhan ISO 55001, termasuk asset performance data, maintenance records, dan management review.'),
            ('Mock Audit Surveillance', 'Melakukan simulasi audit surveillance untuk menguji kesiapan organisasi, mengidentifikasi potensi ketidaksesuaian dalam pengelolaan aset, dan feedback perbaikan.'),
            ('Post-Surveillance Support', 'Memberikan pendampingan pasca audit surveillance untuk menindaklanjuti temuan auditor dan memastikan continuous improvement sistem manajemen aset.')
        ],
        'scope': [
            'Konteks & Ruang Lingkup AMS', 'Kepemimpinan & Asset Policy', 'Asset Management Planning', 'Asset Management Objectives', 
            'Asset Register & Portfolio', 'Lifecycle Management', 'Risk Management Aset', 'Asset Performance Monitoring', 
            'Management Review & Improvement'
        ],
        'cta_title': 'Persiapan Audit Surveillance Aset',
        'cta_desc': 'Konsultasikan persiapan audit surveillance ISO 55001 Anda bersama tim konsultan aset management berpengalaman INOVASS. Kami siap membantu organisasi Anda mempertahankan sertifikasi sistem manajemen aset.'
    },
    '21001': {
        'title': 'Jasa Konsultasi Persiapan Audit Surveillance ISO 21001 – Sistem Manajemen Organisasi Pendidikan',
        'short_title': 'ISO 21001',
        'system': 'Sistem Manajemen Organisasi Pendidikan',
        'breadcrumb': 'Konsultasi Surveillance ISO 21001',
        'year': '2025',
        'benefits': ['Mempertahankan<br>Sertifikasi EOMS', 'Kualitas Pembelajaran<br>Terjaga', 'Kepuasan Learner<br>Meningkat'],
        'description': 'Jasa Konsultasi Persiapan Audit Surveillance ISO 21001:2025 adalah layanan profesional yang membantu organisasi pendidikan mempersiapkan audit surveillance untuk mempertahankan sertifikasi EOMS, memastikan peningkatan kualitas pembelajaran berkelanjutan, dan mendemonstrasikan kepuasan peserta didik yang optimal.',
        'benefits_detail': [
            ('Mempertahankan Sertifikasi EOMS', 'Memastikan institusi pendidikan tetap memenuhi persyaratan ISO 21001 dan mempertahankan validitas sertifikat Educational Organization Management System.'),
            ('Kualitas Pembelajaran Berkelanjutan', 'Menjaga konsistensi standar pembelajaran dan memastikan pencapaian learning outcomes yang telah ditetapkan institusi pendidikan.'),
            ('Continuous Improvement Pendidikan', 'Mengidentifikasi peluang perbaikan dalam proses pendidikan dan meningkatkan efektivitas pembelajaran secara berkelanjutan.'),
            ('Learner-Centered Approach', 'Memastikan fokus berkelanjutan pada kebutuhan dan kepuasan peserta didik serta interested parties dalam sistem pendidikan.'),
            ('Monitoring Kinerja Pendidikan', 'Melakukan evaluasi berkala terhadap educational performance indicators dan efektivitas program pendidikan.'),
            ('Kesiapan Audit Surveillance', 'Mempersiapkan dokumentasi kurikulum, assessment records, dan tim institusi untuk menghadapi audit surveillance dari lembaga sertifikasi.')
        ],
        'process': [
            ('Pre-Surveillance Assessment', 'Kami melakukan evaluasi kesiapan institusi pendidikan menghadapi audit surveillance dengan mereview dokumentasi EOMS, learning outcomes, dan perubahan sejak sertifikasi awal.'),
            ('Gap Analysis Pendidikan', 'Tim konsultan mengidentifikasi gap antara kondisi aktual dengan persyaratan ISO 21001:2025, termasuk evaluasi curriculum design, teaching methods, dan learner assessments.'),
            ('Corrective Actions Support', 'Kami membantu institusi menindaklanjuti temuan audit sebelumnya, menyusun corrective actions untuk gap pembelajaran, dan memastikan efektivitas perbaikan.'),
            ('Evidence Preparation', 'Konsultan membantu menyiapkan bukti objektif kepatuhan ISO 21001, termasuk learner feedback, assessment results, dan management review records.'),
            ('Mock Audit Surveillance', 'Melakukan simulasi audit surveillance untuk menguji kesiapan institusi, mengidentifikasi potensi ketidaksesuaian dalam proses pendidikan, dan feedback perbaikan.'),
            ('Post-Surveillance Support', 'Memberikan pendampingan pasca audit surveillance untuk menindaklanjuti temuan auditor dan memastikan continuous improvement sistem pendidikan.')
        ],
        'scope': [
            'Konteks Organisasi Pendidikan', 'Kepemimpinan & Educational Policy', 'Perencanaan EOMS', 'Curriculum Design & Development', 
            'Learning Delivery & Assessment', 'Learner Support Services', 'Educational Resources', 'Performance Evaluation', 
            'Management Review & Improvement'
        ],
        'cta_title': 'Persiapan Audit Surveillance Pendidikan',
        'cta_desc': 'Konsultasikan persiapan audit surveillance ISO 21001 Anda bersama tim konsultan pendidikan berpengalaman INOVASS. Kami siap membantu institusi Anda mempertahankan sertifikasi EOMS.'
    }
}

# Continue with more standards...
