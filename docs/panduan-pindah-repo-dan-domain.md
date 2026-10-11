# Panduan: pindah repo ke akun GitHub lain + pasang domain

Kondisi sekarang:

| Komponen | Saat ini | Setelah pindah repo |
|---|---|---|
| Repo GitHub | `github.com/afidzulinn/web-inovass` | `github.com/<AKUN-BARU>/web-inovass` |
| Image Docker | `ghcr.io/afidzulinn/web-inovass` | `ghcr.io/<akun-baru>/web-inovass` |
| Cloudflare Workers | project `web-inovass` di akun Cloudflare yang sama | **tetap**, hanya sambungan Git-nya diganti |
| VPS | `ubuntu@129.226.157.124`, folder `~/apps/web-inovass` | **tetap**, tidak perlu disentuh manual |

Di panduan ini, `<AKUN-BARU>` adalah username GitHub tujuan dan `<akun-baru>` adalah versi **huruf kecil** dari username itu (nama image Docker wajib huruf kecil).

---

## Bagian A: Pindah repo ke akun GitHub lain

### A1. Pindahkan repo (pilih salah satu)

**Cara 1, Transfer (disarankan):** riwayat commit tetap ada, dan link lama otomatis dialihkan.
1. Login ke akun lama → buka repo `web-inovass` → **Settings → General** → paling bawah **Danger Zone → Transfer ownership**.
2. Isi username akun baru → ketik nama repo untuk konfirmasi → **I understand, transfer this repository**.
3. Login ke akun baru → buka email dari GitHub → **terima** transfer-nya.

**Cara 2, Repo baru:** dipakai kalau transfer tidak bisa.
1. Login ke akun baru → **New repository** → nama `web-inovass` → **Public** → *jangan* centang README/.gitignore → **Create**.
2. Di laptop (folder project):
   ```bash
   git remote set-url origin https://github.com/<AKUN-BARU>/web-inovass.git
   git push -u origin main
   ```

> **Public atau private?** Disarankan tetap **Public**: GitHub Actions gratis tanpa batas, dan server bisa mengambil image tanpa login. Kalau **Private**: Actions dapat 2.000 menit/bulan (cukup, karena satu deploy ±1 menit), tapi server perlu login ke GHCR (lihat A5).

### A2. Arahkan laptop ke repo baru
Kalau memakai Cara 1 (Transfer):
```bash
git remote set-url origin https://github.com/<AKUN-BARU>/web-inovass.git
git remote -v        # pastikan sudah menunjuk ke akun baru
```
Kalau Git meminta login, login sebagai akun baru.

### A3. Ganti nama image di 2 file
Cari teks `afidzulinn/web-inovass` dan ganti dengan `<akun-baru>/web-inovass` (huruf kecil) di:
- `docker-compose.yml` → baris `image:`
- `.github/workflows/deploy.yml` → baris `IMAGE:`

(README juga menyebut nama lama, jadi boleh ikut diganti.) Jangan push dulu, selesaikan A4 terlebih dahulu.

### A4. Isi secrets di repo baru
Repo baru → **Settings → Secrets and variables → Actions**. Kalau memakai Transfer, cek dulu apakah 3 secret ini sudah ikut pindah. Kalau belum ada, buat dengan **New repository secret**:

| Name | Value |
|---|---|
| `SSH_HOST` | `129.226.157.124` |
| `SSH_USER` | `ubuntu` |
| `SSH_KEY` | private key deploy. Ambil di server dengan `cat ~/.ssh/github_deploy2`, salin seluruhnya termasuk baris `-----BEGIN…` dan `-----END…` |

Paste private key **langsung ke GitHub**, jangan lewat chat atau email.

### A5. (Hanya jika repo Private) Izinkan server mengambil image
1. Akun baru → **Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token** → centang hanya `read:packages` → Generate → salin token-nya.
2. Di server:
   ```bash
   echo '<TOKEN>' | docker login ghcr.io -u <AKUN-BARU> --password-stdin
   ```

### A6. Push dan cek deploy ke VPS
```bash
git add -A
git commit -m "Pindah image ke akun baru"
git push
```
Repo baru → tab **Actions** → **Build & Deploy** harus hijau, dan step **Deploy to VPS** harus *success* (bukan *skipped*).

Cek di server:
```bash
docker ps --format '{{.Names}}  {{.Image}}  {{.Status}}'
# inovass-web harus memakai ghcr.io/<akun-baru>/web-inovass:latest
```

### A7. Sambungkan ulang Cloudflare ke repo baru
Akun Cloudflare tetap sama; yang diganti hanya sumber Git-nya.
1. dash.cloudflare.com → **Workers & Pages** → **web-inovass** → **Settings** → bagian **Build** → **Git repository**.
2. Klik **Disconnect** (atau **Manage**) pada repo lama → **Connect**.
3. Pilih **GitHub** → kalau akun baru belum terdaftar, klik **Add account / Install** → login sebagai akun baru → pilih **Only select repositories** → `web-inovass` → **Install & Authorize**.
4. Pilih akun baru → repo `web-inovass` → branch `main` → **Connect**. Deploy command biarkan `npx wrangler deploy`.
5. Tes: push perubahan kecil, lalu lihat **web-inovass → Deployments**. Harus muncul build baru dengan status *Success*.

Alamat `https://web-inovass.inovass.workers.dev` **tidak berubah**, karena nama project dan akun Cloudflare-nya sama.

> Nama project di Cloudflare (`web-inovass`) harus tetap sama dengan `"name"` di `wrangler.jsonc`. Jangan ganti salah satunya saja.

### A8. Bersih-bersih (setelah semua hijau)
- **Akun lama**: hapus package image lama di **Profile → Packages → web-inovass → Package settings → Delete package**, lalu cabut akses Cloudflare di **Settings → Applications → Installed GitHub Apps → Cloudflare Workers and Pages → Configure → Uninstall** (kalau tidak dipakai repo lain).
- **Server**: hapus image lama supaya disk tidak penuh:
  ```bash
  docker rmi ghcr.io/afidzulinn/web-inovass:latest
  docker image prune -f
  ```
- Folder `~/apps/web-inovass` di server hanya membutuhkan `docker-compose.yml` (dan `.env` kalau ada). Isi Git lain di sana tidak dipakai deploy.

### Checklist Bagian A
- [ ] Repo ada di akun baru, dan laptop sudah `git remote set-url`
- [ ] Nama image diganti di `docker-compose.yml` dan `deploy.yml`
- [ ] Secret `SSH_HOST`, `SSH_USER`, `SSH_KEY` ada di repo baru
- [ ] Actions hijau, dan step **Deploy to VPS** *success*
- [ ] Cloudflare **web-inovass** tersambung ke repo baru, dan build setelah push *Success*
- [ ] Image dan akses lama dibersihkan

---

## Bagian B: Beli dan pasang domain (`inovass.com`)

Rencananya: domain utama dilayani **Cloudflare Workers** (cepat, gratis, tanpa VPS). VPS menjadi cadangan (opsional).

### B1. Beli domain (pilih salah satu)

**Opsi 1, beli langsung di Cloudflare (paling mudah):** domain otomatis aktif di Cloudflare, tanpa ganti nameserver.
1. dash.cloudflare.com → **Domain Registration → Register Domains** → cari `inovass.com` → **Purchase** (bayar kartu kredit/PayPal, harga modal ±US$10/tahun untuk `.com`).
2. Lanjut ke **B3**.

**Opsi 2, beli di registrar lain** (Niagahoster, Rumahweb, Domainesia, dll., bisa bayar transfer bank/QRIS):
1. Beli `inovass.com` di registrar tersebut.
2. Lanjut ke **B2**.

> Catatan: `.co.id` mensyaratkan dokumen perusahaan (akta/NIB), sedangkan `.com` dan `.id` tidak serumit itu.

### B2. (Hanya Opsi 2) Pindahkan DNS ke Cloudflare
1. dash.cloudflare.com → **Add a domain** (atau *Onboard a domain*) → isi `inovass.com` → pilih plan **Free** → lanjut.
2. Cloudflare menampilkan **2 nameserver** (contoh: `xxx.ns.cloudflare.com`, `yyy.ns.cloudflare.com`).
3. Login ke registrar tempat beli domain → menu **Nameserver / DNS** → ganti nameserver bawaan dengan 2 nameserver Cloudflare tadi → simpan.
4. Tunggu sampai status domain di Cloudflare menjadi **Active**. Biasanya beberapa menit, paling lama 24 jam, dan Cloudflare mengirim email saat aktif.

### B3. Pasang domain ke website (Cloudflare Workers)
1. **Workers & Pages → web-inovass → Settings → Domains & Routes → Add → Custom domain**.
2. Isi `inovass.com` → **Add domain**.
3. Ulangi untuk `www.inovass.com`.
4. Tunggu 1–5 menit (Cloudflare otomatis membuat sertifikat HTTPS), lalu buka https://inovass.com dan https://www.inovass.com.

*(Opsional)* Arahkan `www` ke alamat tanpa www supaya hanya ada satu alamat resmi: **Domain inovass.com → Rules → Redirect Rules → Create rule → template "Redirect from WWW to root"** → Deploy.

### B4. VPS setelah punya domain (pilih salah satu)

**Pilihan 1, matikan VPS (paling sederhana):** website sudah dilayani Cloudflare.
```bash
cd ~/apps/web-inovass && docker compose down
```
Lalu di GitHub hapus secret `SSH_HOST` agar langkah deploy VPS di-skip.

**Pilihan 2, VPS sebagai cadangan di subdomain** (misalnya `vps.inovass.com`). Jangan pakai `inovass.com`/`www`, karena dua alamat itu sudah dipakai Workers.
1. **Zero Trust → Networks → Tunnels → Create a tunnel** → *Cloudflared* → nama `inovass-vps` → salin **token** (teks setelah `--token`). Lewati langkah instalasi.
2. Tab **Public Hostname → Add**: Subdomain `vps`, Domain `inovass.com`, Type `HTTP`, URL `web:80` → Save.
3. Di server:
   ```bash
   cd ~/apps/web-inovass
   echo 'TUNNEL_ARGS=run --token <TOKEN>' > .env
   docker compose up -d
   ```
4. Buka https://vps.inovass.com. Alamat trycloudflare lama otomatis tidak dipakai lagi.

### B5. (Opsional) Email @inovass.com gratis
Website saat ini memakai `inovass.adm@gmail.com`. Kalau ingin alamat seperti `info@inovass.com` yang diteruskan ke Gmail:
**Domain inovass.com → Email → Email Routing → Get started** → buat alamat `info@inovass.com` → tujuan `inovass.adm@gmail.com` → verifikasi lewat email. Ganti teks email di website setelah itu berjalan.

### B6. Ganti domain lagi di kemudian hari
Tidak perlu mengubah kode, karena domain tidak ditulis di mana pun dalam situs.
1. Tambahkan domain baru ke Cloudflare (B1/B2).
2. **web-inovass → Settings → Domains & Routes** → tambah custom domain baru, lalu hapus yang lama.

### Checklist Bagian B
- [ ] Domain dibeli, dan status di Cloudflare **Active**
- [ ] `inovass.com` dan `www.inovass.com` terpasang sebagai Custom domain di **web-inovass**
- [ ] https://inovass.com terbuka dengan gembok (HTTPS)
- [ ] VPS: dimatikan, **atau** dipasang di `vps.inovass.com`
