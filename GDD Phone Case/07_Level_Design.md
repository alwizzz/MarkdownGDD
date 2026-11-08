# 07. Level Design L1–L10

[← Kembali ke indeks](00_README.md)

Draft: *berdasarkan level yang dicapai player, tingkat kesulitan dan peralatan yang digunakan akan semakin kompleks, dan variasi pelanggan semakin beragam.* [DRAFT]

Hal yang ditentukan oleh level [DRAFT]:
1. Variasi pelanggan
2. Model dan material hias casing
3. Variasi device
4. Penambahan karyawan dan kasir
5. Unlock dekorasi store
6. Gatekeep store tycoon

---

## 1. Tabel unlock dari draft [DRAFT]

| L | Unlock New Customer | Unlocked Decor | Unlock Tycoon | Unlock Color |
|---|---|---|---|---|
| 1 | Normal | | | 5 |
| 2 | | Stool | Pattern Shelf | 2 |
| 3 | Fancy Girl/Boy | | Employee +1 | 2 |
| 4 | | Table | Sticker Stock | 2 |
| 5 | Thief | Sofa | | 2 |
| 6 | | Plant Pot | Glossy Finish Paint Shelf | 2 |
| 7 | Old Club | Trash Bin | Employee +1 | 2 |
| 8 | | Statue | Waiting Room Expand | 2 |
| 9 | Rich Kid | | | 2 |
| 10 | | Fish Tank | Employee +1 | 2 |

## 2. Tabel level lengkap (V1)

Kolom tambahan diisi GDD ini [USULAN] dan angka waktu dari [SIM].

| L | XP ke level berikut | Tiba di level ini (menit main) | Pelanggan baru | Device baru | Langkah craft aktif | Tycoon (harga) | Dekor (harga Basic) | Warna (total) | Pola / Stiker / Bentuk baru | Gems level-up |
|---|---|---|---|---|---|---|---|---|---|---|
| **1** | 50 | 0 | Normal | Aphone 18 Pro Max | Shape, Paint, Smoothing, Cleaning (4) | — | Cat tembok, lantai, papan nama | 5 | Bentuk Slim, Bumper | — |
| **2** | 120 | 2,1 | — | — | + Top Pattern (5) | Pattern Shelf (120) | Stool (60), warna meja | 7 | Pola Glitter, Dots, Stripes | 5 |
| **3** | 220 | 6,9 | Fancy Girl/Boy | Samsam X26 Ultra | 5 | Employee #1 (350) | Hiasan dinding | 9 | Bentuk Bunny Ears | 5 |
| **4** | 350 | 15,2 | — | — | + Sticker (6) | Sticker Stock (600) | Table (180) | 11 | 12 stiker, pola Hearts | 5 |
| **5** | 500 | 26,2 | Thief | Earpod | 6 | — | Sofa (400), model kasir | 13 | Bentuk Round Shell, Bear Ears | 10 |
| **6** | 680 | 40,7 | — | — | 6 + Glossy | Glossy Finish Paint Shelf (1.500) | Plant Pot (300) | 15 | +4 stiker, pola Stars & Checker, Kitty Ears | 5 |
| **7** | 880 | 60,7 | Old Club | Tablet | 6 + Glossy | Employee #2 (2.200) | Trash Bin (250) | 17 | Bentuk Folio, Slim Bumper | 5 |
| **8** | 1.100 | 83,8 | — | — | 6 + Glossy | Waiting Room Expand (3.000) | Statue (900) | 19 | +4 stiker, pola Marble Swirl | 5 |
| **9** | 1.350 | 109,8 | Rich Kid | Macbook | 6 + Glossy | — | — | 21 | Bentuk Hard Shell, Bumper Corners | 5 |
| **10** | — (cap V1) | 142,0 | — | — | 6 + Glossy | Employee #3 (6.500) | Fish Tank (2.000) | 23 | +4 stiker | 20 |

**Total XP L1→L10: 5.250.** Total Gems dari level-up: 65 💎.

### Daftar warna per level [USULAN]
Setiap warna punya **nama + ikon simbol** untuk aksesibilitas.

| L | Warna (hex) |
|---|---|
| 1 | Bubblegum Pink `#FF8FC7` ♥, Sky Blue `#7CC8FF` ☁, Lemon Yellow `#FFE45C` ★, Mint Green `#7BE0B0` ♣, Snow White `#F7F7FA` ❄ |
| 2 | Lavender `#B9A2FF` ✿, Peach `#FFB58A` ● |
| 3 | Coral Red `#FF6B6B` ♦, Midnight Black `#2B2B36` ☾ |
| 4 | Grape Purple `#8A4FD8` ◆, Ocean Teal `#22B3A6` ≈ |
| 5 | Sunset Orange `#FF8A3D` ☀, Baby Blue `#BFE3FF` ○ |
| 6 | Cherry Red `#D7263D` ♥♥, Cream `#FFF3D6` ◇ |
| 7 | Forest Green `#2E8B57` ♠, Dusty Rose `#D99AA5` ❀ |
| 8 | Navy `#24325F` ⚓, Lilac `#D8B4F8` ✦ |
| 9 | Hot Pink `#FF3EA5` ✚, Charcoal `#4A4A55` ■ |
| 10 | Cocoa Brown `#8B5A3C` ☕, Neon Lime `#B6FF3B` ⚡ |

---

## 3. Kurva pengalaman

```
Menit main:  0    2.1   6.9   15.2   26.2    40.7     60.7     83.8      109.8      142.0
Level:       L1───L2────L3────L4─────L5──────L6───────L7───────L8────────L9─────────L10
Durasi lvl:   2.1   4.8   8.3   11.0   14.5    20.0     23.1     26.0      32.2
```

| Fase | Level | Durasi per level | Tujuan |
|---|---|---|---|
| **Hook** | L1–L3 | 2–8 menit | Hadiah cepat. Pemain merasakan 3 level-up dalam 8 menit pertama |
| **Bangun toko** | L4–L6 | 11–20 menit | Semua langkah craft terbuka, toko mulai ramai. Target akhir sesi pertama ada di L5 (±26 menit) |
| **Kelola toko** | L7–L9 | 23–32 menit | Karyawan ke-2 dan ke-3, device besar, pelanggan premium. Biasanya di sesi ke-2 sampai ke-4 |

**Patokan:** pemain gratis mencapai L10 dalam **±2,4 jam main aktif** (142 menit) [SIM]. Bonus teman, grup, Premium, dan AFK hanya menambah **cash** (toko lebih cepat lengkap), tidak mempercepat level, karena XP tidak ikut bonus. Dengan gamepass 2x XP sekitar 1,2 jam.

---

## 4. Detail per level

### Level 1: "Grand Opening" (FTUE)
- **Pemain baru:** spawn di kota, kamera menyapu kota lalu berhenti di plot sendiri. Teks: *"Your shop is ready!"*
- **Pelanggan tutorial "Mia"** (Normal), Aphone 18 Pro Max, request: Bubblegum Pink.
- Tutorial langkah per langkah dengan **panah kuning di lantai** dan **cincin kuning** di objek [FMP]:
  1. Mia masuk dan bicara ke kasir → pesanan muncul di waiting table → [E] → order card → **I'LL MAKE IT!**
  2. Craft Bench (pemain tidak berpindah tempat): pilih Shape **Slim** dari list HUD → Paint (pink) → Smoothing → Cleaning → TURN IT ON
  3. Langkah terakhir selesai → **langsung dibayar**: layar reward +45 cash (gaji 31 + sesuai 8 + cepat 6), +26 XP → Mia mengambil case dari bench → badge **Open For Business!**
  4. Bar waktu bonus kecepatan dikenalkan di pesanan ini, dengan target longgar (×1,5 di L1–L2).
- Pesanan ke-2 tanpa tutorial (panah hanya menunjuk waiting table).
- **Level up di pesanan ke-2** (50 XP).
- Isi toko: lihat [05](05_Toko_Tycoon_Karyawan.md#1-isi-toko-di-level-1-gratis).

### Level 2: "Sparkle Time"
- Unlock: **Pattern Shelf** (hologram muncul, harga 120), **Stool** (60), 2 warna, 3 pola.
- Tutorial singkat: panah ke hologram Pattern Shelf di dinding belakang Craft Bench → BUILD → tab pola baru berkilau di tray HUD → pesanan berikutnya otomatis memakai Top Pattern dengan Glitter.
- Pertama kali bisa menghias toko: popup kecil "Make it yours!" ke app Decor (warna meja terbuka).
- Pemain biasanya punya 85 cash saat tiba [SIM], jadi Pattern Shelf terbeli ±1,2 menit kemudian.

### Level 3: "Fancy Customers"
- Unlock: **Fancy Girl/Boy**, **Samsam X26 Ultra**, bentuk Bunny Ears, **Employee #1** (350), hiasan dinding, 2 warna.
- Pelanggan pertama setelah level-up dijamin Fancy, request Bunny Ears + Lavender.
- Setelah Employee #1 dibeli: cutscene 3 detik karyawan masuk lewat pintu dan melambai. Tutorial: *"The cashier assigns simple orders to your staff!"*
- Bobot device mulai bercampur (60/40).

### Level 4: "Sticker Shop"
- Unlock: **Sticker Stock** (600), **Table** (180), 12 stiker, pola Hearts, 2 warna.
- Semua 6 langkah craft sudah ada. Pesanan rata-rata 5,3 langkah.
- Tutorial stiker: drag, pinch/scroll untuk skala, putar.
- Hint app Staff: *"Teach Pattern to Jules so they can take more orders!"* (sink skill karyawan pertama).

### Level 5: "Stop, Thief!"
- Unlock: **Thief**, **Earpod**, **Sofa** (400), model mesin kasir, 2 warna.
- Pelanggan pertama setelah level-up dijamin Thief. Tombol STOP THIEF! diperkenalkan dengan slow-motion 0,5 detik pertama kali.
- Earpod adalah pesanan cepat (faktor waktu 0,7×), berfungsi sebagai "napas" di antara pesanan berat.
- **Tutorial Display Rack & AFK** di level ini: *"Show off your best cases! They earn cash even while you're offline."* Ini menutup sesi pertama dengan alasan untuk kembali.
- Gems level-up: 10.

### Level 6: "Glossy Glam"
- Unlock: **Glossy Finish Paint Shelf** (1.500), **Plant Pot** (300), Kitty Ears, pola Stars & Checker, +4 stiker, 2 warna.
- Request Glossy mulai muncul (40%, Fancy 70%).
- Pemain tiba dengan ±1.117 cash, jadi Glossy Shelf terbeli ±5 menit kemudian [SIM].

### Level 7: "The Old Club"
- Unlock: **Old Club**, **Tablet**, **Employee #2** (2.200), **Trash Bin** (250), 2 warna.
- Pesanan 2 case serasi pertama. Case kedua otomatis memakai bentuk yang sama.
- Tablet memperkenalkan area besar dengan payout tinggi.

### Level 8: "Bigger Shop"
- Unlock: **Waiting Room Expand** (3.000), **Statue** (900), pola Marble Swirl, +4 stiker, 2 warna.
- Momen visual terbesar di V1: animasi ekspansi bangunan ke taman [DRAFT].
- Waiting Table 2→3, kursi tunggu 3→6.

### Level 9: "Rich Kid in Town"
- Unlock: **Rich Kid**, **Macbook**, bentuk Hard Shell & Bumper Corners, 2 warna.
- Bonus Offer + HAGGLE diperkenalkan.
- Level terpanjang (±32 menit). Diimbangi payout tertinggi dan pelanggan paling bervariasi.

### Level 10: "Gallery Master" (cap V1)
- Unlock: **Employee #3** (6.500), **Fish Tank** (2.000), +4 stiker, 2 warna, 20 Gems.
- Badge **Gallery Master**. Papan nama toko mendapat bintang emas.
- XP setelah L10 diubah menjadi **Prestige Stars** (kosmetik di papan nama) sampai konten L11+ rilis [USULAN].
- Sink setelah L10: upgrade skill/speed/quality karyawan, varian dekor Cute dan Premium, Best Case of the Week.

---

## 5. Ritme dalam satu jam main [USULAN]

| Pola | Aturan |
|---|---|
| Momen spesial | Fancy dijamin minimal 1× per 5 pelanggan. Ada momen "wow" setiap ±5 menit |
| Pesanan istirahat | Earpod dan pelanggan Thief adalah pesanan pendek di antara pesanan Tablet/Macbook/Old Club |
| Unlock yang terlihat | Setiap level membuka minimal 1 hal yang langsung terlihat di toko (hologram tycoon atau dekor) |
| Next unlock | HUD selalu menampilkan "Next: Lv X – [hal yang dibuka]" [FMP] |
| Tidak ada level kosong | L9 tidak punya tycoon/dekor di draft. Diisi Rich Kid + Macbook + bentuk baru supaya tetap terasa besar |
