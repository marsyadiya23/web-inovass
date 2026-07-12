#!/bin/bash

# Update links di layanan-iso.html
sed -i '' 's|<h3>Jasa Sertifikasi ISO Organisasi</h3>.*<a href="kontak.html"|<h3>Jasa Sertifikasi ISO Organisasi</h3>\n            <p>Pendampingan lengkap proses sertifikasi ISO untuk berbagai standar manajemen</p>\n            <a href="layanan-detail-jasa-sertifikasi-iso.html"|g' layanan-iso.html

sed -i '' 's|<h3>Jasa Persiapan Surveillance Audit Organisasi</h3>.*<a href="kontak.html"|<h3>Jasa Persiapan Surveillance Audit Organisasi</h3>\n            <p>Persiapan dan pendampingan audit surveillance untuk menjaga sertifikasi ISO</p>\n            <a href="layanan-detail-jasa-surveillance-audit-organisasi.html"|g' layanan-iso.html

sed -i '' 's|<h3>Jasa Perawatan Sistem Sertifikasi Organisasi</h3>.*<a href="kontak.html"|<h3>Jasa Perawatan Sistem Sertifikasi Organisasi</h3>\n            <p>Pemeliharaan dan peningkatan berkelanjutan sistem manajemen yang tersertifikasi</p>\n            <a href="layanan-detail-jasa-perawatan-sistem-sertifikasi.html"|g' layanan-iso.html

sed -i '' 's|<h3>Jasa Audit Internal Sistem Manajemen Standar ISO Organisasi</h3>.*<a href="kontak.html"|<h3>Jasa Audit Internal Sistem Manajemen Standar ISO Organisasi</h3>\n            <p>Audit internal komprehensif untuk memastikan kepatuhan terhadap standar ISO</p>\n            <a href="layanan-detail-jasa-audit-internal-iso.html"|g' layanan-iso.html

sed -i '' 's|<h3>Jasa Persiapan Surveillance Audit Akreditasi Laboratorium</h3>.*<a href="kontak.html"|<h3>Jasa Persiapan Surveillance Audit Akreditasi Laboratorium</h3>\n            <p>Persiapan audit surveillance untuk laboratorium terakreditasi</p>\n            <a href="layanan-detail-jasa-surveillance-audit-lab.html"|g' layanan-iso.html

sed -i '' 's|<h3>Jasa Persiapan Re-Sertifikasi Audit Akreditasi Laboratorium</h3>.*<a href="kontak.html"|<h3>Jasa Persiapan Re-Sertifikasi Audit Akreditasi Laboratorium</h3>\n            <p>Pendampingan proses perpanjangan dan re-sertifikasi akreditasi laboratorium</p>\n            <a href="layanan-detail-jasa-resertifikasi-audit-lab.html"|g' layanan-iso.html

echo "✅ layanan-iso.html updated"
