# Hierarki & Hak Akses Admin — INOVASS CMS

Panel admin: `/admin`. Dokumen ini memetakan **apa saja yang bisa dilakukan admin** saat ini (Fase 1) dan **usulan pembagian peran** untuk Fase 2.

> **Okt 2026:** admin dibatasi ke Pelatihan, Pendaftar, dan Pengaturan Situs. **Pesan Masuk** dan seluruh **Konten Website** tidak lagi didaftarkan di panel (lihat `AdminPanelProvider`). Kodenya masih ada di `app/Filament` bila suatu saat dibutuhkan lagi.

> Status saat ini: hanya ada **satu peran**. Setiap akun yang bisa login punya akses penuh ke semua menu di bawah. Akun admin baru ditambahkan di **Pengaturan → Akun Admin**.

---

## 1. Pohon menu & kemampuan (Fase 1, sudah berjalan)

```
Admin INOVASS
│
├── Dasbor
│   ├── Perlu tindakan: daftar tugas hari ini (pendaftar belum dihubungi > 24 jam, kursi hampir habis,
│   │                   batas daftar dekat, belum lunas menjelang pelatihan, jadwal/pendaftaran belum ditutup) → klik langsung ke halamannya
│   ├── Angka ringkas: perlu ditindaklanjuti, jadwal mendatang, peserta bulan ini, perkiraan pemasukan bulan ini
│   ├── Lihat jadwal terdekat (klik → edit jadwal)
│   └── Lihat pendaftaran terbaru (klik → detail pendaftaran)
│
├── Pendaftaran   (badge = jumlah yang masih perlu ditindaklanjuti: Baru, Dihubungi, Penawaran dikirim)
│   ├── Tab: Perlu ditindaklanjuti (bawaan) · per tahap · Semua; cari nama/kontak; filter jadwal
│   ├── Tahap: Baru → Dihubungi → Penawaran dikirim → Dikonfirmasi → Lunas → Selesai, atau Batal
│   │          (Batal = kursi kembali ke kuota; Dikonfirmasi & Batal mengirim email ke pendaftar)
│   ├── Tombol cepat per baris: → tahap berikutnya, WhatsApp (pesan berisi no. pendaftaran)
│   ├── Ubah tahap massal (centang beberapa) · Hapus massal
│   ├── Detail: data pendaftar, tahap, catatan internal, Riwayat (siapa, apa, kapan — otomatis, tidak bisa diedit)
│   ├── Tambah pendaftaran manual (mis. daftar lewat telepon)
│   └── Ekspor Excel (ikut tab & filter aktif)
│
├── PELATIHAN  ← inti CMS
│   ├── Jadwal Pelatihan
│   │   ├── Tambah jadwal (program, tanggal mulai/selesai, jam, batas daftar,
│   │   │                  metode offline/online/hybrid, lokasi, biaya, kuota, status, catatan)
│   │   ├── Ubah jadwal
│   │   ├── Duplikat jadwal (untuk batch berikutnya)
│   │   ├── Ubah status: Dibuka / Penuh / Ditutup / Batal
│   │   ├── Sembunyikan harga di website (tampil "Hubungi kami"; harga tetap tersimpan)
│   │   ├── Halaman ubah jadwal: daftar pendaftar jadwal ini (terisi X dari Y kursi), proses tahap, ekspor peserta (.xlsx)
│   │   ├── Hapus jadwal  ⚠ ikut menghapus pendaftarnya — lebih aman set status "Batal"
│   │   ├── Filter: akan datang / sudah lewat, kategori, metode, status
│   │   └── Lihat jumlah peserta terisi vs kuota
│   │
│   ├── Program Pelatihan
│   │   ├── Tambah program baru (nama, ringkasan, poin utama, deskripsi lengkap, kategori, durasi,
│   │   │                        harga default, gambar, silabus PDF/gambar; alamat halaman, SEO & urutan di panel "Lanjutan")
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
├── (tidak aktif) Pesan Masuk — form Kontak; kode ada, tidak didaftarkan di panel
│
├── (tidak aktif) KONTEN WEBSITE  (compro statis; kode ada, tidak didaftarkan di panel)
│   ├── Halaman: Beranda · Tentang Kami · Halaman Produk · Halaman Kontak  → ubah teks & gambar per section
│   ├── Kategori Layanan  → ubah, urutkan, tampil/sembunyi (tanpa hapus)
│   ├── Layanan (521 halaman layanan lama) → tambah, ubah, tampil/sembunyi, hapus, filter kategori/level/induk
│   ├── Produk · Klien · Testimoni · FAQ  → tambah, ubah, urutkan, tampil/sembunyi, hapus
│   └── Berita  → tulis, jadwalkan tanggal terbit, kategori, tampil/sembunyi, hapus
│
└── PENGATURAN
    ├── Pengaturan Situs → tampilkan/sembunyikan harga pelatihan, nama, tagline, logo, telepon, nomor WhatsApp (dipakai tombol WA),
    │                      email, alamat, media sosial, teks copyright
    └── Akun Admin → tambah / ubah / hapus akun (semua akun = penerima email pendaftaran)
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
| Pendaftar: lihat, pindah tahap, catatan, WhatsApp | ✅ | ✅ | ✅ |
| Pendaftar: tambah manual | ✅ | ✅ | ✅ |
| Pendaftar: hapus | ✅ | ❌ | ❌ |
| Export peserta (Fase 2) | ✅ | ✅ | ✅ |
| Pesan masuk: baca & proses | ✅ | ✅ | ✅ |
| Konten Website (compro) | ✅ | ✅ | ❌ |
| Pengaturan Situs | ✅ | ❌ | ❌ |
| Kelola akun admin (tambah, reset password, nonaktifkan) | ✅ | ❌ | ❌ |

Catatan implementasi: kolom `role` di tabel `users` + Laravel Policy per resource + menu "Pengguna" khusus Super Admin. Tanpa paket tambahan.
