# INOVASS Website

Website statis (HTML/CSS/JS) untuk **inovass.com**, dikemas sebagai container Nginx.

## Gambaran cara kerja

```
 Laptop                GitHub (gratis)                         VPS 129.226.157.124
 ──────                ───────────────                         ───────────────────
 edit public/  ──push──▶  repo afidzulinn/web-inovass
                          │
                          ▼  GitHub Actions (.github/workflows/deploy.yml)
                          1. build image Docker (nginx + public/)
                          2. push ke ghcr.io/afidzulinn/web-inovass
                          3. SSH ke VPS ─────────────────────────▶  ~/apps/web-inovass/docker-compose.yml
                                                                     docker compose pull web && up -d
                                                                       ├─ inovass-web     (nginx, port 8080)
                                                                       └─ inovass-tunnel  (cloudflared)
                                                                               │
 Pengunjung ◀──── HTTPS ──── Cloudflare ◀──────── tunnel keluar ───────────────┘
                 (trycloudflare.com sementara, nanti inovass.com)
```

- **Tidak ada database atau backend**. Isinya hanya file HTML/CSS/JS/gambar.
- **Tidak perlu buka port 80/443 di VPS**. Cloudflare Tunnel yang membuat koneksi keluar ke Cloudflare, dan HTTPS diurus Cloudflare.
- **Deploy otomatis**: setiap push ke branch `main` situs ter-update sendiri dalam ±1–2 menit.

```
public/                          # semua isi website (= root domain)
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
deploy/nginx.conf                # konfigurasi Nginx di dalam container
Dockerfile                       # nginx:alpine + public/
docker-compose.yml               # dijalankan di VPS (~/apps/web-inovass): web + Cloudflare Tunnel
.github/workflows/deploy.yml     # CI/CD: build -> push ke GHCR -> SSH ke VPS -> docker compose up
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

## Alur update (sehari-hari)

1. Edit file di `public/`
2. `git add . && git commit -m "update ..." && git push`
3. GitHub Actions membangun image `ghcr.io/afidzulinn/web-inovass:latest`, lalu SSH ke VPS dan menjalankan `docker compose pull web && docker compose up -d` (hanya container website yang diganti; tunnel tidak disentuh). Selesai dalam ±1–2 menit. Status deploy: tab **Actions** di GitHub.

Cek lokal sebelum push: buka `public/index.html` dengan Live Preview / double-click, atau:

```bash
cd public && python -m http.server 8080
# atau persis seperti production:
docker build -t web-inovass . && docker run --rm -p 8080:80 web-inovass
# buka http://localhost:8080
```

## Setup awal (sekali saja)

Repo: https://github.com/afidzulinn/web-inovass (publik, jadi GitHub Actions gratis tanpa batas dan image GHCR bisa di-pull tanpa login).

### 1. Siapkan VPS (129.226.157.124)
Login SSH ke server, pastikan Docker sudah ada (`docker compose version`). Lalu buat SSH key khusus deploy:

```bash
ssh-keygen -t ed25519 -f ~/.ssh/github_deploy -N "" -C "github-actions"
cat ~/.ssh/github_deploy.pub >> ~/.ssh/authorized_keys
cat ~/.ssh/github_deploy        # salin SELURUH isinya (private key) untuk langkah 2
```

User yang dipakai (`ubuntu`) harus ada di grup `docker`. Cek dengan `id -nG`. File deploy disimpan di `~/apps/web-inovass`.

### 2. Secrets di GitHub
Repo → **Settings → Secrets and variables → Actions → New repository secret**:

| Name | Value |
|---|---|
| `SSH_HOST` | `129.226.157.124` |
| `SSH_USER` | `ubuntu` |
| `SSH_KEY`  | isi private key `~/.ssh/github_deploy` (termasuk baris `-----BEGIN/END-----`) |

Lalu **Actions → Build & Deploy → Run workflow** (atau push apa saja). Setelah hijau, cek di server:

```bash
docker ps                                   # inovass-web & inovass-tunnel harus "Up"
docker logs inovass-tunnel 2>&1 | grep trycloudflare.com
```

URL `https://xxxx.trycloudflare.com` dari log itu adalah alamat situs sementara (HTTPS, tanpa domain). Bisa juga dibuka langsung di `http://129.226.157.124:8080` (jika port 8080 diizinkan firewall).

> Quick Tunnel tidak perlu akun Cloudflare, tetapi URL-nya **berubah** setiap container `inovass-tunnel` di-restart. Cocok untuk sementara sebelum punya domain.

### 3. Nanti, setelah domain dibeli: pindah ke domain sendiri
Tidak ada perubahan kode, karena domain tidak ditulis di mana pun dalam situs.

1. Cloudflare dashboard → **Add a domain** → `inovass.com` → plan **Free**.
2. Di registrar tempat beli domain, ganti **nameserver** ke 2 nameserver dari Cloudflare. Tunggu status *Active*.
3. **Zero Trust → Networks → Tunnels → Create a tunnel** → *Cloudflared* → nama `inovass` → salin **token** (teks panjang setelah `--token`). Lewati langkah instalasi, karena container-nya sudah ada.
4. Tab **Public Hostname** → tambahkan dua baris:
   | Subdomain | Domain | Type | URL |
   |---|---|---|---|
   | *(kosong)* | inovass.com | HTTP | `web:80` |
   | `www` | inovass.com | HTTP | `web:80` |
5. Di server:
   ```bash
   cd ~/apps/web-inovass
   echo 'TUNNEL_ARGS=run --token <TOKEN-DARI-LANGKAH-3>' > .env
   docker compose up -d
   ```
6. Buka https://inovass.com. Di Zero Trust, status tunnel harus *Healthy*.

Ganti ke domain lain di kemudian hari: ulangi langkah 1–2 untuk domain baru, lalu tambahkan Public Hostname-nya di tunnel `inovass` yang sama (langkah 4). Token tidak berubah, jadi server tidak perlu disentuh. Setelah memakai domain, port 8080 boleh ditutup: hapus baris `ports` di `docker-compose.yml`.

## Memantau container (gratis)
- **Portainer CE** (opsional, belum terpasang): kalau ingin tampilan web untuk melihat status/log/restart container, pasang sekali dengan `docker run -d --name portainer --restart=always -p 127.0.0.1:9443:9443 -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:lts`, lalu akses lewat SSH tunnel: `ssh -L 9443:127.0.0.1:9443 ubuntu@129.226.157.124` → buka https://localhost:9443. Tidak dipakai untuk deploy.
- Tanpa Portainer: `docker ps`, `docker logs -f inovass-web`, `docker compose -f ~/apps/web-inovass/docker-compose.yml restart`.
- Notifikasi jika situs mati: Cloudflare (Zero Trust → tunnel status) atau Uptime Kuma (self-hosted, gratis).

## Rollback
Setiap build diberi tag commit SHA. Cara termudah: `git revert <commit>` lalu push. Cara cepat di server:
```bash
cd ~/apps/web-inovass && sed -i 's#web-inovass:latest#web-inovass:<sha>#' docker-compose.yml && docker compose up -d
```
(Deploy berikutnya dari GitHub akan mengembalikan ke `:latest`.)

## Tanya-jawab

**Kenapa GitHub, bukan GitLab?**
Keduanya gratis dan punya CI/CD. Tapi GitHub Actions tidak dibatasi untuk repo publik (repo private dapat 2.000 menit/bulan), sedangkan GitLab gratis hanya 400 menit/bulan dan akun baru biasanya diminta verifikasi kartu kredit. Satu kali deploy di sini makan ±1 menit.

**Apakah wajib pakai Portainer?**
Tidak. Deploy dilakukan GitHub Actions lewat SSH, langsung dengan `docker compose`. Portainer hanya opsional untuk *melihat* status/log container (lihat *Memantau container*).

**Kenapa sekarang alamatnya `xxxx.trycloudflare.com`?**
Domain `inovass.com` belum dibeli. Quick Tunnel Cloudflare memberi alamat HTTPS gratis tanpa domain. Kekurangannya, alamat ini berganti setiap container `inovass-tunnel` di-restart (misalnya VPS reboot). Deploy biasa tidak me-restart tunnel, hanya `inovass-web`. Untuk update `cloudflared` sesekali: `cd ~/apps/web-inovass && docker compose pull cloudflared && docker compose up -d`, lalu ambil URL baru dari log. Setelah domain dibeli, ikuti bagian *"Nanti, setelah domain dibeli"* di atas.

**Bisa ganti domain nanti?**
Bisa, tanpa mengubah kode. Domain hanya diatur di dashboard Cloudflare (Public Hostname tunnel). Nginx menerima domain apa pun (`server_name _`).

**Kenapa form kontak membuka WhatsApp?**
Website ini tidak punya backend/server email. Sebelumnya form hanya menampilkan "Pesan berhasil dikirim!" padahal pesan tidak terkirim ke mana pun. Sekarang tombol *Kirim Pesan* membuka WhatsApp INOVASS dengan pesan yang sudah terisi (nama, email, telepon, keperluan, pesan). Kalau nanti ingin masuk ke email, perlu layanan form (mis. Formspree) atau backend kecil.

**Apakah perubahan CSS langsung terlihat setelah deploy?**
Ya. Nginx menyuruh browser selalu mengecek ulang file CSS/JS (`Cache-Control: no-cache`). Gambar di-cache 7 hari, jadi kalau mengganti gambar, pakai **nama file baru**.

## Troubleshooting

| Gejala | Penyebab & solusi |
|---|---|
| Halaman tampil polos tanpa CSS saat dibuka lokal | Ada link yang diawali `/` (path absolut). Ganti jadi relatif (`../../assets/...`). Cek: `grep -rn 'href="/' public` |
| Actions merah di step **Deploy to VPS** | Secret `SSH_HOST`/`SSH_USER`/`SSH_KEY` salah, atau public key belum ada di `~/.ssh/authorized_keys` server. Lihat log step tersebut di tab Actions. |
| Step **Deploy to VPS** ter-*skip* | Secret `SSH_HOST` belum diisi. Build tetap jalan, tapi server tidak di-update. |
| Actions merah di step build | Biasanya `Dockerfile` atau `deploy/nginx.conf` rusak. Tes lokal: `docker build -t web-inovass .` |
| Alamat trycloudflare tidak bisa dibuka | `docker logs inovass-tunnel` → ambil URL terbaru (URL lama mati setelah restart). |
| `http://129.226.157.124:8080` tidak bisa dibuka | Port 8080 diblokir firewall VPS/provider. Tidak masalah kalau aksesnya lewat Cloudflare. |
| Menu hamburger / animasi tidak jalan di satu halaman | Buka DevTools (F12) → Console. Biasanya ada `Identifier '...' has already been declared` → hapus deklarasi ganda di `<script>` halaman itu (lihat *Aturan penting*). |

## Catatan perubahan (Oktober 2026)
- Struktur dirapikan: 560 file HTML di root dipindah ke `public/` dengan folder per kategori; CSS/JS/gambar ke `public/assets/`.
- Dihapus: skrip generator (`*.py`, `*.sh`), file laporan (`*.md`), template tak terpakai, dan 51 gambar yang tidak dipakai di halaman mana pun.
- Diperbaiki: 6 link rusak (termasuk 5 link `onclick` ke halaman yang tidak ada), error JavaScript di 548 halaman, form kontak palsu, dan tampilan mobile. Tab layanan, grid beranda, garis timeline, breadcrumb, dan grid 3/4 kolom sebelumnya meluber di HP.
- Hasil pengecekan otomatis: 555 halaman × 3 ukuran layar (375/768/1280px), tanpa scroll ke samping, tanpa error JavaScript, dan 18.299 link valid.
- Ditambahkan: Docker (nginx), deploy otomatis via GitHub Actions, dan Cloudflare Tunnel.
