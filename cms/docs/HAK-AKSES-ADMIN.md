# Hierarki & Hak Akses Admin — INOVASS CMS

Panel admin: `/admin`. Dokumen ini memetakan **apa saja yang bisa dilakukan admin** saat ini (Fase 1) dan **usulan pembagian peran** untuk Fase 2.

> **Okt 2026:** admin dibatasi ke Pelatihan, Pendaftar, dan Pengaturan Situs. **Pesan Masuk** dan seluruh **Konten Website** tidak lagi didaftarkan di panel (lihat `AdminPanelProvider`). Kodenya masih ada di `app/Filament` bila suatu saat dibutuhkan lagi.

> Status saat ini: hanya ada **satu peran**. Setiap akun yang bisa login punya akses penuh ke semua menu di bawah. Menambah akun admin baru belum bisa dari panel (harus lewat developer).

---

## 1. Pohon menu & kemampuan (Fase 1, sudah berjalan)

```
Admin INOVASS
│
├── Dashboard
│   ├── Lihat ringkasan: jadwal mendatang (+ jumlah bulan ini), pendaftar baru, program aktif, pesan baru
│   ├── Lihat 6 jadwal terdekat (klik → edit jadwal)
│   └── Lihat 5 pendaftar terbaru (klik → proses pendaftar)
│
├── PELATIHAN  ← inti CMS
│   ├── Jadwal Pelatihan
│   │   ├── Tambah jadwal (program, tanggal mulai/selesai, jam, batas daftar,
│   │   │                  metode offline/online/hybrid, lokasi, biaya, kuota, status, catatan)
│   │   ├── Ubah jadwal
│   │   ├── Duplikat jadwal (untuk batch berikutnya)
│   │   ├── Ubah status: Dibuka / Penuh / Ditutup / Batal
│   │   ├── Sembunyikan harga di website (tampil "Hubungi kami"; harga tetap tersimpan)
│   │   ├── Hapus jadwal  ⚠ ikut menghapus pendaftarnya — lebih aman set status "Batal"
│   │   ├── Filter: akan datang / sudah lewat, kategori, metode, status
│   │   └── Lihat jumlah peserta terisi vs kuota
│   │
│   ├── Program Pelatihan
│   │   ├── Tambah program baru (nama, slug/URL, ringkasan, poin utama, deskripsi lengkap,
│   │   │                        kategori, durasi, harga default, gambar, brosur PDF, SEO)
│   │   ├── Ubah program
│   │   ├── Kelola jadwal langsung dari halaman program (tambah / ubah / duplikat / hapus)
│   │   ├── Tampilkan / sembunyikan dari website (toggle)
│   │   ├── Buat kategori baru langsung dari form program
│   │   ├── Lihat di website (tombol "Lihat")
│   │   ├── Hapus program (massal)  ⚠ ikut menghapus jadwal & pendaftarnya
│   │   └── Filter: kategori, ada/belum ada jadwal, status tampil · Cari nama
│   │
│   └── Kategori Pelatihan
│       ├── Tambah / ubah kategori
│       ├── Urutkan (drag & drop)
│       └── Tampilkan / sembunyikan (ikut menyembunyikan jadwalnya dari website)
│
├── KOTAK MASUK
│   ├── Pendaftar   (badge = jumlah pendaftar berstatus Baru)
│   │   ├── Lihat semua pendaftar (terbaru dulu), cari nama/kontak
│   │   ├── Proses: ubah status Baru → Dikonfirmasi / Batal (Batal = kursi kembali ke kuota)
│   │   ├── Tulis catatan internal
│   │   ├── Hubungi via WhatsApp (1 klik)
│   │   ├── Tambah pendaftar manual (mis. daftar lewat telepon)
│   │   ├── Hapus (massal)
│   │   └── Filter: status, jadwal
│   │
│   └── Pesan Masuk   (dari form Kontak; badge = pesan Baru)
│       ├── Baca pesan, ubah status Baru / Dihubungi / Selesai / Spam, catatan internal
│       ├── Filter status · Cari
│       └── Hapus (massal)   — tidak bisa membuat pesan baru dari admin
│
├── KONTEN WEBSITE  (compro; tertutup default, jarang diubah)
│   ├── Halaman: Beranda · Tentang Kami · Halaman Produk · Halaman Kontak  → ubah teks & gambar per section
│   ├── Kategori Layanan  → ubah, urutkan, tampil/sembunyi (tanpa hapus)
│   ├── Layanan (521 halaman layanan lama) → tambah, ubah, tampil/sembunyi, hapus, filter kategori/level/induk
│   ├── Produk · Klien · Testimoni · FAQ  → tambah, ubah, urutkan, tampil/sembunyi, hapus
│   └── Berita  → tulis, jadwalkan tanggal terbit, kategori, tampil/sembunyi, hapus
│
└── PENGATURAN
    └── Pengaturan Situs → nama, tagline, logo, telepon, nomor WhatsApp (dipakai tombol WA),
                           email, alamat, media sosial, teks copyright
```

---

## 2. Usulan hierarki peran (Fase 2, belum dibangun)

```
Super Admin  (IT / pemilik)
   └── Admin  (manajer pelatihan / marketing)
          └── Staf Pendaftaran  (CS / admin operasional)
```

| Kemampuan | Super Admin | Admin | Staf Pendaftaran |
|---|:-:|:-:|:-:|
| Lihat dashboard | ✅ | ✅ | ✅ |
| Jadwal: lihat | ✅ | ✅ | ✅ |
| Jadwal: tambah / ubah / duplikat / ubah status | ✅ | ✅ | ❌ |
| Jadwal: hapus | ✅ | ❌ (pakai status Batal) | ❌ |
| Program & kategori pelatihan: tambah / ubah | ✅ | ✅ | ❌ |
| Program & kategori: hapus | ✅ | ❌ | ❌ |
| Pendaftar: lihat, proses status, catatan, WhatsApp | ✅ | ✅ | ✅ |
| Pendaftar: tambah manual | ✅ | ✅ | ✅ |
| Pendaftar: hapus | ✅ | ❌ | ❌ |
| Export peserta (Fase 2) | ✅ | ✅ | ✅ |
| Pesan masuk: baca & proses | ✅ | ✅ | ✅ |
| Konten Website (compro) | ✅ | ✅ | ❌ |
| Pengaturan Situs | ✅ | ❌ | ❌ |
| Kelola akun admin (tambah, reset password, nonaktifkan) | ✅ | ❌ | ❌ |

Catatan implementasi: kolom `role` di tabel `users` + Laravel Policy per resource + menu "Pengguna" khusus Super Admin. Tanpa paket tambahan.
