# INOVASS Website

Website statis (HTML/CSS/JS) untuk **inovass.com**.

- **Hosting:** shared hosting cPanel Rumahweb (akun `inom3994`, server `kumai.iixcp.rumahweb.net`).
- **Deploy:** otomatis oleh GitHub Actions setiap push ke `main` yang mengubah `public/`. Isi `public/` dibungkus jadi **satu `site.zip`**, di-upload via FTPS, lalu diekstrak ke `public_html/` oleh cron di server (±2 menit total).
- **CMS jadwal & pendaftaran pelatihan:** aplikasi Laravel di folder [`cms/`](cms/README.md). Terpisah dari situs statis; push ke `cms/` **tidak** memicu deploy `public/`. CMS punya workflow sendiri (`deploy-cms.yml`) dan tampil di `inovass.com/jadwal-pelatihan` serta `inovass.com/admin` (diteruskan oleh `public/.htaccess`). Panduan: [`cms/docs/PANDUAN-DEPLOY.md`](cms/docs/PANDUAN-DEPLOY.md).

## Gambaran cara kerja

```
 Laptop                GitHub                                   cPanel Rumahweb
 ──────                ──────                                   ───────────────
 edit public/  ──push──▶  repo marsyadiya23/web-inovass
                          │
                          ▼  GitHub Actions (.github/workflows/deploy-cpanel.yml)
                          zip public/ → upload site.zip ───────▶  /home/inom3994/inovass
                                                                  cron + deploy.php → ekstrak ke public_html
                                                                  (Apache + public/.htaccess)
 Pengunjung ◀──────────────── HTTPS ──────────────────────────────  https://inovass.com
```

- **Tidak ada database atau backend**. Isinya hanya file HTML/CSS/JS/gambar.
- **Kenapa zip, bukan upload per file?** FTP Rumahweb butuh ±5 detik per file. 600+ file = puluhan menit; satu zip = ±1 menit. Detail mekanisme (cron, `deploy.php`): [`cms/docs/PANDUAN-DEPLOY.md`](cms/docs/PANDUAN-DEPLOY.md) bagian 1 dan 3.8.

```
public/                          # semua isi website (= public_html di server)
  .htaccess                      # clean URL, cache, header keamanan (Apache)
  index.html  tentang.html  kontak.html  produk.html
  layanan/
    sertifikasi-organisasi/      # index.html = halaman kategori, sisanya halaman detail
    akreditasi-organisasi/
    pelatihan-sertifikasi/
    pelatihan-akreditasi/
    pranata-laboratorium/
    lab-mineral/
    lab-teknik-sipil/
  assets/css/  (style.css, pages.css)
  assets/js/   (script.js)
  assets/img/
.github/workflows/deploy-cpanel.yml   # CI/CD: zip public/ → upload → cron mengekstrak ke public_html
```

Nama folder kategori mengikuti label tab di halaman Layanan:

| Folder | Tab di website | Nama file lama |
|---|---|---|
| `sertifikasi-organisasi/` | Sertifikasi Organisasi | `layanan-iso.html` |
| `akreditasi-organisasi/` | Akreditasi Organisasi | `layanan-akreditasi.html` |
| `pelatihan-sertifikasi/` | Pelatihan Sertifikasi | `layanan-pelatihan.html` |
| `pelatihan-akreditasi/` | Pelatihan Akreditasi | `layanan-sertifikasi.html` |
| `pranata-laboratorium/` | Pranata Laboratorium | `layanan-pranata-lab.html` |
| `lab-mineral/` | Manajemen Lab Mineral | `layanan-lab-mineral.html` |
| `lab-teknik-sipil/` | Manajemen Lab Teknik Sipil | `layanan-lab-teknik-sipil.html` |

Halaman detail dulu bernama `layanan-detail-xxx.html` di root. Sekarang prefix-nya dibuang, misalnya `layanan-detail-akreditasi-lab.html` → `layanan/akreditasi-organisasi/akreditasi-lab.html`.

### Aturan penting saat mengedit
- **Pakai path relatif.** Contoh dari `layanan/<kategori>/`: `../../assets/css/style.css`, `../../index.html`. Jangan pakai `/assets/...` (diawali `/`), karena CSS akan hilang saat dibuka lewat VS Code Live Preview.
- **Halaman baru**: salin halaman sejenis di folder kategori yang sama, lalu ubah isinya. Path-nya otomatis sudah benar karena kedalaman foldernya sama.
- **Jangan menulis ulang kode menu/navbar di `<script>` halaman.** Menu hamburger, navbar saat scroll, animasi reveal, dan tab sudah diurus `assets/js/script.js`. Mendeklarasikan ulang `const hamburgerBtn`, `const mobileMenu`, atau `const navbar` akan membuat **seluruh** script di halaman itu error. Bug ini pernah terjadi di 548 halaman.
- **Perbaikan tampilan mobile** dikumpulkan di blok `RESPONSIVE FIXES` di akhir `assets/css/style.css`. Tambahkan perbaikan baru di situ.
- **Nomor WhatsApp untuk form kontak** ada di script di bagian bawah `kontak.html` (`wa.me/6281311173707`).
- **Jangan edit file langsung di File Manager cPanel.** Perubahan itu akan tertimpa deploy berikutnya. Selalu edit di repo lalu push.

## Alur update (sehari-hari)

1. Edit file di `public/`
2. `git add . && git commit -m "update ..." && git push`
3. GitHub Actions meng-upload `site.zip` (±1 menit), lalu cron mengekstraknya ke `public_html/` (≤ 1 menit). Status deploy: tab **Actions** di GitHub; hasil ekstrak: `inovass/storage/logs/deploy.log`.

Cek lokal sebelum push: buka `public/index.html` dengan Live Preview / double-click, atau:

```bash
cd public && python -m http.server 8080
# buka http://localhost:8080
```

## Setup awal (sekali saja)

### 1. Akun FTP, secrets, dan cron
Situs statis memakai akun FTP, secrets GitHub, dan cron yang **sama dengan CMS**:
- Akun FTP `deploycms@inovass.com` → `/home/inom3994/inovass` (bukan `public_html`)
- Secrets: `FTP_SERVER`, `CMS_FTP_USERNAME`, `CMS_FTP_PASSWORD`
- Cron permanen yang menjalankan `deploy.php`

Langkahnya: [`cms/docs/PANDUAN-DEPLOY.md`](cms/docs/PANDUAN-DEPLOY.md) bagian 3.1, 3.5, dan 3.8. Akun FTP lama `deploy@inovass.com` dan secret `FTP_USERNAME`/`FTP_PASSWORD` tidak dipakai lagi (boleh dihapus).

### 2. Deploy pertama
**Actions → Deploy to cPanel → Run workflow** (atau push perubahan di `public/`), lalu cek `inovass/storage/logs/deploy.log` berakhir `deploy selesai`.

## Rollback
`git revert <commit>` lalu push. Versi lama di-zip dan diekstrak ulang.

## Tanya-jawab

**Kenapa form kontak membuka WhatsApp?**
Website ini tidak punya backend/server email. Sebelumnya form hanya menampilkan "Pesan berhasil dikirim!" padahal pesan tidak terkirim ke mana pun. Sekarang tombol *Kirim Pesan* membuka WhatsApp INOVASS dengan pesan yang sudah terisi (nama, email, telepon, keperluan, pesan). Kalau nanti ingin masuk ke email, perlu layanan form (mis. Formspree) atau backend kecil.

**Apakah perubahan CSS langsung terlihat setelah deploy?**
Ya. `.htaccess` menyuruh browser selalu mengecek ulang file CSS/JS (`Cache-Control: no-cache`). Gambar di-cache 7 hari, jadi kalau mengganti gambar, pakai **nama file baru**.

**File yang dihapus dari repo, apakah ikut terhapus di server?**
**Tidak.** Ekstraksi zip hanya menambah/menimpa file. File yang dihapus dari `public/` tetap ada di `public_html/` sampai dihapus manual lewat File Manager. File lain di server (mis. folder `inovass/` milik CMS) tidak disentuh.

## Troubleshooting

| Gejala | Penyebab & solusi |
|---|---|
| Halaman tampil polos tanpa CSS saat dibuka lokal | Ada link yang diawali `/` (path absolut). Ganti jadi relatif (`../../assets/...`). Cek: `grep -rn 'href="/' public` |
| Actions merah: login gagal | Secret `FTP_SERVER`/`CMS_FTP_USERNAME`/`CMS_FTP_PASSWORD` salah. Coba login dengan FileZilla memakai data yang sama. |
| Actions hijau tapi situs tidak berubah | Cron belum mengekstrak. Cek `inovass/storage/logs/deploy.log` dan cron di cPanel (PANDUAN-DEPLOY 3.8a). |
| Actions merah: error TLS/sertifikat | Ganti `protocol: ftps` menjadi `ftp` di `deploy-cpanel.yml`. |
| Workflow tidak jalan setelah push | Hanya jalan jika ada perubahan di `public/`. Jalankan manual: **Actions → Deploy to cPanel → Run workflow**. |
| File di server tidak ter-update | Run workflow lagi. Kalau upload zip dilewati, hapus `inovass/.ftp-deploy-sync-state-site.json` lalu Run workflow. |
| `/tentang` 404 padahal `/tentang.html` bisa | `.htaccess` belum ter-upload. Cek di File Manager (aktifkan *Show Hidden Files*). |
| Menu hamburger / animasi tidak jalan di satu halaman | Buka DevTools (F12) → Console. Biasanya ada `Identifier '...' has already been declared` → hapus deklarasi ganda di `<script>` halaman itu (lihat *Aturan penting*). |

## Catatan perubahan (Oktober 2026)
- Struktur dirapikan: 560 file HTML di root dipindah ke `public/` dengan folder per kategori; CSS/JS/gambar ke `public/assets/`.
- Dihapus: skrip generator (`*.py`, `*.sh`), file laporan (`*.md`), template tak terpakai, dan 51 gambar yang tidak dipakai di halaman mana pun.
- Diperbaiki: 6 link rusak (termasuk 5 link `onclick` ke halaman yang tidak ada), error JavaScript di 548 halaman, form kontak palsu, dan tampilan mobile. Tab layanan, grid beranda, garis timeline, breadcrumb, dan grid 3/4 kolom sebelumnya meluber di HP.
- Hasil pengecekan otomatis: 555 halaman × 3 ukuran layar (375/768/1280px), tanpa scroll ke samping, tanpa error JavaScript, dan 18.299 link valid.
- Pindah hosting dari VPS (Docker + Cloudflare Tunnel) ke shared hosting cPanel; deploy via FTPS dari GitHub Actions.
