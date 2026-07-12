#!/usr/bin/env python3
import re

# Mapping service title ke filename
service_mapping = {
    # ISO Services
    "Jasa Sertifikasi ISO Organisasi": "jasa-sertifikasi-iso",
    "Jasa Persiapan Surveillance Audit Organisasi": "jasa-surveillance-audit-organisasi",
    "Jasa Perawatan Sistem Sertifikasi Organisasi": "jasa-perawatan-sistem-sertifikasi",
    "Jasa Audit Internal Sistem Manajemen Standar ISO Organisasi": "jasa-audit-internal-iso",
    "Jasa Persiapan Surveillance Audit Akreditasi Laboratorium": "jasa-surveillance-audit-lab",
    "Jasa Persiapan Re-Sertifikasi Audit Akreditasi Laboratorium": "jasa-resertifikasi-audit-lab",
    
    # Akreditasi Services
    "Konsultasi Akreditasi Lembaga Inspeksi Standar ISO 17020:2012": "konsultasi-akreditasi-inspeksi",
    "Konsultasi Persiapan Surveillance Audit Akreditasi Lembaga Inspeksi": "konsultasi-surveillance-inspeksi",
    "Konsultasi Persiapan Re-Sertifikasi Audit Akreditasi Lembaga Inspeksi": "konsultasi-resertifikasi-inspeksi",
    "Konsultasi Akreditasi Lembaga Sertifikasi Personel (LSP) Standar ISO 17024:2012": "konsultasi-akreditasi-lsp",
    "Konsultasi Persiapan Surveillance Audit Akreditasi LSP Standar ISO 17024:2012": "konsultasi-surveillance-lsp",
    "Konsultasi Persiapan Re-Sertifikasi Audit Akreditasi LSP Standar ISO 17024:2012": "konsultasi-resertifikasi-lsp",
    "Konsultasi Akreditasi Lembaga Sertifikasi Produk (LSPro) Standar ISO 17065:2012": "konsultasi-akreditasi-lspro",
    "Konsultasi Persiapan Surveillance Audit Akreditasi LSPro Standar ISO 17065:2012": "konsultasi-surveillance-lspro",
    "Konsultasi Persiapan Re-Sertifikasi Audit Akreditasi LSPro Standar ISO 17065:2012": "konsultasi-resertifikasi-lspro",
    
    # Pelatihan Services
    "Public Training": "public-training",
    "In House Training": "in-house-training",
    "Executive Training": "executive-training",
    "Private Training": "private-training",
    "Pelatihan Auditor Internal ISO": "pelatihan-auditor-internal-iso",
    "Pelatihan Implementasi ISO": "pelatihan-implementasi-iso",
    "Pelatihan K3 & Lingkungan": "pelatihan-k3-lingkungan",
    
    # Sertifikasi Services
    "Sertifikasi Auditor Internal QMS": "sertifikasi-auditor-qms",
    "Sertifikasi Auditor Internal EMS": "sertifikasi-auditor-ems",
    "Sertifikasi Auditor Internal OHSMS": "sertifikasi-auditor-ohsms",
    "Sertifikasi Auditor Internal ISMS": "sertifikasi-auditor-isms",
    "Sertifikasi Manager Representative ISO": "sertifikasi-manager-representative",
    "Sertifikasi Ahli K3 Umum": "sertifikasi-ahli-k3-umum",
}

files_to_update = [
    'layanan-iso.html',
    'layanan-akreditasi.html',
    'layanan-pelatihan.html',
    'layanan-sertifikasi.html'
]

for filename in files_to_update:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update links
        for service_title, detail_filename in service_mapping.items():
            # Escape special characters in title for regex
            escaped_title = re.escape(service_title)
            
            # Pattern to find: <h3>Title</h3>...content...<a href="kontak.html"
            # Replace with: <h3>Title</h3>...content...<a href="layanan-detail-X.html"
            pattern = f'(<h3>{escaped_title}</h3>.*?<a href=")kontak\\.html(")'
            replacement = f'\\1layanan-detail-{detail_filename}.html\\2'
            
            content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        # Write back
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f'✅ Updated {filename}')
        
    except FileNotFoundError:
        print(f'⚠️  File not found: {filename}')
    except Exception as e:
        print(f'❌ Error updating {filename}: {e}')

print('\n✅ All files updated successfully!')
