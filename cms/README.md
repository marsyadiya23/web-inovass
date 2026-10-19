# INOVASS CMS

CMS untuk **jadwal & pendaftaran pelatihan** INOVASS (Laravel 13 + Filament v5).
Website compro statis tetap di folder `../public/` dan tidak bergantung pada folder ini.

- Kebutuhan produk: [PRD.md](PRD.md)
- Peta menu & hak akses admin: [docs/HAK-AKSES-ADMIN.md](docs/HAK-AKSES-ADMIN.md)
- PRD lama (CMS compro, sudah tidak dipakai): [docs/PRD-compro-v1.md](docs/PRD-compro-v1.md)

## Isi

| Bagian | Lokasi |
|---|---|
| Panel admin (`/admin`) | `app/Filament/` (Resources, Pages, Widgets) |
| Halaman jadwal & pelatihan | `app/Http/Controllers/PelatihanController.php`, `resources/views/pelatihan/` |
| Halaman compro (salinan tampilan situs) | `resources/views/{home,pages,layanan,berita}/` |
| Model & aturan bisnis (kuota, status, batas daftar) | `app/Models/TrainingSchedule.php` |
| Skema database | `database/migrations/` |
| Data awal (katalog 127 pelatihan, 521 halaman layanan) | `database/seeders/`, `database/seeders/data/layanan.json` |
| CSS/JS/gambar situs | `public/assets/`, gambar konten di `public/uploads/legacy/` |

## Menjalankan di lokal

Butuh PHP 8.3+ (ekstensi: pdo_sqlite, mbstring, intl, gd, zip, fileinfo, openssl, curl) dan Composer.

```bash
cd cms
composer install
cp .env.example .env
php artisan key:generate
touch database/database.sqlite        # Windows cmd: type nul > database\database.sqlite
php artisan migrate --seed
php artisan serve
```

- Website: http://127.0.0.1:8000 · Jadwal: http://127.0.0.1:8000/jadwal-pelatihan
- Admin: http://127.0.0.1:8000/admin · login `admin@inovass.com` / `inovass123` (lokal saja; set `ADMIN_PASSWORD` di `.env` sebelum seed di server)
- Reset semua data ke awal: `php artisan migrate:fresh --seed` (menghapus semua isian admin)
- Test: `php artisan test`

## Catatan

- Upload dari admin disimpan di `public/uploads/` (tidak di-commit), tanpa `storage:link`.
- Jadwal & pendaftar contoh hanya dibuat di environment `local`/`testing`.
## Deploy ke cPanel (CI/CD)

Push ke `main` yang mengubah `cms/` → GitHub Actions ([`deploy-cms.yml`](../.github/workflows/deploy-cms.yml)) menjalankan `composer install --no-dev`, lalu meng-upload file yang berubah via FTPS ke `/home/inom3994/inovass`. Cron di server lalu menjalankan `migrate` + `optimize`. Workflow situs statis (`deploy-cpanel.yml`) tetap terpisah.

Setup sekali saja:

1. **PHP:** cPanel → *MultiPHP Manager* → domain/subdomain CMS pakai PHP 8.3+. Di *Select PHP Version* aktifkan `intl`, `pdo_mysql`, `fileinfo`, `gd`, `zip`.
2. **Domain:** cPanel → *Domains* → buat subdomain (mis. `cms.inovass.com`) dengan Document Root `inovass/public`. Domain utama tetap melayani situs statis sampai diputuskan pindah.
3. **Database:** *MySQL Databases* → buat DB `inom3994_inovass` + user, beri *All Privileges*.
4. **FTP:** *FTP Accounts* → buat `deploycms`, Directory `inovass`.
5. **GitHub secrets:** `CMS_FTP_USERNAME` (`deploycms@inovass.com`), `CMS_FTP_PASSWORD`. `FTP_SERVER` dipakai bersama dengan situs statis.
6. **Deploy pertama:** GitHub → *Actions* → *Deploy CMS to cPanel* → *Run workflow* (pertama kali lama: ribuan file `vendor/`).
7. **`.env`:** File Manager → `inovass/.env`. Isi seperti PRD §9.6 (`APP_ENV=production`, `APP_DEBUG=false`, `APP_URL`, `DB_*`, `QUEUE_CONNECTION=sync`, `ADMIN_PASSWORD`). `APP_KEY` dibuat di lokal: `php artisan key:generate --show`.
8. **Cron** (*Cron Jobs*, tiap menit). Cron ini hanya bekerja bila ada file `deploy-pending` dari CI:
   ```
   cd ~/inovass && [ -f deploy-pending ] && rm deploy-pending && (/opt/cpanel/ea-php83/root/usr/bin/php artisan migrate --force && /opt/cpanel/ea-php83/root/usr/bin/php artisan optimize) >> storage/logs/deploy.log 2>&1
   ```
9. **Seed sekali** (data awal + akun admin): tambah cron sementara `cd ~/inovass && /opt/cpanel/ea-php83/root/usr/bin/php artisan db:seed --force >> storage/logs/deploy.log 2>&1`. Hapus cron itu setelah `deploy.log` menunjukkan sukses. Bisa juga lewat cPanel → *Terminal* bila tersedia.

Catatan:
- Jangan edit file di File Manager kecuali `.env`. Perubahan lain akan tertimpa deploy berikutnya.
- `.env`, `storage/` (log, sesi, upload di `storage/app`), dan upload admin di `public/uploads/` tidak disentuh deploy.
- Selama upload dan sampai cron jalan (≤1 menit), situs bisa sempat error atau route baru 404.
- Gagal migrate? Lihat `inovass/storage/logs/deploy.log` dan `storage/logs/laravel.log`.
