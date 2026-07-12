#!/bin/bash

# List halaman yang perlu dibuat untuk akreditasi
declare -a pages=(
  "konsultasi-akreditasi-inspeksi:Konsultasi Akreditasi Lembaga Inspeksi Standar ISO 17020\:2012"
  "konsultasi-akreditasi-lsp:Konsultasi Akreditasi LSP Standar ISO 17024\:2012"
  "konsultasi-surveillance-lsp:Konsultasi Persiapan Surveillance Audit Akreditasi LSP"
  "konsultasi-resertifikasi-lsp:Konsultasi Persiapan Re-Sertifikasi Audit Akreditasi LSP"
  "konsultasi-akreditasi-lspro:Konsultasi Akreditasi LSPro Standar ISO 17065\:2012"
  "konsultasi-surveillance-lspro:Konsultasi Persiapan Surveillance Audit Akreditasi LSPro"
  "konsultasi-resertifikasi-lspro:Konsultasi Persiapan Re-Sertifikasi Audit Akreditasi LSPro"
)

for page in "${pages[@]}"; do
  IFS=':' read -r filename title <<< "$page"
  
  if [ ! -f "layanan-detail-${filename}.html" ]; then
    cp layanan-detail-penyusunan-dokumen.html "layanan-detail-${filename}.html"
    
    # Update title dan konten placeholder
    sed -i '' "s|Jasa Penyusunan Dokumen Standar ISO, K3 & CSMS|${title}|g" "layanan-detail-${filename}.html"
    
    echo "Created: layanan-detail-${filename}.html"
  fi
done

echo "Done!"
