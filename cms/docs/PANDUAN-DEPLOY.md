# Panduan CMS INOVASS: Lokal, cPanel, dan CI/CD

Panduan lengkap untuk menjalankan CMS jadwal & pendaftaran pelatihan di laptop, memasangnya di cPanel Rumahweb, dan mengirim perubahan secara otomatis lewat GitHub Actions.

| | |
|---|---|
| Repo | https://github.com/marsyadiya23/web-inovass (folder `cms/`) |
| Hosting | cPanel Rumahweb, akun `inom3994`, server `kumai.iixcp.rumahweb.net` |
| Lokasi aplikasi di server | `/home/inom3994/inovass` (di **luar** `public_html`). Hanya isi `public/` yang disalin ke `public_html/inovass/public` |
| Alamat | `https://inovass.com/jadwal-pelatihan` · admin: `https://inovass.com/admin` (diteruskan ke CMS oleh `public/.htaccess` situs statis). `jadwal.inovass.com` tetap jalan sebagai alamat cadangan |
| Situs compro statis | Tetap di `public_html` (`inovass.com`), deploy terpisah. Lihat [README root](../../README.md) |

---

## Checklist go-live (urutan kerja)

| # | Langkah | Di mana | Bagian |
|---|---|---|---|
| 1 | Akun FTP `deploycms` → `/home/inom3994/inovass` | cPanel | [3.1](#31-akun-ftp) |
| 2 | Database + user MySQL | cPanel | [3.2](#32-database-mysql) |
| 3 | Subdomain `jadwal.inovass.com` → `public_html/inovass/public` | cPanel | [3.3](#33-subdomain) |
| 4 | PHP 8.4 (patch ≥ 8.4.27) untuk subdomain | cPanel | [3.4](#34-versi-php) |
| 5 | Secrets GitHub (`FTP_SERVER`, `CMS_FTP_USERNAME`, `CMS_FTP_PASSWORD`) | GitHub | [3.5](#35-github-secrets) |
| 6 | Buat APP_KEY: `php artisan key:generate --show` | Laptop | [3.7](#37-buat-env-di-server) |
| 7 | Buat `.env` server | cPanel File Manager | [3.7](#37-buat-env-di-server) |
| 8 | Pasang cron permanen (menjalankan `deploy.php`) | cPanel Cron Jobs | [3.8](#38-cron) |
| 9 | Push ke `main` → Actions hijau (±3 menit) → tunggu cron ≤ 1 menit | Laptop + GitHub | [3.6](#36-deploy-pertama) |
| 9b | Isi data awal sekali (cron seed, lalu **hapus**) | cPanel Cron Jobs | [3.8](#38-cron) |
| 10 | Buka website & login admin | Browser | [3.9](#39-cek-hasil) |
| 11 | Email `noreply@inovass.com` + SPF/DKIM untuk notifikasi | cPanel | [3.10](#310-email-notifikasi-pendaftar) |

Setelah itu, **CI/CD otomatis**: setiap push ke `main` yang mengubah `cms/` langsung ter-deploy (bagian [4](#4-alur-update-sehari-hari)).

## Daftar isi

1. [Gambaran cara kerja](#1-gambaran-cara-kerja)
2. [Menjalankan di lokal](#2-menjalankan-di-lokal)
3. [Setup cPanel (sekali saja)](#3-setup-cpanel-sekali-saja)
4. [Alur update sehari-hari](#4-alur-update-sehari-hari)
5. [Perubahan database](#5-perubahan-database)
6. [Isi panel admin](#6-isi-panel-admin)
7. [Backup & rollback](#7-backup--rollback)
8. [Troubleshooting](#8-troubleshooting)
9. [Aturan penting (jangan dilanggar)](#9-aturan-penting-jangan-dilanggar)

---

## 1. Gambaran cara kerja

```
 Laptop                 GitHub                                       cPanel Rumahweb
 ──────                 ──────                                       ───────────────
 edit cms/  ──push main──▶ marsyadiya23/web-inovass
                           │
                           ▼ GitHub Actions (.github/workflows/deploy-cms.yml)
                           1. composer install --no-dev  (vendor/ + aset Filament)
                           2. bungkus semuanya jadi SATU file release.zip (±50 MB)
                           3. upload release.zip + deploy.php via FTPS ──▶ /home/inom3994/inovass
                           4. upload penanda deploy-pending (paling akhir) ──▶ /home/inom3994/inovass
                                                                    │
                                                    Cron tiap menit ▼
                                   ada deploy-pending? → php deploy.php:
                                     • ekstrak release.zip ke /home/inom3994/inovass
                                     • salin public/ → /home/inom3994/public_html/inovass/public
                                     • migrate + optimize
                                                                    │
 Pengunjung ◀── HTTPS ── jadwal.inovass.com ◀── document root public_html/inovass/public
                                                (index.php membaca aplikasi dari /home/inom3994/inovass)
```

> **Kenapa satu zip, bukan upload file satu per satu?** FTP Rumahweb butuh ±5 detik per file/folder. Aplikasi ini ±20.000 file `vendor/`: upload per file akan memakan puluhan jam dan dibatalkan GitHub setelah 6 jam. Satu zip selesai dalam ±1 menit; cron di server yang membukanya.
>
> **Kenapa `public/` disalin ke `public_html/inovass/public`?** cPanel Rumahweb hanya mengizinkan document root di dalam `public_html`. Kode aplikasi dan `.env` tidak boleh berada di folder publik, jadi aplikasi tetap di `/home/inom3994/inovass`, dan hanya isi `public/` (index.php, CSS/JS, gambar) yang disalin ke sana. `cms/public/index.php` otomatis mencari aplikasi di `../../../inovass` bila `vendor/` tidak ada di sebelahnya.
>
> **Kenapa CMS bisa dibuka di `inovass.com/jadwal-pelatihan` dan `inovass.com/admin`?** `public/.htaccess` situs statis meneruskan alamat `jadwal-pelatihan`, `pelatihan`, `admin`, `filament`, dan `livewire-…` ke `inovass/public/index.php`. Alamat lain tetap dilayani file HTML statis. Di `.env` server, `APP_URL=https://inovass.com` (link yang dibuat CMS memakai domain utama) dan `ASSET_URL=https://inovass.com/inovass/public` (CSS/JS/gambar/upload CMS diambil dari folder aslinya). Menambah halaman CMS dengan awalan baru? Tambahkan awalannya di aturan `.htaccess` itu.

Poin penting:

- **Server tidak butuh Composer, Node, Git, atau SSH.** Semua dibangun di GitHub Actions, server hanya menerima file.
- **Yang di-upload tiap deploy hanya 3 file:** `release.zip`, `deploy.php`, dan `deploy-pending`. Catatan upload FTP disimpan di `.ftp-deploy-sync-state*.json` di `/home/inom3994/inovass` (aman, di luar folder publik; boleh dihapus kalau perlu).
- **Ekstraksi hanya menimpa/menambah file, tidak menghapus.** File yang dihapus dari repo tetap tertinggal di server sampai dihapus manual. Tidak berbahaya untuk aplikasi ini.
- **Yang tidak pernah disentuh deploy:** `.env`, isi `storage/` (log, sesi, cache), dan file upload admin di `public_html/inovass/public/uploads/`. File-file itu tidak ada di repo, jadi aman.
- Situs statis (`public/` di root repo → `public_html`) punya workflow sendiri (`deploy-cpanel.yml`) dengan cara yang sama: `public/` dibungkus jadi `site.zip`, di-upload ke `/home/inom3994/inovass`, lalu `deploy.php` (cron yang sama) mengekstraknya ke `public_html`. Push ke `cms/` tidak memicunya, dan sebaliknya.

Struktur di server setelah deploy:

```
/home/inom3994/
├── public_html/              ← situs compro statis (inovass.com)
│   └── inovass/public/       ← document root jadwal.inovass.com (salinan cms/public)
│       ├── index.php  .htaccess  assets/  css/  js/
│       └── uploads/          ← gambar/brosur yang di-upload admin
└── inovass/                  ← aplikasi CMS (isi folder cms/ dari repo), TIDAK bisa diakses dari web
    ├── .env                  ← dibuat manual di File Manager, tidak ada di repo
    ├── app/ config/ database/ routes/ resources/ vendor/ ...
    ├── storage/logs/         ← laravel.log (error aplikasi), deploy.log (hasil cron)
    └── public/               ← salinan cadangan, tidak dipakai web
```

---

## 2. Menjalankan di lokal

### Kebutuhan

- **PHP 8.4+** dengan ekstensi `pdo_sqlite`, `mbstring`, `intl`, `gd`, `zip`, `fileinfo`, `openssl`, `curl`
- **Composer**
- Database lokal memakai **SQLite** (satu file, tanpa install MySQL)

Cek: `php -v` dan `composer -V`.

> **`.env` di laptop selalu `DB_CONNECTION=sqlite`.** Data MySQL (`inom3994_...`) hanya untuk `.env` di server. Kalau diisi di laptop, semua halaman error 500 (`could not find driver`), karena PHP laptop tidak punya driver MySQL dan database server tidak bisa diakses dari laptop.

### Pertama kali (setelah clone)

PowerShell / terminal VS Code:

```powershell
cd cms
composer install
copy .env.example .env
php artisan key:generate
type nul > database\database.sqlite
php artisan migrate --seed
```

Mac/Linux: ganti `copy` → `cp` dan `type nul >` → `touch`.

### Sehari-hari

```powershell
cd cms
php artisan serve
```

| Halaman | URL |
|---|---|
| Website | http://127.0.0.1:8000 |
| Jadwal pelatihan | http://127.0.0.1:8000/jadwal-pelatihan |
| Admin | http://127.0.0.1:8000/admin · email = `ADMIN_EMAIL` di `.env` (mis. `inovass.adm@gmail.com`), password `inovass123` (hanya lokal) |
| Email notifikasi | Lokal tidak benar-benar terkirim (`MAIL_MAILER=log`). Isinya tertulis di `storage/logs/laravel.log` |

Matikan server: **Ctrl + C**.

### Perintah berguna

| Perintah | Fungsi |
|---|---|
| `php artisan test` | Jalankan semua test. **Wajib hijau sebelum push** |
| `php artisan migrate:fresh --seed` | Reset database lokal ke data awal (semua isian admin lokal hilang) |
| `php artisan optimize:clear` | Hapus semua cache bila perubahan config/route tidak terbaca |
| `php artisan route:list` | Lihat semua URL |

---

## 3. Setup cPanel (sekali saja)

Kerjakan **berurutan**. Langkah 6 (`.env`) harus selesai sebelum langkah 7 (cron).

### 3.1 Akun FTP

cPanel → **FTP Accounts** → *Add FTP Account*:

| Field | Isi |
|---|---|
| Log In | `deploycms` → menjadi `deploycms@inovass.com` |
| Directory | `inovass` → path `/home/inom3994/inovass` |
| Quota | Unlimited |

Pastikan kolom *Path* di daftar akun benar-benar `/home/inom3994/inovass`. Workflow meng-upload `release.zip` ke root akun FTP ini. Akun FTP situs statis (`deploy@inovass.com`, root `public_html`) **tidak dipakai** oleh CMS.

### 3.2 Database MySQL

cPanel → bagian **Databases** → **Database Wizard** (satu alur untuk database + user + hak akses):

1. **Step 1 · Create A Database.** Isi `inovass` → *Next Step*. Nama sebenarnya: `inom3994_inovass`.
2. **Step 2 · Create Database Users.**
   - Username `inovass` (maks. 7 huruf, karena awalan `inom3994_` sudah 9 dari batas 16 karakter) → `inom3994_inovass`.
   - Klik **Password Generator** → centang *I have copied this password in a safe place* → *Use Password*. **Salin dan simpan password-nya** (tidak bisa dilihat lagi; bisa direset di *Manage My Databases*).
   - *Create User*.
3. **Step 3 · Add User to the Database.** Centang **ALL PRIVILEGES** → *Make Changes*.
4. **Cek:** cPanel → **Manage My Databases** → di *Current Databases* harus ada `inom3994_inovass` dengan *Privileged Users* berisi user-nya (di akun ini `inom3994_admin`). Nama user itu yang dipakai di `DB_USERNAME`.

Hasilnya dipakai di `.env` server (3.7):

```dotenv
DB_HOST=localhost
DB_DATABASE=inom3994_inovass
DB_USERNAME=inom3994_admin
DB_PASSWORD="...password-dari-langkah-2..."
```

- Host selalu `localhost` (database di server yang sama), bukan alamat IP atau `kumai.iixcp.rumahweb.net`.
- Password yang mengandung `#`, `$`, spasi, atau tanda kutip **wajib diberi tanda kutip** di `.env`, kalau tidak terpotong dan muncul `Access denied`.
- Tabel **tidak dibuat manual**: dibuat otomatis oleh `migrate` lewat cron (3.8). Jangan impor SQL atau buat tabel di phpMyAdmin.
- Cek isi database kapan saja: cPanel → **phpMyAdmin** → `inom3994_inovass`.

### 3.3 Subdomain

cPanel → **Domains** → *Create A New Domain*:

| Field | Isi |
|---|---|
| Domain | `jadwal.inovass.com` |
| Share document root | **Tidak dicentang** |
| Document Root | `inovass/public` (di belakang awalan `/public_html/` yang tidak bisa dihapus) |

Cek di *List Domains*: document root `jadwal.inovass.com` = **`/public_html/inovass/public`**. cPanel Rumahweb tidak mengizinkan document root di luar `public_html` (`../` diabaikan), karena itu workflow menyalin `public/` ke sana (lihat bagian 1).

DNS: kalau nameserver `inovass.com` di Rumahweb, subdomain aktif otomatis. Kalau DNS dikelola di tempat lain (mis. Cloudflare), tambah record **A** `jadwal` → `202.10.43.124` (Shared IP di cPanel).

SSL: cPanel → **SSL/TLS Status** → *Run AutoSSL*. Biasanya terpasang otomatis dalam beberapa menit.

> Kalau suatu saat CMS mau dipakai di `inovass.com` langsung, document root domain utama diubah ke `inovass/public`, dan situs statis di `public_html` tidak dipakai lagi. Jangan dilakukan tanpa rencana.

### 3.4 Versi PHP

- cPanel → **MultiPHP Manager** → centang `jadwal.inovass.com` → pilih **PHP 8.4** (atau lebih baru) → *Apply*.
  **Harus 8.4.** Paket di `composer.lock` (Symfony 8) menolak berjalan di PHP 8.3.
- cPanel → **Select PHP Version** (bila ada) → pastikan aktif: `intl`, `pdo_mysql`, `mbstring`, `fileinfo`, `gd`, `zip`, `curl`, `openssl`, `xml`, `bcmath`.
- Opsi PHP: `memory_limit` ≥ 256M, `upload_max_filesize` dan `post_max_size` ≥ 12M (brosur PDF hingga 10 MB).

### 3.5 GitHub secrets

GitHub → repo `marsyadiya23/web-inovass` → **Settings → Secrets and variables → Actions → New repository secret**:

| Name | Value |
|---|---|
| `FTP_SERVER` | `kumai.iixcp.rumahweb.net` |
| `CMS_FTP_USERNAME` | `deploycms@inovass.com` (username FTP lengkap dari 3.1) |
| `CMS_FTP_PASSWORD` | password akun FTP dari 3.1 |

Tiga secret itu cukup untuk CMS. `FTP_SERVER` juga dipakai workflow situs statis (bersama `FTP_USERNAME`/`FTP_PASSWORD` miliknya). Secrets tidak ikut berpindah antar-repo: kalau repo ini baru, isi ulang semuanya.

### 3.6 Deploy pertama

Lakukan **setelah** `.env` server (3.7) dan cron permanen (3.8a) terpasang.

1. Pastikan kode sudah di branch `main`, lalu push. Atau GitHub → **Actions → Deploy CMS to cPanel → Run workflow**.
2. Actions hijau dalam ±3–5 menit (build ±2 menit, upload zip ±1 menit).
3. Dalam ≤ 1 menit setelah hijau, cron mengekstrak dan menjalankan migrate. Cek `inovass/storage/logs/deploy.log`: harus berakhir `deploy selesai`.
4. Isi data awal sekali (cron seed di 3.8b).

### 3.7 Buat `.env` di server

1. Di laptop, buat APP_KEY untuk production (jangan pakai key lokal):
   ```powershell
   cd cms
   php artisan key:generate --show
   ```
2. cPanel → **File Manager** → `/home/inom3994/inovass/` → **+ File** → nama `.env` → *Edit*, isi:

```dotenv
APP_NAME=INOVASS
APP_ENV=production
APP_DEBUG=false
APP_KEY=base64:...hasil-perintah-di-atas...
APP_URL=https://inovass.com
ASSET_URL=https://inovass.com/inovass/public
APP_LOCALE=id
APP_FALLBACK_LOCALE=en

LOG_CHANNEL=stack
LOG_STACK=single
LOG_LEVEL=error

DB_CONNECTION=mysql
DB_HOST=localhost
DB_PORT=3306
DB_DATABASE=inom3994_inovass
DB_USERNAME=inom3994_admin
DB_PASSWORD=...password-database-dari-3.2...

SESSION_DRIVER=database
SESSION_LIFETIME=120
CACHE_STORE=database
QUEUE_CONNECTION=sync
FILESYSTEM_DISK=local

# Akun admin (dibuat sekali oleh db:seed). Email ini juga menerima notifikasi pendaftar.
ADMIN_EMAIL=inovass.adm@gmail.com
ADMIN_PASSWORD=...password-admin-minimal-12-karakter...

# Email notifikasi pendaftar baru (lihat 3.10)
MAIL_MAILER=smtp
MAIL_SCHEME=smtps
MAIL_HOST=mail.inovass.com
MAIL_PORT=465
MAIL_USERNAME=noreply@inovass.com
MAIL_PASSWORD=...password-akun-email-noreply...
MAIL_FROM_ADDRESS=noreply@inovass.com
MAIL_FROM_NAME="INOVASS Pelatihan"
```

- `.env` berisi password. **Jangan di-commit, jangan dibagikan.** File Manager tidak menampilkannya di URL publik karena berada di luar `public/`.
- `APP_DEBUG=false` wajib di production. Kalau `true`, error akan menampilkan password database ke pengunjung.

### 3.8 Cron

cPanel → **Cron Jobs**. *Common Settings*: **Once Per Minute** (`* * * * *`).

PHP untuk cron: di server `kumai` (akun inom3994, dites 2026-10-22), `php` biasa = *cgi-fcgi*, sedangkan **`/opt/cpanel/ea-php84/root/usr/bin/php` = versi CLI yang benar** (8.4.26 saat dites, harus ≥ 8.4.27 setelah patch). Semua cron di bawah memakai path itu. Cara cek ulang: cron sementara `/opt/cpanel/ea-php84/root/usr/bin/php -v > ~/phpver.txt 2>&1`, baca `/home/inom3994/phpver.txt`, lalu hapus cron tes.

**a. Cron permanen: jalankan `deploy.php` setiap ada deploy baru** (pasang sekali, biarkan aktif selamanya)

```
cd ~/inovass && [ -f deploy-pending ] && /opt/cpanel/ea-php84/root/usr/bin/php deploy.php >> storage/logs/deploy.log 2>&1 && rm deploy-pending
```

- Jalan tiap menit tapi hanya bekerja kalau CI baru meng-upload `deploy-pending`.
- `deploy-pending` dihapus **hanya kalau sukses**. Kalau gagal (mis. zip belum selesai ter-upload), dicoba lagi menit berikutnya. Cek `storage/logs/deploy.log`.
- Pasang cron ini **sebelum** deploy pertama.

**b. Data awal (sekali saja, setelah `deploy.log` menunjukkan `deploy selesai`)**: katalog 127 program pelatihan dan akun admin.

```
cd ~/inovass && (/opt/cpanel/ea-php84/root/usr/bin/php artisan config:clear && /opt/cpanel/ea-php84/root/usr/bin/php artisan db:seed --force && /opt/cpanel/ea-php84/root/usr/bin/php artisan optimize) >> storage/logs/deploy.log 2>&1
```

Tunggu 1–2 menit, cek `deploy.log` (ada `Seeding database` tanpa `ERROR`), lalu **hapus cron ini segera**.

> ⚠ **Jangan biarkan cron ini aktif dan jangan jalankan `db:seed` lagi.** Setiap kali seed jalan, password admin direset ke `ADMIN_PASSWORD` dan Pengaturan Situs (nomor WhatsApp, alamat, dll.) ditimpa ke nilai awal.
> `config:clear` di awal wajib: kalau config sedang di-cache, `ADMIN_PASSWORD` tidak terbaca dan password admin menjadi `inovass123`.

### 3.9 Cek hasil

1. Buka https://inovass.com/jadwal-pelatihan → daftar jadwal tampil.
2. Buka https://inovass.com/admin → login `ADMIN_EMAIL` + `ADMIN_PASSWORD`.
3. Klik avatar (kanan atas) → **Profil** → ganti password bila perlu. Setelah itu `ADMIN_PASSWORD` di `.env` boleh dihapus.
4. **Pengaturan → Pengaturan Situs** → cek nomor WhatsApp (dipakai tombol konfirmasi pendaftaran).
5. Coba daftar satu pelatihan dari website → muncul di **Kotak Masuk → Pendaftar**, dan email notifikasi masuk ke Gmail admin (cek juga folder Spam).

### 3.10 Email notifikasi pendaftar

Email yang dikirim CMS:

| Kapan | Ke | Isi |
|---|---|---|
| Pendaftar baru | **Semua akun admin** (email login) | Program & jadwal, data pendaftar, tombol **Proses di admin**. *Balas* = langsung ke pendaftar |
| Pendaftar baru | **Pendaftar** | "Pendaftaran diterima", ringkasan, info akan dihubungi ≤ 1×24 jam kerja, tombol WhatsApp |
| Admin mengubah status ke **Dikonfirmasi** | **Pendaftar** | Konfirmasi + waktu, tempat, jumlah peserta, catatan jadwal |
| Admin mengubah status ke **Batal** | **Pendaftar** | Pemberitahuan pembatalan |

Email ke pendaftar memakai Reply-To = email di **Pengaturan Situs**, jadi balasan pendaftar masuk ke email kantor. Selama `MAIL_MAILER=log`, semua email ini hanya tercatat di `storage/logs/laravel.log` (tidak terkirim).

Pengirimnya akun email domain sendiri di cPanel, supaya tidak masuk spam:

1. cPanel → **Email Accounts** → *Create* → `noreply@inovass.com`, password kuat. Isi `MAIL_USERNAME`, `MAIL_PASSWORD`, `MAIL_FROM_ADDRESS` di `.env` (3.7).
2. Di akun itu → **Connect Devices** → lihat *Outgoing Server* & port SMTP (SSL/TLS). Biasanya `mail.inovass.com` port `465`. Kalau berbeda (mis. `kumai.iixcp.rumahweb.net`), pakai yang tertulis di sana untuk `MAIL_HOST`.
3. cPanel → **Email Deliverability** → `inovass.com` → SPF dan DKIM harus **Valid**. Kalau ada masalah, klik *Repair*. Tanpa ini Gmail cenderung menaruh email di Spam.
4. Setelah mengubah `.env`, jalankan sekali via cron: `cd ~/inovass && php artisan optimize`.
5. Uji: daftar dari website. Kalau email masuk Spam, tandai **Bukan spam** sekali di Gmail.

- **Ganti penerima notifikasi:** ganti email lewat **Profil** di admin. Notifikasi ikut ke email baru.
- **Email gagal tidak menggagalkan pendaftaran.** Data tetap tersimpan, error dicatat di `storage/logs/laravel.log`.
- Alternatif tanpa email cPanel: SMTP Gmail (`MAIL_HOST=smtp.gmail.com`, `MAIL_PORT=465`, `MAIL_USERNAME` = alamat Gmail, `MAIL_PASSWORD` = *App Password* dari Google Account → Security → 2-Step Verification → App passwords).

---

## 4. Alur update sehari-hari

### Mengubah kode/tampilan CMS

```powershell
git checkout main
git pull
git checkout -b fitur/nama-perubahan     # opsional, disarankan

# ... edit file di cms/ ...
cd cms
php artisan serve                        # cek di browser
php artisan test                         # harus hijau

git add .
git commit -m "jelaskan perubahannya"
git push                                 # lalu merge ke main (Pull Request di GitHub)
```

Setelah masuk `main`:

1. GitHub Actions membangun dan meng-upload `release.zip` (tab **Actions → Deploy CMS to cPanel**, ±1 menit).
2. Dalam ≤ 1 menit setelah hijau, cron mengekstrak zip, menyalin `public/`, lalu menjalankan `migrate` + `optimize`.
3. Cek `storage/logs/deploy.log`: baris terakhir harus `deploy selesai`.

Selama proses ekstraksi (beberapa detik), situs bisa sebentar error atau URL baru 404. Hindari deploy saat jam ramai pendaftaran.

### Membaca status GitHub Actions

| Tampilan | Artinya | Perlu tindakan? |
|---|---|---|
| ✅ hijau (*success*) | Zip dan penanda ter-upload. Hasilnya baru terlihat setelah cron berjalan (≤ 1 menit) | Tidak. Cek `deploy.log` bila ragu |
| ⚪ abu-abu (*cancelled*) | Dibatalkan otomatis karena ada push yang lebih baru (`cancel-in-progress`), atau dibatalkan manual | Tidak. Run terbaru yang berlaku |
| ❌ merah (*failed*) | Salah satu langkah gagal. Klik run → klik langkah merah → baca pesan errornya | **Ya**, lihat tabel di bawah |

Penyebab merah yang pernah terjadi:

| Pesan di langkah merah | Penyebab | Solusi |
|---|---|---|
| `Input required and not supplied: username` | Secret `CMS_FTP_USERNAME` belum ada atau salah nama | Isi di Settings → Secrets → Actions, lalu **Re-run all jobs** |
| `530 Login authentication failed` | Username/password FTP salah | Cek dengan FileZilla, perbarui secret, lalu Re-run |
| Langkah **Build** merah, `requires php >=8.4` | `php-version` di workflow bukan 8.4 | Ubah ke `8.4` di `deploy-cms.yml` |
| Job berjalan berjam-jam lalu dibatalkan | Meng-upload ribuan file lewat FTP (cara lama) | Sudah diganti zip; pastikan memakai workflow terbaru |

> Status merah juga bisa muncul dari **run lama** (mis. percobaan pertama sebelum secret diisi). Yang menentukan adalah **run paling atas** di tab Actions.

### Mengubah jadwal, program, pendaftar

**Tidak perlu deploy.** Dilakukan langsung di https://inovass.com/admin. Data tersimpan di MySQL server, bukan di repo.

> Data lokal (SQLite di laptop) dan data server (MySQL) **terpisah**. Mengisi jadwal di lokal tidak muncul di server.

### Deploy ulang manual

GitHub → **Actions → Deploy CMS to cPanel → Run workflow**. Berguna setelah mengganti secrets atau saat deploy sebelumnya gagal di tengah.

---

## 5. Perubahan database

- **Tambah kolom/tabel = buat migration baru**: `php artisan make:migration add_xxx_to_yyy_table`. Cron menjalankannya otomatis setelah deploy.
- **Jangan mengedit migration lama** yang sudah pernah jalan di server. Server tidak akan menjalankannya ulang.
- **Jangan pakai `migrate:fresh` / `db:wipe` di server.** Semua data pendaftar akan hilang.
- Migration yang menghapus kolom/tabel: backup database dulu (lihat [7](#7-backup--rollback)).
- Lokal memakai SQLite, server MySQL. Hindari SQL mentah khusus salah satunya. Pakai Schema Builder / Eloquent.
- Gagal migrate? Lihat `storage/logs/deploy.log`. Perbaiki dengan migration baru, push lagi.

---

## 6. Isi panel admin

Admin dibatasi ke urusan pelatihan:

| Menu | Fungsi |
|---|---|
| Dasbor | Jadwal mendatang, pendaftar baru, program aktif, 6 jadwal terdekat, 5 pendaftar terbaru |
| Pelatihan → Jadwal Pelatihan | Tambah/ubah/duplikat jadwal, kuota, status Dibuka/Penuh/Ditutup/Batal, **sembunyikan harga** (website tampil "Hubungi kami"), **Ekspor peserta** per jadwal ke Excel |
| Pelatihan → Program Pelatihan | Katalog program, deskripsi, harga, **silabus** (PDF atau gambar; tampil juga di setiap jadwalnya), tampil/sembunyi |
| Pelatihan → Kategori Pelatihan | Kategori & urutan |
| Kotak Masuk → Pendaftar | Proses pendaftar (Baru → Dikonfirmasi/Batal; pendaftar otomatis dapat email), catatan, hubungi via WhatsApp, **Ekspor Excel** (ikut filter status/jadwal yang aktif) |
| Pengaturan → Pengaturan Situs | Nomor WhatsApp, kontak, logo |
| Profil (avatar kanan atas) | Ganti nama, email, password admin |

Detail hak akses: [HAK-AKSES-ADMIN.md](HAK-AKSES-ADMIN.md).

Menu konten compro (Beranda, Layanan, Berita, Pesan Masuk, dll.) sengaja **tidak didaftarkan**. Kodenya masih ada di `app/Filament/`. Untuk mengaktifkannya lagi, tambahkan class-nya ke `->resources([...])` / `->pages([...])` di `app/Providers/Filament/AdminPanelProvider.php`.

Menambah akun admin baru belum bisa dari panel. Sementara: ganti email/password akun yang ada lewat Profil.

---

## 7. Backup & rollback

### Backup

| Apa | Cara | Kapan |
|---|---|---|
| Database | cPanel → **phpMyAdmin** → pilih `inom3994_inovass` → *Export* → Quick, SQL | Mingguan, dan **sebelum deploy yang mengubah database** |
| Upload admin | File Manager → `inovass/public/uploads` → *Compress* → download | Mingguan |
| `.env` | Download, simpan di tempat aman (bukan repo) | Sekali, dan setiap diubah |
| Kode | Repo GitHub = backup | Otomatis |

cPanel → **Backup** / **JetBackup** (bila tersedia di paket) bisa memulihkan home dir + database harian.

### Rollback kode

```powershell
git revert <hash-commit-yang-bermasalah>
git push
```

Workflow membangun ulang versi lama, lalu cron mengekstraknya di atas versi sekarang. **Catatan:** file yang baru ditambahkan di versi bermasalah tidak ikut terhapus, dan rollback kode tidak membatalkan migration yang sudah jalan. Kalau perubahan database ikut bermasalah, pulihkan dari backup phpMyAdmin (*Import*).

---

## 8. Troubleshooting

Langkah pertama untuk hampir semua masalah di server: buka **`inovass/storage/logs/laravel.log`** (baris paling bawah) dan **`inovass/storage/logs/deploy.log`**.

| Gejala | Penyebab & solusi |
|---|---|
| Actions merah di langkah **Build**: `requires php >=8.4` | `php-version` di `deploy-cms.yml` harus `8.4` (atau lebih baru) |
| Actions merah: **login failed / 530** atau `Input required: username` | `CMS_FTP_USERNAME`/`CMS_FTP_PASSWORD`/`FTP_SERVER` salah, kosong, atau salah nama. Uji dengan FileZilla memakai data yang sama |
| Actions hijau tapi website tidak berubah | Cron belum mengekstrak. Cek ada tidaknya `inovass/deploy-pending` di File Manager, lalu `storage/logs/deploy.log`. Pastikan cron 3.8a terpasang |
| `deploy.log` berhenti setelah `public/ disalin`, berulang tiap menit, tanpa `deploy selesai` | Versi lama `deploy.php` memanggil `artisan` lewat `passthru`, yang diblokir hosting. Sudah diganti (Laravel dijalankan di dalam `deploy.php`). Pastikan deploy terbaru sudah ter-upload |
| `deploy.log`: `ERROR ...` | Pesan error lengkap tertulis di baris itu. Penyebab umum: password DB atau `APP_KEY` di `.env` server salah |
| `deploy.log`: `release.zip hilang atau rusak` | Zip belum selesai ter-upload. Biasanya sembuh sendiri di menit berikutnya. Kalau terus berulang, *Run workflow* lagi |
| **500 di laptop**, log: `could not find driver` | `.env` laptop berisi `DB_CONNECTION=mysql`. Kembalikan ke `sqlite` (data MySQL hanya untuk `.env` server) |
| Website menampilkan daftar file / 403 di `jadwal.inovass.com` | `public/` belum tersalin. Cek `deploy.log` (baris `public/ disalin`) dan isi `public_html/inovass/public` di File Manager |
| Gambar upload admin tidak tampil | Upload tersimpan di `public_html/inovass/public/uploads`. Pastikan deploy terakhir sukses (`cms/public/index.php` versi terbaru, ada `usePublicPath`) |
| Actions merah: **TLS / certificate** | Ubah `protocol: ftps` → `ftp` di `deploy-cms.yml` |
| Workflow tidak jalan setelah push | Hanya jalan untuk push ke `main` yang mengubah `cms/`. Jalankan manual: *Actions → Run workflow* |
| File di server tidak ter-update | *Run workflow* lagi. Kalau upload zip dilewati, hapus `inovass/.ftp-deploy-sync-state.json`, lalu *Run workflow* |
| **500 Server Error** | Lihat `laravel.log`. Penyebab umum: `.env` belum ada/salah, `APP_KEY` kosong, password DB salah |
| `No application encryption key` | `APP_KEY` di `.env` kosong. Isi dari `php artisan key:generate --show`, lalu jalankan `php artisan config:clear` via cron sekali |
| `SQLSTATE[HY000] [1045] Access denied` | `DB_USERNAME`/`DB_PASSWORD` salah, atau user belum ditambahkan ke database (Database Wizard langkah privileges) |
| `Table '...sessions' doesn't exist` | Migrate belum jalan. Cek cron 3.8 dan `deploy.log` |
| Halaman putih / `Composer detected issues in your platform` | PHP subdomain bukan 8.4. Atur di **MultiPHP Manager** |
| Perubahan `.env` tidak berpengaruh | Config di-cache. Jalankan sekali via cron: `cd ~/inovass && php artisan optimize` (cache ulang dari `.env` baru) |
| URL baru 404 setelah deploy | Route masih di-cache versi lama. Tunggu cron (≤ 1 menit). Cek `deploy-pending` sudah hilang dan `deploy.log` |
| `deploy.log` tidak pernah terisi | Cron salah perintah PHP atau path. Ulangi tes 3.8a |
| Admin tampil tanpa CSS | Folder `public/css/filament` belum ter-upload. *Run workflow* lagi |
| Upload brosur gagal | `upload_max_filesize` / `post_max_size` di **Select PHP Version → Options** kurang dari 12M |
| Lupa password admin | Ganti `ADMIN_PASSWORD` di `.env`, lalu cron sekali: `cd ~/inovass && php artisan config:clear && php artisan tinker --execute="App\Models\User::where('email',env('ADMIN_EMAIL'))->update(['password'=>bcrypt(env('ADMIN_PASSWORD'))])" && php artisan optimize`. **Jangan** pakai `db:seed` (menimpa pengaturan) |
| Email notifikasi tidak masuk | Cek folder Spam Gmail. Lalu `laravel.log`: `Connection could not be established` = `MAIL_HOST`/`MAIL_PORT` salah. `Authentication failed` = `MAIL_USERNAME`/`MAIL_PASSWORD` salah. Setelah ubah `.env`, jalankan `php artisan optimize` via cron |
| Jadwal tampil tapi tombol daftar tidak ada | Jadwal lewat batas daftar, kuota penuh, atau status bukan *Dibuka* (sesuai aturan bisnis, bukan bug) |

---

## 9. Aturan penting (jangan dilanggar)

1. **Jangan edit file aplikasi di File Manager** (kecuali `.env`). Akan tertimpa deploy berikutnya. Edit di repo, push.
2. **Jangan jalankan `db:seed`, `migrate:fresh`, atau `db:wipe` di server** setelah setup pertama.
3. **`APP_DEBUG=false`** di server, selalu.
4. **Jangan commit `.env`**, `database.sqlite`, atau `vendor/` (sudah di `.gitignore`).
5. **Kode aplikasi dan `.env` hanya di `/home/inom3994/inovass`.** Di `public_html/inovass/public` hanya boleh isi `cms/public` (index.php, aset, uploads), disalin otomatis oleh `deploy.php`. Jangan pernah menyalin `.env` atau `vendor/` ke dalam `public_html`.
6. **Jangan hapus `.ftp-deploy-sync-state.json`** kecuali memang ingin upload ulang semua.
7. **`php artisan test` harus hijau sebelum merge ke `main`.** `main` = production.
