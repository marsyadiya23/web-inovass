#!/bin/bash

# Base template file
TEMPLATE="layanan-detail-k3-lab-pendidikan-kedokteran.html"

# Function to create and customize page
create_page() {
    local filename="$1"
    local page_title="$2"
    local breadcrumb_text="$3"
    local highlight1="$4"
    local highlight2="$5"
    local highlight3="$6"
    
    echo "Creating $filename..."
    cp "$TEMPLATE" "$filename"
}

# Create 5 pages
create_page "layanan-detail-k3-lab-pendidikan-kebidanan.html" \
    "Jasa Konsultasi K3 Laboratorium Pendidikan Kebidanan" \
    "K3 Lab Pendidikan Kebidanan" \
    "Maternal<br>Safety" \
    "Zero Lab<br>Incident" \
    "Student<br>Protection"

create_page "layanan-detail-k3-lab-rumah-sakit.html" \
    "Jasa Konsultasi K3 Laboratorium Rumah Sakit" \
    "K3 Lab Rumah Sakit" \
    "Hospital Lab<br>Safety" \
    "Zero<br>Incident" \
    "Quality<br>Assurance"

create_page "layanan-detail-k3-lab-klinik.html" \
    "Jasa Konsultasi K3 Laboratorium Klinik" \
    "K3 Lab Klinik" \
    "Clinical Lab<br>Safety" \
    "Zero<br>Incident" \
    "Quality<br>Standards"

create_page "layanan-detail-k3-lab-puskesmas.html" \
    "Jasa Konsultasi K3 Laboratorium Puskesmas" \
    "K3 Lab Puskesmas" \
    "Primary Care<br>Safety" \
    "Zero Lab<br>Incident" \
    "Community<br>Health"

create_page "layanan-detail-k3-lab-analis-kesehatan.html" \
    "Jasa Konsultasi K3 Laboratorium Pendidikan Analis Kesehatan / Teknologi Laboratorium Medik (TLM)" \
    "K3 Lab Pendidikan Analis Kesehatan / TLM" \
    "Lab Analysis<br>Excellence" \
    "Zero Lab<br>Incident" \
    "Student<br>Protection"

echo "All 5 files created successfully!"
echo "Files created:"
echo "  1. layanan-detail-k3-lab-pendidikan-kebidanan.html"
echo "  2. layanan-detail-k3-lab-rumah-sakit.html"
echo "  3. layanan-detail-k3-lab-klinik.html"
echo "  4. layanan-detail-k3-lab-puskesmas.html"
echo "  5. layanan-detail-k3-lab-analis-kesehatan.html"
