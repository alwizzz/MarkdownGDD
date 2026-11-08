# 11. UI/UX

[← Kembali ke indeks](00_README.md)

Arahan UI mengikuti pola **Fix My Phone!** [FMP]. Polanya sudah terbukti dipahami pemain Roblox saat ini, dan temanya sama (toko HP). Yang kita ambil adalah **struktur dan perilakunya**, bukan aset atau tampilan persisnya.

## 1. Pola FMP yang diadopsi

| Pola FMP | Versi Phone Case Gallery |
|---|---|
| Menu utama di dalam **HP dalam game** | Tombol HP di kanan HUD membuka HP berisi app |
| Prompt **[E]** untuk bicara/ambil, **[R]** untuk mulai di bench | Sama. Di mobile berupa tombol ProximityPrompt besar |
| **Order card** (device, kerusakan, request) | Order card: device, bentuk, warna, pola, stiker, finish, dialog pelanggan |
| **Step counter** "Step X of N" | Sama, di tengah atas layar craft |
| **Kata konfirmasi** per langkah (CLEAN!, NO BUBBLES, IT WORKS!) | PERFECT FIT!, COLORFUL!, SMOOTH!, SHINY!, SPARKLY!, CUTE!, SPOTLESS!, ALL DONE! |
| **Tombol aksi besar berlabel** (I'LL FIX IT!, PUT DOWN, TURN IT ON, LEAVE) | I'LL MAKE IT!, PUT DOWN, DONE ✓ (Sticker), TURN IT ON, STOP THIEF! |
| **Panah kuning di lantai + cincin kuning** di objek | Sama, untuk FTUE dan setiap unlock baru |
| **Layar reward** (cash, XP, badge) | Muncul **langsung saat case selesai**, merinci gaji dasar + bonus kesesuaian + bonus kecepatan + bonus sosial |
| **Next unlock** "Next Level: 3 – Parts Cabinet" | "Next: Lv 3 – Employee" di bawah bar XP |
| App **Codes** | App Codes di HP |
| Intro "Opening your shop" → "We're open!" | Kamera menyapu kota → "Your shop is ready!" |

---

## 2. HUD (mode dunia)

```
┌──────────────────────────────────────────────────────────────┐
│ [Lv 4 ▓▓▓▓▓░░░ 210/350]   💵 1.240  [+]   💎 35 [+]    👥+20% │
│  Next: Lv 5 – Thief & Sofa                                   │
│                                                              │
│                                                     ┌──────┐ │
│                                                     │  📱  │ │  ← tombol HP (menu utama)
│                                                     └──────┘ │
│                                                     ┌──────┐ │
│                                                     │ 🎁 3 │ │  ← Daily quest / login (badge angka)
│ ┌──────────────────────┐                            └──────┘ │
│ │ Mia reached Level 8! │  ← feed server (pudar 4 dtk)        │
│ └──────────────────────┘          [ E  Take Order ]          │  ← prompt kontekstual
└──────────────────────────────────────────────────────────────┘
```

| Elemen | Posisi | Catatan |
|---|---|---|
| Level + bar XP + Next unlock | Kiri atas | Bar XP beranimasi mengisi saat XP masuk |
| Cash & Gems | Tengah atas | Angka "menghitung naik" saat bertambah. [+] membuka app Store |
| Bonus sosial | Kanan atas | Hanya tampil jika > 0% |
| Tombol HP | Kanan tengah | Tombol terbesar di HUD. Badge merah jika ada yang bisa diklaim |
| Quest/Login | Di bawah tombol HP | |
| Feed server | Kiri bawah | Maks 2 baris |
| Prompt kontekstual | Tengah bawah | ProximityPrompt bergaya kustom |

**Aturan mobile:** semua tombol minimal **44×44 pt**, tidak ada elemen penting di area thumbstick kiri bawah dan tombol lompat kanan bawah bawaan Roblox. Hormati safe area (notch).

---

## 3. HP dalam game (menu utama)

HP digambar sebagai HP besar di tengah layar dengan wallpaper sesuai **case yang sedang di-equip pemain** (detail kecil yang memperkuat identitas).

| App | Ikon | Isi | Buka |
|---|---|---|---|
| **Orders** | 📋 | Isi Waiting Table, pesanan yang dikerjakan karyawan + progresnya | L1 |
| **Build** | 🔨 | Daftar item tycoon: terbuka / terkunci (level) / harga. Tombol BUILD | L1 |
| **Decor** | 🎨 | Kategori dekor, varian, tombol pratinjau di toko | L1 |
| **Staff** | 👥 | Karyawan: skill, Speed, Quality, tombol upgrade, ganti nama | L3 |
| **Album** | 🖼 | 30 case terakhir. Aksi: Equip, Display, Submit to Gallery | L1 |
| **Gallery** | ⭐ | Best Case of the Week: entri saya, swipe & like entri global, Hall of Fame | L3 |
| **Visit** | 🏠 | 7 toko lain di server, tombol teleport | L1 |
| **Quests** | 🎯 | 3 daily quest + login 7 hari | L1 |
| **Store** | 🛒 | Gems, Passes, Boosts, Premium Decor | L1 |
| **Codes** | 🎟 | Kolom input code | L1 |
| **Settings** | ⚙ | Musik, SFX, haptic, kualitas grafis, bahasa | L1 |

App yang belum terbuka tampil abu-abu dengan label "Lv 3".

---

## 4. Layar craft (mode bench)

Kamera berpindah ke sudut close-up **Craft Bench** dan tetap di sana sampai pesanan selesai. Semua langkah dikerjakan di bench yang sama. Pergantian langkah hanya memutar/memiringkan case dan mengganti isi tray HUD bawah. HUD dunia disembunyikan kecuali Cash/Gems.

```
┌──────────────────────────────────────────────────────────────┐
│ [✕ PUT DOWN]          Step 2 of 5 · Base Painting       [⚡4💎]│
│                        ●──●──○──○──○                          │
│                  ⏱ ▓▓▓▓▓▓▓▓░░░░  0:41   Speed bonus           │
│ ┌─────────────┐                                               │
│ │ ORDER       │                                               │
│ │ 👧 Mia      │              ┌───────────┐                    │
│ │ Aphone 18   │              │           │                    │
│ │ ✔ Slim      │              │   CASE    │   ← area interaksi │
│ │ ○ Pink ♥    │              │  (3D)     │      (drag di sini)│
│ │ ○ Dots      │              │           │                    │
│ └─────────────┘              └───────────┘                    │
│                         ▓▓▓▓▓▓▓▓░░░░ 68%                      │
│ ┌───────────────────────────────────────────────┐ ┌────────┐ │
│ │ ♥ ☁ ★ ♣ ❄ ✿ ●  🔒       (tray bahan, scroll) │ │   ↶    │ │
│ └───────────────────────────────────────────────┘ └────────┘ │
└──────────────────────────────────────────────────────────────┘
```

| Elemen | Perilaku |
|---|---|
| Step counter + titik langkah | Titik terisi saat langkah selesai |
| Order card (kiri) | Item request dicentang ✔ hijau saat terpenuhi. Bisa diciutkan di HP kecil |
| Area case (tengah) | Satu-satunya area drag. Kursor berubah menjadi alat (spray, buffer, roller, kain) |
| Progress bar | Di bawah case. Langkah selesai otomatis di 100% (auto-fill saat ≥ 90%) |
| Tray bahan (bawah) | Scroll horizontal. Isinya berganti sesuai langkah: **list bentuk** (Step 1), palet warna (Step 2), alat buffer/kuas glossy (Step 3), pola & glitter (Step 4), stiker (Step 5), kain (Step 6). Item request bertanda ✔. Item terkunci 🔒 / 💎 |
| Step 1: list bentuk | Kartu ikon bentuk besar (min. 72 pt) untuk device pesanan ini saja. **Satu tap = bentuk terpilih dan langkah selesai**. Tidak ada mini-game |
| DONE ✓ | Hanya muncul di langkah Sticker |
| **Bar waktu (Speed bonus)** | Di bawah step counter. Hijau → kuning (sisa 25%) → abu-abu saat bonus terlewat, dengan teks kecil "Speed bonus missed". Tidak ada suara negatif. Berhenti saat PUT DOWN |
| ⚡ Instant Finish | Kecil, pojok kanan atas, harga 💎 selalu terlihat |
| Kata konfirmasi | Teks besar miring melompat di tengah + partikel, tampil 0,8 detik |

### Layar reward (langsung saat case selesai)
```
        ★ ★ ★            ← bintang muncul satu per satu (SFX naik nada)
     "I LOVE IT!"        ← reaksi pelanggan
   ✔ Order complete       💵 77
   ✔ Perfect match  +25%  💵 19
   ✔ Speed bonus    +20%  💵 15
   👥 Friends       +20%  💵 22
   ──────────────────────────────
   💵 +133         ⭐ +47 XP
   [ Earn 2x with 2x Cash ]   ← teks kecil (jika belum punya)
        [ COLLECT ]
```
Bintang = ★ selesai, ★ sesuai, ★ cepat. Bonus yang tidak didapat tampil abu-abu dengan tanda ✕ kecil (tanpa suara negatif). Layar reward tampil di atas dunia (bukan layar penuh) dan otomatis tertutup setelah 3 detik jika pemain tidak menekan apa pun, supaya alur tetap cepat.

### Layar level-up
Konfeti layar penuh singkat, "LEVEL 5!", lalu kartu unlock bergulir satu per satu (pelanggan baru, device, dekor, tycoon, warna). Tombol **LET'S GO!** mengaktifkan panah kuning ke hologram baru.

---

## 5. UI dunia (world-space)

| Elemen | Tampilan |
|---|---|
| Hologram unlock | Kerangka biru transparan berkilau + BillboardGui: nama, harga, "Lv 6". Jika level belum cukup: gembok |
| Progress karyawan | Bar kecil melayang di atas kepala karyawan + ikon langkah yang sedang dikerjakan |
| Bubble pelanggan | Ikon request singkat (warna + bentuk) di atas kepala saat antre |
| Tip Jar | Toples dengan isi koin naik sesuai jumlah. Label "$ 640 / 1.037" |
| Papan nama toko | Nama pemain + level + ❤ jumlah like + bintang emas L10 |

---

## 6. Gaya visual UI

| Token | Nilai |
|---|---|
| Font judul | **Fredoka One** (`Enum.Font.FredokaOne`): bulat, ramah |
| Font isi | **Builder Sans Bold** / Gotham Bold |
| Primer | Bubblegum Pink `#FF5FA2` |
| Sekunder | Sky Blue `#4FB8FF` |
| Aksen aksi (tombol positif) | Mint `#3DDC97` |
| Aksen panduan | Kuning `#FFD23F` (panah, cincin, sama seperti FMP) |
| Gems | Ungu `#9B5CFF` |
| Panel | Putih `#FFFFFF` 95% + sudut 16px + stroke 3px warna gelap `#2B2140` |
| Teks | `#2B2140` di panel terang, putih + stroke gelap di atas dunia |
| Bayangan | Drop shadow lembut 4px di bawah panel dan tombol |

- Tombol: bentuk kapsul tebal, bayangan bawah 4px, saat ditekan turun 2px (efek "empuk").
- Animasi: semua panel masuk dengan **scale 0,8 → 1,05 → 1,0** dalam 0,2 detik (pop).
- Ikon: gaya flat dengan outline tebal, cocok dengan dunia low-poly.

## 7. Aksesibilitas
- Setiap warna punya nama + simbol (lihat [07](07_Level_Design.md#daftar-warna-per-level-usulan)).
- Tidak ada aksi tahan (hold) di langkah craft. Semua aksi berupa tap atau drag.
- Teks minimal 18 pt di HP.
- Lokalisasi V1: **English** (utama) dan **Bahasa Indonesia**. Semua string lewat tabel lokalisasi Roblox sejak awal.
- UI tidak berkedip saat input berganti (touch ↔ gamepad) [SRC Analisis S25].
