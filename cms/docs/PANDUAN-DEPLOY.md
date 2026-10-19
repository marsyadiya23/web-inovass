# Panduan CMS INOVASS: Lokal, cPanel, dan CI/CD

Panduan lengkap untuk menjalankan CMS jadwal & pendaftaran pelatihan di laptop, memasangnya di cPanel Rumahweb, dan mengirim perubahan secara otomatis lewat GitHub Actions.

| | |
|---|---|
| Repo | https://github.com/marsyadiya23/web-inovass (folder `cms/`) |
| Hosting | cPanel Rumahweb, akun `inom3994`, server `kumai.iixcp.rumahweb.net` |
| Lokasi aplikasi di server | `/home/inom3994/inovass` (di **luar** `public_html`) |
| Alamat | `https://jadwal.inovass.com` · admin: `/admin` |
| Situs compro statis | Tetap di `public_html` (`inovass.com`), deploy terpisah. Lihat [README root](../../README.md) |

---

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
                           2. buat file penanda deploy-pending
                           3. upload file yang BERUBAH via FTPS ──▶ /home/inom3994/inovass
                                                                    │
                                                    Cron tiap menit ▼
                                         ada deploy-pending? → migrate + optimize
                                                                    │
 Pengunjung ◀────────────────── HTTPS ── jadwal.inovass.com ◀── document root inovass/public
```

Poin penting:

- **Server tidak butuh Composer, Node, Git, atau SSH.** Semua dibangun di GitHub Actions, server hanya menerima file.
- **Hanya file yang berubah yang di-upload.** Daftar file yang sudah ter-upload disimpan di `/home/inom3994/inovass/.ftp-deploy-sync-state.json`. **Jangan dihapus**, kecuali sengaja ingin upload ulang semua.
- **Yang tidak pernah disentuh deploy:** `.env`, isi `storage/` (log, sesi, cache), dan file upload admin di `public/uploads/`. File-file itu tidak ada di repo, jadi aman.
- Situs statis (`public/` di root repo → `public_html`) punya workflow sendiri (`deploy-cpanel.yml`). Push ke `cms/` tidak memicunya, dan sebaliknya.

Struktur di server setelah deploy:

```
/home/inom3994/
├── public_html/          ← situs compro statis (inovass.com), JANGAN dicampur
└── inovass/              ← aplikasi CMS (isi folder cms/ dari repo)
    ├── .env              ← dibuat manual di File Manager, tidak ada di repo
    ├── app/ config/ database/ routes/ resources/ vendor/ ...
    ├── storage/logs/     ← laravel.log (error aplikasi), deploy.log (hasil cron)
    └── public/           ← document root jadwal.inovass.com
        ├── index.php  .htaccess
        └── uploads/      ← gambar/brosur yang di-upload admin
```

---

## 2. Menjalankan di lokal

### Kebutuhan

- **PHP 8.4+** dengan ekstensi `pdo_sqlite`, `mbstring`, `intl`, `gd`, `zip`, `fileinfo`, `openssl`, `curl`
- **Composer**
- Database lokal memakai **SQLite** (satu file, tanpa install MySQL)

Cek: `php -v` dan `composer -V`.

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
| Admin | http://127.0.0.1:8000/admin · `admin@inovass.com` / `inovass123` (hanya lokal) |

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

Pastikan kolom *Path* di daftar akun benar-benar `/home/inom3994/inovass`. Workflow meng-upload ke root akun FTP ini.

### 3.2 Database MySQL

cPanel → **Database Wizard**:

1. Nama database: `inovass` → otomatis menjadi `inom3994_inovass`
2. User: `inovass` → menjadi `inom3994_inovass`. Pakai *Password Generator*, **simpan password-nya**.
3. Privileges: centang **ALL PRIVILEGES** → *Next Step*.

Host database dari aplikasi: `localhost`.

### 3.3 Subdomain

cPanel → **Domains** → *Create A New Domain*:

| Field | Isi |
|---|---|
| Domain | `jadwal.inovass.com` |
| Share document root | **Tidak dicentang** |
| Document Root | `inovass/public` |

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

`FTP_SERVER` dipakai bersama oleh workflow situs statis.

### 3.6 Deploy pertama

1. Pastikan kode sudah di branch `main` (merge dari `feat/cms`) lalu push. Atau GitHub → **Actions → Deploy CMS to cPanel → Run workflow**.
2. Upload pertama **lama** (±10–30 menit), karena ada ribuan file `vendor/`. Deploy berikutnya hanya file yang berubah, biasanya < 2 menit.
3. Tunggu sampai centang hijau di tab Actions.

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
APP_URL=https://jadwal.inovass.com
APP_LOCALE=id
APP_FALLBACK_LOCALE=en

LOG_CHANNEL=stack
LOG_STACK=single
LOG_LEVEL=error

DB_CONNECTION=mysql
DB_HOST=localhost
DB_PORT=3306
DB_DATABASE=inom3994_inovass
DB_USERNAME=inom3994_inovass
DB_PASSWORD=...password-database-dari-3.2...

SESSION_DRIVER=database
SESSION_LIFETIME=120
CACHE_STORE=database
QUEUE_CONNECTION=sync
FILESYSTEM_DISK=local

ADMIN_PASSWORD=...password-admin-minimal-12-karakter...
```

- `.env` berisi password. **Jangan di-commit, jangan dibagikan.** File Manager tidak menampilkannya di URL publik karena berada di luar `public/`.
- `APP_DEBUG=false` wajib di production. Kalau `true`, error akan menampilkan password database ke pengunjung.

### 3.8 Cron

cPanel → **Cron Jobs**. *Common Settings*: **Once Per Minute** (`* * * * *`).

**a. Cek perintah PHP yang dipakai cron**

Tambah cron sementara:

```
php -v > ~/phpver.txt 2>&1
```

Tunggu 1–2 menit, buka `/home/inom3994/phpver.txt` di File Manager.

- Tertulis `PHP 8.4.x` → pakai `php` di perintah-perintah berikut.
- Versi lain → pakai path lengkap. Di Rumahweb biasanya `/opt/alt/php84/usr/bin/php`, atau `/opt/cpanel/ea-php84/root/usr/bin/php`. Ulangi tes dengan path itu sampai muncul 8.4.

Hapus cron tes ini setelah ketemu. Di bawah ditulis `php`; ganti bila perlu.

**b. Setup pertama (sekali saja)**: membuat tabel, data awal (katalog 127 pelatihan), dan akun admin.

```
cd ~/inovass && (php artisan config:clear && php artisan migrate --force && php artisan db:seed --force && php artisan optimize) >> storage/logs/deploy.log 2>&1
```

Tunggu 1–2 menit, buka `inovass/storage/logs/deploy.log`. Kalau ada baris `Seeding database` dan `Caching ...` tanpa `ERROR`, **hapus cron ini segera**.

> ⚠ **Jangan biarkan cron ini aktif dan jangan jalankan `db:seed` lagi.** Setiap kali seed jalan, password admin direset ke `ADMIN_PASSWORD` dan Pengaturan Situs (nomor WhatsApp, alamat, dll.) ditimpa ke nilai awal.
> `config:clear` di awal wajib: kalau config sedang di-cache, `ADMIN_PASSWORD` tidak terbaca dan password admin menjadi `inovass123`.

**c. Cron permanen untuk setiap deploy**

```
cd ~/inovass && [ -f deploy-pending ] && rm deploy-pending && (php artisan migrate --force && php artisan optimize) >> storage/logs/deploy.log 2>&1
```

Cron ini jalan tiap menit, tapi hanya bekerja kalau CI baru saja meng-upload file `deploy-pending`. Biarkan aktif selamanya.

### 3.9 Cek hasil

1. Buka https://jadwal.inovass.com/jadwal-pelatihan → daftar jadwal tampil.
2. Buka https://jadwal.inovass.com/admin → login `admin@inovass.com` + `ADMIN_PASSWORD`.
3. Klik avatar (kanan atas) → **Profil** → ganti password bila perlu. Setelah itu `ADMIN_PASSWORD` di `.env` boleh dihapus.
4. **Pengaturan → Pengaturan Situs** → cek nomor WhatsApp (dipakai tombol konfirmasi pendaftaran).
5. Coba daftar satu pelatihan dari website → muncul di **Kotak Masuk → Pendaftar**.

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

1. GitHub Actions membangun & meng-upload (tab **Actions → Deploy CMS to cPanel**).
2. Dalam ≤ 1 menit setelah upload selesai, cron menjalankan `migrate` + `optimize`.
3. Cek hasil di `storage/logs/deploy.log` bila ada perubahan database.

Selama upload berjalan sampai cron selesai, situs bisa sebentar error atau URL baru 404. Hindari deploy saat jam ramai pendaftaran.

### Mengubah jadwal, program, pendaftar

**Tidak perlu deploy.** Dilakukan langsung di https://jadwal.inovass.com/admin. Data tersimpan di MySQL server, bukan di repo.

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
| Pelatihan → Jadwal Pelatihan | Tambah/ubah/duplikat jadwal, kuota, status Dibuka/Penuh/Ditutup/Batal |
| Pelatihan → Program Pelatihan | Katalog program, deskripsi, harga, brosur, tampil/sembunyi |
| Pelatihan → Kategori Pelatihan | Kategori & urutan |
| Kotak Masuk → Pendaftar | Proses pendaftar (Baru → Dikonfirmasi/Batal), catatan, hubungi via WhatsApp |
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

Workflow meng-upload ulang file versi lama. **Catatan:** rollback kode tidak membatalkan migration yang sudah jalan. Kalau perubahan database ikut bermasalah, pulihkan dari backup phpMyAdmin (*Import*).

---

## 8. Troubleshooting

Langkah pertama untuk hampir semua masalah di server: buka **`inovass/storage/logs/laravel.log`** (baris paling bawah) dan **`inovass/storage/logs/deploy.log`**.

| Gejala | Penyebab & solusi |
|---|---|
| Actions merah di langkah **Build**: `requires php >=8.4` | `php-version` di `deploy-cms.yml` harus `8.4` (atau lebih baru) |
| Actions merah: **login failed / 530** | `CMS_FTP_USERNAME`/`CMS_FTP_PASSWORD`/`FTP_SERVER` salah. Uji dengan FileZilla memakai data yang sama |
| Actions merah: **TLS / certificate** | Ubah `protocol: ftps` → `ftp` di `deploy-cms.yml` |
| Workflow tidak jalan setelah push | Hanya jalan untuk push ke `main` yang mengubah `cms/`. Jalankan manual: *Actions → Run workflow* |
| File di server tidak ter-update | Hapus `inovass/.ftp-deploy-sync-state.json`, lalu *Run workflow* (upload ulang semua) |
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
| Lupa password admin | Ganti `ADMIN_PASSWORD` di `.env`, lalu cron sekali: `cd ~/inovass && php artisan config:clear && php artisan tinker --execute="App\Models\User::where('email','admin@inovass.com')->update(['password'=>bcrypt(env('ADMIN_PASSWORD'))])" && php artisan optimize`. **Jangan** pakai `db:seed` (menimpa pengaturan) |
| Jadwal tampil tapi tombol daftar tidak ada | Jadwal lewat batas daftar, kuota penuh, atau status bukan *Dibuka* (sesuai aturan bisnis, bukan bug) |

---

## 9. Aturan penting (jangan dilanggar)

1. **Jangan edit file aplikasi di File Manager** (kecuali `.env`). Akan tertimpa deploy berikutnya. Edit di repo, push.
2. **Jangan jalankan `db:seed`, `migrate:fresh`, atau `db:wipe` di server** setelah setup pertama.
3. **`APP_DEBUG=false`** di server, selalu.
4. **Jangan commit `.env`**, `database.sqlite`, atau `vendor/` (sudah di `.gitignore`).
5. **Jangan taruh folder `inovass/` di dalam `public_html`.** `.env` dan kode harus di luar folder publik.
6. **Jangan hapus `.ftp-deploy-sync-state.json`** kecuali memang ingin upload ulang semua.
7. **`php artisan test` harus hijau sebelum merge ke `main`.** `main` = production.
