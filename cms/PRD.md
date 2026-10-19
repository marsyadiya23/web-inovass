# PRD — INOVASS CMS Pelatihan

| | |
|---|---|
| Produk | CMS katalog & jadwal pelatihan INOVASS, menyatu dengan situs company profile inovass.com |
| Versi | 2.0 — 17 Oktober 2026 (perubahan scope) |
| Pembaca | Stakeholder INOVASS (keputusan bisnis, §2, §8, §13) · Tim developer yang mengeksekusi dengan Claude Code (§5–§11) |
| Menggantikan | [`docs/PRD-compro-v1.md`](docs/PRD-compro-v1.md) (CMS untuk mengedit seluruh situs compro). Dokumen lama hanya referensi latar belakang; scope-nya tidak berlaku lagi |
| Konvensi | **(asumsi)** = belum dikonfirmasi INOVASS, lihat §13. "Fase 1" = MVP yang sedang dibangun. Nama field dan status ditulis persis seperti di kode |

---

## 1. Ringkasan & Latar Belakang Perubahan Scope

### 1.1 Keputusan

> "inovass.com itu cuma company profile. Ide bikin CMS itu untuk update jadwal pelatihan dll, dan pelatihannya nanti bertambah dengan tambahan lain."

Konsekuensinya:

1. **Inti CMS = pelatihan.** Admin INOVASS mengelola katalog program pelatihan (akan terus bertambah), jadwal/batch tiap program, dan pendaftar.
2. **Situs compro praktis statis.** Tampilan dan isi inovass.com (beranda, tentang, layanan, produk, kontak, berita) tetap seperti sekarang. Situs itu tetap dirender aplikasi Laravel yang sama supaya halaman jadwal memakai layout, header, dan footer yang sama. Editor konten compro yang sudah terbangun **tidak dihapus**, tetapi disimpan di grup menu "Konten Website" yang tertutup (collapsed). Fitur ini tidak dikembangkan lebih lanjut.
3. **URL lama tetap hidup.** Semua URL `.html` situs lama tetap jalan seperti yang sudah diimplementasi.

### 1.2 Masalah yang diselesaikan

| Masalah sekarang | Setelah Fase 1 |
|---|---|
| Situs lama tidak punya jadwal pelatihan; calon peserta harus bertanya lewat WhatsApp | Halaman `/jadwal-pelatihan` menampilkan semua batch mendatang dengan filter bulan, kategori, dan metode |
| Menambah program pelatihan = menyalin file HTML | Admin mengisi formulir "Program Pelatihan" di `/admin`, lalu halaman langsung tayang |
| Pendaftaran tercecer di chat WhatsApp | Setiap pendaftaran tersimpan di database dengan status, lalu diteruskan ke WhatsApp untuk tindak lanjut |
| Kuota dan batas pendaftaran dipantau manual | Sistem menutup pendaftaran otomatis saat kuota habis atau batas daftar lewat |

### 1.3 Ukuran keberhasilan Fase 1

- Admin bisa menambah program baru beserta 1 batch dalam **≤ 10 menit** tanpa bantuan developer.
- Pendaftaran tidak bisa masuk ke batch yang penuh, ditutup, batal, atau lewat batas daftar (diuji otomatis, lihat §8).
- 100% pendaftaran yang lolos validasi tersimpan, sekalipun pengunjung menutup tab WhatsApp.
- Semua URL compro yang ada sekarang tetap mengembalikan 200 atau 301.

---

## 2. Tujuan & Non-Tujuan

### 2.1 Tujuan

| # | Tujuan | Fase |
|---|---|:-:|
| T1 | Katalog program pelatihan yang bisa ditambah dan diubah admin, dikelompokkan per kategori | 1 |
| T2 | Jadwal/batch per program: tanggal, metode, lokasi, harga, kuota, batas daftar, status | 1 |
| T3 | Halaman publik jadwal dengan filter, halaman detail program, dan form pendaftaran | 1 |
| T4 | Kotak masuk pendaftar dengan alur status `baru → dikonfirmasi / batal` | 1 |
| T5 | Notifikasi email ke admin + balasan otomatis ke pendaftar | 2 |
| T6 | Ekspor daftar peserta per batch (CSV/Excel) | 2 |
| T7 | SEO pelatihan: `sitemap.xml`, JSON-LD `Course`/`Event` | 2 |
| T8 | Peran Admin/Editor | 2 |

### 2.2 Non-tujuan (tidak dibangun, kecuali tercantum di Fase 3)

| Di luar scope | Catatan |
|---|---|
| Payment gateway / e-commerce / keranjang / invoice otomatis | Pembayaran tetap manual lewat admin. Opsi pembayaran online ada di Fase 3 |
| LMS / e-learning / video kelas / kuis | Pelatihan online tetap memakai Zoom/Meet. Opsi LMS ada di Fase 3 |
| Pembuatan sertifikat otomatis | Opsional di Fase 3 |
| Multi-bahasa | Situs hanya berbahasa Indonesia |
| Akun/login peserta | Pendaftar tidak membuat akun |
| Pengembangan CMS compro (section builder, versi, preview, media library, menu editor, migrasi ±540 halaman) | Scope PRD lama. Editor compro yang sudah ada dipertahankan apa adanya |
| Redesain situs compro | Tampilan tetap; hanya ditambah item nav, section beranda, dan halaman pelatihan |
| Integrasi WhatsApp API (kirim otomatis) | WhatsApp hanya berupa tautan `wa.me` |

---

## 3. Pengguna & Peran

| Pengguna | Fase | Akses | Kebutuhan utama |
|---|:-:|---|---|
| **Admin INOVASS** (1–2 orang, staf marketing/admin) | 1 | Seluruh `/admin` | Menambah program & batch, memproses pendaftar, sesekali mengubah pengaturan situs |
| **Editor** | 2 | Pelatihan + Kotak Masuk, tanpa Pengaturan, tanpa Konten Website, tanpa hapus | Staf tambahan yang hanya mengurus jadwal & pendaftar |
| **Pengunjung / calon peserta** (HR, QA/QHSE officer, dosen/laboran, individu) | 1 | Situs publik | Menemukan jadwal, membandingkan batch, mendaftar cepat dari ponsel |
| **Developer** | 1 | Server, repo | Deploy, backup, penambahan fitur |

Fase 1 hanya punya satu peran: setiap user di tabel `users` adalah Admin. Saat ini `User::canAccessPanel()` mengembalikan `true`, dan user hanya dibuat lewat seeder atau `php artisan make:filament-user`. Tidak ada registrasi publik untuk admin.

---

## 4. User Stories & Acceptance Criteria

Format: **Given/When/Then** ringkas. Setiap kriteria harus bisa diuji, baik dengan feature test maupun klik manual.

### US-01 (F1) — Admin menambah program pelatihan baru
Sebagai admin, saya ingin menambah program baru supaya katalog bisa bertambah tanpa developer.
- [ ] Menu **Pelatihan → Program Pelatihan → Buat** menampilkan form dengan field di §5.2. Field wajib: kategori, judul, slug.
- [ ] Slug terisi otomatis dari judul dan bisa diubah. Slug yang sudah dipakai ditolak dengan pesan validasi.
- [ ] Setelah disimpan dengan `is_published = true`, `/pelatihan/{slug}` mengembalikan 200 dan program muncul di `/pelatihan` di bawah kategorinya. Dengan `is_published = false`, URL itu mengembalikan 404.
- [ ] Jadwal bisa ditambahkan langsung dari halaman edit program (relation manager "Jadwal").
- [ ] Brosur hanya menerima PDF (≤ 10 MB) dan gambar hanya jpg/png/webp (≤ 2 MB).

### US-02 (F1) — Admin menambah atau menduplikasi batch
Sebagai admin, saya ingin membuat batch baru dengan cepat karena program yang sama sering diulang tiap bulan.
- [ ] Batch bisa dibuat dari relation manager program atau dari **Pelatihan → Jadwal Pelatihan → Buat** (dengan memilih program).
- [ ] Validasi: `start_date` wajib; `end_date ≥ start_date`; `registration_deadline ≤ start_date`; `quota ≥ 1` bila diisi; `price ≥ 0` bila diisi; `method` ∈ {offline, online, hybrid}.
- [ ] Aksi **Duplikat** pada baris jadwal membuka form berisi salinan semua field kecuali tanggal. Admin wajib mengisi tanggal baru, status di-reset ke `dibuka`, dan pendaftar tidak ikut tersalin.
- [ ] Daftar jadwal punya filter **Mendatang** (default) / **Lewat** / **Semua**, filter program, filter status, dan diurutkan berdasarkan `start_date`.
- [ ] Kolom daftar: program, tanggal, metode, lokasi, harga efektif, terisi/kuota, status publik.

### US-03 (F1) — Admin menandai batch penuh, ditutup, atau batal
- [ ] Status bisa diubah dari form dan dari aksi cepat di tabel: `dibuka`, `penuh`, `ditutup`, `batal`.
- [ ] Batch `penuh`/`ditutup` tetap tampil di publik dengan badge statusnya, tetapi tombol daftar nonaktif.
- [ ] Batch `batal` hilang dari semua halaman publik. Pendaftarnya tetap tersimpan di admin.
- [ ] Mengubah status tidak mengubah atau menghapus data pendaftar.

### US-04 (F1) — Admin melihat dan memproses pendaftar
- [ ] Menu **Kotak Masuk → Pendaftar** menampilkan badge jumlah pendaftar berstatus `baru`.
- [ ] Tabel: tanggal daftar, nama, organisasi, program + tanggal batch, jumlah peserta, status. Bisa dicari (nama, email, organisasi) dan difilter (status, program, batch).
- [ ] Halaman detail menampilkan semua field, tombol **WhatsApp** (`wa.me/{phone}`), dan tombol **Email** (`mailto:`).
- [ ] Admin bisa mengubah status ke `dikonfirmasi` atau `batal` serta mengisi `note` internal. `note` tidak pernah tampil di publik.
- [ ] Pendaftar `batal` tidak lagi dihitung dalam kuota (lihat §8.2).

### US-05 (F2) — Admin mengekspor daftar peserta
- [ ] Dari jadwal atau tabel pendaftar (dengan filter batch), aksi **Ekspor** mengunduh CSV/XLSX berisi kolom pendaftar + program + tanggal batch.
- [ ] Ekspor hanya memuat baris sesuai filter aktif. Nama file: `peserta-{slug-program}-{YYYY-MM-DD}.xlsx`.

### US-06 (F1) — Pengunjung menjelajah jadwal dengan filter
- [ ] `/jadwal-pelatihan` menampilkan batch **mendatang** (§8.4) dari program yang tayang, urut tanggal mulai.
- [ ] Filter (GET, bisa di-bookmark): `?bulan=YYYY-MM`, `?kategori={slug}`, `?metode=offline|online|hybrid`. Filter bisa digabung, dan opsi bulan hanya berisi bulan yang punya batch.
- [ ] Setiap baris/kartu: judul program (tautan ke detail), tanggal (mis. "12–13 November 2026"), jam, metode, lokasi, harga (§8.5), status publik, tombol **Daftar**.
- [ ] Bila tidak ada hasil, tampil pesan "Belum ada jadwal untuk filter ini" + tautan WhatsApp untuk menanyakan jadwal atau in-house.
- [ ] Layout nyaman dibaca di lebar 360 px.

### US-07 (F1) — Pengunjung membuka program dan mendaftar ke sebuah batch
- [ ] `/pelatihan/{slug}` menampilkan judul, ringkasan, highlights, deskripsi, durasi, harga default, brosur (bila ada), daftar batch mendatang, dan form pendaftaran.
- [ ] Form: pilihan batch (hanya batch yang `isOpen()`), nama*, email*, telepon/WA*, organisasi, jabatan, jumlah peserta* (default 1), pesan. Tanda * = wajib (asumsi, Q4).
- [ ] Tombol **Daftar** di `/jadwal-pelatihan` membuka halaman detail dengan batch tersebut sudah terpilih (`?jadwal={id}#daftar`).
- [ ] Bila program tidak punya batch terbuka, form diganti CTA "Tanyakan jadwal berikutnya / in-house" (WhatsApp + tautan kontak).
- [ ] Submit ke `POST /pelatihan/{slug}/daftar`. Validasi server dan aturan §8 dicek ulang saat submit. Bila gagal, form kembali dengan input lama dan pesan galat yang jelas.

### US-08 (F1) — Pengunjung mendapat konfirmasi + tautan WhatsApp
- [ ] Setelah sukses, halaman menampilkan pesan "Pendaftaran diterima" dengan ringkasan (program, tanggal batch, nama, jumlah peserta) dan penjelasan bahwa tim INOVASS akan menghubungi.
- [ ] Tombol **Lanjut via WhatsApp** membuka `https://wa.me/{settings.whatsapp}?text=` dengan pesan terisi, misalnya: "Halo INOVASS, saya {nama} ({organisasi}) baru mendaftar {program} batch {tanggal}, {n} peserta. No. pendaftaran #{id}."
- [ ] Refresh halaman sukses tidak membuat pendaftaran ganda (pola redirect-after-POST).

### US-09 (F1 badge, F2 email) — Admin mendapat notifikasi pendaftaran baru
- [ ] **F1:** badge nav Pendaftar + widget dashboard "Pendaftar terbaru". Tidak ada email.
- [ ] **F2:** email ke alamat di Pengaturan Situs (bisa lebih dari satu, Q3) berisi ringkasan + tautan ke record di admin. Email balasan otomatis ke pendaftar berisi ringkasan + kontak WhatsApp.
- [ ] **F2:** kegagalan SMTP tidak boleh menggagalkan penyimpanan pendaftaran. Error dicatat di log.

---

## 5. Content Model

Sumber kebenaran: `database/migrations/2026_10_18_000001_create_training_tables.php` dan `app/Models/{TrainingCategory,Training,TrainingSchedule,Registration}.php`. Semua tabel punya `id`, `created_at`, dan `updated_at`.

### 5.1 `training_categories` — Kategori Pelatihan

| Field | Tipe | Wajib | Catatan |
|---|---|:-:|---|
| `name` | string | ✓ | "Pelatihan Sertifikasi ISO" |
| `slug` | string, unik | ✓ | dipakai di filter `?kategori=` |
| `description` | text | – | intro kategori di `/pelatihan` |
| `sort` | uint, default 0 | ✓ | urutan tampil |
| `is_published` | bool, default true | ✓ | |

Relasi: punya banyak `trainings`. Kategori yang masih punya program **tidak bisa dihapus** (`restrictOnDelete`).

### 5.2 `trainings` — Program Pelatihan

| Field | Tipe | Wajib | Catatan |
|---|---|:-:|---|
| `training_category_id` | FK | ✓ | |
| `title` | string | ✓ | "Pelatihan ISO 9001:2015" |
| `slug` | string, unik | ✓ | URL `/pelatihan/{slug}` |
| `summary` | text | – | 1–2 kalimat untuk kartu & meta fallback |
| `highlights` | JSON array of string | – | poin singkat (situs lama: 3) |
| `description` | longText (rich text) | – | isi utama: tujuan, materi, peserta |
| `duration` | string | – | teks bebas, mis. "2 hari (16 jam)" |
| `price` | uint (rupiah) | – | harga default; bisa ditimpa per batch |
| `image` | string (path) | – | gambar kartu/hero |
| `brochure` | string (path PDF) | – | tombol "Unduh Brosur" |
| `sort` | uint, default 0 | ✓ | urutan dalam kategori |
| `is_published` | bool, default true | ✓ | `false` = 404 + batch disembunyikan |
| `meta_description` | string | – | fallback ke `summary` |

Relasi: `category()`, `schedules()`, `upcomingSchedules()`. Menghapus program **ikut menghapus semua batch dan pendaftarnya** (cascade, lihat §8.7).

### 5.3 `training_schedules` — Jadwal / Batch

| Field | Tipe | Wajib | Catatan |
|---|---|:-:|---|
| `training_id` | FK | ✓ | |
| `start_date` | date (indexed) | ✓ | |
| `end_date` | date | – | kosong = 1 hari |
| `time` | string | – | "08.30 – 16.30 WIB" |
| `method` | string, default `offline` | ✓ | `offline` (Tatap muka) / `online` / `hybrid` |
| `location` | string | – | kota/venue, atau "Zoom Meeting" |
| `price` | uint (rupiah) | – | kosong = pakai `trainings.price` |
| `quota` | uint | – | kosong = tanpa batas |
| `registration_deadline` | date | – | kosong = `start_date` |
| `status` | string, default `dibuka` | ✓ | `dibuka` / `penuh` / `ditutup` / `batal` |
| `note` | text | – | catatan tampil di publik, mis. "Termasuk makan siang" (asumsi) |

Method model: `effectivePrice()`, `seatsTaken()`, `seatsLeft()`, `isOpen()`, `publicStatus()`, `dateLabel()`, `methodLabel()`, scope `upcoming()` dan `visible()`. Aturannya ada di §8.

### 5.4 `registrations` — Pendaftar

| Field | Tipe | Wajib | Catatan |
|---|---|:-:|---|
| `training_schedule_id` | FK | ✓ | batch yang dipilih |
| `name` | string | ✓ | |
| `email` | string | ✓ | format email valid |
| `phone` | string | ✓ | nomor WA; disimpan dinormalisasi `62…` (asumsi) |
| `organization` | string | – | perusahaan/instansi |
| `position` | string | – | jabatan |
| `participants` | uint, default 1 | ✓ | 1–50 (asumsi) |
| `message` | text | – | pertanyaan pendaftar |
| `status` | string, default `baru` | ✓ | `baru` / `dikonfirmasi` / `batal` |
| `note` | text | – | **internal admin**, tidak pernah tampil di publik |

Hanya field di `$fillable` yang bisa diisi. Field `status` dan `note` tidak boleh diterima dari form publik: controller wajib memakai `validated()` + whitelist, bukan `$request->all()`.

### 5.5 Data awal (seed)

| Kategori | Jumlah program | Sumber |
|---|--:|---|
| Pelatihan Sertifikasi ISO | 18 | halaman Public Training situs lama |
| Pelatihan Akreditasi | 11 | halaman Public Training Akreditasi |
| Pranata Laboratorium | 98 | 4 halaman induk pranata lab (MIPA, Sosial, Kedokteran, Kesehatan) |
| **Total** | **127** | `TrainingSeeder` dari `database/seeders/data/layanan.json` |

- Judul dinormalisasi: "Public Training ISO 9001" menjadi "Pelatihan ISO 9001"; slug `public-training-*` menjadi `pelatihan-*`. `duration` dan `price` kosong, admin melengkapinya.
- Seeder idempoten (`updateOrCreate` per slug), jadi aman dijalankan ulang.
- **Jadwal & pendaftar contoh** (6 batch, 2 pendaftar) hanya dibuat bila `APP_ENV ≠ production` dan tabel jadwal masih kosong. Production dimulai tanpa jadwal.

---

## 6. Fitur Admin CMS (Filament v5, `/admin`)

### 6.1 Navigasi sidebar

| Grup | Menu | Isi |
|---|---|---|
| — | **Dashboard** | §6.2 |
| **Pelatihan** | Program Pelatihan | CRUD program + relation manager **Jadwal** (inline) |
| | Jadwal Pelatihan | Semua batch lintas program; filter Mendatang/Lewat/Semua, program, status, metode; aksi **Duplikat** dan ubah status |
| | Kategori Pelatihan | CRUD kategori, urutan |
| **Kotak Masuk** | Pendaftar | Badge jumlah `baru`; alur status; tombol WA/email |
| | Pesan Masuk | Pesan dari form kontak (sudah ada) |
| **Konten Website** *(collapsed default)* | Beranda, Tentang, Produk, Kontak | Editor halaman compro yang sudah ada |
| | Layanan, Klien, Testimoni, FAQ, Berita | Resource compro yang sudah ada |
| **Pengaturan** | Pengaturan Situs | Nama, kontak, **nomor WhatsApp** (dipakai tautan pendaftaran), email, sosial |

### 6.2 Dashboard

| Widget | Isi |
|---|---|
| Statistik (4 kartu) | **Jadwal mendatang** (batch `upcoming()`), **Pendaftar baru** (`status = baru`), **Program aktif** (`is_published`), **Pesan baru** (kontak belum dibaca) |
| Jadwal terdekat | Tabel 5–10 batch mendatang: program, tanggal, metode, terisi/kuota, status publik; klik untuk edit |
| Pendaftar terbaru | Tabel 5–10 pendaftaran terakhir: waktu, nama, program/batch, status; klik untuk detail |

### 6.3 Detail perilaku

- **Form program:** dua kolom; rich text untuk `description`; repeater sederhana (string) untuk `highlights`; upload gambar/PDF ke disk `public`.
- **Relation manager Jadwal:** kolom tanggal, metode, lokasi, harga efektif, terisi/kuota, status publik; bisa create/edit/duplikat langsung tanpa meninggalkan halaman program.
- **Harga** tampil sebagai `Rp 3.500.000`. Input berupa angka tanpa titik, dengan prefix "Rp".
- **Hapus:** batch yang punya pendaftar hanya bisa dihapus setelah konfirmasi yang menyebut jumlah pendaftar yang ikut terhapus. Program yang punya batch disarankan dinonaktifkan (`is_published = false`), bukan dihapus. Lihat §8.7.
- **Bahasa admin:** Indonesia (`APP_LOCALE=id`).

---

## 7. Fitur Website Publik & URL

### 7.1 URL baru (Fase 1)

| Method | URL | Nama route | Isi |
|---|---|---|---|
| GET | `/jadwal-pelatihan` | `jadwal.index` | Semua batch mendatang + filter `bulan`, `kategori`, `metode` |
| GET | `/pelatihan` | `pelatihan.index` | Katalog per kategori (kartu program; jumlah batch mendatang per program) |
| GET | `/pelatihan/{slug}` | `pelatihan.show` | Detail program + batch mendatang + form daftar (`#daftar`) |
| POST | `/pelatihan/{slug}/daftar` | `pelatihan.daftar` | Simpan pendaftaran; `throttle`, honeypot, CSRF |

### 7.2 Perubahan di halaman compro

- Item nav utama **"Jadwal Pelatihan"** → `/jadwal-pelatihan`, ada di desktop dan menu mobile.
- Section beranda **"Jadwal Pelatihan Terdekat"**: 3–6 batch `visible()` terdekat + tombol "Lihat semua jadwal". Bila tidak ada batch, section disembunyikan.
- Selain itu tidak ada perubahan. `/`, `/tentang.html`, `/produk.html`, `/kontak.html`, `/layanan/{kategori}/…`, dan `/berita` tetap seperti sekarang; `/index.html` → 301 `/`.

### 7.3 Hubungan dengan halaman pelatihan lama

Halaman pelatihan lama di `/layanan/pelatihan-*/…html` tetap hidup (Fase 1), sehingga sementara ada dua halaman untuk program yang sama. Fase 1 menambah CTA "Lihat jadwal & daftar" di halaman lama yang mengarah ke `/pelatihan/{slug}` bila programnya bisa dipetakan (asumsi). Fase 2 memutuskan antara `rel=canonical` ke halaman baru atau 301 (Q8).

### 7.4 Tampilan

- Memakai layout Blade compro yang sama (header, footer, warna, font).
- Status publik ditampilkan sebagai badge: Dibuka (hijau), Penuh (abu), Pendaftaran ditutup (abu), Ditutup (abu). Batch Batal tidak tampil.
- Bila `quota` diisi dan sisa kursi ≤ 5, tampil keterangan "Sisa {n} kursi" (asumsi; bisa dimatikan bila INOVASS tidak ingin menampilkan angka).
- Tanggal ditulis dalam bahasa Indonesia (`dateLabel()`): "12–13 November 2026", "30 Okt – 1 Nov 2026".

---

## 8. Aturan Bisnis

Aturan ini **diimplementasikan di model** (`TrainingSchedule`) dan dipakai bersama oleh admin, halaman publik, dan controller pendaftaran. Jangan menduplikasi logikanya di view.

### 8.1 Status batch

| Status tersimpan (`status`) | Diatur oleh | Tampil di publik? | Bisa daftar? |
|---|---|:-:|:-:|
| `dibuka` | admin (default) | ✓ | ya, bila lolos §8.2–8.3 |
| `penuh` | admin | ✓ badge "Penuh" | ✗ |
| `ditutup` | admin | ✓ badge "Ditutup" | ✗ |
| `batal` | admin | ✗ | ✗ |

**Status publik turunan** (`publicStatus()`) untuk batch `dibuka`:
- sisa kursi = 0 → **"Penuh"**
- `isOpen()` = true → **"Dibuka"**
- selain itu (batas daftar lewat) → **"Pendaftaran ditutup"**

Sistem **tidak pernah mengubah `status` tersimpan secara otomatis**. Status "Penuh"/"Pendaftaran ditutup" dihitung saat dibaca, jadi tidak perlu cron.

### 8.2 Kuota

- `seatsTaken()` = jumlah `participants` dari pendaftar dengan status ≠ `batal` (`baru` dan `dikonfirmasi` dihitung).
- `seatsLeft()` = `null` bila `quota` kosong (tanpa batas), selain itu `max(0, quota − seatsTaken())`.
- Saat submit: tolak bila `participants > seatsLeft()` dengan pesan "Sisa kursi tinggal {n}".
- Membatalkan pendaftar (`→ batal`) otomatis mengembalikan kursinya.
- Batas Fase 1: dua submit yang benar-benar bersamaan bisa melampaui kuota 1–2 kursi. Ini diterima karena admin mengonfirmasi manual. Fase 2 bisa memakai `lockForUpdate` bila dibutuhkan.

### 8.3 Batas pendaftaran

- `isOpen()` = `status = dibuka` **dan** hari ini ≤ (`registration_deadline` ?? `start_date`) **dan** (kuota tanpa batas **atau** `seatsLeft() > 0`).
- Batas berlaku inklusif sampai akhir hari tersebut.
- **Wajib:** zona waktu aplikasi `Asia/Jakarta`. Saat ini `config/app.php` masih `'timezone' => 'UTC'`, sehingga `today()` tertinggal hingga 7 jam: pendaftaran tetap terbuka sampai pukul 07.00 WIB keesokan harinya, dan batch dianggap "mendatang" 7 jam lebih lama. Ubah ke `'Asia/Jakarta'` sebelum go-live.

### 8.4 Jadwal yang sudah lewat

- `upcoming()` = `status ≠ batal` **dan** `COALESCE(end_date, start_date) ≥ hari ini`, urut `start_date`. Batch yang sedang berlangsung masih tampil (tetapi biasanya sudah tidak bisa didaftari karena lewat batas).
- `visible()` = `upcoming()` + program `is_published = true`. Hanya scope ini yang dipakai di publik. Kategori yang `is_published = false` juga disembunyikan dari katalog dan filter (asumsi; tambahkan kondisi kategori di `visible()`).
- Batch lewat tidak dihapus. Batch itu tetap ada di admin (filter "Lewat") bersama pendaftarnya sebagai arsip.

### 8.5 Harga

- `effectivePrice()` = `schedule.price` ?? `training.price`.
- Bila keduanya kosong, tampil **"Hubungi kami"** (dengan tautan WhatsApp), bukan "Rp 0".
- `price = 0` berarti **"Gratis"**.
- Bila INOVASS memutuskan harga tidak ditampilkan di publik (Q1), satu pengaturan global menyembunyikan semua harga dan menampilkan "Hubungi kami". Pengaturan ini hanya dibuat bila Q1 dijawab "tidak tampil".

### 8.6 Validasi pendaftaran (server)

| Aturan | Nilai |
|---|---|
| `training_schedule_id` | wajib; harus milik program `{slug}` di URL; harus `visible()` dan `isOpen()` saat submit |
| `name` | wajib, ≤ 120 |
| `email` | wajib, `email:rfc`, ≤ 160 |
| `phone` | wajib, 8–20 digit setelah membuang spasi/`-`/`+`; awalan `0` dinormalisasi ke `62` |
| `organization`, `position` | opsional, ≤ 160 |
| `participants` | wajib, integer 1–50, ≤ `seatsLeft()` bila berkuota |
| `message` | opsional, ≤ 2000 |
| honeypot | field tersembunyi harus kosong; bila terisi, respons "sukses" palsu tanpa menyimpan |
| throttle | 5 submit / menit / IP (sama dengan form kontak) |

### 8.7 Integritas data

- Hapus kategori yang masih punya program → ditolak (FK `restrict`).
- Hapus program → batch & pendaftar ikut terhapus (FK `cascade`). Admin disarankan menonaktifkan, bukan menghapus.
- Hapus batch → pendaftarnya ikut terhapus (FK `cascade`). Untuk batch yang dibatalkan, pakai status `batal`, jangan dihapus.
- Ubah slug program → URL lama program itu menjadi 404. Fase 1 menampilkan peringatan di field slug untuk program yang sudah tayang (asumsi).

---

## 9. Arsitektur & Hosting (cPanel)

### 9.1 Stack

| Lapisan | Pilihan |
|---|---|
| Aplikasi | Laravel 13 monolit (SSR Blade), satu repo untuk compro + pelatihan + admin |
| Admin | Filament v5 di `/admin` |
| Database | MySQL 8 / MariaDB ≥ 10.6 di cPanel; SQLite untuk lokal |
| Aset | Vite, di-build **di mesin lokal/CI** lalu `public/build` di-upload; server tidak butuh Node |
| Session / cache | `database` (tabel sudah ada di migrasi) |
| Queue | `sync` di production Fase 1 (tidak ada job antrean) |

### 9.2 Kebutuhan server

- **PHP ≥ 8.3** (pilih di cPanel → *MultiPHP Manager* / *Select PHP Version*).
- Ekstensi: `bcmath`, `ctype`, `curl`, `dom`, `fileinfo`, `filter`, `intl` (wajib untuk Filament), `mbstring`, `openssl`, `pdo_mysql`, `session`, `tokenizer`, `xml`, `zip` (untuk ekspor di Fase 2), `gd` (thumbnail).
- `memory_limit ≥ 256M`, `upload_max_filesize` dan `post_max_size ≥ 12M` (brosur 10 MB).
- Fungsi `symlink` aktif (untuk `storage:link`). Bila dinonaktifkan hosting, gunakan disk `public` yang mengarah langsung ke `public/storage` (lihat 9.4).

### 9.3 Struktur folder & document root

```
/home/{user}/inovass/          ← seluruh aplikasi (di LUAR public_html)
/home/{user}/inovass/public    ← document root domain
```

- **Disarankan:** cPanel → *Domains* → ubah *Document Root* `inovass.com` ke `inovass/public`.
- **Bila document root domain utama tidak bisa diubah:** salin isi `inovass/public/` ke `public_html/`, lalu ubah dua path di `public_html/index.php` (`__DIR__.'/../inovass/vendor/autoload.php'` dan `__DIR__.'/../inovass/bootstrap/app.php'`). Folder `.env`, `vendor`, dan `storage` tidak boleh berada di dalam `public_html`.

### 9.4 Deploy tanpa SSH

1. Di lokal: `composer install --no-dev --optimize-autoloader` dan `npm ci && npm run build`.
2. Zip proyek **tanpa** `.env`, `node_modules`, `storage/logs/*`, `database/*.sqlite`, `tests`.
3. cPanel → *File Manager*: upload ke `/home/{user}/inovass`, extract. Pada update, timpa file, tetapi jangan timpa `.env` dan `storage/app/public`.
4. cPanel → *MySQL Databases*: buat DB + user, beri *All Privileges*.
5. Buat `.env` di File Manager (lihat 9.6).
6. Jalankan perintah artisan sekali jalan. Pilih salah satu: (a) cPanel → *Terminal* bila tersedia (tidak selalu butuh paket SSH), atau (b) cPanel → *Cron Jobs*, tambah job tiap menit:
   `cd ~/inovass; php artisan migrate --force; php artisan db:seed --force; php artisan storage:link; php artisan optimize >> storage/logs/deploy.log 2>&1`
   lalu **hapus cron itu** setelah `deploy.log` menunjukkan sukses. Bila `php` di cron bukan versi 8.3, pakai path lengkap, mis. `/opt/cpanel/ea-php83/root/usr/bin/php`.
7. `db:seed` hanya pada deploy pertama. Seeder idempoten, tetapi admin default dibuat dari `ADMIN_PASSWORD`.
8. Fallback tanpa cron/terminal: import dump SQL hasil `php artisan migrate --seed` lokal (MySQL) lewat *phpMyAdmin*.

### 9.5 Deploy dengan SSH

```bash
cd ~/inovass
git pull origin main                      # atau rsync dari CI
composer install --no-dev --optimize-autoloader
php artisan down
php artisan migrate --force
php artisan storage:link                  # sekali
php artisan optimize && php artisan filament:optimize
php artisan up
```

`public/build` di-upload terpisah (rsync/scp) karena tidak di-build di server.

### 9.6 `.env` production (minimal)

```
APP_NAME=INOVASS
APP_ENV=production
APP_DEBUG=false
APP_KEY=base64:...            # php artisan key:generate --show (di lokal)
APP_URL=https://inovass.com
APP_LOCALE=id
DB_CONNECTION=mysql
DB_HOST=localhost
DB_DATABASE={user}_inovass
DB_USERNAME={user}_inovass
DB_PASSWORD=...
SESSION_DRIVER=database
CACHE_STORE=database
QUEUE_CONNECTION=sync
FILESYSTEM_DISK=public
ADMIN_PASSWORD=...            # kuat, ≥ 12 karakter; ganti setelah login pertama
MAIL_MAILER=smtp              # Fase 2; Fase 1 boleh tetap log
```

### 9.7 Cron

**Tidak dibutuhkan untuk Fase 1.** Status turunan dihitung saat dibaca, dan tidak ada job antrean atau scheduler. Fase 2 boleh menambah `* * * * * php artisan schedule:run` bila ada pengingat atau backup terjadwal.

### 9.8 Backup

- cPanel → *Backup* / JetBackup: harian (DB + home dir) bila tersedia di paket hosting.
- Tambahan manual mingguan: unduh dump DB (phpMyAdmin → Export) + folder `storage/app/public` (gambar & brosur), simpan di Google Drive INOVASS.
- Kode: repo Git = backup.
- Uji restore satu kali sebelum go-live.

---

## 10. Non-Functional Requirements

### 10.1 Keamanan

- CSRF di semua form (bawaan Laravel). Throttle 5/menit/IP + honeypot pada form pendaftaran dan kontak.
- Admin: tidak ada registrasi publik; password default seeder (`inovass123` bila `ADMIN_PASSWORD` kosong) **wajib diganti** sebelum go-live; throttle login bawaan Filament; `APP_DEBUG=false`.
- Mass assignment: form publik hanya mengisi field yang divalidasi; `status`/`note` tidak bisa disuntik.
- Output publik di-escape (`{{ }}`). Rich text `description` hanya diisi admin, tetapi tetap dirender dari editor Filament, bukan HTML bebas.
- Upload: whitelist MIME (jpg/png/webp/pdf), batas ukuran, nama file acak.
- Data pribadi pendaftar (UU PDP): hanya admin yang bisa melihat; tidak ada endpoint publik yang mengembalikan data pendaftar; Kebijakan Privasi menyebut tujuan pemakaian data (Q7).
- Fase 2: `canAccessPanel()` dibatasi berdasarkan peran dan domain email, bukan `true`.

### 10.2 Performa

- `/jadwal-pelatihan` dan `/pelatihan/{slug}` ≤ 10 query (eager load `training.category` dan agregat `registrations`; hindari `seatsLeft()` per baris tanpa `withSum`).
- TTFB ≤ 800 ms di shared hosting; halaman ≤ 1 MB; gambar program ≤ 200 KB (WebP disarankan).
- Tidak ada JS framework di publik; filter memakai form GET biasa.

### 10.3 SEO

- **Fase 1:** `<title>` unik ("{Program} — Jadwal & Pendaftaran | INOVASS"), `meta description` dari `meta_description` ?? `summary`, `canonical`, URL bersih, heading hierarkis. Halaman filter (`?bulan=` dsb.) memakai `canonical` ke `/jadwal-pelatihan`.
- **Fase 2:** `sitemap.xml` (halaman compro + `/pelatihan/*`), JSON-LD `Course` per program dengan `hasCourseInstance` per batch (atau `Event` dengan `startDate`, `location`, `offers.price`, `eventAttendanceMode`), dan `robots.txt` yang merujuk sitemap.

### 10.4 Aksesibilitas & lokal

Label form terlihat; pesan galat di dekat field; tombol bisa diakses keyboard; kontras AA. Bahasa `id`, zona waktu `Asia/Jakarta`, format rupiah `Rp 3.500.000`, tanggal Indonesia.

### 10.5 Kualitas kode (untuk Claude Code)

- Satu feature test per aturan §8: batch penuh/ditutup/batal/lewat-deadline ditolak; kuota dengan `participants > seatsLeft`; harga fallback; honeypot; throttle; batch milik program lain ditolak.
- Aturan bisnis hanya di model; controller tipis; tanpa package baru untuk hal yang bisa dibuat beberapa baris.
- `php artisan test` hijau sebelum setiap deploy.

---

## 11. Roadmap

| Fase | Isi | Estimasi | Status |
|---|---|--:|---|
| **Fase 1 — MVP** | Migrasi & model (§5), seeder katalog 127 program, admin Pelatihan + Kotak Masuk + dashboard, grup "Konten Website" collapsed, halaman `/jadwal-pelatihan`, `/pelatihan`, `/pelatihan/{slug}`, form daftar + WhatsApp, section beranda + nav, feature test §8, deploy cPanel | **≈ 2–3 person-week** | Sedang dibangun (model & seeder selesai) |
| **Fase 2** | Email notifikasi admin + auto-reply pendaftar (0,5 pw) · Ekspor CSV/XLSX peserta (0,5 pw) · `sitemap.xml` + `robots.txt` (0,25 pw) · JSON-LD `Course`/`Event` (0,25 pw) · Peran Admin/Editor + policy (1 pw) · Canonical/301 halaman pelatihan lama (0,25 pw) · Pengaturan tampil-harga bila perlu (0,25 pw) | **≈ 3 person-week** | Setelah Fase 1 dipakai ±1 bulan |
| **Fase 3 (opsional)** | Pembayaran online (Midtrans/Xendit: invoice, webhook, status bayar) **3–4 pw** · Sertifikat PDF otomatis + verifikasi QR **2 pw** · LMS/e-learning (materi, video, kuis, akun peserta) **8–12 pw**, atau integrasi LMS siap pakai **2–3 pw** | **≈ 5–18 person-week** | Butuh keputusan bisnis terpisah |

Kriteria selesai Fase 1: semua acceptance criteria US-01–04 dan US-06–09 (bagian F1) lolos; `php artisan test` hijau; zona waktu `Asia/Jakarta`; password admin diganti; uji restore backup; minimal 1 batch nyata diisi INOVASS.

---

## 12. Risiko & Mitigasi

| Risiko | Dampak | Mitigasi |
|---|---|---|
| Zona waktu masih UTC | Pendaftaran tetap terbuka hingga 7 jam setelah batas | Ubah `config/app.php` ke `Asia/Jakarta` + test deadline (§8.3) |
| Admin menghapus program/batch → pendaftar ikut terhapus | Data peserta hilang | Konfirmasi hapus yang menyebut jumlah pendaftar; anjurkan nonaktif/`batal`; backup harian |
| Duplikasi konten halaman pelatihan lama vs baru | SEO terpecah, pengunjung bingung | CTA dari halaman lama (F1), canonical/301 (F2, Q8) |
| Katalog 127 program tanpa harga & durasi | Halaman terlihat kurang informatif | Fallback "Hubungi kami"; INOVASS melengkapi bertahap mulai dari program yang punya jadwal |
| Shared hosting tanpa SSH/symlink/PHP 8.3 | Deploy macet | Cek prasyarat §9.2 sebelum mulai; jalur cron sekali jalan / phpMyAdmin (§9.4) |
| Spam pendaftaran | Kotak masuk kotor, kuota "terisi" palsu | Honeypot + throttle; admin bisa set `batal`; Fase 2 Turnstile bila spam > 5/minggu |
| Overbooking karena submit bersamaan | 1–2 kursi lebih | Konfirmasi manual admin; `lockForUpdate` di Fase 2 bila terjadi |
| Password admin default `inovass123` | Akses admin oleh pihak lain | `ADMIN_PASSWORD` wajib di `.env` production; ganti setelah login pertama |
| Scope creep kembali ke CMS compro | Jadwal molor | Konten Website dibekukan; permintaan baru masuk backlog Fase 2+ |

---

## 13. Pertanyaan Terbuka untuk INOVASS

| # | Pertanyaan | Dibutuhkan sebelum | Default bila belum dijawab |
|---|---|---|---|
| Q1 | Apakah harga pelatihan ditampilkan di website publik? | Go-live F1 | Tampil bila diisi; kosong → "Hubungi kami" |
| Q2 | In-house training: hanya by request (tanpa jadwal publik), atau juga dijadwalkan? | Go-live F1 | By request: CTA WhatsApp di setiap program, tanpa batch |
| Q3 | Siapa penerima notifikasi pendaftaran (email/WA, boleh lebih dari satu)? | Fase 2 | `inovass.adm@gmail.com` + WA `6281311173707` |
| Q4 | Field pendaftar wajib apa saja? Perlu NIK/NIP, alamat, data per peserta bila > 1 orang? | Go-live F1 | Nama, email, WA wajib; organisasi & jabatan opsional; satu kontak per pendaftaran |
| Q5 | Proses konfirmasi: kapan "dikonfirmasi" (setelah ditelepon? setelah bayar/transfer?) dan berapa lama SLA balasan? | Go-live F1 | Dikonfirmasi setelah dihubungi admin; teks sukses "dihubungi maks. 1×24 jam kerja" |
| Q6 | Tampilkan sisa kursi ("Sisa 3 kursi") atau cukup "Dibuka/Penuh"? | Go-live F1 | Tampil bila ≤ 5 |
| Q7 | Kebijakan Privasi untuk data pendaftar: siapa yang menulis? | Go-live F1 | Paragraf singkat di bawah form + halaman menyusul |
| Q8 | Halaman pelatihan lama `/layanan/pelatihan-*`: biarkan, canonical ke halaman baru, atau 301? | Fase 2 | Biarkan + CTA ke halaman baru |
| Q9 | Siapa admin (nama + email) dan apakah perlu Editor terpisah? | Go-live F1 | 1 admin: `admin@inovass.com` |
| Q10 | Hosting: paket cPanel saat ini sudah mendukung PHP 8.3, MySQL, Terminal/SSH, dan ubah document root? | Sebelum deploy | Developer cek dan laporkan |
| Q11 | Jenis pelatihan baru yang akan ditambah ("tambahan lain"): perlu field khusus (instruktur, sertifikat BNSP, SKP, JP)? | Fase 2 | Ditulis di `description`; field baru setelah ada 3+ program yang membutuhkannya |
| Q12 | Diskon (early bird, grup ≥ n peserta)? | Fase 2 | Ditulis manual di `note` batch |
