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
docker-compose.yml               # stack Portainer: web + Cloudflare Tunnel
.github/workflows/deploy.yml     # CI/CD: build -> push ke GHCR -> redeploy Portainer
```

Konvensi:
- Semua link memakai **path relatif** (mis. dari `layanan/<kategori>/`: `../../assets/css/style.css`, `../../index.html`), jadi situs bisa dibuka lewat VS Code Live Preview, double-click file, maupun server production.
- Halaman detail baru: taruh di folder kategori yang sesuai, salin halaman sejenis sebagai template.
- Perbaikan tampilan mobile ada di blok `RESPONSIVE FIXES` di akhir `assets/css/style.css`.

## Alur update (sehari-hari)

1. Edit file di `public/`
2. `git add . && git commit -m "update ..." && git push`
3. GitHub Actions membangun image `ghcr.io/afidzulinn/web-inovass:latest`, lalu memanggil webhook Portainer, dan Portainer menarik image baru & me-restart container. Selesai dalam ±1–2 menit.

Cek lokal sebelum push: buka `public/index.html` dengan Live Preview / double-click, atau:

```bash
cd public && python -m http.server 8080
# atau persis seperti production:
docker build -t inovass-web . && docker run --rm -p 8080:80 inovass-web
# buka http://localhost:8080
```

## Setup awal (sekali saja)

### 1. GitHub
1. Buat repo di GitHub, lalu push project ini ke branch `main`.
2. Push pertama otomatis menjalankan Actions dan membuat package `web-inovass` di GHCR.
3. Buka **GitHub → profil → Packages → web-inovass → Package settings → Change visibility → Public**
   (agar server bisa `pull` tanpa login. Isinya hanya website publik.)
   *Kalau ingin tetap private:* di Portainer tambahkan **Registries → Custom registry** `ghcr.io` dengan username GitHub + Personal Access Token (scope `read:packages`).

> Jika username/nama repo GitHub berbeda dari `afidzulinn`, ganti nama image di `docker-compose.yml` dan `.github/workflows/deploy.yml` (harus huruf kecil).

### 2. Cloudflare (gratis) + domain
Syarat: domain `inovass.com` sudah terdaftar (dibeli) di registrar mana pun.

1. Cloudflare dashboard → **Add a domain** → `inovass.com` → pilih plan **Free**.
2. Ganti **nameserver** di registrar domain ke 2 nameserver yang diberikan Cloudflare. Tunggu aktif.
3. **Zero Trust → Networks → Tunnels → Create a tunnel** → tipe *Cloudflared* → beri nama `inovass` → salin **token** (string panjang setelah `--token`).
4. Tab **Public Hostname**, tambahkan:
   | Subdomain | Domain | Service |
   |---|---|---|
   | *(kosong)* | inovass.com | `HTTP` → `web:80` |
   | `www` | inovass.com | `HTTP` → `web:80` |

HTTPS otomatis dari Cloudflare, dan tidak perlu buka port 80/443 di VPS.

### 3. Portainer (server 129.226.157.124)
1. **Stacks → Add stack** → nama `inovass` → **Repository**
   - Repository URL: URL repo GitHub (aktifkan *Authentication* + PAT jika repo private)
   - Compose path: `docker-compose.yml`
2. **Environment variables**:
   - `CF_TUNNEL_TOKEN` = token dari langkah Cloudflare
   - `WEB_PORT` = `8080` (opsional; untuk tes langsung via `http://129.226.157.124:8080`)
3. Aktifkan **GitOps updates** → Mechanism **Webhook**, aktifkan **Re-pull image** dan **Force redeployment** → salin **Webhook URL**.
4. **Deploy the stack.**
5. Di GitHub repo → **Settings → Secrets and variables → Actions → New repository secret**:
   `PORTAINER_WEBHOOK_URL` = webhook URL dari langkah 3.

Pastikan port Portainer (default `9443`) bisa diakses dari internet supaya GitHub Actions bisa memanggil webhook.

## Rollback
Setiap build juga diberi tag commit SHA. Di Portainer, ganti image stack ke `ghcr.io/afidzulinn/web-inovass:<sha>` lalu redeploy, atau `git revert` lalu push.
