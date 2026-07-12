#!/usr/bin/env python3
"""Apply improved template to all detail pages"""

import re

# Define all services with their metadata
services = {
    # ISO Services
    'layanan-detail-jasa-sertifikasi-iso.html': {
        'title': 'Jasa Sertifikasi ISO Organisasi',
        'breadcrumb': 'Sertifikasi ISO',
        'category': 'Konsultasi & Sertifikasi ISO',
        'category_link': 'layanan-iso.html'
    },
    'layanan-detail-jasa-surveillance-audit-organisasi.html': {
        'title': 'Jasa Persiapan Surveillance Audit Organisasi',
        'breadcrumb': 'Surveillance Audit',
        'category': 'Konsultasi & Sertifikasi ISO',
        'category_link': 'layanan-iso.html'
    },
    'layanan-detail-jasa-perawatan-sistem-sertifikasi.html': {
        'title': 'Jasa Perawatan Sistem Sertifikasi Organisasi',
        'breadcrumb': 'Perawatan Sistem',
        'category': 'Konsultasi & Sertifikasi ISO',
        'category_link': 'layanan-iso.html'
    },
    'layanan-detail-jasa-audit-internal-iso.html': {
        'title': 'Jasa Audit Internal Sistem Manajemen Standar ISO Organisasi',
        'breadcrumb': 'Audit Internal ISO',
        'category': 'Konsultasi & Sertifikasi ISO',
        'category_link': 'layanan-iso.html'
    },
    'layanan-detail-jasa-surveillance-audit-lab.html': {
        'title': 'Jasa Persiapan Surveillance Audit Akreditasi Laboratorium',
        'breadcrumb': 'Surveillance Lab',
        'category': 'Konsultasi & Sertifikasi ISO',
        'category_link': 'layanan-iso.html'
    },
    'layanan-detail-jasa-resertifikasi-audit-lab.html': {
        'title': 'Jasa Persiapan Re-Sertifikasi Audit Akreditasi Laboratorium',
        'breadcrumb': 'Re-Sertifikasi Lab',
        'category': 'Konsultasi & Sertifikasi ISO',
        'category_link': 'layanan-iso.html'
    },
    
    # Akreditasi Services
    'layanan-detail-akreditasi-lab.html': {
        'title': 'Jasa Konsultasi Persiapan Akreditasi Laboratorium',
        'breadcrumb': 'Akreditasi Lab',
        'category': 'Konsultasi Akreditasi',
        'category_link': 'layanan-akreditasi.html'
    },
    'layanan-detail-akreditasi-rs.html': {
        'title': 'Jasa Konsultasi Persiapan Akreditasi Rumah Sakit',
        'breadcrumb': 'Akreditasi RS',
        'category': 'Konsultasi Akreditasi',
        'category_link': 'layanan-akreditasi.html'
    },
    'layanan-detail-akreditasi-puskesmas.html': {
        'title': 'Jasa Konsultasi Persiapan Akreditasi Puskesmas',
        'breadcrumb': 'Akreditasi Puskesmas',
        'category': 'Konsultasi Akreditasi',
        'category_link': 'layanan-akreditasi.html'
    },
    'layanan-detail-akreditasi-klinik.html': {
        'title': 'Jasa Konsultasi Persiapan Akreditasi Klinik',
        'breadcrumb': 'Akreditasi Klinik',
        'category': 'Konsultasi Akreditasi',
        'category_link': 'layanan-akreditasi.html'
    },
    'layanan-detail-akreditasi-ban-pt.html': {
        'title': 'Jasa Konsultasi Akreditasi BAN PT',
        'breadcrumb': 'Akreditasi BAN PT',
        'category': 'Konsultasi Akreditasi',
        'category_link': 'layanan-akreditasi.html'
    },
    'layanan-detail-akreditasi-lam-ptkes.html': {
        'title': 'Jasa Konsultasi Akreditasi LAM PTKes',
        'breadcrumb': 'Akreditasi LAM PTKes',
        'category': 'Konsultasi Akreditasi',
        'category_link': 'layanan-akreditasi.html'
    },
    'layanan-detail-akreditasi-ban-paud-pnf.html': {
        'title': 'Jasa Konsultasi Akreditasi BAN PAUD dan PNF',
        'breadcrumb': 'Akreditasi PAUD & PNF',
        'category': 'Konsultasi Akreditasi',
        'category_link': 'layanan-akreditasi.html'
    },
    'layanan-detail-akreditasi-ban-sm.html': {
        'title': 'Jasa Konsultasi Akreditasi BAN S/M',
        'breadcrumb': 'Akreditasi BAN S/M',
        'category': 'Konsultasi Akreditasi',
        'category_link': 'layanan-akreditasi.html'
    },
    'layanan-detail-akreditasi-lsp.html': {
        'title': 'Jasa Persiapan Lisensi LSP',
        'breadcrumb': 'Lisensi LSP',
        'category': 'Konsultasi Akreditasi',
        'category_link': 'layanan-akreditasi.html'
    },
    
    # Pelatihan Services
    'layanan-detail-public-training.html': {
        'title': 'Public Training',
        'breadcrumb': 'Public Training',
        'category': 'Pelatihan Profesional',
        'category_link': 'layanan-pelatihan.html'
    },
    'layanan-detail-in-house-training.html': {
        'title': 'In-House Training',
        'breadcrumb': 'In-House Training',
        'category': 'Pelatihan Profesional',
        'category_link': 'layanan-pelatihan.html'
    },
    'layanan-detail-online-training.html': {
        'title': 'Online Training (Webinar)',
        'breadcrumb': 'Online Training',
        'category': 'Pelatihan Profesional',
        'category_link': 'layanan-pelatihan.html'
    },
    'layanan-detail-executive-training.html': {
        'title': 'Executive Training',
        'breadcrumb': 'Executive Training',
        'category': 'Pelatihan Profesional',
        'category_link': 'layanan-pelatihan.html'
    },
    'layanan-detail-workshop-seminar.html': {
        'title': 'Workshop & Seminar',
        'breadcrumb': 'Workshop & Seminar',
        'category': 'Pelatihan Profesional',
        'category_link': 'layanan-pelatihan.html'
    },
    'layanan-detail-customized-training.html': {
        'title': 'Customized Training Program',
        'breadcrumb': 'Customized Training',
        'category': 'Pelatihan Profesional',
        'category_link': 'layanan-pelatihan.html'
    },
    
    # More Akreditasi Services
    'layanan-detail-konsultasi-akreditasi-lsp.html': {
        'title': 'Konsultasi Akreditasi LSP',
        'breadcrumb': 'Akreditasi LSP',
        'category': 'Konsultasi Akreditasi',
        'category_link': 'layanan-akreditasi.html'
    },
    'layanan-detail-konsultasi-akreditasi-lspro.html': {
        'title': 'Konsultasi Akreditasi LSPRO',
        'breadcrumb': 'Akreditasi LSPRO',
        'category': 'Konsultasi Akreditasi',
        'category_link': 'layanan-akreditasi.html'
    },
    'layanan-detail-konsultasi-akreditasi-inspeksi.html': {
        'title': 'Konsultasi Akreditasi Lembaga Inspeksi',
        'breadcrumb': 'Akreditasi Inspeksi',
        'category': 'Konsultasi Akreditasi',
        'category_link': 'layanan-akreditasi.html'
    },
    'layanan-detail-konsultasi-surveillance-lsp.html': {
        'title': 'Konsultasi Surveillance LSP',
        'breadcrumb': 'Surveillance LSP',
        'category': 'Konsultasi Akreditasi',
        'category_link': 'layanan-akreditasi.html'
    },
    'layanan-detail-konsultasi-surveillance-lspro.html': {
        'title': 'Konsultasi Surveillance LSPRO',
        'breadcrumb': 'Surveillance LSPRO',
        'category': 'Konsultasi Akreditasi',
        'category_link': 'layanan-akreditasi.html'
    },
    'layanan-detail-konsultasi-surveillance-inspeksi.html': {
        'title': 'Konsultasi Surveillance Lembaga Inspeksi',
        'breadcrumb': 'Surveillance Inspeksi',
        'category': 'Konsultasi Akreditasi',
        'category_link': 'layanan-akreditasi.html'
    },
    'layanan-detail-konsultasi-resertifikasi-lsp.html': {
        'title': 'Konsultasi Re-Sertifikasi LSP',
        'breadcrumb': 'Re-Sertifikasi LSP',
        'category': 'Konsultasi Akreditasi',
        'category_link': 'layanan-akreditasi.html'
    },
    'layanan-detail-konsultasi-resertifikasi-lspro.html': {
        'title': 'Konsultasi Re-Sertifikasi LSPRO',
        'breadcrumb': 'Re-Sertifikasi LSPRO',
        'category': 'Konsultasi Akreditasi',
        'category_link': 'layanan-akreditasi.html'
    },
    'layanan-detail-konsultasi-resertifikasi-inspeksi.html': {
        'title': 'Konsultasi Re-Sertifikasi Lembaga Inspeksi',
        'breadcrumb': 'Re-Sertifikasi Inspeksi',
        'category': 'Konsultasi Akreditasi',
        'category_link': 'layanan-akreditasi.html'
    },
    
    # More Pelatihan Services
    'layanan-detail-private-training.html': {
        'title': 'Private Training',
        'breadcrumb': 'Private Training',
        'category': 'Pelatihan Profesional',
        'category_link': 'layanan-pelatihan.html'
    },
    'layanan-detail-pelatihan-auditor-internal-iso.html': {
        'title': 'Pelatihan Auditor Internal ISO',
        'breadcrumb': 'Auditor Internal ISO',
        'category': 'Pelatihan Profesional',
        'category_link': 'layanan-pelatihan.html'
    },
    'layanan-detail-pelatihan-implementasi-iso.html': {
        'title': 'Pelatihan Implementasi ISO',
        'breadcrumb': 'Implementasi ISO',
        'category': 'Pelatihan Profesional',
        'category_link': 'layanan-pelatihan.html'
    },
    'layanan-detail-pelatihan-k3-lingkungan.html': {
        'title': 'Pelatihan K3 dan Lingkungan',
        'breadcrumb': 'K3 & Lingkungan',
        'category': 'Pelatihan Profesional',
        'category_link': 'layanan-pelatihan.html'
    },
    
    # Sertifikasi Personel Services
    'layanan-detail-sertifikasi-asesor.html': {
        'title': 'Sertifikasi Asesor Kompetensi',
        'breadcrumb': 'Sertifikasi Asesor',
        'category': 'Sertifikasi Personel',
        'category_link': 'layanan-sertifikasi.html'
    },
    'layanan-detail-sertifikasi-auditor.html': {
        'title': 'Sertifikasi Auditor ISO',
        'breadcrumb': 'Sertifikasi Auditor',
        'category': 'Sertifikasi Personel',
        'category_link': 'layanan-sertifikasi.html'
    },
    'layanan-detail-sertifikasi-auditor-qms.html': {
        'title': 'Sertifikasi Auditor QMS (ISO 9001)',
        'breadcrumb': 'Auditor QMS',
        'category': 'Sertifikasi Personel',
        'category_link': 'layanan-sertifikasi.html'
    },
    'layanan-detail-sertifikasi-auditor-ems.html': {
        'title': 'Sertifikasi Auditor EMS (ISO 14001)',
        'breadcrumb': 'Auditor EMS',
        'category': 'Sertifikasi Personel',
        'category_link': 'layanan-sertifikasi.html'
    },
    'layanan-detail-sertifikasi-auditor-ohsms.html': {
        'title': 'Sertifikasi Auditor OHSMS (ISO 45001)',
        'breadcrumb': 'Auditor OHSMS',
        'category': 'Sertifikasi Personel',
        'category_link': 'layanan-sertifikasi.html'
    },
    'layanan-detail-sertifikasi-auditor-isms.html': {
        'title': 'Sertifikasi Auditor ISMS (ISO 27001)',
        'breadcrumb': 'Auditor ISMS',
        'category': 'Sertifikasi Personel',
        'category_link': 'layanan-sertifikasi.html'
    },
    'layanan-detail-sertifikasi-k3.html': {
        'title': 'Sertifikasi K3 (Keselamatan dan Kesehatan Kerja)',
        'breadcrumb': 'Sertifikasi K3',
        'category': 'Sertifikasi Personel',
        'category_link': 'layanan-sertifikasi.html'
    },
    'layanan-detail-sertifikasi-ahli-k3-umum.html': {
        'title': 'Sertifikasi Ahli K3 Umum',
        'breadcrumb': 'Ahli K3 Umum',
        'category': 'Sertifikasi Personel',
        'category_link': 'layanan-sertifikasi.html'
    },
    'layanan-detail-sertifikasi-profesi.html': {
        'title': 'Sertifikasi Profesi & Kompetensi',
        'breadcrumb': 'Sertifikasi Profesi',
        'category': 'Sertifikasi Personel',
        'category_link': 'layanan-sertifikasi.html'
    },
    'layanan-detail-sertifikasi-manager-representative.html': {
        'title': 'Sertifikasi Management Representative',
        'breadcrumb': 'Management Representative',
        'category': 'Sertifikasi Personel',
        'category_link': 'layanan-sertifikasi.html'
    },
}

# Read the improved template
with open('template-minimal.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Apply template to each service
for filename, data in services.items():
    content = template
    content = content.replace('TITLE_PLACEHOLDER', data['title'])
    content = content.replace('BREADCRUMB_PLACEHOLDER', data['breadcrumb'])
    content = content.replace('CATEGORY_PLACEHOLDER', data['category'])
    content = content.replace('CATEGORY_LINK_PLACEHOLDER', data['category_link'])
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'✅ Updated: {filename}')

print(f'\n🎉 Successfully updated {len(services)} detail pages with improved design!')
