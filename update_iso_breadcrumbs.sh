#!/bin/bash

# Update breadcrumb untuk semua file ISO
for file in layanan-detail-iso-*.html; do
    if [ -f "$file" ]; then
        echo "Updating: $file"
        sed -i '' 's|Jasa Konsultasi Sertifikasi ISO</a>|Jasa Konsultasi Sertifikasi Standar ISO/IEC/SNI</a>|g' "$file"
    fi
done

echo "Done! All ISO breadcrumbs updated."
