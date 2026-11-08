# 04. Mekanik Hands-On

[← Kembali ke indeks](00_README.md)

Daftar langkah dari draft [DRAFT]:

| # | Langkah | Fungsi (draft) | Buka di | Skill karyawan |
|---|---|---|---|---|
| 1 | **Case Shape** | Memilih bentuk casing customer | L1 | `shape` (basic) |
| 2 | **Base Painting** | Pewarnaan dasar casing | L1 | `paint` (basic) |
| 3 | **Smoothing** | Penghalusan permukaan / coating | L1 (Glossy di L6) | `smooth` (basic), `glossy` (upgrade) |
| 4 | **Top Pattern** | Glitter, pattern (topping) | L2 (Pattern Shelf) | `pattern` (upgrade) |
| 5 | **Sticker** | Menempel stiker | L4 (Sticker Stock) | `sticker` (upgrade) |
| 6 | **Screen Cleaning** | Pembersihan sebelum diberikan ke customer | L1 | `clean` (otomatis dimiliki semua karyawan) |

> Draft menyebut skill dasar karyawan adalah Case Shape, Basic Painting, dan Smoothing. GDD ini menambahkan `clean` sebagai skill bawaan semua karyawan, karena setiap pesanan selalu diakhiri Screen Cleaning [USULAN].

### Satu bench untuk semua langkah
Semua 6 langkah dikerjakan di **satu Craft Bench**. Pemain **tidak berpindah lokasi** selama mengerjakan pesanan.

| Aturan | Detail |
|---|---|
| Posisi pemain | Avatar berdiri di depan Craft Bench sejak I'LL MAKE IT! sampai pesanan selesai |
| Kamera | Tetap di bench. Antar langkah hanya ada transisi kecil: case berputar/miring sesuai kebutuhan langkah (belakang untuk Paint–Sticker, depan untuk Cleaning) |
| Alat | Semua alat (spray, buffer, kuas glossy, toples glitter, roller, kain) muncul di **tray HUD bawah** sesuai langkah aktif. Di dunia 3D, alat terlihat tergantung di papan alat di bench |
| Bahan | Warna, bentuk, pola, dan stiker dipilih dari **tray HUD bawah**, bukan dari rak di dunia |
| Rak tycoon (Pattern Shelf, Sticker Stock, Glossy Finish Paint Shelf) | Tetap dibeli sebagai item tycoon [DRAFT], tetapi berfungsi sebagai **unlock**: setelah dibeli, bahan barunya muncul di tray HUD. Raknya dipasang di dinding **tepat di belakang Craft Bench** sebagai pajangan visual, jadi pemain tidak perlu berjalan ke sana |
| Karyawan | Sama: setiap karyawan mengerjakan semua langkah di work bench miliknya sendiri |

---

## 1. Kerangka umum setiap langkah

Setiap langkah memakai pola yang sama supaya mudah dibuat dan mudah dipahami pemain:

```
Masuk langkah → case berputar ke sisi yang dikerjakan (tetap di bench yang sama) → "Step X of N" di atas
  → pemain memilih bahan (bentuk/warna/pola/stiker) dari tray HUD bawah
  → aksi utama (tap / drag) → progress bar naik
  → progress 100% → langkah selesai otomatis
    (sisa ≤ 10% diisi otomatis supaya pemain tidak mencari piksel terakhir)
  → KATA KONFIRMASI + partikel + SFX → langkah berikutnya
```

| Aturan | Nilai | Alasan |
|---|---|---|
| Selesai langkah | Otomatis di 100% (auto-fill saat ≥ 90%) | Tidak ada penilaian kualitas. Yang dinilai hanya **kesesuaian request** dan **kecepatan** |
| Tombol DONE | Hanya di langkah Sticker (pemain menentukan kapan selesai menempel) | |
| **Timer kecepatan** | Berjalan sejak langkah pertama dimulai sampai langkah terakhir selesai. Berhenti saat PUT DOWN | Menentukan bonus kecepatan 20% (bagian 3) |
| Undo | 1 tingkat per langkah (tombol ↶) | Mengurangi frustrasi, murah dibuat |
| Durasi target per langkah | 5–22 detik | Total satu pesanan ±60–95 detik [SIM] |
| PUT DOWN | Pesanan diletakkan di bench, progres disimpan | Pemain bisa pergi membeli upgrade lalu kembali [FMP] |

---

## 2. Detail per langkah

### Step 1. Case Shape
| | |
|---|---|
| Lokasi | Craft Bench |
| Aksi | **Pilih 1 bentuk dari list di HUD bawah** (kartu ikon bentuk, scroll horizontal). Tap = bentuk dipakai, langkah langsung selesai. Tidak ada mini-game |
| Tampilan list | Hanya bentuk yang sudah terbuka **untuk device pesanan ini**. Bentuk yang diminta pelanggan ditandai ✔ hijau. Bentuk terkunci tampil abu-abu dengan label "Lv X" |
| Visual | Case polos putih "pop" muncul di atas device dengan bounce kecil dan berputar sekali |
| Durasi | ±2–5 detik (waktu target 5 detik) |
| Kata konfirmasi | **PERFECT FIT!** |
| Request yang bisa muncul | Bentuk tertentu (L3+, terutama Fancy) |
| Data hasil | `shapeId` |

**Daftar bentuk V1 [USULAN]:**

| Device | Bentuk | Buka |
|---|---|---|
| Aphone 18 Pro Max | Slim, Bumper | L1 |
| | Bunny Ears | L3 |
| | Kitty Ears | L6 |
| Samsam X26 Ultra | Slim, Bumper | L3 |
| | Bunny Ears | L3 |
| | Kitty Ears | L6 |
| Earpod | Round Shell, Bear Ears | L5 |
| Tablet | Folio, Slim Bumper | L7 |
| Macbook | Hard Shell, Bumper Corners | L9 |

### Step 2. Base Painting
| | |
|---|---|
| Lokasi | Craft Bench |
| Aksi | Pilih 1 warna dari palet di tray HUD bawah → **drag** di atas case untuk menyemprot. Kuas menutupi area sekitar titik sentuh |
| Mekanik coverage | Bagian belakang case dibagi grid **8 × 16 sel**. Satu semprotan menutup area 2×2 sel (3×3 dengan gamepass *Wide Spray*) |
| Visual | Partikel kabut warna, sel yang sudah tersemprot berubah warna dengan sedikit gradasi tepi. Saat 100%, case berubah menjadi warna solid dengan kilau singkat |
| Kata konfirmasi | **COLORFUL!** |
| Request | Warna tertentu (selalu muncul mulai pesanan ke-2) |
| Data hasil | `baseColorId` |

### Step 3. Smoothing (+ Glossy Finish)
| | |
|---|---|
| Lokasi | Craft Bench, alat **Buffer** (amplas putar) dari tray HUD |
| Aksi | **Drag melingkar / bolak-balik** di atas case. Permukaan punya tekstur kasar (butiran). Setiap sel punya nilai kasar 0–3, setiap lintasan buffer mengurangi 1 (2 dengan gamepass *Power Buffer*) |
| Visual | Debu halus beterbangan, butiran memudar per sel, highlight kilap bergerak mengikuti buffer |
| Kata konfirmasi | **SMOOTH!** |
| Sub-step Glossy (L6+) | Jika pesanan meminta **Glossy**, setelah Smoothing muncul sub-step: celup kuas di kaleng clear coat → **3 sapuan panjang** dari atas ke bawah case. Kilau sapuan (shine sweep) melintas setelah sapuan ke-3. Kata: **SHINY!** |
| Request | Finish Matte / Glossy (L6+) |
| Data hasil | `finish` = `matte` / `glossy` |

### Step 4. Top Pattern
| | |
|---|---|
| Lokasi | Craft Bench. Bahan pola terbuka setelah **Pattern Shelf** dibeli (tycoon L2) |
| Aksi A: Glitter | Pilih toples glitter → **goyang**: tap berulang / drag cepat bolak-balik. Setiap goyangan menaburkan glitter (+8% progress) |
| Aksi B: Pola stempel | Pilih pola + warna pola → **roller**: 3 sapuan drag melintang case. Setiap sapuan membuka 1/3 pola |
| Visual | Glitter: partikel berkilau jatuh dan menempel. Pola: decal muncul mengikuti arah roller |
| Kata konfirmasi | **SPARKLY!** (glitter) / **STYLISH!** (pola) |
| Request | Pola tertentu, kadang dengan warna pola tertentu |
| Data hasil | `patternId`, `patternColorId` |

**Daftar pola V1 [USULAN]:**

| Pola | Tipe | Buka |
|---|---|---|
| Glitter Sprinkle | Glitter | L2 |
| Polka Dots | Stempel | L2 |
| Stripes | Stempel | L2 |
| Hearts | Stempel | L4 |
| Stars | Stempel | L6 |
| Checkerboard | Stempel | L6 |
| Marble Swirl | Stempel | L8 |
| Holo Glitter | Glitter (premium, Gems) | L2 |
| Neon Grid | Stempel (premium, Gems) | L6 |

### Step 5. Sticker
| | |
|---|---|
| Lokasi | Craft Bench. Stiker terbuka setelah **Sticker Stock** dibeli (tycoon L4) |
| Aksi | Drag stiker dari tray ke case. Skala: pinch (mobile) / scroll (PC) / LB-RB (gamepad), rentang 0,6×–1,4×. Putar: dua jari / Q-E / stik kanan. Tap stiker untuk memilih, tombol 🗑 untuk hapus |
| Batas | Maksimal **3 stiker** per case (5 dengan VIP) |
| Aturan posisi | Stiker tidak boleh menutupi lubang kamera. Posisi di-*clamp* ke area aman |
| Visual | Stiker "peel" dari tray, menempel dengan bounce kecil + efek kilat putih |
| Kata konfirmasi | **CUTE!** |
| Selesai | Tombol **DONE ✓**. Boleh 0 stiker jika pelanggan tidak meminta stiker |
| Request | Stiker tertentu (harus benar-benar ditempel) |
| Data hasil | `stickers[]` = `{id, u, v, scale, rot}` |

**Stiker V1:** 24 stiker 2D orisinal [USULAN]: 12 di L4, +4 di L6, +4 di L8, +4 di L10. Tema: makanan lucu, hewan kawaii, luar angkasa, Y2K. Lihat [15](15_Konten_Aset_MVP.md).

### Step 6. Screen Cleaning
| | |
|---|---|
| Lokasi | Craft Bench, alat **Cloth + Spray Cleaner** dari tray HUD |
| Aksi | Device dibalik ke depan. Layar punya 4–6 noda (sidik jari, debu, tumpahan). **Drag** kain di atas noda sampai hilang. Noda besar perlu 2 lintasan |
| Penutup | Tombol besar **TURN IT ON** → layar menyala menampilkan wallpaper pelanggan, case berputar 360° di turntable, efek kamera "flash" menyimpan foto ke Album [USULAN, terinspirasi FMP]. **Pesanan langsung selesai dan dibayar** (bagian 3). Pelanggan berjalan ke bench, mengambil case, lalu pergi. Timer berhenti saat noda terakhir bersih, jadi animasi penutup tidak memakan waktu bonus |
| Kata konfirmasi | **SPOTLESS!** lalu **ALL DONE!** |
| Data hasil | — |

---

## 3. Penilaian & bayaran

Pesanan **langsung selesai dan dibayar** begitu langkah terakhir selesai. Tidak ada DELIVER ke kasir.

| Komponen | Syarat | Bayaran | Bintang |
|---|---|---|---|
| **Gaji dasar** | Pesanan selesai (pasti didapat) | 100% gaji dasar | ★ |
| **Bonus kesesuaian** | Semua request pelanggan terpenuhi | +25% gaji dasar | ★ |
| **Bonus kecepatan** | Selesai ≤ waktu target | +20% gaji dasar | ★ |

- Bayaran maksimal = **1,45 × gaji dasar**. Rumus lengkap di [08](08_Ekonomi.md#2-rumus-bayaran-pesanan).
- Bintang (1–3★) hanya tampilan dari tiga komponen ini: ★ selesai, ★ sesuai, ★ cepat.
- Tidak ada kondisi gagal. Pesanan yang selesai selalu dibayar gaji dasar [SRC 04].

### Waktu target
```
waktu_target = Σ target_langkah × faktor_waktu_device
level pemain ≤ 2 → waktu_target × 1,5   (pemain baru masih belajar)
```

| Langkah | Shape | Paint | Smoothing | Glossy (sub-step) | Top Pattern | Sticker | Cleaning |
|---|---|---|---|---|---|---|---|
| Target (detik) | 5 | 18 | 16 | +6 | 16 | 22 | 12 |

| Contoh | Hitungan | Waktu target |
|---|---|---|
| L1, Aphone, 4 langkah | (5+18+16+12) × 1,0 × 1,5 | 77 dtk |
| L4, Samsam, 6 langkah | (5+18+16+16+22+12) × 1,0 | 89 dtk |
| L7, Tablet, 6 langkah + Glossy | (5+18+16+6+16+22+12) × 1,4 | 133 dtk |

- Timer dihitung **di server** sejak langkah pertama dimulai, berhenti saat PUT DOWN, dan berhenti total saat langkah terakhir selesai.
- Target sedikit lebih longgar dari waktu rata-rata pemain [SIM], sehingga ±70% pesanan diperkirakan mendapat bonus kecepatan.
- Gamepass alat (Wide Spray, Power Buffer, Magic Wipe) tidak mengubah target. Mereka membuat bonus kecepatan lebih mudah didapat.
- Saat bonus kecepatan terlewat, tidak ada suara atau efek negatif. Bar waktu hanya berubah abu-abu dengan teks kecil "Speed bonus missed".

### Pengecekan kesesuaian request

| Elemen | Aturan |
|---|---|
| Warna | `baseColorId` sama persis dengan request (warna dipilih dari palet, jadi tidak ada masalah RGBA seperti game sumber) |
| Pola | `patternId` sama. Jika request menyebut warna pola, `patternColorId` juga harus sama |
| Stiker | Stiker yang diminta ada di `stickers[]` |
| Bentuk | `shapeId` sama |
| Finish | `finish` sama |
| "Surprise me!" | Request kosong untuk elemen itu. Apa pun pilihan pemain dianggap sesuai |

**Bantuan aksesibilitas:** item yang diminta pelanggan ditandai **✔ hijau** di tray saat dipilih dan dicentang di order card. Setiap warna punya nama dan ikon simbol, jadi pemain buta warna tetap bisa mencocokkan [SRC Analisis 6.3].

---

## 4. Kontrol per device

| Aksi | Mobile | PC | Gamepad |
|---|---|---|---|
| Interaksi dunia (ambil pesanan, kembali ke bench, beli, ambil Tip Jar) | Tombol prompt di layar | **[E]** | **X / ▢** |
| Mulai craft di bench | Tombol prompt | **[R]** atau [E] di bench [FMP] | **X / ▢** |
| Spray, buffer, wipe, roller | Drag satu jari | Klik kiri + drag | Kursor virtual (stik kiri) + **RT** |
| Pilih bentuk / warna / pola / stiker di tray HUD | Tap | Klik | D-pad kiri/kanan + **A** |
| Goyang glitter | Tap cepat / goyang drag | Klik cepat | Tekan **A** berulang |
| Stiker skala | Pinch | Scroll | **LB / RB** |
| Stiker putar | Putar dua jari | Q / E | Stik kanan |
| DONE (langkah Sticker) | Tombol besar kanan bawah | Tombol / Enter | **A** |
| Undo | Tombol ↶ | Ctrl+Z | **Y** |
| PUT DOWN (keluar craft) | Tombol kiri atas | Esc | **B** |

- Deteksi input memakai `UserInputService.PreferredInput` (bukan `TouchEnabled`) [SRC Analisis S25].
- Haptic ringan saat case muncul (Step 1), goyang glitter, dan stiker menempel (mobile + gamepad).

---

## 5. Freestyle Mode di bench [USULAN]
Di luar pesanan, pemain bisa membuat case bebas di bench (tanpa pelanggan, tanpa cash/XP). Hasilnya bisa dipajang di display rack, dipegang avatar, atau dikirim ke Best Case of the Week. Ini menjaga sisi ekspresi diri tanpa mengganggu ekonomi. Freestyle memakai bahan yang sudah terbuka saja.
