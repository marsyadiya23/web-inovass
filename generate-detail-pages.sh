#!/bin/bash

# Script untuk generate halaman detail template untuk semua layanan

# Array layanan ISO
declare -a iso_services=(
  "Jasa Sertifikasi ISO Organisasi:jasa-sertifikasi-iso"
  "Jasa Persiapan Surveillance Audit Organisasi:jasa-surveillance-audit-organisasi"
  "Jasa Perawatan Sistem Sertifikasi Organisasi:jasa-perawatan-sistem-sertifikasi"
  "Jasa Audit Internal Sistem Manajemen Standar ISO Organisasi:jasa-audit-internal-iso"
  "Jasa Persiapan Surveillance Audit Akreditasi Laboratorium:jasa-surveillance-audit-lab"
  "Jasa Persiapan Re-Sertifikasi Audit Akreditasi Laboratorium:jasa-resertifikasi-audit-lab"
)

# Array layanan Akreditasi
declare -a akreditasi_services=(
  "Konsultasi Akreditasi Lembaga Inspeksi Standar ISO 17020:2012:konsultasi-akreditasi-inspeksi"
  "Konsultasi Persiapan Surveillance Audit Akreditasi Lembaga Inspeksi:konsultasi-surveillance-inspeksi"
  "Konsultasi Persiapan Re-Sertifikasi Audit Akreditasi Lembaga Inspeksi:konsultasi-resertifikasi-inspeksi"
  "Konsultasi Akreditasi Lembaga Sertifikasi Personel (LSP) Standar ISO 17024:2012:konsultasi-akreditasi-lsp"
  "Konsultasi Persiapan Surveillance Audit Akreditasi LSP Standar ISO 17024:2012:konsultasi-surveillance-lsp"
  "Konsultasi Persiapan Re-Sertifikasi Audit Akreditasi LSP Standar ISO 17024:2012:konsultasi-resertifikasi-lsp"
  "Konsultasi Akreditasi Lembaga Sertifikasi Produk (LSPro) Standar ISO 17065:2012:konsultasi-akreditasi-lspro"
  "Konsultasi Persiapan Surveillance Audit Akreditasi LSPro Standar ISO 17065:2012:konsultasi-surveillance-lspro"
  "Konsultasi Persiapan Re-Sertifikasi Audit Akreditasi LSPro Standar ISO 17065:2012:konsultasi-resertifikasi-lspro"
)

# Array layanan Pelatihan
declare -a pelatihan_services=(
  "Public Training:public-training"
  "In House Training:in-house-training"
  "Executive Training:executive-training"
  "Private Training:private-training"
  "Pelatihan Auditor Internal ISO:pelatihan-auditor-internal-iso"
  "Pelatihan Implementasi ISO:pelatihan-implementasi-iso"
  "Pelatihan K3 & Lingkungan:pelatihan-k3-lingkungan"
)

# Array layanan Sertifikasi Personel
declare -a sertifikasi_services=(
  "Sertifikasi Auditor Internal QMS:sertifikasi-auditor-qms"
  "Sertifikasi Auditor Internal EMS:sertifikasi-auditor-ems"
  "Sertifikasi Auditor Internal OHSMS:sertifikasi-auditor-ohsms"
  "Sertifikasi Auditor Internal ISMS:sertifikasi-auditor-isms"
  "Sertifikasi Manager Representative ISO:sertifikasi-manager-representative"
  "Sertifikasi Ahli K3 Umum:sertifikasi-ahli-k3-umum"
)

# Function untuk create detail page
create_detail_page() {
  local title="$1"
  local filename="$2"
  local category="$3"
  
  cat > "layanan-detail-${filename}.html" << 'HTMLEOF'
<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>TITLE_PLACEHOLDER — INOVASS</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="style.css" />
  <link rel="stylesheet" href="pages.css" />
</head>
<body>

  <nav class="navbar">
    <a href="index.html" class="nav-logo">
      <img src="image/logo.png" alt="INOVASS Logo" class="nav-logo-img" />
    </a>
    <div class="nav-menu">
      <a href="index.html" class="nav-link">Beranda</a>
      <a href="layanan-iso.html" class="nav-link active">Layanan</a>
      <a href="produk.html" class="nav-link">Produk</a>
      <a href="tentang.html" class="nav-link">Tentang Kami</a>
    </div>
    <div class="nav-right">
      <a href="kontak.html" class="nav-cta">Hubungi Kami</a>
      <button class="nav-hamburger" aria-label="Menu" id="hamburgerBtn">
        <span></span><span></span><span></span>
      </button>
    </div>
  </nav>
  <div class="mobile-menu" id="mobileMenu">
    <a href="index.html" class="mobile-link">Beranda</a>
    <a href="layanan-iso.html" class="mobile-link active">Layanan</a>
    <a href="produk.html" class="mobile-link">Produk</a>
    <a href="tentang.html" class="mobile-link">Tentang Kami</a>
    <a href="kontak.html" class="mobile-cta">Hubungi Kami</a>
  </div>

  <!-- DETAIL HERO -->
  <section class="detail-hero">
    <img src="image/layanan kami.jpeg" alt="TITLE_PLACEHOLDER" class="detail-hero-bg" />
    <div class="detail-hero-overlay"></div>
    <div class="detail-hero-content">
      <nav class="detail-breadcrumb" aria-label="Breadcrumb">
        <a href="index.html">Beranda</a>
        <span>›</span>
        <a href="CATEGORY_LINK_PLACEHOLDER">Layanan</a>
        <span>›</span>
        <span>TITLE_PLACEHOLDER</span>
      </nav>
      <h1 class="detail-hero-title">TITLE_PLACEHOLDER</h1>
      <p class="detail-hero-subtitle">CATEGORY_PLACEHOLDER</p>
      <p class="detail-hero-desc">Konten detail untuk layanan ini akan segera hadir. Hubungi kami untuk informasi lebih lanjut mengenai layanan TITLE_PLACEHOLDER.</p>
      <a href="kontak.html" class="detail-hero-cta">Hubungi Kami</a>
    </div>
  </section>

  <!-- CONTENT PLACEHOLDER -->
  <section class="detail-features">
    <div class="detail-features-container">
      <div style="text-align: center; padding: 4rem 2rem;">
        <h2 style="font-size: 2rem; color: #1e3a8a; margin-bottom: 1rem;">Konten Sedang Dalam Pengembangan</h2>
        <p style="font-size: 1.1rem; color: #6b7280; margin-bottom: 2rem;">Informasi lengkap mengenai layanan ini akan segera ditambahkan.</p>
        <a href="kontak.html" style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 1rem 2rem; background: #00c278; color: white; border-radius: 50px; text-decoration: none; font-weight: 600;">
          Hubungi Kami Untuk Informasi
        </a>
      </div>
    </div>
  </section>

  <!-- CTA SECTION -->
  <section class="page-cta reveal">
    <h2>Siap memulai<br /><em>proyek Anda?</em></h2>
    <p>Hubungi kami untuk konsultasi gratis dan penawaran terbaik untuk organisasi Anda.</p>
    <a href="kontak.html" class="btn-outline">Hubungi Kami Sekarang</a>
  </section>

  <!-- FOOTER -->
  <footer class="footer">
    <div class="footer-top">
      <div class="footer-brand reveal-left">
        <a href="index.html" class="footer-logo-link">
          <img src="image/logo.png" alt="INOVASS Logo" class="nav-logo-img" />
        </a>
        <p class="footer-tagline">Inovasi untuk Masa Depan</p>
        <p class="footer-desc">Perusahaan konsultan ISO dan pengembangan solusi digital yang membantu organisasi meningkatkan mutu, efisiensi, dan daya saing.</p>
        <div class="footer-socials" style="margin-top:1.5rem;">
          <a href="#">INSTAGRAM</a>
          <a href="#">LINKEDIN</a>
          <a href="#">YOUTUBE</a>
        </div>
      </div>
      <div class="footer-links reveal-right">
        <div class="footer-col">
          <h4>Office</h4>
          <ul>
            <li>Jl. Danau Melahayu No. 23A</li>
            <li>Pesona Telaga Cibinong</li>
            <li>Kel. Harapan Jaya, Kec. Cibinong,</li>
            <li>Kab. Bogor</li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Contact Us</h4>
          <ul>
            <li><a href="https://wa.me/6281311173707">+62-813-1117-3707</a></li>
            <li><a href="mailto:inovass.adm@gmail.com">inovass.adm@gmail.com</a></li>
          </ul>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <p>© 2026 INOVASS. Hak cipta dilindungi undang-undang.</p>
      <div class="footer-bottom-links">
        <a href="#">Kebijakan Privasi</a>
        <a href="#">Syarat &amp; Ketentuan</a>
      </div>
    </div>
  </footer>

  <script src="script.js"></script>
  <script>
    const hamburgerBtn = document.getElementById('hamburgerBtn');
    const mobileMenu = document.getElementById('mobileMenu');
    hamburgerBtn.addEventListener('click', () => {
      hamburgerBtn.classList.toggle('active');
      mobileMenu.classList.toggle('open');
    });
    console.log('✅ Detail page loaded');
  </script>
</body>
</html>
HTMLEOF

  # Replace placeholders
  sed -i '' "s/TITLE_PLACEHOLDER/$title/g" "layanan-detail-${filename}.html"
  sed -i '' "s/CATEGORY_PLACEHOLDER/$category/g" "layanan-detail-${filename}.html"
  sed -i '' "s|CATEGORY_LINK_PLACEHOLDER|layanan-iso.html|g" "layanan-detail-${filename}.html"
  
  echo "Created: layanan-detail-${filename}.html"
}

# Generate pages untuk ISO
for service in "${iso_services[@]}"; do
  IFS=':' read -r title filename <<< "$service"
  create_detail_page "$title" "$filename" "Konsultasi & Sertifikasi ISO"
done

# Generate pages untuk Akreditasi
for service in "${akreditasi_services[@]}"; do
  IFS=':' read -r title filename <<< "$service"
  create_detail_page "$title" "$filename" "Konsultasi Akreditasi"
done

# Generate pages untuk Pelatihan
for service in "${pelatihan_services[@]}"; do
  IFS=':' read -r title filename <<< "$service"
  create_detail_page "$title" "$filename" "Pelatihan Profesional"
done

# Generate pages untuk Sertifikasi
for service in "${sertifikasi_services[@]}"; do
  IFS=':' read -r title filename <<< "$service"
  create_detail_page "$title" "$filename" "Sertifikasi Personel"
done

echo ""
echo "✅ All detail pages created successfully!"
echo "Total files created: $((${#iso_services[@]} + ${#akreditasi_services[@]} + ${#pelatihan_services[@]} + ${#sertifikasi_services[@]}))"
