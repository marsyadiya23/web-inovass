#!/usr/bin/env python3
"""Script to update 8 Penyusunan Dokumen ISO pages"""
import re

iso_standards = {
    "9001": {
        "title": "Jasa Penyusunan Dokumen ISO/SNI 9001 – Sistem Manajemen Mutu",
        "year": "2015",
        "breadcrumb": "Penyusunan Dokumen ISO/SNI 9001",
        "benefit_highlights": [
            "Dokumen Lengkap Sesuai<br>Persyaratan Standar",
            "Mempercepat Proses<br>Sertifikasi",
            "Siap Implementasi dan<br>Audit Eksternal"
        ],
        "definition": "Jasa Penyusunan Dokumen ISO/SNI 9001:2015 membantu organisasi menyusun dokumentasi Sistem Manajemen Mutu yang lengkap, sesuai persyaratan standar, dan siap untuk implementasi serta audit sertifikasi.",
        "benefits": [
            ("Dokumen yang Komprehensif", "Menyusun seluruh dokumentasi yang diperlukan sesuai persyaratan ISO 9001:2015"),
            ("Menghemat Waktu dan Tenaga", "Tim profesional menyusun dokumen sehingga organisasi fokus pada operasional"),
            ("Mempercepat Proses Sertifikasi", "Dokumentasi yang lengkap dan sesuai standar mempercepat persiapan audit"),
            ("Customized dengan Proses Bisnis", "Dokumen disesuaikan dengan karakteristik dan kebutuhan organisasi"),
            ("Meningkatkan Pemahaman Standar", "Proses penyusunan melibatkan transfer knowledge kepada tim internal"),
            ("Siap Audit Eksternal", "Dokumentasi disusun dengan format yang mudah dipahami auditor")
        ],
        "process_step2": "Tim kami melakukan identifikasi proses bisnis organisasi, menyusun dokumentasi tingkat 1 (manual/kebijakan), tingkat 2 (prosedur), dan tingkat 3 (instruksi kerja, formulir) sesuai persyaratan ISO 9001:2015.",
        "target_title": "Dokumen yang Kami Susun untuk ISO 9001",
        "target_desc": "Kami menyusun dokumentasi lengkap Sistem Manajemen Mutu sesuai persyaratan ISO 9001:2015.",
        "targets": [
            "Manual Mutu / Kebijakan Mutu",
            "Prosedur Wajib ISO 9001",
            "Prosedur Operasional",
            "Instruksi Kerja",
            "Formulir dan Record",
            "Context of Organization",
            "Risk & Opportunity Management",
            "Dokumentasi Proses Bisnis",
            "Template Audit Internal"
        ],
        "target_footer": "Semua dokumen disesuaikan dengan skala dan kompleksitas organisasi Anda serta siap untuk implementasi dan audit sertifikasi."
    },
    "14001": {
        "title": "Jasa Penyusunan Dokumen ISO/SNI 14001 – Sistem Manajemen Lingkungan",
        "year": "2015",
        "breadcrumb": "Penyusunan Dokumen ISO/SNI 14001",
        "benefit_highlights": [
            "Dokumentasi Lengkap Aspek<br>dan Dampak Lingkungan",
            "Memenuhi Persyaratan<br>Regulasi Lingkungan",
            "Siap Audit Sertifikasi<br>ISO 14001"
        ],
        "definition": "Jasa Penyusunan Dokumen ISO/SNI 14001:2015 membantu organisasi menyusun dokumentasi Sistem Manajemen Lingkungan yang lengkap, termasuk identifikasi aspek dan dampak lingkungan, serta program pengelolaan lingkungan.",
        "benefits": [
            ("Dokumentasi Aspek Lingkungan Lengkap", "Menyusun identifikasi dan evaluasi aspek serta dampak lingkungan yang sistematis"),
            ("Compliance dengan Regulasi", "Memastikan dokumen sesuai dengan peraturan lingkungan yang berlaku"),
            ("Program Pengelolaan Lingkungan", "Menyusun program dan target untuk perbaikan kinerja lingkungan"),
            ("Emergency Preparedness", "Dokumentasi prosedur tanggap darurat keadaan lingkungan"),
            ("Monitoring dan Measurement", "Menyusun sistem pemantauan dan pengukuran kinerja lingkungan"),
            ("Legal Compliance Register", "Menyusun register peraturan perundangan lingkungan yang relevan")
        ],
        "process_step2": "Tim kami melakukan identifikasi aspek dan dampak lingkungan, menyusun manual lingkungan, prosedur pengelolaan lingkungan, dan dokumentasi compliance sesuai ISO 14001:2015.",
        "target_title": "Dokumen yang Kami Susun untuk ISO 14001",
        "target_desc": "Kami menyusun dokumentasi lengkap Sistem Manajemen Lingkungan sesuai persyaratan ISO 14001:2015.",
        "targets": [
            "Manual Lingkungan",
            "Identifikasi Aspek & Dampak Lingkungan",
            "Legal Compliance Register",
            "Program Pengelolaan Lingkungan",
            "Prosedur Operasional Lingkungan",
            "Emergency Response Procedure",
            "Monitoring dan Measurement Plan",
            "Dokumentasi Waste Management",
            "Environmental Objectives & Targets"
        ],
        "target_footer": "Semua dokumen lingkungan disesuaikan dengan jenis industri dan dampak lingkungan spesifik organisasi Anda."
    },
    "45001": {
        "title": "Jasa Penyusunan Dokumen ISO 45001 – Sistem Manajemen Keselamatan dan Kesehatan Kerja (SMK3)",
        "year": "2018",
        "breadcrumb": "Penyusunan Dokumen ISO 45001",
        "benefit_highlights": [
            "Dokumentasi HIRARC dan<br>Pengendalian Risiko K3",
            "Memenuhi Persyaratan<br>Peraturan K3",
            "Siap Audit Sertifikasi<br>ISO 45001"
        ],
        "definition": "Jasa Penyusunan Dokumen ISO 45001:2018 membantu organisasi menyusun dokumentasi Sistem Manajemen K3 yang lengkap, termasuk HIRARC, prosedur K3, dan program pencegahan kecelakaan kerja.",
        "benefits": [
            ("Dokumentasi HIRARC Lengkap", "Menyusun Hazard Identification, Risk Assessment, and Risk Control yang sistematis"),
            ("Compliance Peraturan K3", "Memastikan dokumen sesuai dengan regulasi keselamatan dan kesehatan kerja"),
            ("Program Pencegahan Kecelakaan", "Menyusun program K3 untuk mencegah kecelakaan dan penyakit akibat kerja"),
            ("Emergency Procedures", "Dokumentasi prosedur tanggap darurat dan evakuasi"),
            ("PPE Management", "Menyusun sistem pengelolaan Alat Pelindung Diri (APD)"),
            ("Legal Register K3", "Menyusun register peraturan K3 yang berlaku")
        ],
        "process_step2": "Tim kami melakukan HIRARC di seluruh area kerja, menyusun manual K3, prosedur keselamatan kerja, dan dokumentasi compliance sesuai ISO 45001:2018.",
        "target_title": "Dokumen yang Kami Susun untuk ISO 45001",
        "target_desc": "Kami menyusun dokumentasi lengkap Sistem Manajemen K3 sesuai persyaratan ISO 45001:2018.",
        "targets": [
            "Manual K3 / Kebijakan K3",
            "HIRARC (Hazard Identification)",
            "Legal Compliance Register K3",
            "Program K3 Tahunan",
            "Prosedur Operasional K3",
            "Emergency Response Procedure",
            "PPE Management System",
            "Permit to Work System",
            "Accident Investigation Procedure"
        ],
        "target_footer": "Semua dokumen K3 disesuaikan dengan jenis industri dan risiko spesifik organisasi Anda."
    },
    "22000": {
        "title": "Jasa Penyusunan Dokumen ISO 22000 – Sistem Manajemen Keamanan Pangan",
        "year": "2018",
        "breadcrumb": "Penyusunan Dokumen ISO 22000",
        "benefit_highlights": [
            "Dokumentasi HACCP dan<br>Prerequisite Programs",
            "Memenuhi Persyaratan<br>Food Safety",
            "Siap Audit Sertifikasi<br>ISO 22000"
        ],
        "definition": "Jasa Penyusunan Dokumen ISO 22000:2018 membantu organisasi menyusun dokumentasi Sistem Manajemen Keamanan Pangan yang lengkap, termasuk HACCP Plan, Prerequisite Programs, dan Food Safety Management.",
        "benefits": [
            ("HACCP Plan Lengkap", "Menyusun HACCP (Hazard Analysis Critical Control Point) sesuai Codex Alimentarius"),
            ("Prerequisite Programs (PRP)", "Dokumentasi program prasyarat keamanan pangan"),
            ("Food Safety Policy", "Menyusun kebijakan dan manual keamanan pangan"),
            ("Product Description", "Dokumentasi deskripsi produk dan flow diagram proses"),
            ("Monitoring dan Verification", "Menyusun sistem pemantauan dan verifikasi keamanan pangan"),
            ("Traceability System", "Dokumentasi sistem penelusuran produk")
        ],
        "process_step2": "Tim kami melakukan hazard analysis, menyusun HACCP plan, prerequisite programs, dan dokumentasi sistem keamanan pangan sesuai ISO 22000:2018.",
        "target_title": "Dokumen yang Kami Susun untuk ISO 22000",
        "target_desc": "Kami menyusun dokumentasi lengkap Sistem Manajemen Keamanan Pangan sesuai persyaratan ISO 22000:2018.",
        "targets": [
            "Manual Keamanan Pangan",
            "HACCP Plan (7 Prinsip)",
            "Prerequisite Programs (PRP)",
            "Hazard Analysis",
            "Product Description & Flow Diagram",
            "Monitoring dan Verification",
            "Traceability Procedure",
            "Supplier Control System",
            "Product Recall Procedure"
        ],
        "target_footer": "Semua dokumen keamanan pangan disesuaikan dengan jenis produk dan proses produksi organisasi Anda."
    },
    "27001": {
        "title": "Jasa Penyusunan Dokumen ISO/IEC 27001 – Sistem Manajemen Keamanan Informasi",
        "year": "2022",
        "breadcrumb": "Penyusunan Dokumen ISO/IEC 27001",
        "benefit_highlights": [
            "Dokumentasi Information Security<br>Management System",
            "Risk Assessment Keamanan<br>Informasi",
            "Siap Audit Sertifikasi<br>ISO 27001"
        ],
        "definition": "Jasa Penyusunan Dokumen ISO/IEC 27001:2022 membantu organisasi menyusun dokumentasi Sistem Manajemen Keamanan Informasi yang lengkap, termasuk risk assessment, security controls, dan policies.",
        "benefits": [
            ("Information Security Policy", "Menyusun kebijakan keamanan informasi yang komprehensif"),
            ("Risk Assessment & Treatment", "Dokumentasi penilaian dan penanganan risiko keamanan informasi"),
            ("Security Controls (Annex A)", "Menyusun kontrol keamanan sesuai Annex A ISO 27001"),
            ("Access Control Management", "Dokumentasi sistem pengelolaan akses informasi"),
            ("Incident Management", "Prosedur penanganan insiden keamanan informasi"),
            ("Business Continuity Plan", "Dokumentasi rencana kontinuitas bisnis terkait IT")
        ],
        "process_step2": "Tim kami melakukan information security risk assessment, menyusun security policies, procedures, dan dokumentasi kontrol keamanan sesuai ISO/IEC 27001:2022.",
        "target_title": "Dokumen yang Kami Susun untuk ISO 27001",
        "target_desc": "Kami menyusun dokumentasi lengkap Sistem Manajemen Keamanan Informasi sesuai persyaratan ISO/IEC 27001:2022.",
        "targets": [
            "Information Security Policy",
            "Risk Assessment & Treatment Plan",
            "Statement of Applicability (SoA)",
            "Security Controls (Annex A)",
            "Access Control Procedures",
            "Incident Response Plan",
            "Business Continuity Plan",
            "Security Awareness Program",
            "Vendor Security Management"
        ],
        "target_footer": "Semua dokumen keamanan informasi disesuaikan dengan infrastruktur IT dan profil risiko organisasi Anda."
    },
    "22301": {
        "title": "Jasa Penyusunan Dokumen ISO 22301 – Sistem Manajemen Keberlangsungan Bisnis (BCMS)",
        "year": "2019",
        "breadcrumb": "Penyusunan Dokumen ISO 22301",
        "benefit_highlights": [
            "Dokumentasi Business Impact<br>Analysis (BIA)",
            "Business Continuity Plan<br>dan Recovery Strategy",
            "Siap Audit Sertifikasi<br>ISO 22301"
        ],
        "definition": "Jasa Penyusunan Dokumen ISO 22301:2019 membantu organisasi menyusun dokumentasi Sistem Manajemen Keberlangsungan Bisnis yang lengkap, termasuk BIA, Business Continuity Plan, dan Disaster Recovery Plan.",
        "benefits": [
            ("Business Impact Analysis", "Menyusun analisis dampak bisnis untuk mengidentifikasi proses kritis"),
            ("Business Continuity Plan", "Dokumentasi rencana keberlangsungan bisnis yang komprehensif"),
            ("Recovery Strategies", "Menyusun strategi pemulihan untuk berbagai skenario gangguan"),
            ("Crisis Management Plan", "Dokumentasi prosedur manajemen krisis dan komunikasi"),
            ("Testing dan Exercise Plan", "Menyusun rencana pengujian dan simulasi BCP"),
            ("Recovery Time Objective", "Dokumentasi RTO dan RPO untuk proses bisnis kritis")
        ],
        "process_step2": "Tim kami melakukan Business Impact Analysis, menyusun Business Continuity Plan, Disaster Recovery Plan, dan dokumentasi BCMS sesuai ISO 22301:2019.",
        "target_title": "Dokumen yang Kami Susun untuk ISO 22301",
        "target_desc": "Kami menyusun dokumentasi lengkap Sistem Manajemen Keberlangsungan Bisnis sesuai persyaratan ISO 22301:2019.",
        "targets": [
            "Business Continuity Policy",
            "Business Impact Analysis (BIA)",
            "Business Continuity Plan (BCP)",
            "Disaster Recovery Plan (DRP)",
            "Crisis Management Plan",
            "Recovery Strategies",
            "Testing dan Exercise Plan",
            "Communication Plan",
            "Supplier Continuity Management"
        ],
        "target_footer": "Semua dokumen BCMS disesuaikan dengan proses bisnis kritis dan profil risiko organisasi Anda."
    },
    "37001": {
        "title": "Jasa Penyusunan Dokumen ISO 37001 – Sistem Manajemen Anti Penyuapan",
        "year": "2016",
        "breadcrumb": "Penyusunan Dokumen ISO 37001",
        "benefit_highlights": [
            "Dokumentasi Anti Bribery<br>Management System",
            "Due Diligence dan<br>Risk Assessment",
            "Siap Audit Sertifikasi<br>ISO 37001"
        ],
        "definition": "Jasa Penyusunan Dokumen ISO 37001:2016 membantu organisasi menyusun dokumentasi Sistem Manajemen Anti Penyuapan yang lengkap, termasuk anti-bribery policy, due diligence, dan risk assessment.",
        "benefits": [
            ("Anti-Bribery Policy", "Menyusun kebijakan anti suap yang jelas dan komprehensif"),
            ("Bribery Risk Assessment", "Dokumentasi penilaian risiko penyuapan di berbagai area bisnis"),
            ("Due Diligence Procedures", "Menyusun prosedur uji tuntas untuk mitra bisnis dan pihak ketiga"),
            ("Gift and Hospitality Register", "Dokumentasi sistem pencatatan pemberian dan penerimaan hadiah"),
            ("Whistleblowing Mechanism", "Prosedur pelaporan dugaan penyuapan yang aman dan rahasia"),
            ("Training Program", "Dokumentasi program pelatihan anti suap untuk karyawan")
        ],
        "process_step2": "Tim kami melakukan bribery risk assessment, menyusun anti-bribery policy, due diligence procedures, dan dokumentasi ABMS sesuai ISO 37001:2016.",
        "target_title": "Dokumen yang Kami Susun untuk ISO 37001",
        "target_desc": "Kami menyusun dokumentasi lengkap Sistem Manajemen Anti Penyuapan sesuai persyaratan ISO 37001:2016.",
        "targets": [
            "Anti-Bribery Policy",
            "Bribery Risk Assessment",
            "Due Diligence Procedures",
            "Gift and Hospitality Policy",
            "Conflict of Interest Register",
            "Whistleblowing Procedure",
            "Third Party Management",
            "Training Program Documentation",
            "Investigation Procedures"
        ],
        "target_footer": "Semua dokumen anti penyuapan disesuaikan dengan profil risiko dan area bisnis organisasi Anda."
    },
    "37301": {
        "title": "Jasa Penyusunan Dokumen ISO 37301 – Sistem Manajemen Kepatuhan",
        "year": "2021",
        "breadcrumb": "Penyusunan Dokumen ISO 37301",
        "benefit_highlights": [
            "Dokumentasi Compliance<br>Management System",
            "Register Peraturan dan<br>Compliance Obligations",
            "Siap Audit Sertifikasi<br>ISO 37301"
        ],
        "definition": "Jasa Penyusunan Dokumen ISO 37301:2021 membantu organisasi menyusun dokumentasi Sistem Manajemen Kepatuhan yang lengkap, termasuk compliance register, risk assessment, dan monitoring procedures.",
        "benefits": [
            ("Compliance Policy", "Menyusun kebijakan kepatuhan yang komprehensif"),
            ("Legal Register", "Dokumentasi register peraturan perundangan yang berlaku"),
            ("Compliance Risk Assessment", "Penilaian risiko ketidakpatuhan di berbagai area bisnis"),
            ("Compliance Monitoring", "Sistem pemantauan kepatuhan terhadap regulasi"),
            ("Non-Compliance Management", "Prosedur penanganan ketidakpatuhan dan tindakan korektif"),
            ("Compliance Training", "Dokumentasi program pelatihan kepatuhan untuk karyawan")
        ],
        "process_step2": "Tim kami melakukan compliance obligations mapping, menyusun compliance policy, legal register, dan dokumentasi CMS sesuai ISO 37301:2021.",
        "target_title": "Dokumen yang Kami Susun untuk ISO 37301",
        "target_desc": "Kami menyusun dokumentasi lengkap Sistem Manajemen Kepatuhan sesuai persyaratan ISO 37301:2021.",
        "targets": [
            "Compliance Policy",
            "Legal & Regulatory Register",
            "Compliance Obligations Mapping",
            "Compliance Risk Assessment",
            "Monitoring dan Measurement Plan",
            "Non-Compliance Handling Procedure",
            "Compliance Reporting System",
            "Training Program Documentation",
            "Compliance Audit Procedures"
        ],
        "target_footer": "Semua dokumen kepatuhan disesuaikan dengan regulasi spesifik yang berlaku untuk industri organisasi Anda."
    }
}

def update_penyusunan_page(filename, iso_num, data):
    """Update penyusunan dokumen page"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update title
        content = re.sub(r'<title>.*?</title>', f'<title>{data["title"]} — INOVASS</title>', content)
        
        # Update breadcrumb
        content = re.sub(r'<span class="breadcrumb-current"[^>]*>.*?</span>',
                        f'<span class="breadcrumb-current" style="color: #00e0a0 !important;">{data["breadcrumb"]}</span>', content)
        
        # Update page title
        content = re.sub(r'<h1 class="detail-page-title"[^>]*>.*?</h1>',
                        f'<h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important; font-weight: 700 !important;">{data["title"]}</h1>', content)
        
        # Update benefit highlights title
        title_text = f"ISO/SNI {iso_num}:{data['year']}" if iso_num in ["9001", "14001"] else f"ISO {iso_num}:{data['year']}"
        if iso_num == "27001":
            title_text = f"ISO/IEC {iso_num}:{data['year']}"
        
        content = re.sub(r'<h2 class="benefit-highlight-title">Dengan ISO .*? Organisasi Anda Dapat:</h2>',
                        f'<h2 class="benefit-highlight-title">Dengan Jasa Penyusunan Dokumen {title_text}:</h2>', content)
        
        # Update benefit cards
        benefit_cards = '\n          '.join([f'<div class="benefit-highlight-card">\n            <p>{b}</p>\n          </div>' for b in data["benefit_highlights"]])
        content = re.sub(r'(<div class="benefit-highlight-grid">)(.*?)(</div>\s*</div>\s*<!-- PENGERTIAN)',
                        f'\\1\n          {benefit_cards}\n        \\3', content, flags=re.DOTALL)
        
        # Update pengertian title
        content = re.sub(r'<h2 class="iso-content-title">Pengertian ISO.*?</h2>',
                        f'<h2 class="iso-content-title">Tentang Layanan Kami</h2>', content)
        
        # Update pengertian description
        content = re.sub(r'(<p class="iso-content-desc">)\s*<strong>ISO.*?</strong>.*?(</p>)',
                        f'\\1\n            {data["definition"]}\n          \\2', content, flags=re.DOTALL)
        
        # Update manfaat title
        content = re.sub(r'<h2 class="iso-benefit-section-title">Manfaat Implementasi ISO.*?</h2>',
                        f'<h2 class="iso-benefit-section-title">Keunggulan Layanan Penyusunan Dokumen</h2>', content)
        
        # Update benefit cards
        benefit_cards_html = '\n          '.join([f'<div class="iso-benefit-modern-card">\n            <h3>{t}</h3>\n            <p>{d}</p>\n          </div>' for t, d in data["benefits"]])
        content = re.sub(r'(<div class="iso-benefits-modern-grid">)(.*?)(</div>\s*</div>\s*<!-- CTA)',
                        f'\\1\n          {benefit_cards_html}\n        \\3', content, flags=re.DOTALL)
        
        # Update process title
        content = re.sub(r'<h2 class="iso-process-title">Proses Sertifikasi ISO.*?</h2>',
                        f'<h2 class="iso-process-title">Proses Penyusunan Dokumen {title_text}</h2>', content)
        
        # Update process step 1
        content = re.sub(r'(<h3>Konsultasi & Perencanaan</h3>\s*<p>).*?(</p>)',
                        f'\\1Kami melakukan assessment awal untuk memahami proses bisnis organisasi, mengidentifikasi dokumentasi yang diperlukan, dan menyusun rencana penyusunan dokumen yang sesuai dengan kebutuhan.\\2', content, flags=re.DOTALL)
        
        # Update process step 2
        content = re.sub(r'(<h3>Pelatihan & Implementasi</h3>\s*<p>).*?(</p>)',
                        f'\\1{data["process_step2"]}\\2', content, flags=re.DOTALL)
        
        # Update process step 3
        content = re.sub(r'(<h3>Audit Internal & Tinjauan Manajemen</h3>\s*<p>).*?(</p>)',
                        f'\\1Kami melakukan review dokumen bersama tim internal organisasi, menerima feedback, dan melakukan revisi untuk memastikan dokumen sesuai dengan kebutuhan operasional.\\2', content, flags=re.DOTALL)
        
        # Update process step 5
        content = re.sub(r'(<h3>Penerbitan Sertifikat</h3>\s*<p>).*?(</p>)',
                        f'\\1Kami menyerahkan seluruh dokumentasi dalam bentuk softcopy dan hardcopy (jika diperlukan), lengkap dengan panduan penggunaan dan template yang dapat digunakan untuk update dokumen di masa mendatang.\\2', content, flags=re.DOTALL)
        
        # Update step 4 title and content (Audit Sertifikasi -> Finalisasi)
        content = re.sub(r'<h3>Audit Sertifikasi</h3>',
                        '<h3>Finalisasi Dokumen</h3>', content)
        
        content = re.sub(r'(<h3>Finalisasi Dokumen</h3>.*?<div class="process-substeps">)(.*?)(</div>)',
                        r'\1\n                <p>Setelah review dan revisi, kami melakukan finalisasi seluruh dokumen dengan memastikan:</p>\n                <p><strong>• Kelengkapan:</strong> Semua dokumen sesuai checklist persyaratan standar.</p>\n                <p><strong>• Konsistensi:</strong> Format dan struktur dokumen yang seragam.</p>\n                <p><strong>• Kesesuaian:</strong> Dokumen mencerminkan proses bisnis aktual organisasi.</p>\n              \3', content, flags=re.DOTALL)
        
        # Update step 6 title and content (Surveillance -> Dukungan)
        content = re.sub(r'<h3>Audit Surveillance & Re-Sertifikasi</h3>',
                        '<h3>Dukungan Implementasi & Konsultasi</h3>', content)
        
        content = re.sub(r'(<h3>Dukungan Implementasi & Konsultasi</h3>\s*<p>).*?(</p>)',
                        r'\1Kami memberikan dukungan konsultasi lanjutan untuk implementasi dokumen, menjawab pertanyaan terkait penggunaan dokumen, dan membantu persiapan audit sertifikasi.\2', content, flags=re.DOTALL)
        
        # Update target title
        content = re.sub(r'<h2 class="iso-target-section-title"[^>]*>Siapa yang .*?</h2>',
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
    "9001": "layanan-detail-penyusunan-dokumen-iso-9001.html",
    "14001": "layanan-detail-penyusunan-dokumen-iso-14001.html",
    "45001": "layanan-detail-penyusunan-dokumen-iso-45001.html",
    "22000": "layanan-detail-penyusunan-dokumen-iso-22000.html",
    "27001": "layanan-detail-penyusunan-dokumen-iso-27001.html",
    "22301": "layanan-detail-penyusunan-dokumen-iso-22301.html",
    "37001": "layanan-detail-penyusunan-dokumen-iso-37001.html",
    "37301": "layanan-detail-penyusunan-dokumen-iso-37301.html"
}

print("Updating 8 Penyusunan Dokumen ISO pages...")
print("=" * 50)

for iso_num, filename in file_mappings.items():
    data = iso_standards[iso_num]
    update_penyusunan_page(filename, iso_num, data)

print("=" * 50)
print("Update complete!")
