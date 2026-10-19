> **Superseded** oleh [`PRD.md`](../PRD.md) (17 Oktober 2026, perubahan scope: CMS untuk katalog & jadwal pelatihan). Dokumen ini disimpan sebagai referensi.

# PRD — INOVASS CMS

| | |
|---|---|
| Produk | INOVASS CMS: sistem manajemen konten + situs publik pengganti inovass.com statis |
| Versi dokumen | 1.1 — 17 Oktober 2026 (revisi hasil review) |
| Pemilik | INOVASS (stakeholder bisnis) · Tim developer (eksekusi dengan Claude Code) |
| Sumber | Crawl 97 halaman `https://inovass.com/` + 6 halaman level-4 yang di-fetch live (5 program pelatihan, 1 sub-layanan akreditasi) + ±20 URL leaf yang hanya dicek status HTTP-nya; catatan inventaris per klaster (home, static, sertifikasi-hub, iso-detail, penyusunan-dokumen, akreditasi, pelatihan, laboratorium). PRD ini **menggantikan sepenuhnya** draft Content Model, Editor UX, dan Arsitektur yang menjadi bahan awalnya. |
| Konvensi | Fakta yang tidak ada di sumber ditandai **(asumsi)**. Konflik antar-sumber direkonsiliasi di tempat (§4.2 peran, §6.6 URL, US-06 masa berlaku preview). Semua angka jumlah halaman di §2, §10, §15 adalah **estimasi dari crawl parsial**; `manifest.json` crawler Fase 0 adalah satu-satunya angka yang mengikat untuk import dan tes. |

---

## 1. Ringkasan Eksekutif

### 1.1 Tujuan

Mengganti situs company profile inovass.com (97 file HTML yang ter-crawl + ±440 halaman leaf yang hidup di server tetapi belum ter-crawl) dengan satu aplikasi CMS yang:

1. Mempertahankan **seluruh URL lama 1:1** (termasuk suffix `.html` dan struktur folder `/layanan/{kategori}/`) sehingga tidak ada tautan atau indeks Google yang putus.
2. Menjadikan teks yang kini di-copy-paste ratusan kali (footer, nomor WhatsApp, CTA, 6 langkah proses, blok "Konten Segera Hadir") sebagai **satu sumber kebenaran**.
3. Memungkinkan staf marketing non-teknis membuat halaman layanan/standar ISO baru melalui **formulir terstruktur**, bukan HTML.
4. **Menyimpan setiap lead** dari form kontak (saat ini hilang jika pengunjung menutup tab WhatsApp).
5. Memperbaiki fondasi SEO yang nyaris nol (tidak ada meta description, sitemap, robots, canonical, favicon; `lang="en"`).

### 1.2 Masalah situs saat ini

| Area | Kondisi |
|---|---|
| Pemeliharaan | Mengubah satu nomor telepon = mengedit 98+ file. Menambah satu standar ISO = menyalin ±1.000 baris CSS inline dan mengganti teks di 30+ titik |
| Konsistensi | Dua nomor WhatsApp berbeda (footer `6281311173707`, form `6281387095353`); CTA "ISO 9001" tersalin ke 10+ halaman standar lain; "ISO 14001:2026"; typo "Person"; urutan langkah proses 1,2,3,6,5,4 |
| Lead | Form kontak tanpa `action`/`name`; hanya membuka `wa.me`. Tidak ada rekaman, tidak ada follow-up |
| SEO | 0 meta description di 98 halaman; 7 hub berjudul generik "Layanan — INOVASS"; kartu navigasi berupa `div onclick` (tidak ter-crawl); tidak ada sitemap/robots/canonical/OG/favicon |
| Konten | 19–20 halaman stub "Konten Segera Hadir"; 3 kartu berita dummy tanpa halaman; testimoni terindikasi fiktif; 5 hub memuat 21+ kartu duplikat tersembunyi (`display:none`); `pranata-lab-mipa.html` terpotong tanpa footer |
| Aksesibilitas | Label form `display:none`, kartu tidak bisa diakses keyboard, iframe peta tanpa `title`, kontras hijau di atas putih gagal AA |

### 1.3 Hasil yang diharapkan

- **MVP (≈11 person-week, lihat §12)**: situs baru live di URL lama, semua ±540 URL mengembalikan 200 atau 301, editor bisa mengelola semua konten, lead tersimpan + notifikasi email, Lighthouse SEO 100 / Performance ≥ 90.
- **v1 (+≈4 pw)**: Berita & Insight, mega menu, section builder beranda, WhatsApp float + notifikasi WA API, riwayat versi, pelacakan pemakaian media, link berbagi preview.
- **v2 (+≈3–4 pw, opsional)**: jadwal & pendaftaran pelatihan, halaman detail produk, brosur PDF.

---

## 2. Analisis Situs Saat Ini (inovass.com)

### 2.1 Struktur 97 halaman ter-crawl + 6 sampel live (per kelompok)

| Kelompok | Folder | Jumlah | Template | Lengkap | Stub |
|---|---|---:|---|---:|---:|
| Beranda | `/index.html` | 1 | `home` | 1 | 0 |
| Statis | `/tentang.html`, `/kontak.html`, `/produk.html` | 3 | `about`, `contact`, `product-list` | 3 | 0 |
| Hub Sertifikasi Organisasi | `/layanan/sertifikasi-organisasi/index.html` | 1 | `layanan-hub` | 1 | 0 |
| Layanan L3 Sertifikasi | `/layanan/sertifikasi-organisasi/*.html` | 11 | `service-list` | 11 | 0 |
| Stub di folder Sertifikasi | `jasa-surveillance-audit-lab`, `jasa-resertifikasi-audit-lab` | 2 | `coming-soon-stub` | 0 | 2 |
| Detail ISO (L4) | `/layanan/sertifikasi-organisasi/iso-*.html`, `ims`, `iso-lainnya` | 19 | `iso-detail` | 19 | 0 |
| Penyusunan Dokumen (L4) | `/layanan/sertifikasi-organisasi/penyusunan-dokumen-*.html` | 19 | `iso-detail` (varian) | 19 | 0 |
| Hub Akreditasi + L3 | `/layanan/akreditasi-organisasi/` | 1 + 7 | `layanan-hub`, `akreditasi-detail` | 8 | 0 |
| Hub Pelatihan Sertifikasi + L3 | `/layanan/pelatihan-sertifikasi/` | 1 + 3 + 4 | `layanan-hub`, `training-format`, `coming-soon-stub` | 4 | 4 |
| Hub Pelatihan Akreditasi + L3 | `/layanan/pelatihan-akreditasi/` | 1 + 3 + 5 | `layanan-hub`, `training-format`, `coming-soon-stub` | 4 | 5 |
| Hub Pranata Lab + L3 | `/layanan/pranata-laboratorium/` | 1 + 4 + 3 | `layanan-hub`, `service-program-list`, `coming-soon-stub` | 5 | 3 |
| Hub Lab Mineral + L3 | `/layanan/lab-mineral/` | 1 + 2 | `layanan-hub`, `coming-soon-stub` | 1 | 2 |
| Hub Lab Teknik Sipil + L3 | `/layanan/lab-teknik-sipil/` | 1 + 4 | `layanan-hub`, `coming-soon-stub` | 1 | 4 |
| **Subtotal ter-crawl** | | **97** | | **77** | **20** |
| Sampel L4 akreditasi (fetch live) | `/layanan/akreditasi-organisasi/akreditasi-iso-17025.html` | 1 | `sub-service-detail` | 1 | 0 |
| Sampel L4 pelatihan (fetch live) | `/layanan/pelatihan-sertifikasi/{public,inhouse,executive}-training-iso-9001.html`, `public-training-ims.html`; `/layanan/pelatihan-akreditasi/public-training-akreditasi-17025.html` | 5 | `training-program-detail` | 5 | 0 |
| **Total tersimpan** | | **103** | | **83** | **20** |

Catatan: sumber menyebut "19 stub" tetapi mengenumerasi 20 (lihat §15); angka pasti ditetapkan oleh crawler Fase 0.

**Halaman live yang tidak ter-crawl** (hanya terjangkau via `div onclick`, semua HTTP 200 saat disampel): ±139 leaf sertifikasi (dari ±177 slug leaf unik di bawah hub sertifikasi, 38 sudah ter-crawl sebagai `iso-*`/`penyusunan-dokumen-*`; sisanya audit internal, surveillance, pemeliharaan, K3, CSMS, K3 lab, QHSE), ±118 sub-layanan akreditasi (1 disampel), 87 program pelatihan (18 ISO × 3 format + 11 akreditasi × 3 format; 5 disampel), 98 program pranata lab (60 MIPA, 12 Sosial, 19 Kedokteran, 7 Kesehatan). **Estimasi total situs: ±540 URL** (97 + ±442); hanya `manifest.json` Fase 0 yang mengikat.

### 2.2 Template yang ditemukan

| Template lama | Halaman | Kerangka |
|---|---:|---|
| `home` | 1 | hero → tentang singkat (4 statistik, 4 value card) → marquee 44 logo → bento 4 layanan → 2 produk → 6 bidang pelatihan → 4 keunggulan → 4 langkah proses → 3 berita → testimoni → FAQ (6) → CTA band |
| `about` / `contact` / `product-list` | 3 | hero gambar + breadcrumb → isi spesifik → CTA band (kontak tanpa CTA band) |
| `layanan-hub` | 7 | hero bersama "Layanan Kami" → 7 tab kategori → h2 + intro + grid kartu (ikon, judul, blurb, "Lihat Detail") → CTA band varian hub. 5 hub memuat 2–3 blok `display:none` duplikat |
| `service-list` / `akreditasi-detail` / `service-program-list` | 11 + 7 + 4 | header gelap (breadcrumb + h1) → intro 2 kolom → h3 + deskripsi + grid kartu anak (4–60) dengan aksen navy/green/yellow → CTA band |
| `training-format` | 6 | sama seperti di atas + section "Keunggulan" 6 kartu ikon |
| `iso-detail` (sertifikasi & penyusunan dokumen; juga ±139 leaf lain + ±118 sub-akreditasi) | 38 (+±257 live) | highlight 3 → pengertian → manfaat 6 → CTA biru inline → proses 6 langkah (badge 1,2,3,6,5,4) → target 9 → CTA band. **Varian sub-akreditasi** (sampel `akreditasi-iso-17025`): target 6 + paragraf "Cocok untuk", CTA inline "Siap Meraih Akreditasi Laboratorium?", **tanpa CTA band bawah** (footer langsung). ±139 leaf sertifikasi lain hanya dicek kerangkanya (header → `iso-content-section` → `page-cta`), jumlah item per section **belum diinventaris** |
| `training-program` / `training-program-detail` | 5 sampel (+180 live) | highlight 3 → tentang → manfaat 6 → CTA biru → materi 6 (badge 1,2,3,6,5,4) → peserta 6 + "Cocok untuk" → CTA band |
| `coming-soon-stub` | 20 | header gelap → blok "Konten Segera Hadir" (ikon jam, 3 chip, 2 tombol), tanpa CTA band |

### 2.3 Komponen bersama

| Komponen | Isi saat ini | Catatan |
|---|---|---|
| Navbar | Logo; Beranda, Layanan (→ hub sertifikasi), Produk, Tentang Kami; CTA "Hubungi Kami"; hamburger | "Layanan" adalah `<a>` polos ke hub sertifikasi di **semua** halaman (0 dari 97 halaman memuat `.nav-mega-menu`/`.nav-dropdown-btn`). Yang ada hanya CSS mati (33 aturan `mega` di `style.css`) dan JS inline mati di `index.html` yang merujuk `#navLayananBtn`/`#navMegaMenu`. **Mega menu = fitur baru (v1)**. Tidak ada landing `/layanan/` |
| Tab kategori layanan | 7 tab urut: Sertifikasi Organisasi, Akreditasi Organisasi, Pelatihan Sertifikasi, Pelatihan Akreditasi, Pranata Laboratorium, Manajemen Lab Mineral, Manajemen Lab Teknik Sipil | Hanya di hub |
| Hero halaman | gambar + overlay + breadcrumb + h1 dua baris (`<em>` hijau) + deskripsi | Hero hub identik di 7 hub (`layanan kami.jpeg`) |
| Header detail | band gelap, breadcrumb "Beranda › Layanan › {judul}" (level kategori hilang), h1 | Target crumb "Layanan" tidak konsisten (hub sendiri vs hub sertifikasi) |
| CTA band | "Siap memulai proyek Anda?" + 3 varian teks: hub "Ceritakan kebutuhan Anda…", detail/L3 **dan 87 program format×standar** "…penawaran terbaik untuk organisasi Anda", 98 program pranata lab "…untuk kebutuhan pelatihan Anda" + "Hubungi Kami Sekarang"; leaf ISO: "Siap Meningkatkan {sistem} Organisasi Anda?"; sub-layanan akreditasi: **tidak ada CTA band** | Teks leaf tersalin "ISO 9001" di 10+ halaman |
| CTA inline biru | "Ahli Kami Selalu Siap Membantu Anda" / "Konsultasikan Gratis"; varian pelatihan & pranata lab | |
| Blok Coming Soon | h2, deskripsi, 3 chip (Konsultan Berpengalaman, Harga Kompetitif, Proses Cepat & Efisien), 2 tombol | Byte-identik di 20 stub |
| Footer | logo, tagline "Inovasi untuk Masa Depan", deskripsi, 3 sosial (`#`), kolom "Office" 4 baris alamat Cibinong, "Contact Us" telepon/WA/email, "© 2026", 2 link legal (`#`) | Heading Inggris, tahun hard-coded |
| WhatsApp float | **tidak ada** di halaman mana pun | Fitur baru |

### 2.4 Temuan masalah (ringkas; daftar lengkap per halaman di §15, checklist perbaikan di §10.5)

- **Broken/placeholder link**: 5× `href="#"` di footer setiap halaman; "Baca Selengkapnya" berita adalah `<span>`; 3 dari 4 kartu bento tanpa link; "Lihat Semua Pelatihan" → hub sertifikasi; kartu tersembunyi "Lihat Detail" → `kontak.html`.
- **Stub**: 20 halaman "Konten Segera Hadir"; 11 di antaranya hanya terjangkau dari blok `display:none` (2 di folder sertifikasi, 4 pelatihan-sertifikasi, 5 pelatihan-akreditasi), 9 dilink dari kartu hub yang terlihat.
- **Duplikasi**: 44 logo ×2 dan testimoni 5+2 diduplikasi manual untuk marquee; 21+ kartu di blok tersembunyi hub; ±1.000 baris CSS inline per halaman ISO; intro hub Pelatihan Akreditasi disalin verbatim dari Pelatihan Sertifikasi; kartu 6 `akreditasi-lab-medis` duplikat kartu 1.
- **Form**: satu-satunya form (`kontak.html`) tanpa backend, label `display:none`, nomor tujuan berbeda dari footer.
- **Salah kategori**: `jasa-surveillance-audit-lab`, `jasa-resertifikasi-audit-lab` (akreditasi di folder sertifikasi); 5 `sertifikasi-auditor-*`/`sertifikasi-ahli-k3-umum` (sertifikasi personel di folder pelatihan-akreditasi); `lab-prodi-kedokteran` (bukan pelatihan).
- **Inkonsistensi penamaan standar**: "ISO/IEC/SNI 17020" vs "SNI ISO/IEC 17020:2012" vs "ISO/IEC 17020"; "ISO ISO 19100"; "ISO/IEC ISO 25010"; "ISO/IEC/SNI 15189" (15189 bukan IEC); slug `inhouse-training-39001` tanpa `iso-`.
- **Copy**: hero beranda berbahasa Inggris dengan tata bahasa salah; "Cocok untuk" campur Indonesia/Inggris di 87 program; 19 halaman Penyusunan Dokumen memakai judul langkah dari template sertifikasi.

### 2.5 Tech stack saat ini

HTML statis, `assets/css/style.css` (3.442 baris) + `assets/css/pages.css` (3.730 baris) + CSS inline per halaman, `assets/js/script.js` (vanilla: hamburger, reveal saat scroll, drag/autoscroll `testimonials-track`, handler newsletter stub, pemusatan nav-tab; **counter statistik dan JS mega menu mati ada inline di `index.html`**, bukan di `script.js`), Google Fonts (Plus Jakarta Sans, Inter), ikon SVG inline gaya Heroicons Outline. Hosting: **LiteSpeed Web Server** (halaman 404 standar LiteSpeed) → hampir pasti shared hosting cPanel lokal; PHP tersedia, Node tidak **(asumsi)**. Tidak ada `sitemap.xml`; `robots.txt` 404.

### 2.6 Desain (font/warna)

| Token | Nilai | Pemakaian |
|---|---|---|
| Font heading | Plus Jakarta Sans 700 | h1 `clamp(2rem,4.5vw,4rem)`, h2 `clamp(2rem,3vw,2.8rem)` |
| Font body | Inter 300/400 | body 0.88rem, eyebrow 0.62–0.65rem uppercase ls 0.15–0.2em |
| Navy | `#1e3a8a` | heading di section terang, teks tombol, ikon |
| Navy gelap | `#0a1628` (footer, section gelap), gradien `#0a1628 → #051a0f` | |
| Hijau | `#00c278`, hijau terang `#00e0a0`, `#00b07a` | eyebrow, `<em>` aksen, nav CTA, nomor langkah |
| Emas | `#f0b800`, `#ffd84d` | tombol hero & outline |
| Biru CTA inline | `#2563eb` / `#3b82f6` | |
| Netral | cream `#e8f0ec`, bg terang `#f7f9f8`, teks `#475569`/`#64748b`, border `#cbd5e1` | |
| Bentuk | kartu radius 16–20px, tombol pill, navbar 70px → pill putih blur setelah scroll 40px | |
| Breakpoint | 1100px, 900px (hamburger), 580px | |
| Animasi | heroZoom 8s, fadeUp stagger, marquee 30/35s, counter angka | harus menghormati `prefers-reduced-motion` |

---

## 3. Tujuan & Non-Tujuan

### 3.1 Tujuan terukur (MVP)

| # | Tujuan | Ukuran |
|---|---|---|
| T1 | Nol URL lama yang putus | `audit:redirects` → 100% URL di `manifest.json` menghasilkan 200 atau 301→200 |
| T2 | Satu sumber kebenaran untuk identitas situs | `rg -n '62(81|83)[0-9]{8}|0813-|inovass\.adm@|Cibinong' resources/views app/View` → 0 hasil (dijalankan di CI) |
| T3 | Editor non-teknis membuat halaman standar ISO baru tanpa developer | Uji tugas: editor menyelesaikan US-02 ≤ 15 menit setelah pelatihan 2 jam |
| T4 | Tidak ada lead hilang | 100% submit valid tersimpan di `PengirimanKontak` walau notifikasi gagal |
| T5 | SEO dasar lengkap | Setiap halaman published: `<title>`, meta description (aturan §6.2), canonical, OG, satu `<h1>`, `lang="id"`; sitemap & robots ada; Lighthouse SEO 100 |
| T6 | Performa | Lighthouse mobile Performance ≥ 90, LCP ≤ 2,5 s, CLS ≤ 0,1; HTML/halaman ≤ 60 KB |
| T7 | Konten bermasalah terlihat | Dashboard "Perlu Review" memuat semua entri bermasalah hasil migrasi dengan checklist |

### 3.2 Non-tujuan (tidak dibangun di MVP)

- Multi-bahasa (situs satu bahasa; copy Inggris di-Indonesia-kan).
- Page builder drag-and-drop bebas (section beranda hanya on/off + urutan di v1).
- Headless API/GraphQL, mobile app, PWA.
- E-commerce/pembayaran, pendaftaran pelatihan online, jadwal pelatihan (v2).
- Newsletter, komentar, live chat widget, pencarian server-side.
- Riwayat versi/diff (v1); di MVP cukup soft delete + Activity Log + backup harian.
- Mega menu "Layanan" (v1); MVP: menu "Layanan" adalah tautan polos ke landing `/layanan/` (situs lama pun hanya tautan polos, lihat §2.3).
- Pelacakan pemakaian media & laporan "tidak terpakai" (v1); MVP mengandalkan FK `media_id` dengan `ON DELETE RESTRICT`.
- Link berbagi preview tanpa login (v1); MVP preview hanya untuk user yang login.
- Draft/published terpisah untuk entri yang sudah published (v1); lihat §6.1.
- Form builder bebas (v2); MVP satu form kontak dengan field tetap.
- Penulisan ulang copy (hero, intro, 87 "Cocok untuk") — pekerjaan tim konten, CMS hanya menyediakan tempat dan checklist.

---

## 4. Pengguna & Peran

### 4.1 Persona

| Persona | Deskripsi | Kebutuhan utama |
|---|---|---|
| Pengunjung (calon klien) | Manajer mutu/HSE, kepala lab, pimpinan perguruan tinggi; mayoritas akses dari HP via jaringan seluler | Menemukan layanan/standar dengan cepat, menghubungi via WhatsApp/form |
| Editor (staf marketing INOVASS) | Non-teknis; terbiasa WhatsApp, Google Docs, Canva | Mengedit teks/gambar, membuat halaman standar baru, melihat lead, tanpa menyentuh HTML |
| Admin (kepala marketing / admin kantor) | Pemilik konten & pengaturan | Mengubah kontak/footer/navigasi, mengelola user, redirect, ekspor lead |
| Developer | 1 full-stack Laravel + Claude Code | Deploy, migrasi, pemeliharaan bulanan |

### 4.2 Peran & hak akses

Rekonsiliasi: dokumen UX mengusulkan 5 peran, Arsitektur mengusulkan 2. Keputusan: **MVP 2 peran** (cukup untuk tim ≤ 5 orang), peran lain ditambah saat ada kebutuhan nyata.

| Kemampuan | Admin | Editor | Viewer (v1) | Kontributor (v2) |
|---|:-:|:-:|:-:|:-:|
| CRUD + publish semua konten (layanan, standar, program, halaman, klien, testimoni, FAQ, produk, artikel) | ✓ | ✓ | – | draft artikel saja |
| Edit section beranda (on/off, urutan) | ✓ | ✓ | – | – |
| Media library (upload, ganti file) | ✓ | ✓ | – | upload |
| Hapus media yang masih dirujuk field terstruktur | ditolak DB (`RESTRICT`) untuk semua peran; v1: Admin dengan daftar dampak | – | – | – |
| Lead inbox: lihat, ubah status, catatan | ✓ | ✓ | lihat | – |
| Ekspor lead CSV / hapus lead | ✓ | – | ekspor | – |
| Pengaturan (SiteSettings, Navigasi, BlokGlobal, SEO default, email tujuan lead) | ✓ | – | – | – |
| Redirect | ✓ | – | – | – |
| User & peran | ✓ | – | – | – |
| Integrasi teknis (SMTP, WA API, GA4, backup) | ✓ (`.env`/panel) | – | – | – |
| Activity Log | semua | miliknya | – | miliknya |

Aturan akun: login email + password (min 10 karakter, bcrypt); **MFA TOTP wajib untuk Admin, opsional Editor** (bawaan Filament 4; rekonsiliasi dari "OTP email" di dokumen UX); throttle login bawaan Laravel 5/menit per email+IP (tanpa lockout persisten — cukup dan lebih sedikit kode); sesi timeout 8 jam dengan `SESSION_DRIVER=database`; middleware `EnsureUserActive` me-logout request berikutnya bila `is_active=false` (menonaktifkan user juga menghapus baris `sessions` miliknya); undangan via email dengan link set-password berlaku 48 jam; user dinonaktifkan (bukan dihapus) agar atribusi konten tetap.

---

## 5. User Stories

Prioritas: **P0** = wajib MVP, **P1** = v1, **P2** = v2.

### US-01 (P0) — Mengubah kontak & footer di satu tempat
**Sebagai** Admin, **saya ingin** mengubah nomor WhatsApp, telepon, email, alamat, sosial media di Pengaturan, **agar** seluruh situs konsisten.
- [ ] Hanya ada satu `whatsapp_nomor` kanonik (regex `^62[0-9]{8,13}$`) dan satu `telepon_tampil`.
- [ ] Setelah simpan, footer semua halaman, halaman Kontak, tombol WA float (v1), dan tujuan notifikasi lead memakai nilai yang sama; perintah T2 (§3.1) menghasilkan 0 baris.
- [ ] Tahun copyright dirender dari tanggal server (`{tahun}` token).
- [ ] Sosial media tanpa URL tidak dirender (bukan `href="#"`); URL `#` ditolak validasi.
- [ ] Perubahan tercatat di Activity Log (`spatie/laravel-activitylog`, `logOnlyDirty`) dengan nilai lama → baru per field.

### US-02 (P0) — Membuat halaman standar ISO baru
**Sebagai** Editor, **saya ingin** membuat halaman "ISO/IEC 42001" di bawah "Jasa Konsultasi Sertifikasi Standar ISO/IEC/SNI", **agar** halaman langsung muncul di grid induk, breadcrumb, dan sitemap.
- [ ] Setelah memilih induk + Standar (atau membuat Standar baru inline), minimal 8 field ter-prefill dari pola: judul, slug, label breadcrumb, judul highlight, judul pengertian, 6 langkah proses default, CTA band bawah bertoken, meta title.
- [ ] Publish diblokir bila meta description kosong (entri buatan CMS; aturan §6.2), salah satu dari 3 highlight kosong, atau repeater di bawah batas §6.2; pesan error menyebut field.
- [ ] ≤ 60 detik setelah publish halaman bisa diakses di `/layanan/sertifikasi-organisasi/iso-42001.html`, tampil sebagai kartu terakhir di induk (aksen warna dihitung dari urutan), tercantum di `sitemap.xml` (dan di mega menu pada v1).
- [ ] Breadcrumb 5 level `Beranda › Layanan › Sertifikasi Organisasi › Jasa Konsultasi Sertifikasi… › ISO/IEC 42001`, semua tautan valid.
- [ ] Kartu di induk dirender sebagai `<a href>`.
- [ ] Dashboard menyarankan membuat 4 draft terkait (Penyusunan Dokumen, Public/In-House/Executive Training) untuk Standar yang sama dalam satu klik.

### US-03 (P0) — Menerima dan menindaklanjuti lead
**Sebagai** Editor, **saya ingin** setiap submit form kontak masuk ke Lead Inbox dan diteruskan ke email (dan WhatsApp di v1), **agar** tidak ada lead hilang.
- [ ] Setiap submit valid membuat 1 record `PengirimanKontak` (semua field + `halaman_sumber` + UTM + timestamp + `ip_hash`); record disimpan **sebelum** dan di luar transaksi pengiriman email; jika notifikasi gagal (termasuk pada queue `sync`, ditangkap `try/catch`), record tetap tersimpan, `notifikasi_status=gagal`, pengunjung tetap melihat halaman sukses, dan Admin bisa kirim ulang. Test mensimulasikan mailer gagal.
- [ ] Email ke semua `email_tujuan_form` dengan `Reply-To` = email pengirim, terkirim ≤ 2 menit (queue).
- [ ] Setelah sukses, pengunjung diarahkan ke `GET /kontak/terima-kasih?ref={id}` (`noindex`) berisi pesan sukses ("Terima kasih, tim kami merespons dalam 1×24 jam") dan tombol opsional "Lanjutkan chat via WhatsApp" ke nomor kanonik dengan pesan pra-isi (perilaku lama dipertahankan sebagai tambahan).
- [ ] Honeypot + Turnstile + rate limit (5/10 menit/IP, 20/hari/IP; IP klien asli di belakang Cloudflare, lihat §8.3) menolak bot dengan HTTP 422 dan teks default "Maaf, pengiriman tidak dapat diproses. Silakan coba lagi atau hubungi kami via WhatsApp." Form **membutuhkan JavaScript** untuk token Turnstile (keputusan: klaim non-JS dihapus; `<noscript>` menampilkan nomor WA + email sebagai jalur alternatif).
- [ ] Di detail lead: tombol "Chat WhatsApp" (`wa.me/{telepon pengirim}` pra-isi), "Balas Email", ubah status (`baru → dihubungi → selesai / spam`), catatan internal; badge jumlah "baru" di sidebar (dihitung per request, tanpa polling).

### US-04 (P0) — Menandai halaman "Segera Hadir" dan mengisinya nanti
**Sebagai** Editor, **saya ingin** menandai halaman layanan `mode = coming_soon` dan mengubahnya ke `normal` saat konten siap.
- [ ] `coming_soon` merender `BlokGlobal.coming_soon` dengan judul/breadcrumb halaman, menyembunyikan CTA band, memasang `noindex`, mengecualikan dari sitemap; kartu di induk tetap tampil dengan badge "Segera".
- [ ] Dashboard memuat daftar semua halaman `coming_soon` (saat migrasi: 9 published, §15.9) dengan kategori dan induk.
- [ ] Mengubah ke `normal` menjalankan validasi template penuh.

### US-05 (P0) — Mengelola logo klien, FAQ, produk
**Sebagai** Editor, **saya ingin** menambah/mengganti logo klien, FAQ, dan produk tanpa duplikasi.
- [ ] Klien disimpan sekali (nama wajib, logo, `baris_marquee`, urutan, `tampil_di_beranda/tentang`); loop marquee dilakukan template.
- [ ] Logo dinormalisasi saat upload (nama file slug, tinggi 72px, WebP); alt = nama klien.
- [ ] FAQ punya `scope` dan urutan; FAQ beranda dirender dengan JSON-LD `FAQPage`.
- [ ] Produk punya `tombol_beranda` (→ `/produk.html#{slug}`) dan `tombol_utama` (→ `/kontak.html?layanan=produk`) yang labelnya mengikuti nama produk (bukan "Konsultasikan DCS"); nama di beranda (`InoSys`/`InoLab`) dan nama di halaman produk (`Document Control System (DCS)`/`Learning Management System (LMS)`) keduanya tersimpan (§6.4).

### US-06 (P0) — Preview sebelum publish
**Sebagai** Editor, **saya ingin** melihat entri berstatus draft persis seperti di situs sebelum mempublikasikannya.
- [ ] Tombol Preview (hanya untuk user login) membuka `/preview/{tipe}/{id}` yang merender entri apa pun statusnya dengan template publik, banner "MODE PREVIEW – belum dipublikasikan", toggle lebar 1280/820/390, `noindex,nofollow`, tidak di-cache, tidak masuk sitemap.
- [ ] Preview adalah render baca-saja; tidak ada data yang berubah. Karena MVP memakai model simpan-langsung (§6.1), preview berguna untuk entri `draft`/`archived`; entri published diubah lewat Simpan langsung tayang.
- [ ] **v1**: link berbagi tanpa login via kolom `preview_token` (random 32 byte) + `preview_token_expires_at` (7 hari; rekonsiliasi dari 24 jam di Content Model); "Cabut" = regenerate token. Signed URL Laravel tidak dipakai karena tidak bisa dicabut.

### US-07 (P0) — Mengelola pengguna & melihat jejak perubahan
**Sebagai** Admin, **saya ingin** mengundang Editor, membatasi akses, dan melihat siapa mengubah apa.
- [ ] Undangan via email, default peran Editor; Editor yang membuka Pengaturan mendapat 403 dan menu tidak tampil di sidebar.
- [ ] Activity Log (`spatie/laravel-activitylog`) difilter per user/tipe/tanggal; menampilkan nilai lama/baru per field untuk semua model yang di-log.
- [ ] Menonaktifkan user menghapus baris `sessions` miliknya → request berikutnya langsung logout (§4.2).

### US-12 (P0) — Mengelola media
**Sebagai** Editor, **saya ingin** mengunggah gambar/PDF sekali dan memakainya di banyak halaman.
- [ ] Upload drag-and-drop ke Media Library (§7.3); setiap field gambar membuka picker modal yang menampilkan rekomendasi ukuran.
- [ ] Alt wajib untuk gambar; nama file dinormalisasi ke slug; WebP + srcset dibuat otomatis.
- [ ] "Ganti file" mempertahankan `media_id` sehingga semua halaman yang merujuknya ikut berubah.
- [ ] Menghapus media yang masih dirujuk field terstruktur gagal dengan pesan jelas (constraint DB).

### US-13 (P0) — Mengelola redirect & halaman generik
**Sebagai** Admin, **saya ingin** menambah redirect manual dan halaman legal tanpa developer.
- [ ] Form Redirect {`dari_path`, `ke_path`, `aktif`}; `dari_path` unik, diawali `/`; disimpan → berlaku ≤ 60 detik; tes: `GET dari_path` → 301 `ke_path`.
- [ ] `Halaman` generik (`/kebijakan-privasi.html`, `/syarat-ketentuan.html`) dengan rich text penuh; tautan legal di footer hanya dirender bila halaman published.
- [ ] Landing `/layanan/` menampilkan 7(+1) kategori published sebagai kartu `<a>`.

### US-14 (P0) — Dashboard "Perlu Review" & section beranda on/off
**Sebagai** Editor, **saya ingin** melihat daftar entri hasil migrasi yang perlu diperbaiki, dan menyembunyikan section beranda yang belum punya konten asli.
- [ ] Dashboard memuat checklist §7.8 dengan tautan langsung ke form; mencentang item mengubah `migrasi_perlu_review=false`.
- [ ] Setiap section Beranda punya toggle `aktif`; section non-aktif tidak dirender; Hero tidak bisa dinonaktifkan.
- [ ] Section Berita/Testimoni tersembunyi otomatis bila tidak ada entri published, dengan catatan di admin.

### US-08 (P1) — Mengatur urutan section beranda
**Sebagai** Editor, **saya ingin** memindahkan FAQ di atas Berita.
- [ ] Drag-and-drop mengubah urutan; Hero terkunci posisi 1. (Toggle on/off sudah ada di MVP, US-14.)

### US-09 (P1) — Menulis dan menjadwalkan artikel
**Sebagai** Editor, **saya ingin** menulis artikel rich text dengan gambar dan jadwal tayang.
- [ ] Paste dari Google Docs menghasilkan heading/list/bold bersih tanpa style inline.
- [ ] Gambar sampul wajib (alt wajib); meta description default dari ringkasan; OG dari sampul.
- [ ] Jadwal publish tayang otomatis (toleransi ≤ 5 menit) dan muncul di beranda; URL `/berita/{slug}`; ubah slug published → 301 otomatis.

### US-10 (P1) — Riwayat versi & pulihkan
- [ ] Setiap save menyimpan snapshot JSON (30 terakhir); panel Riwayat: siapa, kapan, field yang berubah, Pulihkan ≤ 3 klik.
- [ ] Autosave draft 30 detik; soft lock dengan nama user bila dua orang mengedit entri yang sama.

### US-11 (P2) — Jadwal & pendaftaran pelatihan
- [ ] `ProgramPelatihan` punya tab "Jadwal & Biaya" (durasi, metode, harga, jadwal[], instruktur, brosur); `form_pendaftaran_aktif` membuka form yang bermuara ke `PengirimanKontak` dengan `jenis = pendaftaran_pelatihan`; JSON-LD `Course`.

---

## 6. Content Model

### 6.1 Prinsip

- Hierarki 4 level: `KategoriLayanan` (L2, 7+1) → `Layanan` (L3, 50 = 37 published + 13 draft) → `LayananDetail` / `ProgramPelatihan` (L4, ±480). L3 dan L4 berada di **folder URL yang sama** `/layanan/{kategori}/`, jadi **slug unik per folder kategori lintas 3 tipe** — ditegakkan oleh unique index `routes.full_path` (§6.6), bukan validasi lintas tabel.
- `Standar` adalah entitas lookup bersama (±46) yang menjadi sumber nama kanonik dan token (`{standar.kode}`, `{standar.nomor}`, `{standar.nama_sistem}`, `{standar.label_tampilan}`).
- Nilai yang bisa dihitung **tidak disimpan**: nomor langkah (dari posisi), aksen warna kartu (`i mod 3`), breadcrumb (dari relasi), tahun copyright. `Standar.label_tampilan` disimpan **nullable sebagai override**; bila null, accessor menghitung `{kode}{:tahun_edisi} – {nama_sistem}`.
- Tipe field: `string`, `text`, `richtext` (terbatas: p, strong, em, ul/ol, a, h3; artikel/halaman: penuh h2–h4, tabel, gambar, embed), `slug`, `int`, `bool`, `enum`, `date(time)`, `email`, `tel`, `url`, `media` (= FK `media_id` ke tabel `media`, `ON DELETE RESTRICT`), `rel(1)/rel(n)`, `repeater`, `component`, `json`.
- Field sistem semua koleksi: `id, status (draft|published|archived), published_at, scheduled_publish_at, created_by, updated_by, migrasi_perlu_review, legacy_path, timestamps, deleted_at`. Status `review` dan `scheduled_unpublish_at` ditunda (v1).
- **Model simpan-langsung (MVP)**: koleksi tidak punya draft terpisah dari versi published — Simpan pada entri `published` langsung tayang (setelah checklist validasi §7.2); entri `draft` tidak dirender publik dan hanya terlihat via Preview. Singleton disimpan di tabel `singletons {key, data json, updated_by, updated_at}` dan selalu "published" (Simpan = terapkan). Kolom `draft_data` JSON untuk draft-di-atas-published (koleksi maupun singleton) adalah **v1**, bersama riwayat versi.
- **Penamaan**: nama kolom DB dan kunci fixture JSON = nama field di §6 apa adanya (snake_case Bahasa Indonesia); nama kelas PHP/model = Inggris sesuai tabel pemetaan §9.1. Label UI admin = Bahasa Indonesia (§7.1).

### 6.2 Komponen reusable

| Komponen | Field |
|---|---|
| `SEO` | `meta_title` string ≤60 (default `{judul} — INOVASS`); `meta_description` text 70–160 — **satu aturan yang dirujuk semua bagian**: (1) render selalu memakai fallback bila kosong (ringkasan/paragraf pertama; L4: pola §8.2); (2) validasi publish **memblokir** hanya entri dengan `legacy_path = null` (dibuat di CMS); (3) entri migrasi (`legacy_path` terisi) hanya mendapat warning + masuk checklist Perlu Review; `canonical_url`; `og_image` media (fallback `SiteSettings.og_image_default`); `noindex` bool (auto true saat `coming_soon`); `schema_type` enum WebPage/Service/Course/Article/FAQPage/Organization |
| `Tautan` | `label`; `jenis` enum internal/eksternal/anchor/whatsapp/email/telepon; `target_entri` rel polimorfik (URL dirender dari entri, tidak putus saat slug berubah); `url` — validasi skema **hanya** `https`, `http`, `mailto:`, `tel:` (menolak `javascript:`/`data:`); `buka_tab_baru` |
| `Gambar` | `media`, `alt_override` (focal point: v1) |
| `Ikon` | `kunci` Heroicons Outline via `guava/filament-icon-picker` (pencarian bawaan plugin); SVG kustom & ikon gambar ditunda (v1) |
| `KartuIkon` | `ikon` Ikon, `judul` ≤60, `teks` ≤220 |
| `KartuManfaat` | `judul` ≤60, `teks` ≤220 |
| `Statistik` | `angka` int, `sufiks`, `label` ≤40 |
| `JudulDuaBaris` | `eyebrow`, `baris_1` (wajib), `baris_2_aksen` (dirender `<em>`), `deskripsi` |
| `HeroHalaman` | `gambar` Gambar, `judul` JudulDuaBaris, `breadcrumb_label` |
| `CtaBand` | `aktif`, `gunakan_default`, `varian` enum hub/detail/pelatihan/leaf_iso/leaf_generic/beranda, `judul`, `teks`, `tombol_utama`, `tombol_sekunder` (beranda saja); token `{standar.*}` hanya pada `leaf_iso`; bila `standar` null token diganti `{judul}` entri |
| `Langkah` | `judul`, `teks`, `sub_langkah` repeater {label, teks} ≤3; nomor dari posisi |

**Batas repeater kanonik** (satu-satunya sumber; §6.4, §7.2, US-02 merujuk ke sini): `highlight` tepat 3 · `manfaat` 3–8 · `proses`/`materi` 4–8 · `target`/`peserta` 3–12 · `keunggulan` 3–8 · `misi` 1–8 · `statistik` 2–4. Migrasi mengisi nilai aktual situs lama (3/6/6/9 atau 6) yang semuanya di dalam batas.

### 6.3 Singleton

| Tipe | Field utama (tipe · wajib) | Catatan |
|---|---|---|
| `SiteSettings` | `nama_situs`, `tagline` ≤80, `deskripsi_singkat` ≤300, `logo_utama` media, `logo_footer`, `favicon` media (**baru**), `og_image_default` media (**baru**), `bahasa` default `id`, `alamat_baris` repeater 1–6, `alamat_maps_url`, `telepon_tampil`, `whatsapp_nomor` tel regex `^62\d{8,13}$` (**satu-satunya** nomor WA; bila Q1 menjawab nomor lead berbeda, field kedua ditambah saat itu), `whatsapp_pesan_default` ≤300, `whatsapp_float_aktif` bool (v1), `whatsapp_float_label`, `email_utama`, `email_tujuan_form` repeater ≥1 (Admin saja), `jam_operasional`, `sosial` repeater {platform enum, url valid — `#` ditolak}, `footer_judul_kolom_alamat` default "Kantor", `footer_judul_kolom_kontak` default "Hubungi Kami", `copyright_teks` (wajib token `{tahun}`), `tautan_legal` repeater Tautan, `seo_default` SEO, `analytics_id`, `robots_txt` text (hanya dipakai bila `APP_ENV=production`; lingkungan lain selalu `Disallow: /`) | Mengganti 98× footer hard-coded; menyatukan 2 nomor WA. Warna brand = token Tailwind statis (§2.6), **tidak** dapat diedit dari admin |
| `Navigasi` | `menu_utama` repeater 2 level {label, tautan Tautan, anak repeater {label, tautan}} (Filament Repeater bersarang + `reorderable()`, tanpa plugin tree), `cta_header` Tautan, `menu_footer` repeater Tautan | Migrasi: Beranda, Layanan (→ `/layanan/`), Produk, Tentang Kami. **v1**: item `mega_layanan` yang membangun panel mega menu dari KategoriLayanan → Layanan published |
| `BlokGlobal` | `cta_band_hub`, `cta_band_detail`, `cta_band_pelatihan` (component {judul JudulDuaBaris, teks, tombol, gaya}); `cta_band_leaf_iso` {judul_template, teks_template, tombol} dengan token `{standar.nama_sistem}`, `{standar.nomor}`; `cta_band_leaf_generic` (tanpa token standar; dipakai jenis tanpa `standar`); `inline_cta_konsultasi`, `inline_cta_akreditasi` ("Siap Meraih Akreditasi Laboratorium?" + "Hubungi Kami Sekarang"), `inline_cta_pelatihan`, `inline_cta_pranata_lab`; `coming_soon` {judul, deskripsi, chip ×3 KartuIkon, tombol_utama, tombol_sekunder_label}; `proses_default_sertifikasi`, `proses_default_penyusunan_dokumen`, `proses_default_akreditasi`, `proses_default_generic` (repeater Langkah ×6 masing-masing; `generic` diisi dari `proses_default_sertifikasi` saat seed dan diedit Admin); `label_tombol_lihat_detail`, `label_baca_selengkapnya` | Menghapus CTA copy-paste "ISO 9001" dan judul langkah salah di 19 Penyusunan Dokumen. Pemetaan `jenis_layanan` → default ada di §6.4 (setelah `LayananDetail`) |
| `Beranda` | Daftar section berurutan, masing-masing `aktif` + `urutan`: `hero` {eyebrow, judul, gambar_latar, tombol}; `tentang_singkat` {judul, statistik ×4, tombol, nilai ×4 KartuIkon gambar}; `klien_marquee` {label, sumber otomatis/manual, baris 1–2}; `layanan_bento` {judul, kartu ×4 {judul, teks, gambar_latar, tautan **wajib**, ukuran enum}, tombol}; `produk_showcase` {judul, subjudul, produk rel(n) ≤3}; `bidang_pelatihan` {judul, kartu 3–8 KartuIkon, tombol}; `keunggulan` {judul, deskripsi, kartu 3–6}; `proses_kerja` {judul, langkah 3–6}; `berita` {judul, sumber terbaru/pilihan, tombol}; `testimoni` {judul, sumber, autoscroll}; `faq` {judul, sumber, maks_item 6}; `cta_band` varian beranda; `seo` (schema Organization) | MVP: `aktif` toggle saja; v1: reorder |
| `TentangKami` | `hero`, `profil_gambar`, `profil_judul`, `profil_paragraf` richtext, `profil_statistik` ×3, `visi` text, `misi` repeater ×5, `visi_misi_gambar`, `why_us_judul`, `why_us_kartu` ×6 KartuIkon, `klien_judul`, `klien_sumber`, `cta_band`, `seo` | |
| `Kontak` | `hero`, `judul`, `deskripsi`, `info_item` repeater {ikon, label, nilai, tautan} (dirender `tel:`/`mailto:`), `peta_embed_url` (validasi: `parse_url` host **persis** `www.google.com` dan path diawali `/maps/embed`; CSP `frame-src https://www.google.com`; iframe `title`), `form_aktif`, `form_judul`, `form_opsi_layanan` repeater {nilai, label} (iso, akreditasi, pelatihan, sertifikasi, produk, lainnya), `form_label_tombol`, `form_pesan_sukses`, `form_consent_teks` richtext, `cta_band` (aktif=false default), `seo` | Nomor WA diambil dari SiteSettings. Perilaku sukses **tetap** (simpan → email → halaman sukses dengan tombol WA), tidak ada opsi; Turnstile selalu aktif (tidak ada toggle yang bisa dimatikan Editor) |
| `HalamanProduk` | `hero`, `judul_section`, `produk` rel(n) (kosong = semua published), `cta_band`, `seo` | |
| `HalamanLayanan` | `hero_default` HeroHalaman (dipakai semua hub tanpa override), `tampilkan_landing` bool default true (true: `/layanan/` grid 8 kategori; false: 301 ke kategori pertama = perilaku lama), `intro` richtext, `cta_band`, `seo` | Landing `/layanan/` **baru**; menu "Layanan" di navbar mengarah ke sini |

### 6.4 Koleksi

#### `KategoriLayanan` (L2) — 7 published + 1 draft (`sertifikasi-personel`)

| Field | Tipe | Wajib | Catatan |
|---|---|:-:|---|
| `nama` | string ≤40 | ✓ | label tab |
| `slug` | slug | ✓ | unik; **persis folder lama**: `sertifikasi-organisasi`, `akreditasi-organisasi`, `pelatihan-sertifikasi`, `pelatihan-akreditasi`, `pranata-laboratorium`, `lab-mineral`, `lab-teknik-sipil` |
| `urutan` | int | ✓ | urutan tab |
| `hero_override` | HeroHalaman | – | kosong = `HalamanLayanan.hero_default` |
| `judul_section`, `intro` | string, text ≤600 | ✓ | |
| `grid_kolom` | enum 3/4 | ✓ | lab-mineral = 3 |
| `layanan_sumber` | enum otomatis/manual | ✓ | |
| `cta_band` | CtaBand varian hub | – | kosong = `BlokGlobal.cta_band_hub` |
| `ikon` | Ikon | ✓ | ikon tab/kartu landing |
| `deskripsi_singkat` | string ≤160 | ✓ | kartu di landing `/layanan/` |
| `seo` | SEO | ✓ | meta_title default `{nama} — Layanan INOVASS` |

URL: `/layanan/{slug}/index.html`; `/layanan/{slug}/` 301 → `index.html` (satu URL per halaman, konsisten dengan `/index.html` 301 → `/`). Blok tersembunyi hub lama **tidak dimigrasikan**.

#### `Standar` (lookup, ±46, tanpa URL)

| Field | Tipe | Wajib | Catatan |
|---|---|:-:|---|
| `kode` | string | ✓ | unik; kode kanonik lengkap dengan prefix: `ISO 9001`, `SNI ISO/IEC 17025`, `SPMI`, `LAM-PTKes`, `Permenkes 43/2013` |
| `nomor` | string | ✓ | bagian angka/singkat untuk token: `9001`, `17025`, `SPMI` (= `kode` bila tanpa nomor) |
| `tahun_edisi` | string 4 digit | – | validasi mencegah `14001:2026` |
| `nama_sistem` | string | ✓ | `Sistem Manajemen Mutu` |
| `singkatan_sistem` | string | – | `QMS`, `EMS` |
| `label_tampilan` | string | – | override; null = accessor `{kode}{:tahun_edisi} – {nama_sistem}` (§6.1) |
| `slug_suffix` | slug | ✓ | unik; `iso-9001`, `ims`, `iso-lainnya` |
| `keluarga` | enum | ✓ | iso_sistem_manajemen (19) / akreditasi_lembaga (11) / akreditasi_pendidikan (SPMI, SN-Dikti, LAM-PTKes, LAMSPAK) / regulasi (`Permenkes 43/2013`) / lainnya (`Etika Penelitian`) |
| `urutan` | int | ✓ | |
| `deskripsi` | text | – | |
| `aktif` | bool | ✓ | default true |

Field `kode_pendek` dan `prefix_tampilan` dari draft awal dihapus (redundan dengan `nomor` dan `kode`).

#### `Layanan` (L3, 50 = 37 published + 13 draft)

| Field | Tipe | Wajib | Catatan |
|---|---|:-:|---|
| `kategori` | rel(1) KategoriLayanan | ✓ | folder URL & breadcrumb |
| `judul` | string ≤140 | ✓ | |
| `judul_pendek` | string ≤50 | – | breadcrumb & kartu bila judul panjang |
| `slug` | slug | ✓ | **unik per folder kategori** lintas L3/L4 (unique index `routes.full_path`); migrasi persis |
| `urutan` | int | ✓ | |
| `template` | enum | ✓ | `daftar_sub_layanan` (service-list/akreditasi-detail/program-list) · `format_pelatihan` (training-format) · `konten_bebas` |
| `mode` | enum normal/coming_soon | ✓ | |
| `kartu_ikon` | Ikon | ✓ | kartu di hub |
| `kartu_ringkasan` | string ≤160 | ✓ | kartu di hub |
| `kartu_tautan_override` | Tautan | – | kosong = URL entri |
| `intro_judul` | text (≤3 baris, `\n` = `<br>`) | ✓ | |
| `intro_teks` | text ≤900 | ✓ | |
| `keunggulan_judul` | string | jika `format_pelatihan` | |
| `keunggulan_deskripsi` | text | – | |
| `keunggulan` | repeater KartuIkon (batas §6.2) | jika `format_pelatihan` | migrasi 6 |
| `daftar_judul` | string | jika `daftar_sub_layanan` | |
| `daftar_deskripsi` | text | – | |
| `daftar_sumber` | enum anak_otomatis/dari_standar/manual | jika `daftar_sub_layanan` | `dari_standar` mengurutkan mengikuti `Standar.urutan` |
| `daftar_jenis_anak` | enum layanan_detail/program_pelatihan | jika `daftar_sub_layanan` | |
| `daftar_kolom` | enum 3/4 | – | default 4 |
| `daftar_filter_aktif` | bool | – | filter client-side untuk MIPA (60 kartu), v1 |
| `jenis_layanan` | enum sertifikasi/penyusunan_dokumen/audit_internal/surveillance/pemeliharaan/k3/csms/k3_lab/qhse/akreditasi/pelatihan/pranata_lab/lab_manajemen/sertifikasi_personel | **✓ bila `daftar_jenis_anak = layanan_detail`** | memilih default & prefill anak (tabel pemetaan di bawah `LayananDetail`) |
| `pola_judul_anak` | string bertoken | – | `Jasa Penyusunan Dokumen {standar.label_tampilan}` |
| `pola_slug_anak` | string bertoken | – | `penyusunan-dokumen-{standar.slug_suffix}` |
| `isi_bebas` | richtext | jika `konten_bebas` | |
| `cta_band` | CtaBand varian detail | – | kosong = `BlokGlobal.cta_band_detail`; CSMS override sendiri |
| `standar_terkait` | rel(n) Standar | – | |
| `seo` | SEO | ✓ | |

URL: `/layanan/{kategori.slug}/{slug}.html`. Breadcrumb otomatis: `Beranda › Layanan › {kategori.nama} › {judul_pendek|judul}`.

#### `LayananDetail` (L4 jasa, ±295)

Satu tipe untuk ±177 leaf di folder sertifikasi (19 ISO + 19 penyusunan dokumen ter-crawl; ±139 lainnya: audit/surveillance/pemeliharaan, K3, CSMS, K3 lab, QHSE — jumlah per induk ditetapkan crawler) + ±118 sub-akreditasi.

| Field | Tipe | Wajib | Catatan |
|---|---|:-:|---|
| `parent_utama` | rel(1) Layanan | ✓ | folder URL, breadcrumb, jenis_layanan |
| `parent_tambahan` | repeater {layanan rel(1), label_override, urutan} | – | 7 slug QHSE yang dipakai Konstruksi **dan** Industri; canonical & breadcrumb selalu parent utama (fitur `?dari=` dihapus agar cache key bebas query string) |
| `standar` | rel(1) Standar | jika jenis ∈ {sertifikasi, penyusunan_dokumen, audit_internal, surveillance, pemeliharaan} | |
| `judul` | string ≤160 | ✓ | prefill dari `pola_judul_anak` induk |
| `label_kartu` | string ≤160 | ✓ | prefill = judul |
| `label_breadcrumb` | string ≤60 | ✓ | |
| `slug` | slug | ✓ | unik per folder; migrasi persis termasuk anomali (`audit-internal-iso-ims`, `konsultasi-qms`) |
| `urutan` | int | ✓ | |
| `mode` | enum normal/coming_soon | ✓ | |
| `highlight_judul` | string ≤120 | ✓ | |
| `highlight` | repeater {teks ≤120} tepat 3 | ✓ | |
| `pengertian_judul` | string | ✓ | |
| `pengertian_istilah` | string | – | dirender `<strong>` |
| `pengertian_isi` | richtext | ✓ | |
| `manfaat_judul` | string | ✓ | |
| `manfaat` | repeater KartuManfaat (batas §6.2) | ✓ | migrasi 6 |
| `inline_cta_gunakan_default` | bool | ✓ | default true |
| `inline_cta_override` | component {teks, label_tombol} | – | |
| `proses_judul` | string | ✓ | |
| `proses_gunakan_default` | bool | ✓ | migrasi: **false** untuk semua entri (proses aktual halaman disimpan); true hanya untuk entri baru dari CMS |
| `proses` | repeater Langkah (batas §6.2) | jika `proses_gunakan_default=false` | migrasi 6 |
| `target_judul` | string | ✓ | |
| `target_intro` | text | – | |
| `target` | repeater {label ≤80, tautan Tautan opsional} (batas §6.2) | ✓ | ISO 9, sub-akreditasi 6 |
| `target_penutup` | text | – | paragraf "Cocok untuk" sub-akreditasi |
| `cta_band` | CtaBand | – | `aktif` default mengikuti tabel pemetaan di bawah; migrasi sub-akreditasi: `aktif=false` (situs lama tidak punya) |
| `konten_tambahan` | richtext | – | |
| `faq` | rel(n) FAQ | – | |
| `berkas_unduhan` | repeater {label, file pdf} | – | |
| `seo` | SEO | ✓ | schema default `Service` |

URL: `/layanan/{parent_utama.kategori.slug}/{slug}.html`. Aksen kartu di induk `i mod 3`; kartu = `<a href>`.

**Pemetaan `jenis_layanan` → default** (dipakai prefill US-02, `import:legacy`, dan render):

| `jenis_layanan` | `proses_default_*` | inline CTA default | `cta_band` default | `standar` |
|---|---|---|---|:-:|
| sertifikasi, audit_internal, surveillance, pemeliharaan | `proses_default_sertifikasi` | `inline_cta_konsultasi` | `cta_band_leaf_iso` (aktif) | wajib |
| penyusunan_dokumen | `proses_default_penyusunan_dokumen` | `inline_cta_konsultasi` | `cta_band_leaf_iso` (aktif) | wajib |
| akreditasi, lab_manajemen | `proses_default_akreditasi` | `inline_cta_akreditasi` | `cta_band_leaf_generic` (**aktif=false** saat migrasi; menyalakannya = perilaku baru yang disengaja) | – |
| k3, csms, k3_lab, qhse | `proses_default_generic` | `inline_cta_konsultasi` | `cta_band_leaf_generic` (aktif) | – |
| pelatihan, pranata_lab, sertifikasi_personel | – (anak = `ProgramPelatihan`, tidak punya section proses) | `inline_cta_pelatihan` / `inline_cta_pranata_lab` | `cta_band_detail` / `cta_band_pelatihan` (lihat `ProgramPelatihan`) | – |

Validasi publish anak gagal bila `proses_gunakan_default=true` tetapi induk tidak punya `jenis_layanan`. Token `{standar.*}` pada entri tanpa `standar` diganti `{judul}` entri.

#### `ProgramPelatihan` (L4 pelatihan, ±185: 87 format×standar + 98 pranata lab)

| Field | Tipe | Wajib | Catatan |
|---|---|:-:|---|
| `parent` | rel(1) Layanan | ✓ | format pelatihan atau list pranata lab |
| `standar` | rel(n) Standar, 1–10 | – | format: tepat 1; pranata lab 1–8 di situs lama (Kesehatan Lingkungan & Radiologi: hanya `SNI ISO/IEC 17025:2017`; Genetika Kedokteran: 8 termasuk `Etika Penelitian`; Parasitologi memuat `Permenkes 43/2013`) |
| `bidang` | string ≤80 | jika pranata lab | `Kimia`, `Anatomi`, `Kesehatan Masyarakat` |
| `bidang_keterangan` | string ≤120 | – | teks dalam kurung di judul lama: `Laboratorium Epidemiologi, Laboratorium Lingkungan`, `Nursing Skills Laboratory`, `Quality Control Radiologi` |
| `judul` | string ≤200 | ✓ | **prefill** (bukan generate paksa): format `{parent.judul_pendek} {standar.label_tampilan}`; pranata lab `Pelatihan Pranata Laboratorium Pendidikan {bidang} ({bidang_keterangan}) Standar Akreditasi {daftar standar, "dan" sebelum terakhir}`; migrasi menyimpan judul lama **apa adanya** (termasuk "17025 atau 15189", prefix "Pengujian dan Kalibrasi") dan menandai yang menyimpang dari prefill sebagai Perlu Review |
| `label_kartu` | string ≤200 | ✓ | prefill = judul |
| `label_breadcrumb` | string ≤60 | ✓ | `Pranata Lab Pendidikan Kimia` |
| `slug` | slug | ✓ | migrasi persis (`inhouse-training-39001`, `pranata-lab-kesehatan-kesling`) |
| `urutan` | int | ✓ | |
| `mode` | enum normal/coming_soon | ✓ | |
| `highlight` | repeater {teks ≤120} tepat 3 | ✓ | |
| `tentang_judul` | string | ✓ | |
| `tentang_isi` | richtext | ✓ | |
| `manfaat_judul` | string | ✓ | |
| `manfaat` | repeater KartuManfaat (batas §6.2) | ✓ | migrasi 6 |
| `inline_cta_gunakan_default` | bool | ✓ | `inline_cta_pelatihan` (format) / `inline_cta_pranata_lab` (pranata) sesuai parent |
| `inline_cta_override` | component {teks, label_tombol} | – | |
| `materi_judul` | string | ✓ | "Materi Training" |
| `materi` | repeater Langkah (batas §6.2) | ✓ | migrasi 6, diurutkan ulang dari DOM 1,2,3,6,5,4 |
| `peserta_judul` | string | ✓ | |
| `peserta_intro` | text | ✓ | |
| `peserta` | repeater {label} (batas §6.2) | ✓ | migrasi 6 |
| `peserta_penutup` | richtext | – | paragraf "Cocok untuk" |
| `cta_band` | CtaBand | – | **varian per parent saat import**: `parent.template = format_pelatihan` → `cta_band_detail` ("…untuk organisasi Anda", teks yang memang dipakai 87 halaman lama); pranata lab → `cta_band_pelatihan` ("…untuk kebutuhan pelatihan Anda") |
| `seo` | SEO | ✓ | schema `Service` di MVP, `Course` di v2 |
| **v2 (tab "Jadwal & Biaya")**: `durasi`, `metode` enum multi, `harga` int + `harga_tampil`, `jadwal` repeater {tanggal_mulai, tanggal_selesai, kota, kuota, status}, `instruktur` repeater, `sertifikat_teks`, `brosur` pdf, `form_pendaftaran_aktif` | | – | |

URL: `/layanan/{parent.kategori.slug}/{slug}.html`.

#### Koleksi pendukung

| Tipe | Field | Jumlah migrasi |
|---|---|---|
| `Halaman` | `judul` ≤90, `slug` (root, unik), `hero` opsional, `isi` richtext penuh, `cta_band`, `seo`; URL selalu `/{slug}.html` | 2 draft (Kebijakan Privasi, Syarat & Ketentuan) |
| `Produk` | `nama` ✓ (halaman produk: `Document Control System (DCS)`, `Learning Management System (LMS)`), `nama_tampil_beranda` (`InoSys`, `InoLab`; kosong = `nama`), `slug`, `kategori` enum dcs/lms/lims/lainnya, `tagline`, `deskripsi_singkat` ≤300 ✓ (teks kartu beranda), `deskripsi_lengkap` (teks `produk.html`), `gambar_mockup` ✓ (migrasi dari `assets/img/dcs.png` / `lms.png` yang ada di `produk.html`; **hanya gambar showcase beranda** yang memakai wallpaper placeholder dan tidak dimigrasikan), `galeri`, `fitur`, `tombol_beranda` Tautan ✓ (→ `/produk.html#{slug}`), `tombol_utama` Tautan ✓ (→ `/kontak.html?layanan=produk`), `urutan`, `tampil_di_beranda`, `punya_halaman_detail` (v2), `seo` | 2 |
| `Klien` | `nama` ✓, `logo` ✓ (PNG/SVG ≤400 KB, rename slug), `sektor` enum, `url_website`, `tampil_di_beranda`, `tampil_di_tentang`, `baris_marquee` 1/2, `urutan` | 44 (1 logo tanpa nama, alt "Client", file `Logo_2021-09-03cdfc….png` → `nama="(tidak diketahui)"` + `migrasi_perlu_review`) |
| `Testimoni` | `kutipan` 40–400, `nama`, `jabatan`, `organisasi` (dipisah), `klien` rel, `foto`, `layanan_terkait`, `tampil_di_beranda`, `urutan` | 5 **draft** (terindikasi fiktif; `rating`/`terverifikasi` tidak dibangun) |
| `FAQ` | `pertanyaan` ≤160, `jawaban` richtext, `scope` enum multi beranda/layanan_umum/pelatihan/produk/kontak, `standar` rel(n), `urutan` | 6 |
| `KategoriArtikel` | `nama`, `slug`, `deskripsi` | 3 (berita, insight, pengumuman) |
| `Artikel` (v1) | `judul` ≤120, `slug` (unik di `/berita/`), `kategori` rel(1), `ringkasan` 80–220 ✓, `gambar_sampul` ✓ 16:9, `isi` richtext penuh, `penulis` rel User, `tanggal_terbit`, `tag`, `standar_terkait`, `layanan_terkait`, `unggulan` bool, `seo` (Article) | 3 draft tanpa isi |
| `PengirimanKontak` (system, read-only kecuali status/catatan) | `jenis` enum kontak/pendaftaran_pelatihan/permintaan_demo, `nama`, `email`, `telepon` (normalisasi `62…`), `organisasi`, `keperluan`, `pesan` ≤3000, `halaman_sumber`, `entri_terkait` rel polimorfik, `utm` json, `consent`, `ip_hash` = `hash_hmac('sha256', ip, APP_KEY)` (hash polos IPv4 bisa di-brute-force), `user_agent`, `status` enum baru/dihubungi/selesai/spam, `catatan_internal`, `notifikasi_status` enum terkirim/gagal/menunggu; tanpa assignee (v1) | 0 |
| `Redirect` | `dari_path` ✓ unik (awalan `/`, tanpa wildcard), `ke_path` ✓, `kode` 301 tetap, `sumber` manual/otomatis_slug/migrasi, `aktif`; 302/410/wildcard/hit counter: v1 bila diperlukan | ±15 |
| `Media` (tabel sendiri, §7.3) | `file` (jpg/png/webp/svg-disanitasi/avif ≤5 MB; pdf ≤20 MB), `nama_file_publik` (auto slug), `nama_asli`, `alt` ✓ untuk gambar ≤125, `caption`, `folder` string (brand/hero/layanan/produk/klien/artikel/dokumen), `dimensi/ukuran/mime`; focal point & tag: v1 | ±70 |

### 6.5 Relasi & integritas

```
KategoriLayanan 1 ──< n Layanan
Layanan         1 ──< n LayananDetail   (parent_utama)
Layanan         n ──< n LayananDetail   (parent_tambahan, label per parent)  ← 7 slug QHSE
Layanan         1 ──< n ProgramPelatihan
Standar         1 ──< n LayananDetail   (opsional)
Standar         n ──< n ProgramPelatihan
LayananDetail   n ──< n FAQ
Artikel         n ──< n Standar, Layanan
Testimoni       n ──  1 Klien, Layanan (opsional)
```

- `Layanan`/`KategoriLayanan` tidak bisa dihapus selama punya anak published.
- Mengubah `slug` entri published (atau memindah `kategori`/`parent`) **otomatis membuat `Redirect` 301** dari path lama (termasuk anak yang ikut pindah folder), setelah konfirmasi.
- Keunikan slug per folder lintas `Layanan`, `LayananDetail`, `ProgramPelatihan` ditegakkan oleh unique index `routes.full_path` (§6.6); observer menangkap pelanggaran unik dan menampilkannya sebagai error validasi field `slug`.
- **Siklus Redirect migrasi** (observer): saat entri dengan `legacy_path` dipublish, Redirect `dari_path = legacy_path` di-update `ke_path` = URL entri bila berbeda, atau dinonaktifkan bila sama; saat `KategoriLayanan` baru (mis. `sertifikasi-personel`) dipublish, semua Redirect `sumber=migrasi` yang menunjuk hub sementara diarahkan ulang ke hub baru. `GenerateRedirects` meresolusi target akhir agar tidak ada chain.
- **Invalidasi cache (aturan umum)**: setiap transisi `status`/`mode`/`slug`/parent pada entri apa pun — manual atau oleh scheduler — menghapus cache entri itu, rantai induknya (L3 → hub kategori → landing `/layanan/`), dan sitemap; perubahan singleton global (`SiteSettings`, `Navigasi`, `BlokGlobal`) menjalankan `responsecache:clear` penuh karena navbar/footer ada di semua halaman. US-02 "tampil di induk ≤ 60 detik" dipenuhi oleh aturan ini.

### 6.6 Routing & pelestarian URL lama

**Keputusan (rekonsiliasi):** dokumen Arsitektur mengusulkan URL bersih tanpa `.html` + 301 massal; dokumen Content Model dan permintaan PRD ini mensyaratkan **URL lama dipertahankan**. Dipilih **pelestarian 1:1** karena (a) nol risiko redirect chain/hilang ranking, (b) tautan yang sudah beredar di brosur/WA tetap bekerja, (c) tidak ada pekerjaan normalisasi slug yang memblokir launch. Keputusan ini **bukan pertanyaan terbuka** (dihapus dari §14); pindah ke URL bersih adalah keputusan yang bisa dibalik pasca-launch karena resolver berbasis `routes.full_path` + tabel Redirect.

**Resolver (satu mekanisme)**: tabel `routes {full_path unique, routable_type, routable_id, template, status, mode, noindex, updated_at}` diisi observer saat save `KategoriLayanan`, `Layanan`, `LayananDetail`, `ProgramPelatihan`, `Halaman`, `Artikel` (v1). Singleton (`/`, `/tentang.html`, `/produk.html`, `/kontak.html`, `/layanan/`, `/sitemap.xml`, `/robots.txt`, `/preview/*`, `/admin/*`) adalah **route Laravel eksplisit** yang didaftarkan sebelum catch-all. Urutan pencarian: route eksplisit → `routes` (status published) → `redirects` (aktif) → 404 custom. Unique index `full_path` sekaligus menegakkan keunikan slug per folder.

| Pola URL (dipertahankan persis) | Tipe | Catatan |
|---|---|---|
| `/`, `/index.html` | Beranda | `/index.html` 301 → `/` |
| `/tentang.html`, `/produk.html`, `/kontak.html` | singleton | suffix `.html` = canonical |
| `/layanan/{kategori}/index.html` | KategoriLayanan | `/layanan/{kategori}/` 301 → `index.html` (satu URL per halaman) |
| `/layanan/{kategori}/{slug}.html` | Layanan / LayananDetail / ProgramPelatihan | satu baris `routes` per entri |
| `/layanan/` | HalamanLayanan | **baru** |
| `/berita/`, `/berita/{slug}` | Artikel | **baru** (v1), tanpa `.html` |
| `/{slug}.html` | Halaman | baru (legal) |
| `/kontak/kirim` (POST), `/kontak/terima-kasih` | form kontak | **baru**, `noindex` |
| `/preview/{tipe}/{id}` | preview | login wajib (MVP), `noindex`, tidak di-cache |
| `/sitemap.xml`, `/robots.txt`, `/admin` | sistem | sitemap dirender on-demand dari `routes` (cache 1 jam, dihapus oleh aturan invalidasi §6.5) |
| `/assets/img/...` | Media | nama file lama (dengan spasi/`&`) dipetakan via Redirect ke file baru karena mungkin terindeks Google Images |

Aturan slug: regex `^[a-z0-9]+(?:-[a-z0-9]+)*$`, ≤80 karakter, bukan `index`. Saat migrasi slug diisi **persis** dari nama file lama termasuk yang tidak konsisten; perapian (mis. `inhouse-training-39001` → `inhouse-training-iso-39001`) adalah tugas editorial pasca-launch dengan 301 otomatis.

Anomali yang didukung: (1) `jasa-surveillance-audit-lab` & `jasa-resertifikasi-audit-lab` → entri `Layanan` kategori Akreditasi (draft) + 301 path lama → hub akreditasi (saat draft dipublish, Redirect di-update ke URL barunya, §6.5); (2) 5 stub sertifikasi personel → kategori baru `sertifikasi-personel` (draft) + 301 → hub pelatihan-akreditasi (diarahkan ulang otomatis saat kategori dipublish); (3) 7 slug QHSE: satu entri, satu URL, dua parent; breadcrumb & canonical selalu parent utama = parent dengan `Layanan.urutan` terkecil (Konstruksi); `parent_tambahan` hanya menampilkan kartu di grid induk kedua.

Breadcrumb dan JSON-LD `BreadcrumbList` dihitung dari relasi. `sitemap.xml` memuat entri `published` + `mode=normal` + `noindex=false`.

---

## 7. Fitur Admin CMS

Admin panel: **Filament 4** di `/admin`, seluruh label Bahasa Indonesia (istilah teknis slug/SEO/draft/publish dipertahankan).

### 7.1 Navigasi sidebar

```
Dasbor           lead baru 7 hari · draft · halaman "Segera Hadir" · checklist migrasi "Perlu Review"
Kotak Masuk Lead [badge baru] Semua / Baru / Dihubungi / Selesai / Spam
Layanan          Kategori Layanan · Layanan (L3) · Detail Layanan (L4) · Program Pelatihan · Standar
                 (tiga Resource terpisah dengan filter kategori/induk/status/template/mode;
                  tampilan tree 4 level lintas model = v1)
Berita & Insight (v1)  Artikel · Kategori Artikel
Halaman          Beranda · Tentang Kami · Halaman Produk · Kontak · Halaman Layanan · Halaman Generik
Konten Pendukung Klien & Logo · Testimoni · FAQ · Produk Digital
Pustaka Media
Pengaturan [Admin] Identitas Situs · Kontak & Footer · Navigasi · Teks Default Global ·
                 SEO Default · Notifikasi Lead · Redirect · Pengguna & Peran · Log Aktivitas
```

Pemetaan item sidebar → singleton/model §6: Identitas Situs, Kontak & Footer, SEO Default, Notifikasi Lead = empat tab dari `SiteSettings` (`nama_situs`…`og_image_default` / `alamat_*`…`tautan_legal` / `seo_default`, `robots_txt`, `analytics_id` / `email_tujuan_form`); Navigasi = `Navigasi`; Teks Default Global = `BlokGlobal`; Pustaka Media = `Media`; Kotak Masuk Lead = `PengirimanKontak`; Log Aktivitas = `spatie/laravel-activitylog`.

**Glosarium istilah** (label UI Bahasa Indonesia; istilah teknis dipertahankan): Kotak Masuk Lead (= Lead Inbox), Pustaka Media (= Media Library), Pengaturan Situs (= SiteSettings), Log Aktivitas (= Activity Log), Tempat Sampah (= Trash/soft delete), "Segera Hadir" (= `mode=coming_soon`), Ganti File (= replace file), person-week (pw) = 1 orang × 5 hari kerja. Istilah `slug`, `draft`, `publish`, `SEO`, `redirect`, `preview` dipakai apa adanya.

Lintas halaman: tombol "Lihat Situs"/"Lihat Halaman Ini"; **bar admin di situs publik** saat login dengan tombol "Edit halaman ini" (fitur paling berguna bagi staf non-teknis: temukan typo → Edit → publish). Bar admin **tidak** dirender di HTML halaman (yang di-cache untuk publik) melainkan disuntik oleh skrip kecil yang memanggil `GET /admin/bar?path=` setelah load; tanpa sesi admin endpoint mengembalikan 204. Pencarian global Ctrl+K: v1.

### 7.2 Editor halaman (form terstruktur)

- Setiap tipe halaman = form dengan tab: **Konten · Daftar Anak · SEO · Pengaturan**. Repeater dengan drag-order dan batas min/maks sesuai **tabel batas kanonik §6.2**.
- **Pemilih induk** dua Select bertingkat (Kategori → Layanan, `dependsOn`) saat membuat L3/L4; template & `jenis_layanan` diwarisi dari induk.
- **Lookup Standar** dengan tombol "+ Tambah standar baru" inline (`createOptionForm` Filament: kode, nomor, tahun, nama sistem, singkatan).
- **Prefill dari pola** (`pola_judul_anak`, `pola_slug_anak`, `proses_default_*`, `cta_band_leaf_iso`) — semua bisa ditimpa; field dengan token tampil sebagai preview terisi.
- **Link picker** (internal bertingkat / eksternal / anchor / WhatsApp / email / telepon) — mencegah link salah seperti "Lihat Semua Pelatihan" → hub sertifikasi.
- **Icon picker** Heroicons Outline via `guava/filament-icon-picker`; SVG kustom: v1.
- Rich text (TipTap/Filament RichEditor) terbatas untuk konten layanan (p, bold, italic, link, list, h3); penuh untuk artikel/halaman generik (h2–h4, kutipan, tabel, gambar dari Media Library dengan alt+caption, embed YouTube, tombol CTA, callout). Paste dari Word/Google Docs dibersihkan. Tidak ada H1 (judul = H1), tidak ada HTML mentah untuk Editor.
- **Checklist validasi sebelum publish**: judul, slug unik, meta description (aturan §6.2: blokir hanya entri buatan CMS), alt gambar hero, tautan internal (`Tautan.target_entri`) menunjuk entri published, repeater memenuhi batas §6.2. Memblokir publish, tidak memblokir save draft. Pemindaian link di dalam richtext dan gambar bertag `placeholder`: v1.
- Status: `draft → published → archived` (status `review`: v1); flag `mode = coming_soon` terpisah dengan badge jam kuning di daftar.
- Soft delete ke Tempat Sampah 30 hari; entri yang masih dirujuk (FK `RESTRICT`) tidak bisa dihapus permanen.

### 7.3 Pustaka Media

**Arsitektur (keputusan)**: `spatie/laravel-medialibrary` memodelkan media sebagai lampiran milik satu model, bukan pustaka bersama. Karena itu dibuat tabel `media` sendiri dengan model `Media` yang **sendiri** meng-implement `HasMedia` dari spatie hanya untuk pipeline konversi (WebP/srcset/thumb). Field konten bertipe `media` menyimpan `media_id` (FK, `ON DELETE RESTRICT`). Tidak ada plugin Filament berbayar.

- Upload drag-and-drop multi-file; JPG/PNG/WebP/SVG(disanitasi, Admin)/PDF; ≤5 MB gambar, ≤20 MB PDF; gambar di-re-encode (menghapus payload tersembunyi).
- Normalisasi nama file → slug (`konsultasi-sertifikasi-iso.jpeg`); nama asli tersimpan.
- Konversi otomatis: WebP 480/960/1440 + thumb; logo klien tinggi 72px; `<x-img>` mengeluarkan `<picture>` + `srcset` + `width/height` + `loading="lazy"` (hero: `fetchpriority="high"`).
- Metadata: alt wajib (logo klien: alt = nama klien otomatis), caption, folder.
- **Ganti file** mempertahankan `media_id` → semua halaman ikut berubah (satu baris update + konversi ulang; murah karena tabel sendiri).
- Hapus media yang masih dirujuk field terstruktur ditolak oleh constraint DB untuk semua peran (pesan: "Media masih dipakai").
- Picker modal di setiap field gambar dengan rekomendasi ukuran ("Hero: min 1920×1080").
- Laporan "alt kosong" di dasbor migrasi.
- **v1**: tabel `media_usages` (FK + hasil pemindaian richtext saat save) → filter "tidak terpakai" / "dipakai di halaman X", konfirmasi hapus dengan daftar dampak untuk Admin, focal point, tag, laporan "gambar placeholder".

### 7.4 Menu & navigasi

- `Navigasi.menu_utama` repeater 2 level (Filament Repeater bersarang, `reorderable()`), tanpa plugin tree. Migrasi: Beranda, Layanan (→ `/layanan/`), Produk, Tentang Kami; CTA "Hubungi Kami".
- **v1**: item `mega_layanan` membangun panel mega menu dari `KategoriLayanan` → `Layanan` published (fitur **baru**; situs lama tidak memilikinya, §2.3).
- Tab kategori layanan di hub dibangun dari `KategoriLayanan.urutan`.
- Simpan Navigasi/SiteSettings/BlokGlobal = langsung terapkan + `responsecache:clear`; preview sebelum terapkan tidak dibangun (nilai kecil, biaya besar: renderer publik butuh mode draft untuk navbar/footer).

### 7.5 Lead Inbox

- Daftar: tanggal, nama, telepon (→ `wa.me`), email (→ `mailto`), keperluan (badge), halaman asal, status; baris `baru` ditebalkan; badge sidebar = `count(status=baru)` dihitung per request (bawaan Filament `getNavigationBadge`), tanpa polling.
- Filter status/keperluan/tanggal/halaman asal; pencarian nama/telepon/email/pesan.
- Detail: semua field, aksi cepat "Chat WhatsApp" (pesan pra-isi "Halo {nama}, terima kasih sudah menghubungi INOVASS terkait {keperluan}…"), "Balas Email", "Tandai Spam"; catatan internal (timeline), log perubahan status (Activity Log). Assign ke user: v1.
- Ekspor CSV dengan filter aktif (Admin; Viewer v1; Excel tidak dibangun). Retensi 24 bulan lalu hapus otomatis (UU PDP); hapus manual oleh Admin tercatat di Log Aktivitas.
- Widget dasbor (v1): lead per minggu, per keperluan, per halaman asal. MVP: angka "lead baru 7 hari" di Dasbor.
- Notifikasi: email (MVP, queue, `Reply-To` pengirim), WhatsApp Business API via provider Fonnte/Wablas/Twilio (v1, toggle di Notifikasi Lead); kegagalan ditandai dan bisa dikirim ulang.

### 7.6 Preview & publish

- Preview di tab baru (`/preview/{tipe}/{id}`, login wajib) dengan banner "MODE PREVIEW – belum dipublikasikan", toggle desktop/tablet/mobile, `noindex`, tidak di-cache. Link berbagi tanpa login (`preview_token`, 7 hari, bisa dicabut dengan regenerate): v1 (US-06).
- Publish terjadwal (`scheduled_publish_at`); scheduler tiap menit menjalankan transisi → aturan invalidasi §6.5. Unpublish terjadwal: v1.
- Model simpan-langsung (§6.1): tidak ada draft terpisah di atas entri published; singleton selalu published. Draft/published ganda (`draft_data`) + riwayat versi: v1.
- Riwayat versi (v1): snapshot JSON per save, 30 terakhir, Bandingkan + Pulihkan; autosave 30 detik; soft lock.
- Publish memicu aturan invalidasi §6.5 (cache entri + rantai induk + sitemap) dan pembuatan Redirect bila slug berubah. Sitemap dirender on-demand dari `routes` dengan cache; tidak ada job regenerasi.

### 7.7 SEO fields

Komponen `SEO` di setiap tipe halaman (§6.2) dengan pratinjau snippet Google dan hitungan karakter; `SiteSettings.seo_default` untuk pola title dan OG default; `robots_txt` editable (hanya berlaku di produksi); `noindex` otomatis untuk `coming_soon` dan preview.

### 7.8 Dashboard migrasi "Perlu Review"

Checklist yang bisa dicentang per item dengan tautan langsung ke form: entri `migrasi_perlu_review = true` (10 halaman ISO dengan CTA 9001, IMS "sistem manajemen mutu", 14001:2026, LSP "Person", 19 Penyusunan Dokumen, judul pranata lab yang menyimpang dari prefill, logo klien tanpa nama, dll.), laporan nama standar tidak kanonik (tawarkan ganti massal ke `Standar.label_tampilan`), alt kosong, halaman tanpa meta description, kartu bento tanpa tautan. Gambar placeholder & link rusak di richtext: v1.

---

## 8. Fitur Website Publik

### 8.1 Template Blade (8 di MVP: `home`, `page`, `contact`, `hub`, `daftar`, `detail-jasa`, `detail-pelatihan`, `coming-soon`; `post` di v1)

| Template | Dipakai oleh | Section |
|---|---|---|
| `home` | Beranda | 12 section sesuai §6.3, dirender hanya yang `aktif`; marquee & testimoni diduplikasi template via CSS |
| `page` | TentangKami, HalamanProduk, Halaman generik | hero + isi + CTA band |
| `contact` | Kontak | hero + info (tel:/mailto:) + form + peta + (CTA band opsional) |
| `hub` | KategoriLayanan, HalamanLayanan | hero → tab 7(+1) kategori → h2 + intro + grid kartu `<a>` (ikon, judul, blurb, "Lihat Detail", badge "Segera") → CTA band hub |
| `daftar` | Layanan (`daftar_sub_layanan`, `format_pelatihan`, `konten_bebas`) | header gelap + breadcrumb 4 level → intro 2 kolom → [keunggulan 6] → h3 + grid kartu anak `<a>` aksen `i mod 3` [+ search box bila `daftar_filter_aktif`] → CTA band detail |
| `detail-jasa` | LayananDetail | highlight 3 → pengertian → manfaat → CTA inline → proses N (nomor benar) → target [+ penutup] → [FAQ] → [unduhan] → [CTA band bila `cta_band.aktif`; sub-akreditasi migrasi: non-aktif] |
| `detail-pelatihan` | ProgramPelatihan | highlight 3 → tentang → manfaat → CTA inline → materi → peserta [+ penutup] → [jadwal/biaya v2] → CTA band (varian per parent, §6.4) |
| `post` (v1) | Artikel + index `/berita/` | breadcrumb, sampul, penulis, tanggal `17 Oktober 2026`, daftar isi (opsional), isi, artikel terkait, layanan terkait, share WA/LinkedIn; index dengan pagination 12 + filter kategori; RSS |
| `coming-soon` (mode) | entri apa pun `mode = coming_soon` | header + `BlokGlobal.coming_soon`; tombol "Kembali ke Layanan" → hub kategori |

Komponen bersama: `<x-navbar>` (tautan polos dari `Navigasi`, hamburger `<button aria-expanded>`; mega menu v1), `<x-footer>`, `<x-cta-band>`, `<x-page-hero>`, `<x-detail-header>`, `<x-breadcrumb>`, `<x-seo>`, `<x-json-ld>`, `<x-img>`, `<x-whatsapp-float>` (v1), halaman 404 custom.

### 8.2 SEO

- `<html lang="id">`; `<title>` ≤60 pola `{Judul} — INOVASS`; meta description (fallback: ringkasan/paragraf pertama; L4: pola "Jasa konsultasi {service} {standar} oleh INOVASS…"); `canonical`; OG (`og:locale=id_ID`, `og:image` fallback default); Twitter card; favicon + `site.webmanifest`.
- Satu `<h1>`; H1 > 70 karakter dipendekkan di `judul_pendek` dengan judul panjang di `meta_title`.
- `sitemap.xml` dirender on-demand dari tabel `routes` (published, `mode=normal`, `noindex=false`) dengan cache 1 jam yang dihapus oleh aturan §6.5 — tanpa paket tambahan. `robots.txt`: bila `APP_ENV != production` selalu `User-agent: *\nDisallow: /` tanpa membaca DB; di produksi dari `SiteSettings.robots_txt`.
- JSON-LD: `Organization` + `BreadcrumbList` (semua halaman); `Service` (Layanan, LayananDetail); `Service` untuk ProgramPelatihan di MVP → `Course` di v2 saat ada durasi/jadwal; `FAQPage` (beranda, LayananDetail dengan FAQ); `Article` (v1). Validasi 1 sampel per tipe dengan Rich Results Test.
- Semua kartu navigasi `<a href>`; sosial `href="#"` tidak pernah dirender.

### 8.3 Form kontak + WhatsApp

- Field: nama, email, telepon (regex `^(\+62|62|0)8[0-9]{7,11}$`), organisasi (opsional), keperluan (dari `form_opsi_layanan`; prefill dari `?layanan=`), pesan ≤2000, consent (link Kebijakan Privasi). Label terlihat, `autocomplete`, error via `aria-describedby`.
- Endpoint: `POST /kontak/kirim` (form HTML biasa, CSRF). Gagal validasi → 422 `redirect()->back()->withErrors()->withInput()`; sukses → `GET /kontak/terima-kasih?ref={id}` (`noindex`). JavaScript wajib untuk token Turnstile; `<noscript>` menampilkan nomor WA + email.
- Anti-spam: honeypot `spatie/laravel-honeypot` (+ waktu minimum 3 detik), Cloudflare Turnstile (selalu aktif), rate limit 5/10 menit & 20/hari per IP, CSRF, validasi server. **IP klien asli**: `TrustProxies` dipercaya untuk daftar IP Cloudflare dan membaca `CF-Connecting-IP` (atau `real_ip` dari Nginx); tanpa ini seluruh pengunjung berbagi IP Cloudflare dan kuota 20/hari mematikan form. Test memverifikasi rate limiter memakai IP dari header tersebut.
- Alur: simpan `PengirimanKontak` (di luar transaksi apa pun) → `try { dispatch email } catch → notifikasi_status=gagal` (juga pada queue `sync`) → halaman sukses + tombol "Lanjutkan chat via WhatsApp" (`wa.me/{whatsapp_nomor}?text=` pra-isi berisi ringkasan). Form dapat disematkan di LayananDetail/ProgramPelatihan (v2) dengan `entri_terkait` terisi.
- Tautan WA di footer/kontak memakai `whatsapp_nomor` + `whatsapp_pesan_default`; event GA4 `click_whatsapp`.
- **WhatsApp float (v1)**: toggle di SiteSettings, pesan "Halo INOVASS, saya ingin berkonsultasi tentang {judul halaman}", tidak tampil di `/kontak.html`; klik dicatat sebagai event.

### 8.4 Perilaku UI yang dipertahankan / diperbaiki

Dipertahankan: navbar transparan → pill putih setelah scroll, hero zoom, reveal, counter statistik, marquee logo, testimoni autoscroll, FAQ accordion, menu "Layanan" sebagai tautan polos. Diperbaiki: kartu `div onclick` → `<a>`; nomor langkah dari posisi; `prefers-reduced-motion` mematikan marquee/pulse/zoom; kontras hijau di latar putih memakai `#00a877`; skip link, focus ring, Esc menutup menu; iframe peta ber-`title`. Ditambahkan (baru): landing `/layanan/`, halaman sukses form, bar admin; **v1**: mega menu "Layanan" (tidak pernah ada di situs lama), WhatsApp float.

---

## 9. Arsitektur & Tech Stack

### 9.1 Rekomendasi utama: Laravel 13 + Filament 4 (monolit SSR)

**Keadaan awal repo (fakta, 17 Okt 2026)**: folder proyek berisi `PRD.md` dan scaffold `_app/` hasil `laravel new` dengan `laravel/framework ^13.17` (lock: v13.37.0), PHP ^8.3, PHPUnit ^12.5 (bukan Pest), tanpa Filament, hanya `app/Models/User.php` + 3 migrasi bawaan + `tests/Feature/ExampleTest.php`. **Keputusan**: kode hidup di `_app/` (tidak di-rename; `_app/` = root aplikasi di semua rujukan struktur repo di bawah), versi Laravel = yang sudah terpasang (13.x, tidak di-downgrade), test runner = **PHPUnit 12 bawaan** (Pest tidak ditambahkan). Filament 4 dipasang di hari pertama Fase 0; bila constraint composer Filament belum mendukung Laravel 13.x, dipakai rilis Filament terbaru yang mendukungnya dan versinya dicatat di `CLAUDE.md`.

| Lapisan | Pilihan | Alasan |
|---|---|---|
| Framework | Laravel 13 (terpasang di `_app/`), PHP 8.3 | Satu aplikasi, satu bahasa; jalan di VPS Rp 100 rb-an maupun cPanel/LiteSpeed yang sekarang dipakai; talent PHP paling banyak di Indonesia; konvensi jelas untuk Claude Code |
| Admin | Filament 4 + `spatie/laravel-activitylog` (Log Aktivitas old/new per field) + `guava/filament-icon-picker` (icon picker Heroicons) | CRUD + relasi + Repeater bersarang `reorderable()` + rich editor + file upload + MFA TOTP bawaan. **Tidak bawaan** dan karena itu tidak dipakai di MVP: tree drag-drop lintas level, Resource lintas model (tree 4 level), global search sampai media, browser media pusat (dibangun sendiri, §7.3). Tanpa plugin berbayar |
| DB | MySQL 8 / MariaDB 10.11 (SQLite untuk dev) | beban tulis rendah; `SESSION_DRIVER=database` |
| Front-end | Blade SSR + Tailwind 4 (target CSS ≤40 KB gzip) + vanilla JS ≤15 KB gzip | HTML murni untuk SEO; menggantikan ±8.000 baris CSS lama + inline; warna = token statis |
| Media | tabel `media` sendiri + `spatie/laravel-medialibrary` (hanya pipeline konversi pada model `Media`) + Intervention Image | §7.3 |
| Cache | `spatie/laravel-responsecache` driver file dengan **profile kustom**: `shouldCacheRequest` = `GET` ∧ `!auth()->check()` ∧ path bukan `/kontak*`, `/preview/*`, `/admin/*`, `/sitemap.xml`; **cache key = path tanpa query string** (`?utm_*`, `?layanan=` dan query lain diabaikan; tidak ada fitur `?dari=`) sehingga tidak ada ledakan entri cache; invalidasi sesuai §6.5 | beban ≈ file statis; Redis tidak dipasang |
| SEO | komponen `<x-seo>`/`<x-json-ld>`; sitemap on-demand dari `routes` (§6.6) | tanpa `spatie/laravel-sitemap` |
| Form | `spatie/laravel-honeypot`, Turnstile, rate limiter bawaan (IP dari `CF-Connecting-IP` via `TrustProxies`), queue mail | |
| Backup | `spatie/laravel-backup` → Cloudflare R2 | |
| Ikon | `blade-heroicons` | set yang sudah dipakai situs lama |
| Font | self-host Plus Jakarta Sans + Inter (woff2 subset Latin, `font-display: swap`, ≤60 KB) | menghapus 2 request Google Fonts yang lambat di seluler Indonesia |
| Kualitas | Pint, Larastan level 5, PHPUnit 12, Lighthouse CI | |

**Pemetaan entitas §6 → kelas/tabel** (aturan §6.1: kolom DB & kunci fixture = nama field Indonesia; kelas = Inggris):

| Entitas §6 | Model PHP | Tabel |
|---|---|---|
| `SiteSettings`, `Navigasi`, `BlokGlobal`, `Beranda`, `TentangKami`, `Kontak`, `HalamanProduk`, `HalamanLayanan` | `Singleton` (satu model, `key` enum) | `singletons` |
| `KategoriLayanan` | `ServiceCategory` | `service_categories` |
| `Layanan` | `Service` | `services` |
| `LayananDetail` | `ServiceItem` | `service_items` (+ pivot `service_item_parents` untuk `parent_tambahan`) |
| `ProgramPelatihan` | `TrainingProgram` | `training_programs` (+ pivot `training_program_standards`) |
| `Standar` | `Standard` | `standards` |
| `Halaman` | `Page` | `pages` |
| `Produk` | `Product` | `products` |
| `Klien` | `Client` | `clients` |
| `Testimoni` | `Testimonial` | `testimonials` |
| `FAQ` | `Faq` | `faqs` |
| `KategoriArtikel` / `Artikel` (v1) | `PostCategory` / `Post` | `post_categories` / `posts` |
| `PengirimanKontak` | `ContactSubmission` | `contact_submissions` |
| `Redirect` | `Redirect` | `redirects` |
| `Media` | `Media` | `media` |
| (resolver) | `Route` | `routes` |

Struktur repo (di dalam `_app/`):

```
_app/
├── app/Models/            Singleton, ServiceCategory, Service, ServiceItem, TrainingProgram, Standard, Page,
│                          Product, Client, Testimonial, Faq, Post, PostCategory, ContactSubmission, Redirect, Media, Route, User
├── app/Filament/          Resources (1 per model), Pages/ (singleton per key), Widgets/ (lead baru, perlu review)
├── app/View/Components/   Navbar, Footer, CtaBand, PageHero, DetailHeader, Breadcrumb, Seo, JsonLd, Img
├── app/Http/Controllers/  PageController (resolver routes → template), ContactController, SitemapController,
│                          RobotsController, PreviewController, AdminBarController
├── app/Console/Commands/  ImportLegacy, GenerateRedirects, AuditRedirects, AuditLinks
├── database/fixtures/legacy/   JSON hasil ekstraksi — DI-COMMIT
├── resources/views/{layouts,templates,components}/
├── resources/css/app.css · resources/js/app.js
├── scripts/crawl/         crawler Python (href + onclick)
└── tests/Feature/         smoke semua URL, redirect audit, rate limit, mailer gagal; Lighthouse CI di GitHub Actions
```

Routing: route eksplisit singleton/sistem → satu catch-all `GET /{path}` → `PageController` mencari `routes.full_path` (§6.6) → `redirects` → 404 custom. Template dari kolom `template`; `mode = coming_soon` merender blok Coming Soon.

### 9.2 Alternatif: Astro 5 + Keystatic (git-based, output statis)

Cocok bila INOVASS hanya mengedit konten beberapa kali per bulan, tidak butuh Lead Inbox (form via Web3Forms/Formspree ke email), dan nyaman dengan "Save → tunggu build 1–2 menit". Hasil file statis bisa di-upload ke `public_html` mana pun atau Cloudflare Pages gratis; Lighthouse 100 hampir otomatis; effort ≈ 70% opsi Laravel. Konsekuensi: ±575 file MDX, reorder/relasi lebih canggung, v2 (jadwal + pendaftaran) butuh backend tambahan.

Ditolak: Next.js + Payload (butuh Node + Postgres, tidak bisa cPanel, over-engineered), Strapi + Next.js (dua aplikasi), WordPress + ACF (lebih banyak plugin daripada kode, security surface besar, tetap menulis theme PHP).

### 9.3 Hosting & deployment

| Komponen | Produksi (rekomendasi) |
|---|---|
| Server | VPS Ubuntu 24.04, 2 vCPU / 2 GB / 40 GB SSD, region Jakarta (IDCloudHost, Biznet Gio) atau Singapura (DO/Vultr); ±Rp 150 rb/bulan |
| Web | Nginx + PHP 8.3-FPM, `client_max_body_size 20m`, `set_real_ip_from` daftar IP Cloudflare + `real_ip_header CF-Connecting-IP`; Cloudflare Free di depan (TLS Full strict, cache aset, proteksi bot) |
| Proses | cron `schedule:run` tiap menit; `queue:work` via systemd (fallback `sync`) |
| Deploy | GitHub Actions → SSH: `git pull && composer install --no-dev && php artisan migrate --force && php artisan optimize && responsecache:clear`; Vite di-build di CI, **bukan di server** |
| Lingkungan | Lokal: Laravel Herd for Windows + SQLite; Staging: `staging.inovass.com` (basic-auth, `Disallow: /`); Produksi: `inovass.com` (`www` → 301 apex) |
| Monitoring | UptimeRobot (ping 5 menit), log Laravel, Cloudflare analytics |

Fallback shared hosting cPanel (LiteSpeed): PHP ≥ 8.3, document root → `/laravel/public`, `vendor/` di-upload hasil `composer install` lokal, queue `sync` (kegagalan SMTP ditangkap `try/catch` di `ContactController`, §8.3), cache `file`, cron cPanel, image conversion dibatasi 4000 px, backup JetBackup + R2.

Cut-over: staging lolos QA (§10.5) + budget Lighthouse → daftar Google Search Console (verifikasi DNS) → TTL DNS 300 s sehari sebelum → arahkan DNS ke Cloudflare → VPS → submit sitemap → `audit:redirects` → pantau GSC 4 minggu; hosting lama dijaga 30 hari untuk rollback.

---

## 10. Migrasi Konten

### 10.1 Tahap 0 — Crawl ulang situs live (1–2 hari)

Base URL target: `https://inovass.com/` (tanpa kredensial; semua halaman publik). Hasil crawl pertama (97 HTML + 6 sampel + 8 catatan inventaris) tersimpan hanya di scratchpad sesi analisis dan **tidak ada di repo**; Fase 0 meng-crawl ulang dari nol dan meng-commit hasilnya ke `scripts/crawl/out/`. Skrip Python di `scripts/crawl/` (requests + selectolax) mengikuti **`href` dan `onclick="window.location='…'"`** (penyebab crawl pertama hanya menangkap 97 dari ±540). Output `scripts/crawl/out/{path}.html` + `manifest.json` (url, status, template-signature, daftar semua parent-dari-mana-ditemukan) + semua `assets/img/*`. URL 404 masuk daftar "broken link lama". Crawler adalah **sumber kebenaran jumlah halaman**.

**Laporan Fase 0 (wajib sebelum Tahap 2)**: `scripts/crawl/report.md` berisi (a) jumlah halaman per template hasil klasifikasi §10.2, dibandingkan dengan ekspektasi (±295 `iso-detail`, ±185 `training-detail`, 37 L3, 8 hub, 20 stub) — selisih > 5% menghentikan pipeline untuk diperiksa; (b) **min/maks jumlah item per repeater** (highlight, manfaat, langkah, target/peserta) per template, karena ±139 leaf sertifikasi dan ±117 sub-akreditasi belum pernah diinventaris isinya; batas §6.2 disesuaikan bila ada nilai di luar batas.

### 10.2 Tahap 1 — Klasifikasi template (otomatis)

| Template | Penanda DOM (urutan pengecekan) |
|---|---|
| `home/about/contact/product` | 4 path eksplisit (`/index.html`, `/tentang.html`, `/kontak.html`, `/produk.html`) |
| `coming-soon` | `.coming-soon-section` |
| `hub` | `.nav-tabs-card` / `.nav-tabs-section` |
| `training-detail` | `.iso-benefit-highlight` + heading `h2` berteks "Materi Training"/"Materi Pelatihan" — **dicek sebelum `iso-detail`** karena kelima sampel program pelatihan juga memuat `.iso-process-section` (hl=2, proc=3 hit per file) |
| `iso-detail` | `.iso-benefit-highlight` + `.iso-process-section` **dan tidak ada** heading "Materi" (sampel `akreditasi-iso-17025`: highlight + process, 0 "Materi") |
| `training-format` | `.product-details-section` + section keunggulan 6 item |
| `service-list` | `.product-details-section` tanpa `.iso-benefit-highlight` |

Asersi setelah klasifikasi: jumlah per template harus cocok dengan ekspektasi laporan Fase 0 (§10.1); `training-detail` ≈ 185 dan `iso-detail` ≈ 295, tidak boleh 0 `training-detail`.

### 10.3 Tahap 2 — Ekstraksi ke fixture JSON (3–4 hari)

Satu ekstraktor per template → `database/fixtures/legacy/{template}/{old-path}.json`. **Kunci JSON = nama field §6 persis** (snake_case Indonesia) ditambah `_meta {legacy_path, template, parents[], extracted_at}`. Jumlah item repeater diambil **apa adanya** dari DOM (bukan hard-coded 3/6/6/9); laporan Fase 0 (§10.1) yang memverifikasi rentangnya. Field yang tidak ada = `null` dan dicatat di `_gaps.csv` (meta description semua halaman, CTA salin-tempel, dll.) → daftar kerja penulis konten, bukan blocker.

**Selektor DOM per field (4 template utama)**:

| Field §6 | `iso-detail` (sertifikasi, penyusunan dokumen, sub-akreditasi) | `training-detail` |
|---|---|---|
| `judul` / `label_breadcrumb` | `h1.detail-page-title` / crumb terakhir `.detail-header-section` | sama |
| `highlight_judul`, `highlight[]` | `.iso-benefit-highlight h2.benefit-highlight-title`, `.benefit-highlight-card > p` (`<br>` → spasi) | sama |
| `pengertian_*` / `tentang_*` | `.pengertian-card h2.iso-content-title`, `p.iso-content-desc` (`<strong>` pertama → `pengertian_istilah`) | `h2` + `p` setelah highlight |
| `manfaat_judul`, `manfaat[]` | `.iso-benefit-section h2`, `.iso-benefit-modern-card` (h3 → judul, p → teks) | sama |
| inline CTA | `.iso-cta-section` (teks `p`/`h2` + tombol) → dicocokkan ke `inline_cta_*`; selisih → `inline_cta_override` | sama |
| `proses_judul`, `proses[]` / `materi_*` | `.iso-process-section h2.iso-process-title`, `.iso-process-step` (angka dari `.process-step-number`, h3, p, `.process-substeps p` → `sub_langkah`) — **urut naik berdasarkan angka badge**, bukan urutan DOM | sama, section ber-heading "Materi Training" |
| `target_*` / `peserta_*` | `.iso-target-section h2`, `p` intro, `.iso-target-card > h4`, `p.iso-target-footer` / paragraf "Cocok untuk" → `target_penutup` | `h2` "Peserta yang Cocok…", intro `p`, `h4` kartu, paragraf `<strong>Cocok untuk:</strong>` → `peserta_penutup` |
| `cta_band` | `section.page-cta` (h2 + `<em>` + p + tombol); tidak ada → `aktif=false` | `section.page-cta` |
| `seo.meta_title` | `<title>` | `<title>` |

`service-list`/`training-format` (L3): `h1.detail-page-title`, `.detail-content-intro` (`h2.intro-main-title` → `intro_judul`, `p` → `intro_teks`), `.product-details-section` (`h3.product-details-title` → `daftar_judul`, `p` → `daftar_deskripsi`, `.product-detail-item` → daftar anak dengan `href`), section keunggulan 6 kartu (`training-format`). `hub`: `.nav-tabs-card` (tab), `h2` + `p` intro, `.service-item-card` yang **terlihat** (blok `display:none` dilewati) → `kartu_*` anak.

Contoh fixture minimal `iso-detail/layanan__sertifikasi-organisasi__iso-9001.json`:

```json
{
  "_meta": {"legacy_path": "/layanan/sertifikasi-organisasi/iso-9001.html", "template": "iso-detail",
            "parents": ["/layanan/sertifikasi-organisasi/jasa-sertifikasi-iso.html"]},
  "slug": "iso-9001", "judul": "…", "label_breadcrumb": "ISO 9001",
  "standar": {"kode": "ISO 9001"},
  "highlight_judul": "…", "highlight": [{"teks": "…"}, {"teks": "…"}, {"teks": "…"}],
  "pengertian_judul": "…", "pengertian_istilah": "…", "pengertian_isi": "<p>…</p>",
  "manfaat_judul": "…", "manfaat": [{"judul": "…", "teks": "…"}],
  "inline_cta_gunakan_default": true,
  "proses_judul": "…", "proses_gunakan_default": false, "proses": [{"judul": "…", "teks": "…", "sub_langkah": []}],
  "target_judul": "…", "target": [{"label": "…"}], "target_penutup": "…",
  "cta_band": {"aktif": true, "gunakan_default": false, "judul": "…", "teks": "…"},
  "seo": {"meta_title": "…", "meta_description": null}
}
```

**Parent utama** untuk entri yang ditemukan dari lebih dari satu induk (7 slug QHSE): parent dengan `Layanan.urutan` terkecil (Konstruksi); induk lain masuk `parent_tambahan`. Normalisasi deterministik yang dicatat di log: nama standar via lookup `Standar`; `14001:2026` → `2015`; `ISO ISO 19100` → `ISO 19100`; "Person" → "Personel"; nama file gambar → slug. Fixture **di-commit**; perbaikan pra-launch dilakukan sebagai PR pada JSON agar import bisa diulang dari nol sampai cut-over.

### 10.4 Tahap 3 — `php artisan import:legacy` (2 hari)

Idempotent (upsert by `legacy_path`). Urutan: Standar → KategoriLayanan → Layanan → LayananDetail/ProgramPelatihan → singleton & Halaman → Klien/Produk/Testimoni/FAQ → Redirect. Gambar disalin, di-rename, di-attach (konversi WebP saat import). Lalu `audit:redirects` + `audit:links`.

**Peta status migrasi per tipe**

| Tipe | Published | Draft | Keterangan |
|---|---:|---:|---|
| KategoriLayanan | 7 | 1 | Sertifikasi Personel |
| Layanan | 37 (28 normal + 9 coming_soon) | 11 + 2 = 13 | 28 lengkap = 11 sertifikasi + 7 akreditasi + 3 + 3 format pelatihan + 4 pranata; 11 stub aturan B (2 + 4 + 5) + 2 kartu personel tanpa halaman; total 50 |
| Standar | ±46 | 0 | termasuk `Etika Penelitian` (lainnya) dan `Permenkes 43/2013` (regulasi) |
| LayananDetail | ±295 | 0 | 38 ter-crawl + 1 sampel, sisanya di-fetch Fase 0 |
| ProgramPelatihan | ±185 | 0 | 5 sampel; `cta_band` varian per parent (§6.4) |
| Halaman | 0 | 2 | privasi, S&K (konten dari tim legal) |
| Produk | 2 | 0 | `gambar_mockup` dari `dcs.png`/`lms.png` (`produk.html`); hanya gambar showcase beranda yang placeholder |
| Klien | 44 | 0 | 1 tanpa nama → `nama="(tidak diketahui)"`, Perlu Review |
| Testimoni | 0 | 5 | menunggu verifikasi |
| FAQ | 6 | 0 | |
| Artikel | 0 | 3 | v1 |
| Redirect | ±15 | – | |

**Aturan stub**: (A) dilink dari kartu hub yang terlihat → published `mode=coming_soon`, `noindex` (9); (B) hanya terjangkau dari blok `display:none` → draft kosong + 301 ke hub kategori (11).

**Pemetaan field wajib tanpa sumber di situs lama** (keputusan import, dikonfirmasi lewat Q9/Q10):

| Target | Nilai import |
|---|---|
| `Beranda.layanan_bento` kartu 1 "Konsultasi & Sertifikasi ISO" | tautan lama `/layanan/sertifikasi-organisasi/index.html` |
| kartu 2 "Konsultasi Akreditasi" (tanpa link) | `/layanan/akreditasi-organisasi/index.html` |
| kartu 3 "Pelatihan Profesional" (tanpa link) | `/layanan/pelatihan-sertifikasi/index.html` |
| kartu 4 "Sertifikasi Kompetensi" (tanpa link; kategori `sertifikasi-personel` masih draft) | `/kontak.html?layanan=sertifikasi` sampai kategori dipublish, lalu diganti manual |
| `Klien.nama` untuk logo ber-alt "Client" | `"(tidak diketahui)"` + `migrasi_perlu_review` |
| `ProgramPelatihan.judul` pranata lab | teks H1 lama apa adanya (§6.4) |

**Peta 301**

| Dari | Ke | Sumber |
|---|---|---|
| `/index.html` | `/` | sistem |
| `/layanan/sertifikasi-organisasi/jasa-surveillance-audit-lab.html`, `…/jasa-resertifikasi-audit-lab.html` | `/layanan/akreditasi-organisasi/index.html` | aturan B |
| `/layanan/pelatihan-sertifikasi/private-training.html`, `pelatihan-auditor-internal-iso`, `pelatihan-implementasi-iso`, `pelatihan-k3-lingkungan` | `/layanan/pelatihan-sertifikasi/index.html` | aturan B (catatan: `private-training-akreditasi` sudah lengkap, bisa diduplikasi sebagai bahan) |
| `/layanan/pelatihan-akreditasi/sertifikasi-auditor-{qms,ems,ohsms,isms}.html`, `sertifikasi-ahli-k3-umum.html` | `/layanan/pelatihan-akreditasi/index.html` (observer §6.5 mengarahkan ulang ke hub `sertifikasi-personel` saat kategori itu dipublish) | aturan B |
| `/layanan/{kategori}/` | `/layanan/{kategori}/index.html` | sistem |
| `/assets/img/layanan%20kami.jpeg` dsb. | file baru slug | rename aset |
| `www.inovass.com/*` | apex | Nginx/Cloudflare |
| Perubahan slug/parent apa pun pasca-launch | otomatis | observer |

Tidak ada redirect chain: `GenerateRedirects` meresolusi target akhir.

### 10.5 Tahap 4 — Konten yang harus ditulis manusia & QA

Minimal sebelum launch: meta description ±50 halaman L1–L2 (L4 pakai pola), hero beranda Bahasa Indonesia, Kebijakan Privasi + S&K (wajib: situs kini menyimpan data pribadi), URL sosial asli, konfirmasi nomor WA, keputusan testimoni/berita (sembunyikan section bila belum ada konten asli).

Perbaikan konten yang menjadi checklist "Perlu Review" (dikerjakan Editor pasca-import; tidak memblokir launch): intro `jasa-sertifikasi-iso` salah konten; CSMS label ganda; `jasa-perawatan` vs `pemeliharaan`; judul 112 karakter surveillance; label QHSE per induk; intro hub Pelatihan Akreditasi; ikon beaker ganda di hub Akreditasi; ISO 14001 edisi; IMS Stage 2; ISO Lainnya "SNI 19-17025"; 5 highlight tanpa prefix "ISO"; 19 Penyusunan Dokumen (judul langkah 3 & 5, kalimat sisa di langkah 4, H2 "Proses Sertifikasi", "Dokumen yang Kami Susun"); `akreditasi-lab-medis` kartu 6 duplikat; LSP "Person"; inspeksi 3 cara penulisan; "lpup"/"PUP"; biobank IEC; in-house "pelatihan terbuka"; 87 "Cocok untuk" campur bahasa; MIPA typo; Sosial prefix; Kedokteran LAMSPAK di Genetika (verifikasi); Kesehatan slug singkatan.

QA otomatis: PHPUnit membaca `manifest.json` (bukan angka di PRD ini) → setiap URL lama 200 atau 301→200; setiap URL baru punya `<title>`, meta description, canonical, satu `<h1>`. Text-diff teks terlihat lama vs baru → laporkan kehilangan > 5%. Manual: 1 sampel per template di mobile & desktop oleh editor klien di staging.

---

## 11. Non-Functional Requirements

### 11.1 Performa (Lighthouse mobile, Slow 4G)

| Metrik | Target | Cara |
|---|---|---|
| LCP | ≤ 2,5 s p75 | hero WebP ≤150 KB `fetchpriority=high` + preload; font ≤60 KB; full-page cache TTFB < 300 ms |
| CLS | ≤ 0,1 | `width/height` semua `<img>`; font `size-adjust`; tanpa banner menyisip |
| INP | ≤ 200 ms | JS ≤15 KB gzip, tanpa framework, animasi CSS |
| TTFB | ≤ 500 ms dari Jakarta | cache + server JKT/SG |
| HTML | ≤ 60 KB/halaman | CSS inline dihapus; marquee diduplikasi CSS |
| CSS | ≤ 40 KB gzip | Tailwind purge |
| Pihak ketiga | ≤ 2 (GA4; Turnstile hanya di kontak) | tanpa Google Fonts/chat widget; skrip bar admin hanya dimuat bila cookie sesi ada |
| Lighthouse | Perf ≥ 90, SEO 100, A11y ≥ 95, BP ≥ 95 | CI 5 URL sampel; PR gagal bila turun > 5 poin |

### 11.2 Keamanan

MFA TOTP (Admin wajib), throttle login bawaan, sesi 8 jam (`SESSION_DRIVER=database`, `EnsureUserActive`), logout semua perangkat saat ganti password; policy per peran; CSRF; honeypot + Turnstile + rate limit per IP klien asli (`TrustProxies` + `CF-Connecting-IP`); `ip_hash` HMAC dengan `APP_KEY`; validasi skema URL `Tautan` dan host persis `peta_embed_url`; validasi server semua input; upload hanya jpg/png/webp/pdf (SVG Admin, disanitasi), re-encode gambar; rich text disanitasi (allow-list TipTap / `mews/purifier`); header HSTS (preload setelah 1 bulan), `X-Content-Type-Options`, `X-Frame-Options: SAMEORIGIN`, `Referrer-Policy`, CSP report-only → enforce dengan nonce GA4/Turnstile; `.env` di luar git, `APP_DEBUG=false`, rotasi `APP_KEY` saat handover; `composer audit` + `npm audit` + Dependabot, patch bulanan; server SSH key only, fail2ban, ufw 22/80/443, unattended-upgrades, MySQL bind localhost; opsional Cloudflare Access untuk `/admin`. Data pribadi: dicantumkan di Kebijakan Privasi, retensi lead 24 bulan, hapus otomatis via scheduler (UU PDP).

### 11.3 Backup & pemulihan

`spatie/laravel-backup` tiap 02:00 WIB (DB + `storage/app/public`) → Cloudflare R2 bucket `inovass-backup`; retensi 7 harian / 4 mingguan / 3 bulanan; notifikasi email bila gagal. Snapshot VPS mingguan. Repo Git = backup kode + fixture. Uji restore sebelum launch dan tiap 6 bulan ke staging. RPO 24 jam, RTO 2 jam; langkah di `docs/RUNBOOK.md`.

### 11.4 Aksesibilitas (WCAG 2.1 AA dasar)

Kartu = `<a href>`; label form terlihat; `aria-expanded/aria-controls` hamburger, Esc menutup, focus trap sederhana; kontras ≥ 4,5:1 (hijau di putih → `#00a877`); alt wajib; satu `h1`, hierarki heading tidak lompat; `title` iframe; `prefers-reduced-motion`; skip link; focus ring terlihat; `lang="id"`. Lighthouse A11y ≥ 95 di CI.

### 11.5 Analytics

GA4 via `gtag.js` (tanpa GTM), ID di SiteSettings, hanya produksi. Event: `click_whatsapp` (footer/float/form), `click_phone`, `click_email`, `submit_contact` (dengan `keperluan`), `click_cta_band` (nama halaman). Google Search Console diverifikasi via DNS. Widget dashboard dari tabel lead sendiri (tidak embed GA API).

### 11.6 Lokal

Satu bahasa `id`; `APP_TIMEZONE=Asia/Jakarta`; Carbon `id` ("17 Oktober 2026"); telepon tampil `+62 813-1117-3707`, link `tel:` dan `wa.me/62…?text=`.

### 11.7 DevEx

`_app/CLAUDE.md` (content model, pemetaan entitas §9.1, konvensi template, perintah, larangan: jangan edit fixture di DB langsung, jangan build Vite di server); Pint + Larastan + PHPUnit via `composer run lint` / `composer test`; CI: lint → test → build → Lighthouse CI → deploy staging (`main`) / produksi (tag `v*`); `DemoSeeder` dari fixture legacy; `docs/EDITOR.md` + pelatihan 2 jam.

---

## 12. Roadmap & Estimasi

Asumsi: 1 developer full-stack Laravel berpengalaman **yang bekerja bersama Claude Code** (asumsi produktivitas: scaffolding Resource/migrasi/template ±2× lebih cepat dari penulisan manual; logika domain, QA, dan koordinasi klien **tidak** dipercepat) + 1 penulis konten paruh waktu dari INOVASS. Satuan person-week (pw) = 5 hari kerja efektif. Angka di bawah adalah estimasi; klien diberi tahu basisnya.

| Fase | Lingkup | Deliverable | Estimasi |
|---|---|---|---:|
| **0 — Fondasi & migrasi data** | `_app/` + Filament + Tailwind + paket §9.1, Herd, CI, staging VPS; crawler penuh + laporan Fase 0; klasifikasi template; ekstraktor 4 template + fixture JSON; `import:legacy`; `GenerateRedirects`; `_gaps.csv` | ±540 halaman lama ter-import ke DB staging (tanpa tampilan) | 2 pw |
| **1 — MVP** (ganti situs lama 1:1, tapi benar) | Semua model §6 kecuali Artikel (±18 model + tabel `routes`/`singletons`); 8 template Blade + ±11 komponen; `/layanan/` landing; Filament Resources (3 Resource layanan terpisah) + relation manager + 8 singleton simpan-langsung + MFA + 2 peran; prefill bertoken + inline-create Standar + link picker + icon picker (plugin); checklist validasi publish; preview login; form kontak tersimpan + email + Turnstile + TrustProxies + tombol lanjut WA; `Media` sendiri + konversi + ganti file; font self-host; SEO + JSON-LD + sitemap on-demand + robots + 404 + redirect engine + response cache profile + bar admin via fetch; backup R2; GA4; UptimeRobot; Kotak Masuk Lead + CSV; Log Aktivitas (paket); dasbor "Perlu Review"; section beranda on/off; halaman legal; test suite + Lighthouse CI | Situs lengkap di staging | 8 pw |
| **1b — QA & cut-over** | Buffer QA: audit redirect, text-diff, perbaikan bug staging, pelatihan editor 2 jam, cut-over DNS, pantau 1 minggu | Situs live di URL lama; situs lama dimatikan setelah 30 hari | 1 pw |
| **v1 — Konten & alat editor** | Artikel + `/berita/` + Article schema + RSS; mega menu "Layanan" dari data; section builder beranda (reorder); WhatsApp float; notifikasi WA API; draft-di-atas-published (`draft_data`) + riwayat versi + autosave + soft lock; link berbagi preview (`preview_token`); `media_usages` + laporan tidak terpakai + focal point; status `review`, unpublish terjadwal; widget lead dasbor; pencarian global; tree view 4 level; assign lead; Viewer role; filter client-side grid > 20 kartu; `docs/EDITOR.md` | | 4 pw |
| **v2 — Fitur bisnis** (hanya bila diminta) | Jadwal & biaya pelatihan + form pendaftaran + `Course`/`Event` schema; halaman detail produk; brosur PDF; form di halaman layanan; Kontributor role; form builder ringan | | 3–4 pw |

**Total MVP (0+1+1b): ≈ 11 pw · sampai v1: ≈ 15 pw · sampai v2: ≈ 18–19 pw.** Biaya operasional: VPS ±Rp 150 rb/bulan + domain; Cloudflare, GitHub, UptimeRobot, R2 gratis.

Milestone MVP: M1 (akhir minggu 2) laporan Fase 0 + fixture + import; M2 (minggu 5) semua template render di staging dengan data migrasi + resolver + cache; M3 (minggu 8) Filament lengkap + form kontak + SEO + media; M4 (minggu 10) QA selesai, pelatihan editor; M5 (minggu 11) cut-over.

---

## 13. Risiko & Mitigasi

| Risiko | Dampak | Mitigasi |
|---|---|---|
| Jumlah halaman live berbeda dari estimasi ±540 | effort ekstraksi | Crawler Fase 0 = sumber kebenaran; Fase 1 tidak bergantung jumlah karena template hanya 8 |
| ±139 leaf sertifikasi dan ±117 sub-akreditasi belum pernah diinventaris isinya (hanya kerangka DOM) — jumlah item repeater atau section bisa menyimpang dari sampel | ekstraktor gagal / batas §6.2 salah | Laporan min/maks per repeater di Fase 0 (§10.1) sebelum ekstraktor dikunci; ekstraktor menyimpan jumlah apa adanya; entri di luar batas masuk `_gaps.csv` |
| Filament 4 belum mendukung Laravel 13.x yang terpasang di `_app/` | hari 1 Fase 0 | Pakai rilis Filament terbaru yang kompatibel; downgrade Laravel hanya bila tidak ada rilis kompatibel (keputusan dicatat di `CLAUDE.md`) |
| Klien memilih tetap di shared hosting | tanpa queue daemon | Jalur §9.3 fallback; queue `sync`, cache `file` |
| Konten gap (meta, CTA salah, testimoni fiktif) menunda launch | jadwal | Launch tidak diblokir: fallback meta otomatis, section tanpa konten asli disembunyikan, checklist "Perlu Review" |
| Editor kesulitan dengan Filament | adopsi | Editor hanya melihat Resource konten; bar "Edit halaman ini"; pelatihan 2 jam + `EDITOR.md` |
| Kehilangan ranking | trafik | URL dipertahankan 1:1; sitemap + GSC; baseline SEO lama sangat lemah sehingga kemungkinan naik |
| Spam form | beban | Honeypot + Turnstile + rate limit; lead tetap tersimpan |
| Ekstraksi gagal diam-diam pada sebagian halaman | konten hilang | Text-diff lama vs baru > 5% dilaporkan; fixture di-review via PR |
| Slug unik lintas 3 tipe dalam satu folder bertabrakan saat migrasi | import gagal | Validasi di `import:legacy`; konflik masuk `_gaps.csv` untuk keputusan manual |
| Dua nomor WA: salah pilih kanonik | lead ke nomor salah | Pertanyaan Q1 harus dijawab sebelum M3; `whatsapp_nomor_form` tersedia jika memang sengaja beda |
| Ketergantungan satu developer | bus factor | Fixture + seeder + `CLAUDE.md` + CI memungkinkan dev baru bekerja dalam 1 perintah |

---

## 14. Pertanyaan Terbuka untuk Stakeholder

| # | Pertanyaan | Dibutuhkan sebelum | Default bila tidak dijawab |
|---|---|---|---|
| Q1 | Nomor WhatsApp resmi: `0813-1117-3707` (footer) atau `0813-8709-5353` (form)? Apakah lead perlu ke nomor berbeda? | M3 | footer `6281311173707` untuk semua |
| Q2 | Testimoni saat ini (Dr. Ahmad Fauzi/RS Medika Utama, Ir. Sari Dewi/BBLK, Budi Santoso/PT Energi Nusantara, Prof. Hendra Wijaya/UNS, Maya Putri/PT Caltest): asli dan berizin, atau sampel? | M3 | draft; section disembunyikan |
| Q3 | URL: tetap `.html` 1:1 (rekomendasi PRD) atau pindah ke URL bersih bertingkat (`/layanan/{kat}/{layanan}/{item}`) dengan 301 massal? | M1 | tetap `.html` |
| Q4 | Hero beranda berbahasa Inggris ("The Maker of Innovation to be Comes True", "Explore Now"): tulis ulang Indonesia? Teks baru? | M4 | tetap, ditandai Perlu Review |
| Q5 | Angka resmi: 20+ tahun, 200+ organisasi, 500+ program, 10.000+ peserta (beranda) vs 3 statistik Tentang vs "98% keberhasilan" (FAQ) — sumbernya? | M4 | migrasi apa adanya |
| Q6 | Produk InoSys / InoLab: nama resmi, kategori (DCS/LMS/LIMS?), screenshot asli, perlu halaman detail/demo? | M3 (gambar), v2 (detail) | placeholder ditandai |
| Q7 | Kebijakan Privasi & Syarat & Ketentuan: siapa menulis, kapan? (wajib karena form menyimpan data pribadi) | M4 | footer tidak menautkan sampai ada |
| Q8 | URL Instagram, LinkedIn, YouTube resmi? | M4 | tidak dirender |
| Q9 | Konten salah tempat: setuju `jasa-surveillance/resertifikasi-audit-lab` → Akreditasi; 5 sertifikasi personel → kategori baru "Sertifikasi Personel"; `lab-prodi-kedokteran` tetap di Pranata Lab sebagai `lab_manajemen`? | M1 | sesuai usulan §10.4 |
| Q10 | 20 halaman "Segera Hadir": tampilkan dengan badge, sembunyikan, atau isi sekarang? Mana yang prioritas diisi? | M4 | aturan A/B §10.4 |
| Q11 | Landing `/layanan/` netral 8 kategori: setuju menu "Layanan" mengarah ke sana (bukan ke hub Sertifikasi)? | M2 | ya |
| Q12 | Nomor WA tujuan notifikasi lead (bisa > 1) dan email tujuan selain `inovass.adm@gmail.com`? Provider WA API (Fonnte/Wablas/Twilio) untuk v1? | M3 / v1 | email saja di MVP |
| Q13 | Hosting: VPS baru (±Rp 150 rb/bulan) atau tetap cPanel LiteSpeed saat ini? Akses SSH tersedia? | M1 | VPS |
| Q14 | Siapa Admin (≤2) dan Editor (nama + email) untuk undangan awal? | M4 | – |
| Q15 | Field komersial pelatihan (jadwal, harga, durasi, instruktur, brosur, pendaftaran): diperlukan? kapan? | v2 | tidak dibangun |
| Q16 | Apakah ada GA4/Search Console yang sudah ada, atau dibuat baru? | M4 | buat baru |
| Q17 | Kartu Genetika (Kedokteran) mengutip LAMSPAK — benar atau salah salin? | pasca-launch | Perlu Review |

---

## 15. Lampiran: Daftar URL 98 Halaman

Status: **lengkap** = konten penuh; **stub** = "Konten Segera Hadir". Kolom "Migrasi" = tipe tujuan + keputusan.

### 15.1 Beranda & statis (4)

| # | URL | Template lama | Status | Migrasi |
|---|---|---|---|---|
| 1 | `/index.html` | home | lengkap | `Beranda`; `/index.html` 301 → `/` |
| 2 | `/tentang.html` | about-page | lengkap | `TentangKami` |
| 3 | `/kontak.html` | contact-page | lengkap | `Kontak` (form baru dengan backend) |
| 4 | `/produk.html` | product-list-page | lengkap | `HalamanProduk` + 2 `Produk` |

### 15.2 Sertifikasi Organisasi (52)

| # | URL (`/layanan/sertifikasi-organisasi/…`) | Template lama | Status | Migrasi |
|---|---|---|---|---|
| 5 | `index.html` | layanan-hub | lengkap | `KategoriLayanan` |
| 6 | `jasa-sertifikasi-iso.html` | service-list | lengkap | `Layanan` (intro salah konten → Perlu Review) |
| 7 | `penyusunan-dokumen.html` | service-list | lengkap | `Layanan` |
| 8 | `jasa-audit-internal-iso.html` | service-list | lengkap | `Layanan` (19 anak di-fetch) |
| 9 | `jasa-surveillance-audit-organisasi.html` | service-list | lengkap | `Layanan` (judul 112 karakter) |
| 10 | `jasa-perawatan-sistem-sertifikasi.html` | service-list | lengkap | `Layanan` |
| 11 | `k3-standar.html` | service-list | lengkap | `Layanan` (15 anak) |
| 12 | `csms.html` | service-list | lengkap | `Layanan` (CTA override) |
| 13 | `k3-lab-teknik-sipil.html` | service-list | lengkap | `Layanan` (4 anak) |
| 14 | `k3-lab-kesehatan.html` | service-list | lengkap | `Layanan` (12 anak) |
| 15 | `qhse-konstruksi.html` | service-list | lengkap | `Layanan` (18 anak, 7 bersama) |
| 16 | `qhse-industri.html` | service-list | lengkap | `Layanan` (18 anak, 7 bersama) |
| 17 | `jasa-surveillance-audit-lab.html` | coming-soon-stub | stub | draft (kategori Akreditasi) + 301 |
| 18 | `jasa-resertifikasi-audit-lab.html` | coming-soon-stub | stub | draft (kategori Akreditasi) + 301 |
| 19 | `iso-9001.html` | iso-detail | lengkap | `LayananDetail` |
| 20 | `iso-14001.html` | iso-detail | lengkap | `LayananDetail` (edisi 2026 → 2015) |
| 21 | `iso-27001.html` | iso-detail | lengkap | `LayananDetail` |
| 22 | `iso-45001.html` | iso-detail | lengkap | `LayananDetail` |
| 23 | `iso-22000.html` | iso-detail | lengkap | `LayananDetail` |
| 24 | `iso-22301.html` | iso-detail | lengkap | `LayananDetail` |
| 25 | `iso-37001.html` | iso-detail | lengkap | `LayananDetail` |
| 26 | `iso-37301.html` | iso-detail | lengkap | `LayananDetail` |
| 27 | `iso-50001.html` | iso-detail | lengkap | `LayananDetail` |
| 28 | `iso-55001.html` | iso-detail | lengkap | `LayananDetail` |
| 29 | `iso-21001.html` | iso-detail | lengkap | `LayananDetail` |
| 30 | `iso-13485.html` | iso-detail | lengkap | `LayananDetail` |
| 31 | `iso-39001.html` | iso-detail | lengkap | `LayananDetail` (CTA 9001 → Perlu Review) |
| 32 | `iso-10002.html` | iso-detail | lengkap | `LayananDetail` (CTA 9001) |
| 33 | `iso-30301.html` | iso-detail | lengkap | `LayananDetail` (CTA 9001) |
| 34 | `iso-20000-1.html` | iso-detail | lengkap | `LayananDetail` (CTA 9001) |
| 35 | `iso-35001.html` | iso-detail | lengkap | `LayananDetail` (CTA 9001) |
| 36 | `ims.html` | iso-detail | lengkap | `LayananDetail` (CTA 9001, breadcrumb) |
| 37 | `iso-lainnya.html` | iso-detail | lengkap | `LayananDetail` (CTA 9001, target = daftar standar) |
| 38 | `penyusunan-dokumen-ims.html` | iso-detail (varian) | lengkap | `LayananDetail` jenis penyusunan_dokumen (Perlu Review: langkah) |
| 39 | `penyusunan-dokumen-iso-10002.html` | iso-detail (varian) | lengkap | sda |
| 40 | `penyusunan-dokumen-iso-13485.html` | iso-detail (varian) | lengkap | sda |
| 41 | `penyusunan-dokumen-iso-14001.html` | iso-detail (varian) | lengkap | sda |
| 42 | `penyusunan-dokumen-iso-20000-1.html` | iso-detail (varian) | lengkap | sda |
| 43 | `penyusunan-dokumen-iso-21001.html` | iso-detail (varian) | lengkap | sda |
| 44 | `penyusunan-dokumen-iso-22000.html` | iso-detail (varian) | lengkap | sda |
| 45 | `penyusunan-dokumen-iso-22301.html` | iso-detail (varian) | lengkap | sda |
| 46 | `penyusunan-dokumen-iso-27001.html` | iso-detail (varian) | lengkap | sda |
| 47 | `penyusunan-dokumen-iso-30301.html` | iso-detail (varian) | lengkap | sda |
| 48 | `penyusunan-dokumen-iso-35001.html` | iso-detail (varian) | lengkap | sda |
| 49 | `penyusunan-dokumen-iso-37001.html` | iso-detail (varian) | lengkap | sda |
| 50 | `penyusunan-dokumen-iso-37301.html` | iso-detail (varian) | lengkap | sda |
| 51 | `penyusunan-dokumen-iso-39001.html` | iso-detail (varian) | lengkap | sda |
| 52 | `penyusunan-dokumen-iso-45001.html` | iso-detail (varian) | lengkap | sda |
| 53 | `penyusunan-dokumen-iso-50001.html` | iso-detail (varian) | lengkap | sda |
| 54 | `penyusunan-dokumen-iso-55001.html` | iso-detail (varian) | lengkap | sda |
| 55 | `penyusunan-dokumen-iso-9001.html` | iso-detail (varian) | lengkap | sda |
| 56 | `penyusunan-dokumen-iso-lainnya.html` **(asumsi slug; sumber hanya menyebut "lainnya")** | iso-detail (varian) | lengkap | sda |

Tidak ter-crawl di folder ini (fetch di Fase 0): ±177 leaf `audit-internal-*`, `surveillance-*`, `pemeliharaan-*`, `smk3-*`, `csms-*`, `k3-lab-*`, `qhse-*`.

### 15.3 Akreditasi Organisasi (9)

| # | URL (`/layanan/akreditasi-organisasi/…`) | Template lama | Status | Migrasi |
|---|---|---|---|---|
| 57 | `index.html` | layanan-hub | lengkap | `KategoriLayanan` (hapus 3 blok tersembunyi) |
| 58 | `akreditasi-lab.html` | akreditasi-detail | lengkap | `Layanan` (ISO/IEC 17025) |
| 59 | `konsultasi-akreditasi-inspeksi.html` | akreditasi-detail | lengkap | `Layanan` (ISO/IEC 17020; 3 penulisan → kanonik) |
| 60 | `konsultasi-akreditasi-lsp.html` | akreditasi-detail | lengkap | `Layanan` (ISO/IEC 17024; typo "Person") |
| 61 | `konsultasi-akreditasi-lspro.html` | akreditasi-detail | lengkap | `Layanan` (ISO/IEC 17065) |
| 62 | `akreditasi-uji-profisiensi.html` | akreditasi-detail | lengkap | `Layanan` (ISO/IEC 17043) |
| 63 | `akreditasi-lab-medis.html` | akreditasi-detail | lengkap | `Layanan` (ISO 15189; kartu 6 duplikat) |
| 64 | `akreditasi-biobank.html` | akreditasi-detail | lengkap | `Layanan` (ISO 20387) |
| 65 | `akreditasi-iso-17025.html` (sampel fetch live; mewakili ±118 sub-layanan) | sub-service-detail | lengkap | `LayananDetail` jenis akreditasi |

### 15.4 Pelatihan Sertifikasi (8)

| # | URL (`/layanan/pelatihan-sertifikasi/…`) | Template lama | Status | Migrasi |
|---|---|---|---|---|
| 66 | `index.html` | layanan-hub | lengkap | `KategoriLayanan` |
| 67 | `public-training.html` | training-format | lengkap | `Layanan` format_pelatihan (18 anak) |
| 68 | `in-house-training.html` | training-format | lengkap | `Layanan` (18 anak; 6 slug tanpa `iso-`) |
| 69 | `executive-training.html` | training-format | lengkap | `Layanan` (18 anak) |
| 70 | `private-training.html` | coming-soon-stub | stub | draft + 301 → hub |
| 71 | `pelatihan-auditor-internal-iso.html` | coming-soon-stub | stub | draft + 301 |
| 72 | `pelatihan-implementasi-iso.html` | coming-soon-stub | stub | draft + 301 |
| 73 | `pelatihan-k3-lingkungan.html` | coming-soon-stub | stub | draft + 301 |

Tidak ter-crawl: 54 program `public-training-*`, `inhouse-training-*`, `executive-training-*` (5 disampel live, mis. `public-training-iso-9001.html`).

### 15.5 Pelatihan Akreditasi (9)

| # | URL (`/layanan/pelatihan-akreditasi/…`) | Template lama | Status | Migrasi |
|---|---|---|---|---|
| 74 | `index.html` | layanan-hub | lengkap | `KategoriLayanan` (intro disalin dari Pelatihan Sertifikasi → Perlu Review) |
| 75 | `public-training-akreditasi.html` | training-format | lengkap | `Layanan` (11 anak) |
| 76 | `in-house-training-akreditasi.html` | training-format | lengkap | `Layanan` (11 anak) |
| 77 | `private-training-akreditasi.html` | training-format | lengkap | `Layanan` (11 anak) |
| 78 | `sertifikasi-auditor-qms.html` | coming-soon-stub | stub | draft kategori Sertifikasi Personel + 301 |
| 79 | `sertifikasi-auditor-ems.html` | coming-soon-stub | stub | sda |
| 80 | `sertifikasi-auditor-ohsms.html` | coming-soon-stub | stub | sda |
| 81 | `sertifikasi-auditor-isms.html` | coming-soon-stub | stub | sda |
| 82 | `sertifikasi-ahli-k3-umum.html` | coming-soon-stub | stub | sda |

Tidak ter-crawl: 33 program `public-training-akreditasi-*`, `in-house-training-akreditasi-*`, `private-training-akreditasi-*`.

### 15.6 Pranata Laboratorium (8)

| # | URL (`/layanan/pranata-laboratorium/…`) | Template lama | Status | Migrasi |
|---|---|---|---|---|
| 83 | `index.html` | layanan-hub | lengkap | `KategoriLayanan` |
| 84 | `pranata-lab-mipa.html` | service-program-list | lengkap (file terpotong, tanpa footer) | `Layanan` (60 anak; filter aktif) |
| 85 | `pranata-lab-sosial.html` | service-program-list | lengkap | `Layanan` (12 anak) |
| 86 | `pranata-lab-kedokteran.html` | service-program-list | lengkap | `Layanan` (19 anak) |
| 87 | `pranata-lab-kesehatan.html` | service-program-list | lengkap | `Layanan` (7 anak) |
| 88 | `pranata-lab-komputer.html` | coming-soon-stub | stub | published `coming_soon` |
| 89 | `pranata-lab-multimedia.html` | coming-soon-stub | stub | published `coming_soon` |
| 90 | `lab-prodi-kedokteran.html` | coming-soon-stub | stub | published `coming_soon` (jenis `lab_manajemen`) |

Tidak ter-crawl: 98 program `pranata-lab-{mipa,sosial,kedokteran,kesehatan}-*` (4 disampel live).

### 15.7 Manajemen Lab Mineral (3)

| # | URL (`/layanan/lab-mineral/…`) | Template lama | Status | Migrasi |
|---|---|---|---|---|
| 91 | `index.html` | layanan-hub | lengkap | `KategoriLayanan` (grid 3 kolom) |
| 92 | `lab-batubara.html` | coming-soon-stub | stub | published `coming_soon` |
| 93 | `lab-nikel.html` | coming-soon-stub | stub | published `coming_soon` |

### 15.8 Manajemen Lab Teknik Sipil (5)

| # | URL (`/layanan/lab-teknik-sipil/…`) | Template lama | Status | Migrasi |
|---|---|---|---|---|
| 94 | `index.html` | layanan-hub | lengkap | `KategoriLayanan` |
| 95 | `lab-rekayasa-struktur.html` | coming-soon-stub | stub | published `coming_soon` |
| 96 | `lab-rekayasa-tanah.html` | coming-soon-stub | stub | published `coming_soon` |
| 97 | `lab-rekayasa-jalan.html` | coming-soon-stub | stub | published `coming_soon` |
| 98 | `lab-rekayasa-sda.html` | coming-soon-stub | stub | published `coming_soon` |

### 15.9 Rekap

| | Jumlah |
|---|---:|
| Halaman lengkap | 78 |
| Stub → published `coming_soon` (aturan A) | 9 |
| Stub → draft + 301 (aturan B) | 11 |
| Halaman live tidak ter-crawl (fetch Fase 0) | ±480 |
| URL baru | `/layanan/`, `/berita/` (v1), `/kebijakan-privasi.html`, `/syarat-ketentuan.html`, `/sitemap.xml`, `/robots.txt` |
| **Total URL publik setelah migrasi** | **±575 + baru; semua lama 200 atau 301** |
