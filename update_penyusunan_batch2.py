#!/usr/bin/env python3
"""Script to update 11 additional Penyusunan Dokumen ISO pages"""
import re

# ISO standards data
iso_data = {
    "50001": ("2018", "Energi", "kebijakan energi, tinjauan energi, EnPI, dan program efisiensi energi", 
              ["Manual Sistem Manajemen Energi", "Energy Policy & Objectives", "Energy Review & Baseline", "Energy Performance Indicators (EnPI)", "Operational Controls", "Monitoring & Measurement Plan", "Energy Audit Procedures", "Energy Action Plan", "Legal Compliance Register Energi"]),
    "55001": ("2014", "Aset", "strategi aset, Asset Management Plan, lifecycle costing, dan risk assessment", 
              ["Asset Management Policy", "Strategic Asset Management Plan (SAMP)", "Asset Management Objectives", "Asset Register & Inventory", "Lifecycle Management Plan", "Risk Assessment Aset", "Performance Monitoring System", "Asset Maintenance Strategy", "Capital Investment Planning"]),
    "21001": ("2018", "Organisasi Pendidikan", "kebijakan pendidikan, kurikulum, learning outcomes, dan stakeholder satisfaction", 
              ["Educational Organization Policy", "Learning Outcomes & Objectives", "Curriculum Design Documentation", "Student Satisfaction Survey System", "Teaching & Learning Procedures", "Assessment & Evaluation System", "Stakeholder Communication Plan", "Continuous Improvement Program", "Educational Resources Management"]),
    "13485": ("2016", "Mutu Alat Kesehatan", "design control, risk management, regulatory compliance, dan vigilance procedures", 
              ["Quality Manual Alat Kesehatan", "Design Control Procedures", "Risk Management Plan (ISO 14971)", "Regulatory Compliance Register", "Post-Market Surveillance", "Vigilance & Complaint Handling", "Supplier Control System", "Sterilization Validation", "Clinical Evaluation Documentation"]),
    "39001": ("2012", "Keselamatan Lalu Lintas Jalan", "kebijakan RTS, risk assessment lalu lintas, dan safety performance indicators", 
              ["Road Traffic Safety Policy", "RTS Risk Assessment", "Safety Performance Indicators", "Driver Management System", "Vehicle Fleet Management", "Journey Management Procedures", "Accident Investigation & Reporting", "Safety Training Program", "Emergency Response Plan RTS"]),
    "10002": ("2018", "Penanganan Keluhan Pelanggan", "prosedur keluhan, complaint handling process, dan customer satisfaction", 
              ["Complaints Handling Policy", "Complaint Registration System", "Complaint Investigation Procedures", "Resolution & Response Procedures", "Customer Satisfaction Measurement", "Complaint Analysis & Reporting", "Escalation Procedures", "Feedback Management System", "Continuous Improvement from Complaints"]),
}

# Generate Python dict structure
standards = {}
for iso_num, (year, system_name, doc_desc, targets) in iso_data.items():
    standards[iso_num] = {
        "title": f"Jasa Penyusunan Dokumen ISO {iso_num} – Sistem Manajemen {system_name}",
        "year": year,
        "breadcrumb": f"Penyusunan Dokumen ISO {iso_num}",
        "benefit_highlights": [
            "Dokumentasi Lengkap Sesuai<br>Persyaratan Standar",
            "Mempercepat Proses<br>Implementasi",
            "Siap Audit dan<br>Sertifikasi"
        ],
        "definition": f"Jasa Penyusunan Dokumen ISO {iso_num}:{year} membantu organisasi menyusun dokumentasi Sistem Manajemen {system_name} yang lengkap, termasuk {doc_desc}.",
        "benefits": [
            ("Dokumen yang Komprehensif", f"Menyusun seluruh dokumentasi yang diperlukan sesuai persyaratan ISO {iso_num}:{year}"),
            ("Menghemat Waktu dan Tenaga", "Tim profesional menyusun dokumen sehingga organisasi fokus pada operasional"),
            ("Mempercepat Proses Sertifikasi", "Dokumentasi yang lengkap dan sesuai standar mempercepat persiapan audit"),
            ("Customized dengan Proses Bisnis", "Dokumen disesuaikan dengan karakteristik dan kebutuhan organisasi"),
            ("Transfer Knowledge", "Proses penyusunan melibatkan transfer knowledge kepada tim internal"),
            ("Siap Audit Eksternal", "Dokumentasi disusun dengan format yang mudah dipahami auditor")
        ],
        "process_step2": f"Tim kami melakukan identifikasi proses bisnis organisasi, menyusun {doc_desc} sesuai persyaratan ISO {iso_num}:{year}.",
        "target_title": f"Dokumen yang Kami Susun untuk ISO {iso_num}",
        "target_desc": f"Kami menyusun dokumentasi lengkap Sistem Manajemen {system_name} sesuai persyaratan ISO {iso_num}:{year}.",
        "targets": targets,
        "target_footer": "Semua dokumen disesuaikan dengan skala dan kompleksitas organisasi Anda serta siap untuk implementasi dan audit sertifikasi."
    }

# Additional special cases
standards["30301"] = {
    "title": "Jasa Penyusunan Dokumen ISO 30301 – Sistem Manajemen Pengelolaan Arsip",
    "year": "2019",
    "breadcrumb": "Penyusunan Dokumen ISO 30301",
    "benefit_highlights": [
        "Dokumentasi Pengelolaan Arsip<br>yang Sistematis",
        "Memenuhi Persyaratan<br>Regulasi Arsip",
        "Siap Audit dan<br>Akreditasi"
    ],
    "definition": "Jasa Penyusunan Dokumen ISO 30301:2019 membantu organisasi menyusun dokumentasi Sistem Manajemen Pengelolaan Arsip yang lengkap, termasuk kebijakan arsip, klasifikasi, retensi, dan disposal procedures.",
    "benefits": [
        ("Sistem Klasifikasi Arsip", "Menyusun skema klasifikasi dan metadata arsip yang terstruktur"),
        ("Jadwal Retensi Arsip", "Dokumentasi retention schedule sesuai peraturan yang berlaku"),
        ("Prosedur Pengelolaan Lengkap", "Menyusun prosedur capture, storage, retrieval, dan disposal"),
        ("Digital Archive Management", "Dokumentasi sistem pengelolaan arsip elektronik"),
        ("Compliance Dokumentasi", "Memastikan dokumen sesuai dengan regulasi kearsipan"),
        ("Access Control System", "Menyusun sistem pengendalian akses arsip")
    ],
    "process_step2": "Tim kami melakukan survey arsip, menyusun klasifikasi arsip, retention schedule, dan dokumentasi sistem pengelolaan arsip sesuai ISO 30301:2019.",
    "target_title": "Dokumen yang Kami Susun untuk ISO 30301",
    "target_desc": "Kami menyusun dokumentasi lengkap Sistem Manajemen Pengelolaan Arsip sesuai persyaratan ISO 30301:2019.",
    "targets": [
        "Records Management Policy",
        "Classification Scheme & Metadata",
        "Retention & Disposal Schedule",
        "Capture & Registration Procedures",
        "Storage & Preservation System",
        "Access Control & Security",
        "Retrieval & Distribution Procedures",
        "Disposal & Destruction Procedures",
        "Digital Records Management"
    ],
    "target_footer": "Semua dokumen arsip disesuaikan dengan jenis dan volume arsip organisasi Anda."
}

standards["20000-1"] = {
    "title": "Jasa Penyusunan Dokumen ISO/IEC 20000-1 – Sistem Manajemen Layanan Teknologi Informasi",
    "year": "2018",
    "breadcrumb": "Penyusunan Dokumen ISO/IEC 20000-1",
    "benefit_highlights": [
        "Dokumentasi IT Service<br>Management yang Lengkap",
        "Service Catalogue dan<br>SLA Documentation",
        "Siap Audit Sertifikasi<br>ITSM"
    ],
    "definition": "Jasa Penyusunan Dokumen ISO/IEC 20000-1:2018 membantu organisasi menyusun dokumentasi Sistem Manajemen Layanan IT yang lengkap, termasuk service catalogue, SLA, operational procedures, dan ITIL-aligned processes.",
    "benefits": [
        ("Service Catalogue Documentation", "Menyusun katalog layanan IT yang komprehensif"),
        ("SLA & OLA Management", "Dokumentasi Service Level Agreement dan Operational Level Agreement"),
        ("ITIL Process Documentation", "Menyusun prosedur sesuai best practice ITIL"),
        ("Incident & Problem Management", "Dokumentasi prosedur penanganan insiden dan masalah IT"),
        ("Change Management System", "Menyusun sistem manajemen perubahan IT"),
        ("Service Continuity Planning", "Dokumentasi rencana kontinuitas layanan IT")
    ],
    "process_step2": "Tim kami melakukan IT service mapping, menyusun service catalogue, SLA documentation, dan prosedur ITSM sesuai ISO/IEC 20000-1:2018.",
    "target_title": "Dokumen yang Kami Susun untuk ISO/IEC 20000-1",
    "target_desc": "Kami menyusun dokumentasi lengkap Sistem Manajemen Layanan IT sesuai persyaratan ISO/IEC 20000-1:2018.",
    "targets": [
        "IT Service Management Policy",
        "Service Catalogue & Portfolio",
        "Service Level Agreements (SLA)",
        "Incident Management Procedures",
        "Problem Management Procedures",
        "Change Management System",
        "Release & Deployment Management",
        "Service Continuity Plan",
        "Capacity & Availability Management"
    ],
    "target_footer": "Semua dokumen ITSM disesuaikan dengan infrastruktur dan layanan IT organisasi Anda."
}

standards["35001"] = {
    "title": "Jasa Penyusunan Dokumen ISO 35001 – Sistem Manajemen Biorisiko Laboratorium",
    "year": "2019",
    "breadcrumb": "Penyusunan Dokumen ISO 35001",
    "benefit_highlights": [
        "Dokumentasi Bio Risk<br>Assessment Lengkap",
        "Biosafety & Biosecurity<br>Procedures",
        "Siap Audit dan<br>Akreditasi Lab"
    ],
    "definition": "Jasa Penyusunan Dokumen ISO 35001:2019 membantu organisasi menyusun dokumentasi Sistem Manajemen Biorisiko Laboratorium yang lengkap, termasuk bio risk assessment, biosafety procedures, dan incident response.",
    "benefits": [
        ("Biorisk Assessment Documentation", "Menyusun penilaian risiko biologis yang sistematis"),
        ("Biosafety Procedures", "Dokumentasi prosedur keamanan biologis di laboratorium"),
        ("Biosecurity Protocols", "Menyusun protokol keamanan akses bahan biologis"),
        ("Incident Response Plan", "Dokumentasi prosedur tanggap darurat biohazard"),
        ("Personal Protective Equipment", "Menyusun sistem manajemen APD laboratorium"),
        ("Waste Management System", "Dokumentasi pengelolaan limbah biologis")
    ],
    "process_step2": "Tim kami melakukan biorisk assessment, menyusun biosafety procedures, protocols, dan dokumentasi biorisiko sesuai ISO 35001:2019.",
    "target_title": "Dokumen yang Kami Susun untuk ISO 35001",
    "target_desc": "Kami menyusun dokumentasi lengkap Sistem Manajemen Biorisiko Laboratorium sesuai persyaratan ISO 35001:2019.",
    "targets": [
        "Biorisk Management Policy",
        "Biorisk Assessment & Register",
        "Biosafety Operating Procedures",
        "Biosecurity Access Control",
        "Laboratory Emergency Response",
        "PPE Management System",
        "Biological Waste Management",
        "Decontamination Procedures",
        "Incident Investigation & Reporting"
    ],
    "target_footer": "Semua dokumen biorisiko disesuaikan dengan jenis agen biologis dan tingkat biosafety level laboratorium Anda."
}

standards["ims"] = {
    "title": "Jasa Penyusunan Dokumen Integrated Management System (IMS) ISO/IEC/SNI",
    "year": "",
    "breadcrumb": "Penyusunan Dokumen IMS ISO/IEC/SNI",
    "benefit_highlights": [
        "Dokumentasi Terintegrasi<br>Multi-Standar",
        "Mengurangi Duplikasi<br>Dokumen",
        "Efisiensi Audit dan<br>Pengelolaan"
    ],
    "definition": "Jasa Penyusunan Dokumen Integrated Management System (IMS) membantu organisasi menyusun dokumentasi yang mengintegrasikan berbagai standar ISO/IEC/SNI dalam satu sistem manajemen yang kohesif dan efisien.",
    "benefits": [
        ("Dokumentasi Terintegrasi", "Menyusun dokumen yang mengintegrasikan berbagai standar dalam satu sistem"),
        ("Eliminasi Duplikasi", "Menghilangkan tumpang tindih prosedur dan dokumen antar standar"),
        ("Efisiensi Pengelolaan", "Mengurangi beban administrasi dan biaya pengelolaan dokumen"),
        ("Konsistensi Sistem", "Memastikan konsistensi pendekatan di seluruh sistem manajemen"),
        ("Simplified Audit Process", "Memudahkan proses audit terintegrasi untuk berbagai standar"),
        ("Holistic Risk Management", "Mengelola risiko secara menyeluruh lintas standar")
    ],
    "process_step2": "Tim kami melakukan gap analysis multi-standar, menyusun dokumentasi terintegrasi, common procedures, dan dokumentasi IMS yang efisien.",
    "target_title": "Dokumen yang Kami Susun untuk IMS",
    "target_desc": "Kami menyusun dokumentasi Integrated Management System yang mengintegrasikan berbagai standar ISO/IEC/SNI.",
    "targets": [
        "Integrated Management Manual",
        "Common Procedures (Multi-Standard)",
        "Integrated Risk Assessment",
        "Context & Stakeholder Analysis",
        "Combined Objectives & Targets",
        "Integrated Audit Procedures",
        "Unified Corrective Action System",
        "Integrated Performance Monitoring",
        "Management Review Documentation"
    ],
    "target_footer": "IMS cocok untuk organisasi yang menerapkan ISO 9001, 14001, 45001, atau standar lainnya secara bersamaan."
}

standards["lainnya"] = {
    "title": "Jasa Penyusunan Dokumen Sistem Manajemen ISO/IEC/SNI Lainnya",
    "year": "",
    "breadcrumb": "Penyusunan Dokumen ISO/IEC/SNI Lainnya",
    "benefit_highlights": [
        "Dukungan untuk Berbagai<br>Standar ISO/IEC/SNI",
        "Dokumentasi Disesuaikan<br>Kebutuhan Spesifik",
        "Tim Konsultan<br>Berpengalaman"
    ],
    "definition": "Kami menyediakan jasa penyusunan dokumen untuk berbagai standar sistem manajemen ISO/IEC/SNI lainnya yang belum tercantum, dengan pendekatan yang disesuaikan dengan kebutuhan unik organisasi Anda.",
    "benefits": [
        ("Dukungan Multi-Standar", "Menyediakan penyusunan dokumen untuk berbagai standar ISO/IEC/SNI"),
        ("Konsultasi yang Fleksibel", "Menyesuaikan pendekatan dengan kebutuhan organisasi"),
        ("Tim Berpengalaman", "Didukung oleh konsultan dengan keahlian di berbagai standar"),
        ("Dokumentasi yang Komprehensif", "Menyusun seluruh dokumentasi sesuai persyaratan standar"),
        ("Customized Format", "Format dokumen disesuaikan dengan preferensi organisasi"),
        ("Ongoing Support", "Dukungan konsultasi untuk update dan revisi dokumen")
    ],
    "process_step2": "Tim kami melakukan requirement analysis, menyusun dokumentasi sesuai standar yang diperlukan, dan memberikan dukungan implementasi.",
    "target_title": "Standar ISO/IEC/SNI yang Kami Layani",
    "target_desc": "Kami menyediakan penyusunan dokumen untuk berbagai standar sistem manajemen sesuai kebutuhan industri Anda.",
    "targets": [
        "ISO 31000 - Manajemen Risiko",
        "ISO 28000 - Supply Chain Security",
        "ISO 41001 - Facility Management",
        "ISO 56002 - Innovation Management",
        "SNI 19-17025 - Laboratorium",
        "ISO 15189 - Laboratorium Medik",
        "ISO 26000 - Social Responsibility",
        "Dan Standar ISO/IEC/SNI Lainnya",
        "Konsultasikan Kebutuhan Anda"
    ],
    "target_footer": "Hubungi kami untuk mendiskusikan kebutuhan penyusunan dokumen standar ISO/IEC/SNI spesifik yang Anda butuhkan."
}

def update_penyusunan_page(filename, iso_num, data):
    """Update penyusunan dokumen page"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update title
        content = re.sub(r'<title>.*?</title>', f'<title>{data["title"]} — INOVASS</title>', content)
        
        # Update breadcrumb - Important: Change to Jasa Penyusunan Dokumen
        breadcrumb_pattern = r'<a href="layanan-detail-jasa-sertifikasi-iso\.html" class="breadcrumb-link"[^>]*>Jasa Konsultasi Sertifikasi ISO</a>'
        breadcrumb_replace = '<a href="layanan-detail-penyusunan-dokumen.html" class="breadcrumb-link" style="color: rgba(255, 255, 255, 0.5) !important;">Jasa Penyusunan Dokumen Standar ISO/IEC/SNI</a>'
        content = re.sub(breadcrumb_pattern, breadcrumb_replace, content)
        
        content = re.sub(r'<span class="breadcrumb-current"[^>]*>.*?</span>',
                        f'<span class="breadcrumb-current" style="color: #00e0a0 !important;">{data["breadcrumb"]}</span>', content)
        
        # Update page title
        content = re.sub(r'<h1 class="detail-page-title"[^>]*>.*?</h1>',
                        f'<h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important; font-weight: 700 !important;">{data["title"]}</h1>', content)
        
        # Update benefit highlights title
        if data['year']:
            if iso_num == "20000-1":
                title_text = f"ISO/IEC {iso_num.replace('-', '-')}:{data['year']}"
            else:
                title_text = f"ISO {iso_num}:{data['year']}"
        else:
            title_text = "IMS" if iso_num == "ims" else "ISO/IEC/SNI"
        
        content = re.sub(r'<h2 class="benefit-highlight-title">Dengan Jasa Penyusunan Dokumen .*?:</h2>',
                        f'<h2 class="benefit-highlight-title">Dengan Jasa Penyusunan Dokumen {title_text}:</h2>', content)
        
        # Update benefit cards
        benefit_cards = '\n          '.join([f'<div class="benefit-highlight-card">\n            <p>{b}</p>\n          </div>' for b in data["benefit_highlights"]])
        content = re.sub(r'(<div class="benefit-highlight-grid">)(.*?)(</div>\s*</div>\s*<!-- PENGERTIAN)',
                        f'\\1\n          {benefit_cards}\n        \\3', content, flags=re.DOTALL)
        
        # Update pengertian description
        content = re.sub(r'(<p class="iso-content-desc">).*?(</p>)',
                        f'\\1\n            {data["definition"]}\n          \\2', content, flags=re.DOTALL)
        
        # Update benefit cards
        benefit_cards_html = '\n          '.join([f'<div class="iso-benefit-modern-card">\n            <h3>{t}</h3>\n            <p>{d}</p>\n          </div>' for t, d in data["benefits"]])
        content = re.sub(r'(<div class="iso-benefits-modern-grid">)(.*?)(</div>\s*</div>\s*<!-- CTA)',
                        f'\\1\n          {benefit_cards_html}\n        \\3', content, flags=re.DOTALL)
        
        # Update process title
        content = re.sub(r'<h2 class="iso-process-title">Proses Penyusunan Dokumen .*?</h2>',
                        f'<h2 class="iso-process-title">Proses Penyusunan Dokumen {title_text}</h2>', content)
        
        # Update process step 2
        content = re.sub(r'(<h3>Penyusunan Dokumentasi</h3>\s*<p>).*?(</p>)',
                        f'\\1{data["process_step2"]}\\2', content, flags=re.DOTALL)
        
        # Update target title
        content = re.sub(r'<h2 class="iso-target-section-title"[^>]*>Dokumen yang Kami Susun untuk .*?</h2>',
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
    "50001": "layanan-detail-penyusunan-dokumen-iso-50001.html",
    "55001": "layanan-detail-penyusunan-dokumen-iso-55001.html",
    "21001": "layanan-detail-penyusunan-dokumen-iso-21001.html",
    "13485": "layanan-detail-penyusunan-dokumen-iso-13485.html",
    "39001": "layanan-detail-penyusunan-dokumen-iso-39001.html",
    "10002": "layanan-detail-penyusunan-dokumen-iso-10002.html",
    "30301": "layanan-detail-penyusunan-dokumen-iso-30301.html",
    "20000-1": "layanan-detail-penyusunan-dokumen-iso-20000-1.html",
    "35001": "layanan-detail-penyusunan-dokumen-iso-35001.html",
    "ims": "layanan-detail-penyusunan-dokumen-ims.html",
    "lainnya": "layanan-detail-penyusunan-dokumen-iso-lainnya.html"
}

print("Updating 11 additional Penyusunan Dokumen ISO pages...")
print("=" * 50)

for iso_num, filename in file_mappings.items():
    data = standards[iso_num]
    update_penyusunan_page(filename, iso_num, data)

print("=" * 50)
print("Update complete!")
