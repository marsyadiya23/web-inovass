#!/bin/bash

FILE="layanan-detail-k3-lab-pendidikan-kebidanan.html"

# Update Process Section Title
sed -i '' 's/<!-- PROSES KONSULTASI K3 LAB PENDIDIKAN KEDOKTERAN -->/<!-- PROSES KONSULTASI K3 LAB PENDIDIKAN KEBIDANAN -->/g' "$FILE"
sed -i '' 's/<h2 class="iso-process-title">Proses Konsultasi K3 Laboratorium Pendidikan Kedokteran<\/h2>/<h2 class="iso-process-title">Proses Konsultasi K3 Laboratorium Pendidikan Kebidanan<\/h2>/g' "$FILE"

# Update Target Section Title  
sed -i '' 's/<h2 class="iso-target-section-title" style="margin-bottom: 3rem;">Siapa yang Membutuhkan Konsultasi K3 Laboratorium Pendidikan Kedokteran?<\/h2>/<h2 class="iso-target-section-title" style="margin-bottom: 3rem;">Siapa yang Membutuhkan Konsultasi K3 Laboratorium Pendidikan Kebidanan?<\/h2>/g' "$FILE"

# Update CTA Section Title
sed -i '' 's/Siap Meningkatkan <em>K3 Laboratorium Pendidikan Kedokteran<\/em> Anda?/Siap Meningkatkan <em>K3 Laboratorium Pendidikan Kebidanan<\/em> Anda?/g' "$FILE"
sed -i '' 's/Konsultasikan kebutuhan K3 laboratorium pendidikan kedokteran Anda/Konsultasikan kebutuhan K3 laboratorium pendidikan kebidanan Anda/g' "$FILE"
sed -i '' 's/praktikum kedokteran yang aman dan berkualitas/praktikum kebidanan yang aman dan berkualitas/g' "$FILE"

echo "Kebidanan page process and titles updated!"
