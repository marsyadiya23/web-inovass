# INOVASS Website

Website statis (HTML/CSS/JS) untuk **inovass.com**.

- **Hosting:** shared hosting cPanel Rumahweb (akun `inom3994`, server `kumai.iixcp.rumahweb.net`).
- **Deploy:** otomatis oleh GitHub Actions setiap push ke `main` yang mengubah `public/`. Isi folder `public/` di-upload via FTPS ke `public_html/`.
- **CMS jadwal & pendaftaran pelatihan:** aplikasi Laravel di folder [`cms/`](cms/README.md). Terpisah dari situs statis; push ke `cms/` **tidak** memicu deploy `public/`.

## Gambaran cara kerja

```
 Laptop                GitHub                                   cPanel Rumahweb
 ──────                ──────                                   ───────────────
 edit public/  ──push──▶  repo afidzulinn/web-inovass
                          │
                          ▼  GitHub Actions (.github/workflows/deploy-cpanel.yml)
                          upload file yang berubah via FTPS ───▶  /home/inom3994/public_html
                                                                  (Apache + public/.htaccess)
 Pengunjung ◀──────────────── HTTPS ──────────────────────────────  https://inovass.com
```

- **Tidak ada database atau backend**. Isinya hanya file HTML/CSS/JS/gambar.
- **Hanya file yang berubah yang di-upload.** Daftar file yang sudah ter-upload disimpan di `public_html/.ftp-deploy-sync-state.json` (jangan dihapus).

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
.github/workflows/deploy-cpanel.yml   # CI/CD: upload public/ ke cPanel via FTPS
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
3. GitHub Actions meng-upload file yang berubah ke `public_html/`. Selesai dalam ±1 menit. Status deploy: tab **Actions** di GitHub.

Cek lokal sebelum push: buka `public/index.html` dengan Live Preview / double-click, atau:

```bash
cd public && python -m http.server 8080
# buka http://localhost:8080
```

## Setup awal (sekali saja)

### 1. Akun FTP di cPanel
cPanel → **FTP Accounts** → Add FTP Account:
- Log In: `deploy` (menjadi `deploy@inovass.com`)
- Directory: `public_html` (akun ini hanya bisa mengakses folder website)
- Quota: Unlimited

### 2. Secrets di GitHub
Repo → **Settings → Secrets and variables → Actions → New repository secret**:

| Name | Value |
|---|---|
| `FTP_SERVER` | `kumai.iixcp.rumahweb.net` |
| `FTP_USERNAME` | `deploy@inovass.com` |
| `FTP_PASSWORD` | password akun FTP di atas |

### 3. Deploy pertama
1. Kosongkan `public_html` lewat File Manager (hapus file bawaan seperti `default.html`). Deploy tidak menghapus file yang sudah ada di server sebelumnya.
2. **Actions → Deploy to cPanel → Run workflow** (atau push perubahan di `public/`). Deploy pertama meng-upload semua file (±28 MB), jadi lebih lama.
3. Buka https://inovass.com.

## Rollback
`git revert <commit>` lalu push. File yang dikembalikan akan di-upload ulang.

## Tanya-jawab

**Kenapa form kontak membuka WhatsApp?**
Website ini tidak punya backend/server email. Sebelumnya form hanya menampilkan "Pesan berhasil dikirim!" padahal pesan tidak terkirim ke mana pun. Sekarang tombol *Kirim Pesan* membuka WhatsApp INOVASS dengan pesan yang sudah terisi (nama, email, telepon, keperluan, pesan). Kalau nanti ingin masuk ke email, perlu layanan form (mis. Formspree) atau backend kecil.

**Apakah perubahan CSS langsung terlihat setelah deploy?**
Ya. `.htaccess` menyuruh browser selalu mengecek ulang file CSS/JS (`Cache-Control: no-cache`). Gambar di-cache 7 hari, jadi kalau mengganti gambar, pakai **nama file baru**.

**File yang dihapus dari repo, apakah ikut terhapus di server?**
Ya. Deploy mencatat file yang pernah di-upload, jadi file yang dihapus dari `public/` juga dihapus dari `public_html/`. File yang dibuat langsung di server (bukan lewat deploy) tidak disentuh.

## Troubleshooting

| Gejala | Penyebab & solusi |
|---|---|
| Halaman tampil polos tanpa CSS saat dibuka lokal | Ada link yang diawali `/` (path absolut). Ganti jadi relatif (`../../assets/...`). Cek: `grep -rn 'href="/' public` |
| Actions merah: login gagal | Secret `FTP_SERVER`/`FTP_USERNAME`/`FTP_PASSWORD` salah. Coba login dengan FileZilla memakai data yang sama. |
| Actions merah: error TLS/sertifikat | Ganti `protocol: ftps` menjadi `ftp` di `deploy-cpanel.yml`. |
| Workflow tidak jalan setelah push | Hanya jalan jika ada perubahan di `public/`. Jalankan manual: **Actions → Deploy to cPanel → Run workflow**. |
| File di server tidak ter-update / ada yang hilang | Hapus `public_html/.ftp-deploy-sync-state.json` lewat File Manager, lalu Run workflow. Semua file akan di-upload ulang. |
| `/tentang` 404 padahal `/tentang.html` bisa | `.htaccess` belum ter-upload. Cek di File Manager (aktifkan *Show Hidden Files*). |
| Menu hamburger / animasi tidak jalan di satu halaman | Buka DevTools (F12) → Console. Biasanya ada `Identifier '...' has already been declared` → hapus deklarasi ganda di `<script>` halaman itu (lihat *Aturan penting*). |

## Catatan perubahan (Oktober 2026)
- Struktur dirapikan: 560 file HTML di root dipindah ke `public/` dengan folder per kategori; CSS/JS/gambar ke `public/assets/`.
- Dihapus: skrip generator (`*.py`, `*.sh`), file laporan (`*.md`), template tak terpakai, dan 51 gambar yang tidak dipakai di halaman mana pun.
- Diperbaiki: 6 link rusak (termasuk 5 link `onclick` ke halaman yang tidak ada), error JavaScript di 548 halaman, form kontak palsu, dan tampilan mobile. Tab layanan, grid beranda, garis timeline, breadcrumb, dan grid 3/4 kolom sebelumnya meluber di HP.
- Hasil pengecekan otomatis: 555 halaman × 3 ukuran layar (375/768/1280px), tanpa scroll ke samping, tanpa error JavaScript, dan 18.299 link valid.
- Pindah hosting dari VPS (Docker + Cloudflare Tunnel) ke shared hosting cPanel; deploy via FTPS dari GitHub Actions.
