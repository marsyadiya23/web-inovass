#!/usr/bin/env python3
import os
import re

# Mapping service title ke filename dan kategori
service_data = {
    # ISO Services
    "jasa-sertifikasi-iso": {
        "title": "Jasa Sertifikasi ISO Organisasi",
        "breadcrumb": "Sertifikasi ISO",
        "category": "Konsultasi & Sertifikasi ISO",
        "category_link": "layanan-iso.html"
    },
    "jasa-surveillance-audit-organisasi": {
        "title": "Jasa Persiapan Surveillance Audit Organisasi",
        "breadcrumb": "Surveillance Audit",
        "category": "Konsultasi & Sertifikasi ISO",
        "category_link": "layanan-iso.html"
    },
    "jasa-perawatan-sistem-sertifikasi": {
        "title": "Jasa Perawatan Sistem Sertifikasi Organisasi",
        "breadcrumb": "Perawatan Sistem",
        "category": "Konsultasi & Sertifikasi ISO",
        "category_link": "layanan-iso.html"
    },
    "jasa-audit-internal-iso": {
        "title": "Jasa Audit Internal Sistem Manajemen Standar ISO Organisasi",
        "breadcrumb": "Audit Internal ISO",
        "category": "Konsultasi & Sertifikasi ISO",
        "category_link": "layanan-iso.html"
    },
    "jasa-surveillance-audit-lab": {
        "title": "Jasa Persiapan Surveillance Audit Akreditasi Laboratorium",
        "breadcrumb": "Surveillance Audit Lab",
        "category": "Konsultasi & Sertifikasi ISO",
        "category_link": "layanan-iso.html"
    },
    "jasa-resertifikasi-audit-lab": {
        "title": "Jasa Persiapan Re-Sertifikasi Audit Akreditasi Laboratorium",
        "breadcrumb": "Re-Sertifikasi Lab",
        "category": "Konsultasi & Sertifikasi ISO",
        "category_link": "layanan-iso.html"
    },
    # Akreditasi
    "konsultasi-akreditasi-inspeksi": {
        "title": "Konsultasi Akreditasi Lembaga Inspeksi",
        "breadcrumb": "Akreditasi Inspeksi",
        "category": "Konsultasi Akreditasi",
        "category_link": "layanan-akreditasi.html"
    },
    "konsultasi-surveillance-inspeksi": {
        "title": "Konsultasi Surveillance Audit Lembaga Inspeksi",
        "breadcrumb": "Surveillance Inspeksi",
        "category": "Konsultasi Akreditasi",
        "category_link": "layanan-akreditasi.html"
    },
    "konsultasi-resertifikasi-inspeksi": {
        "title": "Konsultasi Re-Sertifikasi Lembaga Inspeksi",
        "breadcrumb": "Re-Sertifikasi Inspeksi",
        "category": "Konsultasi Akreditasi",
        "category_link": "layanan-akreditasi.html"
    },
    "konsultasi-akreditasi-lsp": {
        "title": "Konsultasi Akreditasi LSP",
        "breadcrumb": "Akreditasi LSP",
        "category": "Konsultasi Akreditasi",
        "category_link": "layanan-akreditasi.html"
    },
    "konsultasi-surveillance-lsp": {
        "title": "Konsultasi Surveillance Audit LSP",
        "breadcrumb": "Surveillance LSP",
        "category": "Konsultasi Akreditasi",
        "category_link": "layanan-akreditasi.html"
    },
    "konsultasi-resertifikasi-lsp": {
        "title": "Konsultasi Re-Sertifikasi LSP",
        "breadcrumb": "Re-Sertifikasi LSP",
        "category": "Konsultasi Akreditasi",
        "category_link": "layanan-akreditasi.html"
    },
    "konsultasi-akreditasi-lspro": {
        "title": "Konsultasi Akreditasi LSPro",
        "breadcrumb": "Akreditasi LSPro",
        "category": "Konsultasi Akreditasi",
        "category_link": "layanan-akreditasi.html"
    },
    "konsultasi-surveillance-lspro": {
        "title": "Konsultasi Surveillance Audit LSPro",
        "breadcrumb": "Surveillance LSPro",
        "category": "Konsultasi Akreditasi",
        "category_link": "layanan-akreditasi.html"
    },
    "konsultasi-resertifikasi-lspro": {
        "title": "Konsultasi Re-Sertifikasi LSPro",
        "breadcrumb": "Re-Sertifikasi LSPro",
        "category": "Konsultasi Akreditasi",
        "category_link": "layanan-akreditasi.html"
    },
    # Pelatihan
    "public-training": {
        "title": "Public Training",
        "breadcrumb": "Public Training",
        "category": "Pelatihan Profesional",
        "category_link": "layanan-pelatihan.html"
    },
    "in-house-training": {
        "title": "In House Training",
        "breadcrumb": "In House Training",
        "category": "Pelatihan Profesional",
        "category_link": "layanan-pelatihan.html"
    },
    "executive-training": {
        "title": "Executive Training",
        "breadcrumb": "Executive Training",
        "category": "Pelatihan Profesional",
        "category_link": "layanan-pelatihan.html"
    },
    "private-training": {
        "title": "Private Training",
        "breadcrumb": "Private Training",
        "category": "Pelatihan Profesional",
        "category_link": "layanan-pelatihan.html"
    },
    "pelatihan-auditor-internal-iso": {
        "title": "Pelatihan Auditor Internal ISO",
        "breadcrumb": "Auditor Internal ISO",
        "category": "Pelatihan Profesional",
        "category_link": "layanan-pelatihan.html"
    },
    "pelatihan-implementasi-iso": {
        "title": "Pelatihan Implementasi ISO",
        "breadcrumb": "Implementasi ISO",
        "category": "Pelatihan Profesional",
        "category_link": "layanan-pelatihan.html"
    },
    "pelatihan-k3-lingkungan": {
        "title": "Pelatihan K3 & Lingkungan",
        "breadcrumb": "K3 & Lingkungan",
        "category": "Pelatihan Profesional",
        "category_link": "layanan-pelatihan.html"
    },
    # Sertifikasi
    "sertifikasi-auditor-qms": {
        "title": "Sertifikasi Auditor Internal QMS",
        "breadcrumb": "Auditor QMS",
        "category": "Sertifikasi Personel",
        "category_link": "layanan-sertifikasi.html"
    },
    "sertifikasi-auditor-ems": {
        "title": "Sertifikasi Auditor Internal EMS",
        "breadcrumb": "Auditor EMS",
        "category": "Sertifikasi Personel",
        "category_link": "layanan-sertifikasi.html"
    },
    "sertifikasi-auditor-ohsms": {
        "title": "Sertifikasi Auditor Internal OHSMS",
        "breadcrumb": "Auditor OHSMS",
        "category": "Sertifikasi Personel",
        "category_link": "layanan-sertifikasi.html"
    },
    "sertifikasi-auditor-isms": {
        "title": "Sertifikasi Auditor Internal ISMS",
        "breadcrumb": "Auditor ISMS",
        "category": "Sertifikasi Personel",
        "category_link": "layanan-sertifikasi.html"
    },
    "sertifikasi-manager-representative": {
        "title": "Sertifikasi Manager Representative ISO",
        "breadcrumb": "Manager Representative",
        "category": "Sertifikasi Personel",
        "category_link": "layanan-sertifikasi.html"
    },
    "sertifikasi-ahli-k3-umum": {
        "title": "Sertifikasi Ahli K3 Umum",
        "breadcrumb": "Ahli K3 Umum",
        "category": "Sertifikasi Personel",
        "category_link": "layanan-sertifikasi.html"
    },
}

# Read template
with open('template-minimal.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Apply template to all service files (except penyusunan-dokumen which has full content)
count = 0
for filename_key, data in service_data.items():
    filename = f"layanan-detail-{filename_key}.html"
    
    if not os.path.exists(filename):
        print(f"⚠️  Skipping {filename} (not found)")
        continue
    
    # Create content from template
    content = template.replace("TITLE_PLACEHOLDER", data["title"])
    content = content.replace("BREADCRUMB_PLACEHOLDER", data["breadcrumb"])
    content = content.replace("CATEGORY_PLACEHOLDER", data["category"])
    content = content.replace("CATEGORY_LINK_PLACEHOLDER", data["category_link"])
    
    # Write
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    count += 1
    print(f"✅ Updated {filename}")

print(f"\n✅ Total files updated: {count}")
