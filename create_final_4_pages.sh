#!/bin/bash

TEMPLATE="layanan-detail-k3-lab-pendidikan-kedokteran.html"

echo "Creating final 4 K3 Lab pages..."

# Create 4 pages
cp "$TEMPLATE" "layanan-detail-k3-lab-pendidikan-gizi.html"
cp "$TEMPLATE" "layanan-detail-k3-lab-pendidikan-kesmas.html"
cp "$TEMPLATE" "layanan-detail-k3-lab-pendidikan-biomedis.html"
cp "$TEMPLATE" "layanan-detail-k3-lab-kesehatan-lainnya.html"

echo "✓ 4 files created:"
echo "  1. layanan-detail-k3-lab-pendidikan-gizi.html"
echo "  2. layanan-detail-k3-lab-pendidikan-kesmas.html"
echo "  3. layanan-detail-k3-lab-pendidikan-biomedis.html"
echo "  4. layanan-detail-k3-lab-kesehatan-lainnya.html"
