# INOVASS Website

Website statis (HTML/CSS/JS) untuk **inovass.com**, dikemas sebagai container Nginx.

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
docker-compose.yml               # dijalankan di VPS (/opt/inovass): web + Cloudflare Tunnel
.github/workflows/deploy.yml     # CI/CD: build -> push ke GHCR -> SSH ke VPS -> docker compose up
```

Konvensi:
- Semua link memakai **path relatif** (mis. dari `layanan/<kategori>/`: `../../assets/css/style.css`, `../../index.html`), jadi situs bisa dibuka lewat VS Code Live Preview, double-click file, maupun server production.
- Halaman detail baru: taruh di folder kategori yang sesuai, salin halaman sejenis sebagai template.
- Perbaikan tampilan mobile ada di blok `RESPONSIVE FIXES` di akhir `assets/css/style.css`.

## Alur update (sehari-hari)

1. Edit file di `public/`
2. `git add . && git commit -m "update ..." && git push`
3. GitHub Actions membangun image `ghcr.io/afidzulinn/web-inovass:latest`, lalu SSH ke VPS dan menjalankan `docker compose pull && docker compose up -d`. Selesai dalam ±1–2 menit. Status deploy: tab **Actions** di GitHub.

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

User yang dipakai harus bisa menjalankan `docker` (root, atau user yang ada di grup `docker`).

### 2. Secrets di GitHub
Repo → **Settings → Secrets and variables → Actions → New repository secret**:

| Name | Value |
|---|---|
| `SSH_HOST` | `129.226.157.124` |
| `SSH_USER` | `root` (atau user lain di grup docker) |
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
   cd /opt/inovass
   echo 'TUNNEL_ARGS=run --token <TOKEN-DARI-LANGKAH-3>' > .env
   docker compose up -d
   ```
6. Buka https://inovass.com. Di Zero Trust, status tunnel harus *Healthy*.

Ganti ke domain lain di kemudian hari: ulangi langkah 1–2 untuk domain baru, lalu tambahkan Public Hostname-nya di tunnel `inovass` yang sama (langkah 4). Token tidak berubah, jadi server tidak perlu disentuh. Setelah memakai domain, port 8080 boleh ditutup: hapus baris `ports` di `docker-compose.yml`.

## Memantau container (gratis)
- **Portainer CE** (yang sudah terpasang): tetap bisa dipakai untuk melihat status, log, dan restart container `inovass-web` / `inovass-tunnel`. Tidak lagi dipakai untuk deploy.
- Tanpa Portainer: `docker ps`, `docker logs -f inovass-web`, `docker compose -f /opt/inovass/docker-compose.yml restart`.
- Notifikasi jika situs mati: Cloudflare (Zero Trust → tunnel status) atau Uptime Kuma (self-hosted, gratis).

## Rollback
Setiap build diberi tag commit SHA. Cara termudah: `git revert <commit>` lalu push. Cara cepat di server:
```bash
cd /opt/inovass && sed -i 's#web-inovass:latest#web-inovass:<sha>#' docker-compose.yml && docker compose up -d
```
(Deploy berikutnya dari GitHub akan mengembalikan ke `:latest`.)
