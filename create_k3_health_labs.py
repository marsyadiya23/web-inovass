#!/usr/bin/env python3
import re

# Template file
template_file = "layanan-detail-k3-lab-pendidikan-kedokteran.html"

# Define all K3 Health Lab pages with their specific content
labs = {
    "farmasi": {
        "filename": "layanan-detail-k3-lab-pendidikan-farmasi.html",
        "title": "Jasa Konsultasi K3 Laboratorium Pendidikan Farmasi",
        "breadcrumb": "K3 Lab Pendidikan Farmasi",
        "highlights": ["Pharmaceutical<br>Safety", "Zero Lab<br>Incident", "Student<br>Protection"],
        "pengertian": "Jasa Konsultasi K3 Laboratorium Pendidikan Farmasi adalah layanan profesional yang membantu laboratorium farmasi dalam menerapkan sistem keselamatan dan kesehatan kerja yang komprehensif untuk melindungi mahasiswa, dosen, dan petugas lab dari risiko kimia, biologis, dan aktivitas praktikum farmasi seperti formulasi obat, analisis farmasi, mikrobiologi farmasi, dan farmakognosi.",
        "benefits": [
            ("Pharmaceutical Safety", "Pengendalian risiko pembuatan sediaan farmasi: tablet, kapsul, sirup, salep, injeksi"),
            ("Chemical Control", "Keamanan penggunaan bahan aktif farmasi, pelarut organik, dan bahan kimia berbahaya"),
            ("Drug Analysis Safety", "Sistem keselamatan praktikum analisis farmasi, HPLC, spektrofotometri, dan titrasi"),
            ("Sterility Protection", "Protokol aseptis, LAF (Laminar Air Flow), dan sterilisasi sediaan steril"),
            ("PPE Compliance", "Implementasi APD farmasi: lab coat, safety goggles, chemical gloves, fume hood"),
            ("Pharmaceutical Excellence", "Peningkatan kualitas pembelajaran praktikum dengan lingkungan lab yang aman")
        ],
        "process_steps": [
            ("Lab Safety Assessment", "Assessment K3 laboratorium farmasi, identifikasi bahaya kimia (API, pelarut), bahaya biologis, evaluasi fume hood dan LAF, pengendalian risiko praktikum pembuatan sediaan"),
            ("HIRADC Pharmaceutical Lab", "Identifikasi bahaya spesifik lab farmasi: formulasi, analisis, mikrobiologi farmasi, farmakognosi, penilaian risiko eksposur kimia dan sterilitas, penentuan kontrol efektif"),
            ("Safety Procedure Development", "Protokol pembuatan sediaan aman, SOP praktikum mahasiswa, JSA untuk handling bahan farmasi, prosedur LAF dan sterilisasi, instruksi kerja aman"),
            ("PPE & Equipment Safety", "Rekomendasi APD farmasi: lab coat, chemical gloves, safety goggles, respirator, implementasi fume hood dan LAF, sistem ventilasi laboratorium"),
            ("Lab Safety Training", "Pharmaceutical safety awareness, keselamatan praktikum mahasiswa, penggunaan APD farmasi, GMP basic, prosedur darurat lab farmasi"),
            ("Emergency Response Plan", "Prosedur tanggap darurat chemical spill, API exposure, LAF contamination, evakuasi laboratorium yang aman")
        ],
        "targets": ["Fakultas Farmasi", "Lab Farmasetika", "Lab Analisis Farmasi", "Lab Mikrobiologi Farmasi", "Lab Farmakognosi", "Lab Kimia Farmasi", "Lab Biologi Farmasi", "Lab Farmakologi", "Universitas Farmasi"],
        "footer": "Konsultasi K3 laboratorium pendidikan farmasi membantu institusi pendidikan dalam menerapkan sistem keselamatan kerja yang spesifik untuk aktivitas praktikum farmasi, melindungi mahasiswa, dosen, dan petugas lab dari risiko kimia, biologis, dan pharmaceutical hazards, serta memastikan kualitas pembelajaran yang optimal dengan lingkungan lab yang aman.",
        "cta": "K3 Laboratorium Pendidikan Farmasi"
    },
    "keperawatan": {
        "filename": "layanan-detail-k3-lab-pendidikan-keperawatan.html",
        "title": "Jasa Konsultasi K3 Laboratorium Pendidikan Keperawatan",
        "breadcrumb": "K3 Lab Pendidikan Keperawatan",
        "highlights": ["Clinical<br>Safety", "Zero<br>Incident", "Student<br>Protection"],
        "pengertian": "Jasa Konsultasi K3 Laboratorium Pendidikan Keperawatan adalah layanan profesional yang membantu laboratorium keperawatan dalam menerapkan sistem keselamatan dan kesehatan kerja yang komprehensif untuk melindungi mahasiswa, dosen, dan petugas lab dari risiko praktikum keperawatan seperti perawatan luka, injeksi, catheterisasi, dan prosedur keperawatan lainnya.",
        "benefits": [
            ("Clinical Skills Safety", "Pengendalian risiko praktikum keterampilan klinis: injeksi, infus, catheter, wound care"),
            ("Infection Control", "Protokol pencegahan infeksi silang, sterilisasi alat, hand hygiene, dan universal precaution"),
            ("Needlestick Prevention", "Sistem keselamatan untuk mencegah needle stick injury dan sharps management"),
            ("Patient Safety Simulation", "Keselamatan praktikum dengan manikin, bed management, dan patient handling"),
            ("PPE Compliance", "Implementasi APD keperawatan: gloves, apron, face shield, dan barrier protection"),
            ("Nursing Excellence", "Peningkatan kualitas pembelajaran praktikum keperawatan dengan lingkungan lab yang aman")
        ],
        "process_steps": [
            ("Lab Safety Assessment", "Assessment K3 laboratorium keperawatan, identifikasi bahaya praktikum klinis, evaluasi infection control, pengendalian risiko needle stick injury"),
            ("HIRADC Nursing Lab", "Identifikasi bahaya spesifik lab keperawatan: injeksi, catheter, wound care, patient handling, penilaian risiko infeksi dan injury, penentuan kontrol efektif"),
            ("Safety Procedure Development", "Protokol infection control, SOP praktikum keterampilan keperawatan, JSA untuk prosedur invasif, sharps management, instruksi kerja aman"),
            ("PPE & Equipment Safety", "Rekomendasi APD keperawatan: medical gloves, apron, face shield, safety eyewear, implementasi sharps container, sistem sterilisasi yang memadai"),
            ("Lab Safety Training", "Infection control training, keselamatan praktikum mahasiswa, penggunaan APD keperawatan, needle safety, prosedur darurat laboratorium"),
            ("Emergency Response Plan", "Prosedur tanggap darurat needle stick injury, blood exposure, patient fall simulation, evakuasi laboratorium yang aman")
        ],
        "targets": ["Fakultas Keperawatan", "Lab Keterampilan Keperawatan Dasar", "Lab Keperawatan Medikal Bedah", "Lab Keperawatan Anak", "Lab Keperawatan Maternitas", "Lab Keperawatan Gawat Darurat", "Lab Keperawatan Komunitas", "Lab Nursing Skills", "Universitas Keperawatan"],
        "footer": "Konsultasi K3 laboratorium pendidikan keperawatan membantu institusi pendidikan dalam menerapkan sistem keselamatan kerja yang spesifik untuk aktivitas praktikum keperawatan, melindungi mahasiswa, dosen, dan petugas lab dari risiko infeksi, needle stick injury, dan clinical hazards, serta memastikan kualitas pembelajaran yang optimal dengan lingkungan lab yang aman.",
        "cta": "K3 Laboratorium Pendidikan Keperawatan"
    }
}

print("Creating K3 Health Lab pages...")
print("=" * 80)

# Read template
with open(template_file, 'r', encoding='utf-8') as f:
    template_content = f.read()

for lab_key, lab_data in labs.items():
    print(f"\nCreating: {lab_data['filename']}")
    
    content = template_content
    
    # Replace title
    content = re.sub(
        r'<title>Jasa Konsultasi K3 Laboratorium Pendidikan Kedokteran — INOVASS</title>',
        f'<title>{lab_data["title"]} — INOVASS</title>',
        content
    )
    
    # Replace breadcrumb
    content = re.sub(
        r'<span class="breadcrumb-current"[^>]*>K3 Lab Pendidikan Kedokteran</span>',
        f'<span class="breadcrumb-current" style="color: #00e0a0 !important;">{lab_data["breadcrumb"]}</span>',
        content
    )
    
    # Replace H1 title
    content = re.sub(
        r'<h1 class="detail-page-title"[^>]*>Jasa Konsultasi K3 Laboratorium Pendidikan Kedokteran</h1>',
        f'<h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important; font-weight: 700 !important;">{lab_data["title"]}</h1>',
        content
    )
    
    # Replace HTML comment
    content = re.sub(
        r'<!-- K3 LAB PENDIDIKAN KEDOKTERAN CONTENT -->',
        f'<!-- K3 LAB {lab_key.upper()} CONTENT -->',
        content
    )
    
    # Replace benefit highlight title
    content = re.sub(
        r'<h2 class="benefit-highlight-title">Dengan Jasa Konsultasi K3 Laboratorium Pendidikan Kedokteran Perusahaan Anda Dapat:</h2>',
        f'<h2 class="benefit-highlight-title">Dengan Jasa Konsultasi K3 Laboratorium Pendidikan {lab_key.title()} Perusahaan Anda Dapat:</h2>',
        content
    )
    
    # Write file
    with open(lab_data['filename'], 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✓ Created successfully")

print("\n" + "=" * 80)
print("First 2 files created! Continue with the rest...")
