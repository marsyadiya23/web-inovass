#!/usr/bin/env python3
import re

# Baca template dari ISO 9001
with open('layanan-detail-pemeliharaan-iso-9001.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Data untuk 11 halaman baru
pages_data = [
    {
        "filename": "layanan-detail-pemeliharaan-iso-50001.html",
        "old_iso": "9001",
        "old_version": "ISO/SNI 9001:2015",
        "old_system": "Sistem Manajemen Mutu",
        "old_abbr": "QMS",
        "new_iso": "50001",
        "new_version": "ISO 50001:2018",
        "new_system": "Sistem Manajemen Energi",
        "new_abbr": "EnMS",
        "benefit_1": "Optimasi Konsumsi<br>Energi",
        "benefit_2": "Efisiensi Biaya<br>Operasional",
        "benefit_3": "Keberlanjutan<br>Energi",
        "pengertian": "Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 50001:2018 adalah layanan profesional yang membantu organisasi memelihara, memonitor, dan meningkatkan efektivitas sistem manajemen energi secara berkelanjutan untuk mempertahankan sertifikasi dan performa energi organisasi.",
        "benefits": [
            ("Energy Baseline Update", "Membantu update energy baseline dan EnPI sesuai perubahan proses operasional"),
            ("Performance Monitoring", "Monitoring kinerja energi secara rutin untuk memastikan pencapaian target efisiensi"),
            ("SEU Management", "Dukungan dalam pengelolaan Significant Energy Uses dan action plans"),
            ("Compliance Energy", "Memastikan compliance berkelanjutan terhadap persyaratan ISO 50001:2018"),
            ("Energy Review", "Review berkala terhadap energy performance indicators dan consumption patterns"),
            ("Certification Readiness", "Menjaga kesiapan organisasi untuk audit surveillance dan recertification")
        ],
        "process_title": "Proses Konsultasi Pemeliharaan Sistem Manajemen Energi ISO 50001:2018",
        "process_steps": [
            ("Assessment Sistem Berjalan", "Kami melakukan evaluasi komprehensif terhadap implementasi sistem manajemen energi, meninjau efektivitas EnPI dan action plans, serta mengidentifikasi area yang memerlukan perbaikan dalam pengelolaan konsumsi energi."),
            ("Gap Analysis & Review", "Tim konsultan melakukan analisis kesenjangan antara praktik saat ini dengan persyaratan ISO 50001:2018, meninjau energy baseline dan SEU management, serta mengidentifikasi potensi inefisiensi energi atau area improvement."),
            ("Update Dokumentasi EnMS", "Kami membantu organisasi memperbarui dokumen sistem manajemen energi termasuk energy review, EnPI, action plans, dan operational controls sesuai dengan perubahan teknologi dan best practice energy management terkini."),
            ("Improvement Planning", "Tim konsultan membantu menyusun rencana peningkatan kinerja energi, mengembangkan action plan untuk mengatasi temuan gap analysis dan inefficiency, serta menetapkan target energy savings yang terukur."),
            ("Implementation Support", "Konsultan memberikan pendampingan dalam implementasi energy improvement projects, pelatihan energy awareness untuk personel, dan fasilitasi management review untuk memastikan komitmen top management terhadap pemeliharaan EnMS."),
            ("Monitoring & Follow-up", "Kami melakukan monitoring berkelanjutan terhadap kinerja energi, evaluasi pencapaian energy objectives, dan memberikan dukungan konsultasi untuk memastikan kesiapan menghadapi audit surveillance atau recertification.")
        ],
        "fokus_items": [
            "Energy Baseline & EnPI", "SEU Identification", "Energy Performance",
            "Operational Controls", "Energy Action Plans", "Monitoring & Measurement",
            "Energy Objectives", "Continuous Improvement", "Management Review EnMS"
        ]
    }
]

print("Generating pemeliharaan pages...")
print(f"Template loaded: {len(template)} characters")
print("Script ready!")
