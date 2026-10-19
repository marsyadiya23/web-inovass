# INOVASS CMS

CMS untuk **jadwal & pendaftaran pelatihan** INOVASS (Laravel 13 + Filament v5).
Website compro statis tetap di folder `../public/` dan tidak bergantung pada folder ini.

- **Panduan lokal, deploy cPanel & CI/CD: [docs/PANDUAN-DEPLOY.md](docs/PANDUAN-DEPLOY.md)**
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

Butuh PHP 8.4+ (ekstensi: pdo_sqlite, mbstring, intl, gd, zip, fileinfo, openssl, curl) dan Composer.

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

Push ke `main` yang mengubah `cms/` → GitHub Actions ([`deploy-cms.yml`](../.github/workflows/deploy-cms.yml)) membangun dan meng-upload ke `/home/inom3994/inovass` via FTPS → cron di server menjalankan `migrate` + `optimize`. Live di https://jadwal.inovass.com.

**Panduan lengkap** (setup cPanel, database, `.env`, cron, alur update, backup, troubleshooting): [docs/PANDUAN-DEPLOY.md](docs/PANDUAN-DEPLOY.md).
