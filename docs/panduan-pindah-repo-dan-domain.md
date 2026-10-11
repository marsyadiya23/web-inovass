# Panduan: repo baru → VPS → Cloudflare → domain

Tujuan akhir:

```
 git push (repo baru)
      │
      ▼
 GitHub Actions ── build image ──▶ ghcr.io/<pemilik>/<repo>
      │
      └── SSH ──▶ VPS 129.226.157.124  (~/apps/web-inovass)
                    ├─ inovass-web     : website (nginx)
                    └─ inovass-tunnel  : Cloudflare Tunnel ──▶ Cloudflare ──▶ https://inovass.com
```

- **Website jalan di VPS.** Cloudflare hanya menjadi pintu masuk: domain, HTTPS gratis, dan perlindungan. VPS tidak perlu membuka port 80/443.
- **Pindah repo tidak perlu mengedit file.** Nama image otomatis mengikuti nama repo (`ghcr.io/<pemilik>/<repo>`).
- **Ganti domain tidak perlu menyentuh server maupun kode.** Cukup diatur di dashboard Cloudflare.

Urutan kerja:
1. **Bagian 1**: pindah ke repo baru (sekali).
2. **Bagian 2**: sebelum punya domain, website diakses lewat alamat sementara.
3. **Bagian 3**: beli domain dan sambungkan ke VPS lewat Cloudflare.
4. **Bagian 4**: kapan pun ingin ganti domain.

---

## Bagian 1: Pindah ke repo baru

### 1.1 Siapkan repo baru (pilih salah satu)

**Cara A, Transfer repo yang sekarang** (riwayat commit ikut, link lama otomatis dialihkan):
1. Login akun lama → repo `web-inovass` → **Settings → General** → paling bawah **Transfer ownership**.
2. Isi username/organisasi tujuan → konfirmasi.
3. Login akun tujuan → buka email dari GitHub → **terima** transfernya.

**Cara B, Repo baru yang kosong** (nama repo boleh beda):
1. Login akun tujuan → **New repository** → beri nama → pilih **Public** → *jangan* centang README/.gitignore → **Create repository**.
2. Lanjut ke 1.2, yang sekaligus mengisi repo baru ini.

> **Public atau Private?** Disarankan **Public**: GitHub Actions gratis tanpa batas, dan server bisa mengambil image tanpa login. Kalau **Private**: Actions gratis 2.000 menit/bulan (cukup, karena satu deploy ±1 menit), tapi lakukan langkah 1.4.

### 1.2 Arahkan laptop ke repo baru
Di folder project (VS Code → Terminal):
```bash
git remote set-url origin https://github.com/<AKUN-BARU>/<NAMA-REPO>.git
git remote -v          # pastikan alamatnya sudah benar
git push -u origin main
```
Kalau diminta login, login sebagai akun baru.

### 1.3 Isi secrets di repo baru
Repo baru → **Settings → Secrets and variables → Actions → New repository secret** (kalau memakai Transfer, cek dulu apakah sudah ikut pindah):

| Name | Value |
|---|---|
| `SSH_HOST` | `129.226.157.124` |
| `SSH_USER` | `ubuntu` |
| `SSH_KEY` | private key deploy. Ambil di server dengan `cat ~/.ssh/github_deploy2`, salin **seluruhnya** termasuk baris `-----BEGIN…` dan `-----END…` |

Paste private key **langsung di GitHub**, jangan lewat chat atau email.

### 1.4 (Hanya jika repo Private) Izinkan server mengambil image
1. Akun pemilik repo → **Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token** → centang hanya `read:packages` → **Generate** → salin token.
2. Di server:
   ```bash
   echo '<TOKEN>' | docker login ghcr.io -u <AKUN-BARU> --password-stdin
   ```

### 1.5 Jalankan deploy dan cek
1. Repo baru → tab **Actions** → **Build & Deploy** → **Run workflow** (atau push perubahan apa saja).
2. Tunggu centang hijau. Step **Deploy to VPS** harus *success*, bukan *skipped*. Kalau *skipped*, berarti `SSH_HOST` belum diisi.
3. Cek di server:
   ```bash
   docker ps --format '{{.Names}}  {{.Image}}  {{.Status}}'
   ```
   `inovass-web` harus memakai `ghcr.io/<akun-baru>/<nama-repo>:latest` dengan status *Up (healthy)*.
4. *(Jika repo Public)* Pastikan image-nya juga Public: akun baru → **Packages** → package repo → **Package settings → Change visibility → Public**. Biasanya sudah otomatis mengikuti repo.

### 1.6 Hapus project Cloudflare Workers lama
Deploy tidak memakai Workers/wrangler (file `wrangler.jsonc` sudah dihapus dari repo). Project lama `web-inovass` di Cloudflare masih tersambung ke repo lama, jadi hapus saja:
dash.cloudflare.com → **Workers & Pages → web-inovass → Settings** → paling bawah **Delete** → konfirmasi.

### 1.7 Bersih-bersih akun lama (setelah semua hijau)
- Akun lama → **Packages → web-inovass → Package settings → Delete package**.
- Di server, hapus image lama:
  ```bash
  docker rmi ghcr.io/afidzulinn/web-inovass:latest
  docker image prune -f
  ```

**Checklist Bagian 1**
- [ ] Repo baru berisi kode, dan laptop sudah memakai `origin` yang baru
- [ ] Secret `SSH_HOST`, `SSH_USER`, `SSH_KEY` terisi
- [ ] Actions hijau dan **Deploy to VPS** *success*
- [ ] `docker ps` di server menunjukkan image dari repo baru
- [ ] Project Workers `web-inovass` lama dihapus di Cloudflare

---

## Bagian 2: Sebelum punya domain

Website sudah bisa dibuka tanpa domain:
- **HTTPS sementara (Cloudflare Quick Tunnel):** cek alamatnya di server:
  ```bash
  docker logs inovass-tunnel 2>&1 | grep trycloudflare.com
  ```
  Alamat `https://xxxx.trycloudflare.com` ini berganti kalau container tunnel di-restart (misalnya VPS reboot).
- **Langsung ke IP:** `http://129.226.157.124:8080`

---

## Bagian 3: Beli domain dan sambungkan ke VPS

### 3.1 Beli domain (pilih salah satu)
- **Langsung di Cloudflare (paling mudah):** dash.cloudflare.com → **Domain Registration → Register Domains** → cari `inovass.com` → **Purchase** (kartu kredit/PayPal, `.com` ±US$10/tahun). Domain otomatis aktif di Cloudflare, jadi **lewati 3.2**.
- **Di registrar lokal** (Niagahoster, Rumahweb, Domainesia, dll., bisa transfer bank/QRIS): beli domain, lalu lanjut ke 3.2.

> `.co.id` butuh dokumen perusahaan (akta/NIB). `.com` dan `.id` lebih mudah.

### 3.2 (Hanya jika beli di registrar lain) Pindahkan DNS ke Cloudflare
1. dash.cloudflare.com → **Add a domain** (*Onboard a domain*) → isi domain → plan **Free** → lanjut sampai muncul **2 nameserver Cloudflare** (contoh `xxx.ns.cloudflare.com`).
2. Login ke registrar → menu **Nameserver** → ganti nameserver bawaan dengan 2 nameserver Cloudflare → simpan.
3. Tunggu status domain di Cloudflare menjadi **Active**. Biasanya beberapa menit, paling lama 24 jam, dan ada email pemberitahuan.

### 3.3 Buat Cloudflare Tunnel untuk VPS
1. dash.cloudflare.com → **Zero Trust**. Kalau baru pertama kali, buat nama tim (bebas) dan pilih plan **Free**.
2. **Networks → Tunnels → Create a tunnel** → pilih **Cloudflared** → nama `inovass-vps` → **Save tunnel**.
3. Di halaman instalasi akan muncul perintah berisi `--token eyJ...`. **Salin hanya teks token-nya** (setelah `--token`). Perintah instalasinya **tidak perlu dijalankan**, karena container `cloudflared` sudah ada di server. Klik **Next**.

### 3.4 Arahkan domain ke website
Masih di tunnel `inovass-vps`, pada tab **Public Hostname** (di dashboard baru namanya *Published application routes*) → **Add**:

| Subdomain | Domain | Type | URL |
|---|---|---|---|
| *(kosongkan)* | `inovass.com` | `HTTP` | `web:80` |
| `www` | `inovass.com` | `HTTP` | `web:80` |

`web:80` adalah nama container website di dalam docker-compose, jadi tulis persis seperti itu. Cloudflare otomatis membuat record DNS-nya.

### 3.5 Pasang token di server
Login SSH ke server:
```bash
cd ~/apps/web-inovass
echo 'TUNNEL_ARGS=run --token <TOKEN-DARI-3.3>' > .env
docker compose up -d
docker logs inovass-tunnel 2>&1 | tail -5     # harus ada "Registered tunnel connection"
```
File `.env` hanya ada di server (tidak ada di GitHub) dan tidak ditimpa saat deploy.

### 3.6 Cek
- Buka **https://inovass.com** dan **https://www.inovass.com**. Harus tampil website dengan ikon gembok.
- Di Zero Trust → **Networks → Tunnels**, status `inovass-vps` harus **Healthy**.

### 3.7 (Opsional) Rapikan
- **Satu alamat resmi:** domain → **Rules → Redirect Rules → Create rule** → template **"Redirect from WWW to root"** → Deploy.
- **Tutup akses IP langsung:** hapus 2 baris `ports:` pada service `web` di `docker-compose.yml`, lalu push. Setelah itu website hanya bisa diakses lewat domain.
- **Email `info@inovass.com` gratis:** domain → **Email → Email Routing** → buat alamat `info@inovass.com` → teruskan ke `inovass.adm@gmail.com`. Setelah berjalan, ganti teks email di website.

**Checklist Bagian 3**
- [ ] Domain berstatus **Active** di Cloudflare
- [ ] Tunnel `inovass-vps` dibuat, dengan Public Hostname `inovass.com` dan `www` → `web:80`
- [ ] `.env` berisi token di `~/apps/web-inovass`, lalu `docker compose up -d`
- [ ] https://inovass.com terbuka, dan tunnel **Healthy**

---

## Bagian 4: Ganti domain di kemudian hari

Server dan kode **tidak perlu diubah**, karena token tunnel tetap sama.
1. Tambahkan domain baru ke Cloudflare (3.1 / 3.2).
2. Zero Trust → **Networks → Tunnels → inovass-vps → Public Hostname** → **Add**: domain baru (dan `www`-nya) → `HTTP` → `web:80`.
3. Cek domain baru sudah terbuka, lalu hapus baris Public Hostname domain lama.

Kalau ingin domain lama tetap berfungsi dan mengalihkan ke domain baru: biarkan domain lama di Cloudflare, lalu buat **Redirect Rule** dari domain lama ke domain baru.

---

## Kalau ada masalah

| Gejala | Penyebab & solusi |
|---|---|
| Actions merah di **Deploy to VPS** | Secret SSH salah, atau public key belum ada di `~/.ssh/authorized_keys` server. Buka log step tersebut. |
| **Deploy to VPS** ter-*skip* | Secret `SSH_HOST` belum diisi di repo baru. |
| Server gagal `pull` image (*denied / unauthorized*) | Image Private. Jadikan Public (1.5 poin 4), atau lakukan 1.4. |
| Cloudflare **Error 1033** | Tunnel tidak tersambung: cek `docker logs inovass-tunnel`, dan pastikan token di `.env` benar. |
| Cloudflare **Error 502 / Bad gateway** | Container website mati, atau URL di Public Hostname bukan `web:80`. Cek `docker ps`. |
| Domain belum bisa dibuka | Status domain belum *Active* (nameserver belum berubah). Tunggu, lalu cek di registrar. |
