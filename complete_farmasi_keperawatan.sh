#!/bin/bash

# Update K3 Lab Farmasi - Process Steps & Targets
sed -i '' 's|Proses Konsultasi K3 Laboratorium Pendidikan Kedokteran|Proses Konsultasi K3 Laboratorium Pendidikan Farmasi|g' layanan-detail-k3-lab-pendidikan-farmasi.html

sed -i '' 's|Assessment K3 laboratorium medis, identifikasi bahaya biologis (patogen, spesimen) dan kimia (formalin, reagen), evaluasi biosafety level, pengendalian risiko praktikum mahasiswa|Assessment K3 laboratorium farmasi, identifikasi bahaya kimia (API, pelarut), bahaya biologis, evaluasi fume hood dan LAF, pengendalian risiko praktikum pembuatan sediaan|g' layanan-detail-k3-lab-pendidikan-farmasi.html

sed -i '' 's|Identifikasi bahaya spesifik lab kedokteran: praktikum anatomi, mikrobiologi, patologi, fisiologi, penilaian risiko eksposur biologis dan kimia, penentuan kontrol efektif|Identifikasi bahaya spesifik lab farmasi: formulasi, analisis, mikrobiologi farmasi, farmakognosi, penilaian risiko eksposur kimia dan sterilitas, penentuan kontrol efektif|g' layanan-detail-k3-lab-pendidikan-farmasi.html

sed -i '' 's|Protokol biosafety, SOP praktikum mahasiswa, JSA untuk handling spesimen, prosedur dekontaminasi, dan instruksi kerja aman untuk setiap aktivitas lab|Protokol pembuatan sediaan aman, SOP praktikum mahasiswa, JSA untuk handling bahan farmasi, prosedur LAF dan sterilisasi, instruksi kerja aman|g' layanan-detail-k3-lab-pendidikan-farmasi.html

sed -i '' 's|Rekomendasi APD medis: lab coat, medical gloves, face shield, N95 mask, implementasi biosafety cabinet, autoclave safety, sistem ventilasi laboratorium yang memadai|Rekomendasi APD farmasi: lab coat, chemical gloves, safety goggles, respirator, implementasi fume hood dan LAF, sistem ventilasi laboratorium|g' layanan-detail-k3-lab-pendidikan-farmasi.html

sed -i '' 's|Biosafety awareness, keselamatan praktikum mahasiswa, penggunaan APD medis, infection control, prosedur darurat laboratorium kedokteran|Pharmaceutical safety awareness, keselamatan praktikum mahasiswa, penggunaan APD farmasi, GMP basic, prosedur darurat lab farmasi|g' layanan-detail-k3-lab-pendidikan-farmasi.html

sed -i '' 's|Prosedur tanggap darurat biological spill, chemical exposure, needle stick injury, evakuasi laboratorium yang aman|Prosedur tanggap darurat chemical spill, API exposure, LAF contamination, evakuasi laboratorium yang aman|g' layanan-detail-k3-lab-pendidikan-farmasi.html

# Update Targets Farmasi
sed -i '' 's|<div class="iso-target-card"><h4>Fakultas Kedokteran</h4></div>|<div class="iso-target-card"><h4>Fakultas Farmasi</h4></div>|g' layanan-detail-k3-lab-pendidikan-farmasi.html
sed -i '' 's|<div class="iso-target-card"><h4>Lab Anatomi</h4></div>|<div class="iso-target-card"><h4>Lab Farmasetika</h4></div>|g' layanan-detail-k3-lab-pendidikan-farmasi.html
sed -i '' 's|<div class="iso-target-card"><h4>Lab Mikrobiologi Medis</h4></div>|<div class="iso-target-card"><h4>Lab Analisis Farmasi</h4></div>|g' layanan-detail-k3-lab-pendidikan-farmasi.html
sed -i '' 's|<div class="iso-target-card"><h4>Lab Patologi Klinik</h4></div>|<div class="iso-target-card"><h4>Lab Mikrobiologi Farmasi</h4></div>|g' layanan-detail-k3-lab-pendidikan-farmasi.html
sed -i '' 's|<div class="iso-target-card"><h4>Lab Fisiologi</h4></div>|<div class="iso-target-card"><h4>Lab Farmakognosi</h4></div>|g' layanan-detail-k3-lab-pendidikan-farmasi.html
sed -i '' 's|<div class="iso-target-card"><h4>Lab Biokimia Medis</h4></div>|<div class="iso-target-card"><h4>Lab Kimia Farmasi</h4></div>|g' layanan-detail-k3-lab-pendidikan-farmasi.html
sed -i '' 's|<div class="iso-target-card"><h4>Lab Farmakologi</h4></div>|<div class="iso-target-card"><h4>Lab Biologi Farmasi</h4></div>|g' layanan-detail-k3-lab-pendidikan-farmasi.html
sed -i '' 's|<div class="iso-target-card"><h4>Lab Skills Medis</h4></div>|<div class="iso-target-card"><h4>Lab Farmakologi</h4></div>|g' layanan-detail-k3-lab-pendidikan-farmasi.html
sed -i '' 's|<div class="iso-target-card"><h4>Universitas Kedokteran</h4></div>|<div class="iso-target-card"><h4>Universitas Farmasi</h4></div>|g' layanan-detail-k3-lab-pendidikan-farmasi.html

sed -i '' 's|Konsultasi K3 laboratorium pendidikan kedokteran membantu institusi pendidikan dalam menerapkan sistem keselamatan kerja yang spesifik untuk aktivitas praktikum medis, melindungi mahasiswa, dosen, dan petugas lab dari risiko biologis, kimia, dan needle stick injury|Konsultasi K3 laboratorium pendidikan farmasi membantu institusi pendidikan dalam menerapkan sistem keselamatan kerja yang spesifik untuk aktivitas praktikum farmasi, melindungi mahasiswa, dosen, dan petugas lab dari risiko kimia, biologis, dan pharmaceutical hazards|g' layanan-detail-k3-lab-pendidikan-farmasi.html

sed -i '' 's|<h2>Siap Meningkatkan <em>K3 Laboratorium Pendidikan Kedokteran</em> Anda?</h2>|<h2>Siap Meningkatkan <em>K3 Laboratorium Pendidikan Farmasi</em> Anda?</h2>|g' layanan-detail-k3-lab-pendidikan-farmasi.html

sed -i '' 's|Konsultasikan kebutuhan K3 laboratorium pendidikan kedokteran Anda bersama tim konsultan berpengalaman INOVASS. Kami siap membantu laboratorium Anda menerapkan sistem keselamatan yang komprehensif untuk praktikum medis yang aman dan berkualitas.|Konsultasikan kebutuhan K3 laboratorium pendidikan farmasi Anda bersama tim konsultan berpengalaman INOVASS. Kami siap membantu laboratorium Anda menerapkan sistem keselamatan yang komprehensif untuk praktikum farmasi yang aman dan berkualitas.|g' layanan-detail-k3-lab-pendidikan-farmasi.html

echo "✓ K3 Lab Farmasi completed"

# Update K3 Lab Keperawatan - Process Steps & Targets
sed -i '' 's|Proses Konsultasi K3 Laboratorium Pendidikan Kedokteran|Proses Konsultasi K3 Laboratorium Pendidikan Keperawatan|g' layanan-detail-k3-lab-pendidikan-keperawatan.html

sed -i '' 's|Assessment K3 laboratorium medis, identifikasi bahaya biologis (patogen, spesimen) dan kimia (formalin, reagen), evaluasi biosafety level, pengendalian risiko praktikum mahasiswa|Assessment K3 laboratorium keperawatan, identifikasi bahaya praktikum klinis, evaluasi infection control, pengendalian risiko needle stick injury|g' layanan-detail-k3-lab-pendidikan-keperawatan.html

sed -i '' 's|Identifikasi bahaya spesifik lab kedokteran: praktikum anatomi, mikrobiologi, patologi, fisiologi, penilaian risiko eksposur biologis dan kimia, penentuan kontrol efektif|Identifikasi bahaya spesifik lab keperawatan: injeksi, catheter, wound care, patient handling, penilaian risiko infeksi dan injury, penentuan kontrol efektif|g' layanan-detail-k3-lab-pendidikan-keperawatan.html

sed -i '' 's|Protokol biosafety, SOP praktikum mahasiswa, JSA untuk handling spesimen, prosedur dekontaminasi, dan instruksi kerja aman untuk setiap aktivitas lab|Protokol infection control, SOP praktikum keterampilan keperawatan, JSA untuk prosedur invasif, sharps management, instruksi kerja aman|g' layanan-detail-k3-lab-pendidikan-keperawatan.html

sed -i '' 's|Rekomendasi APD medis: lab coat, medical gloves, face shield, N95 mask, implementasi biosafety cabinet, autoclave safety, sistem ventilasi laboratorium yang memadai|Rekomendasi APD keperawatan: medical gloves, apron, face shield, safety eyewear, implementasi sharps container, sistem sterilisasi yang memadai|g' layanan-detail-k3-lab-pendidikan-keperawatan.html

sed -i '' 's|Biosafety awareness, keselamatan praktikum mahasiswa, penggunaan APD medis, infection control, prosedur darurat laboratorium kedokteran|Infection control training, keselamatan praktikum mahasiswa, penggunaan APD keperawatan, needle safety, prosedur darurat laboratorium|g' layanan-detail-k3-lab-pendidikan-keperawatan.html

sed -i '' 's|Prosedur tanggap darurat biological spill, chemical exposure, needle stick injury, evakuasi laboratorium yang aman|Prosedur tanggap darurat needle stick injury, blood exposure, patient fall simulation, evakuasi laboratorium yang aman|g' layanan-detail-k3-lab-pendidikan-keperawatan.html

# Update Targets Keperawatan
sed -i '' 's|<div class="iso-target-card"><h4>Fakultas Kedokteran</h4></div>|<div class="iso-target-card"><h4>Fakultas Keperawatan</h4></div>|g' layanan-detail-k3-lab-pendidikan-keperawatan.html
sed -i '' 's|<div class="iso-target-card"><h4>Lab Anatomi</h4></div>|<div class="iso-target-card"><h4>Lab Keterampilan Keperawatan Dasar</h4></div>|g' layanan-detail-k3-lab-pendidikan-keperawatan.html
sed -i '' 's|<div class="iso-target-card"><h4>Lab Mikrobiologi Medis</h4></div>|<div class="iso-target-card"><h4>Lab Keperawatan Medikal Bedah</h4></div>|g' layanan-detail-k3-lab-pendidikan-keperawatan.html
sed -i '' 's|<div class="iso-target-card"><h4>Lab Patologi Klinik</h4></div>|<div class="iso-target-card"><h4>Lab Keperawatan Anak</h4></div>|g' layanan-detail-k3-lab-pendidikan-keperawatan.html
sed -i '' 's|<div class="iso-target-card"><h4>Lab Fisiologi</h4></div>|<div class="iso-target-card"><h4>Lab Keperawatan Maternitas</h4></div>|g' layanan-detail-k3-lab-pendidikan-keperawatan.html
sed -i '' 's|<div class="iso-target-card"><h4>Lab Biokimia Medis</h4></div>|<div class="iso-target-card"><h4>Lab Keperawatan Gawat Darurat</h4></div>|g' layanan-detail-k3-lab-pendidikan-keperawatan.html
sed -i '' 's|<div class="iso-target-card"><h4>Lab Farmakologi</h4></div>|<div class="iso-target-card"><h4>Lab Keperawatan Komunitas</h4></div>|g' layanan-detail-k3-lab-pendidikan-keperawatan.html
sed -i '' 's|<div class="iso-target-card"><h4>Lab Skills Medis</h4></div>|<div class="iso-target-card"><h4>Lab Nursing Skills</h4></div>|g' layanan-detail-k3-lab-pendidikan-keperawatan.html
sed -i '' 's|<div class="iso-target-card"><h4>Universitas Kedokteran</h4></div>|<div class="iso-target-card"><h4>Universitas Keperawatan</h4></div>|g' layanan-detail-k3-lab-pendidikan-keperawatan.html

sed -i '' 's|Konsultasi K3 laboratorium pendidikan kedokteran membantu institusi pendidikan dalam menerapkan sistem keselamatan kerja yang spesifik untuk aktivitas praktikum medis, melindungi mahasiswa, dosen, dan petugas lab dari risiko biologis, kimia, dan needle stick injury|Konsultasi K3 laboratorium pendidikan keperawatan membantu institusi pendidikan dalam menerapkan sistem keselamatan kerja yang spesifik untuk aktivitas praktikum keperawatan, melindungi mahasiswa, dosen, dan petugas lab dari risiko infeksi, needle stick injury, dan clinical hazards|g' layanan-detail-k3-lab-pendidikan-keperawatan.html

sed -i '' 's|<h2>Siap Meningkatkan <em>K3 Laboratorium Pendidikan Kedokteran</em> Anda?</h2>|<h2>Siap Meningkatkan <em>K3 Laboratorium Pendidikan Keperawatan</em> Anda?</h2>|g' layanan-detail-k3-lab-pendidikan-keperawatan.html

sed -i '' 's|Konsultasikan kebutuhan K3 laboratorium pendidikan kedokteran Anda bersama tim konsultan berpengalaman INOVASS. Kami siap membantu laboratorium Anda menerapkan sistem keselamatan yang komprehensif untuk praktikum medis yang aman dan berkualitas.|Konsultasikan kebutuhan K3 laboratorium pendidikan keperawatan Anda bersama tim konsultan berpengalaman INOVASS. Kami siap membantu laboratorium Anda menerapkan sistem keselamatan yang komprehensif untuk praktikum keperawatan yang aman dan berkualitas.|g' layanan-detail-k3-lab-pendidikan-keperawatan.html

echo "✓ K3 Lab Keperawatan completed"

echo "Done! Both files customized successfully."
