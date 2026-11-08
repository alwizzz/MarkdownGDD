# 09. Monetisasi

[← Kembali ke indeks](00_README.md)

## 1. Arah dari draft [DRAFT]
1. Buff pendapatan
2. Gems
3. Gamepass
4. Premium dekoratif (plesetan brand besar)
5. Pengerjaan instant

## 2. Prinsip
| # | Prinsip | Alasan |
|---|---|---|
| 1 | **Tanpa iklan paksa.** Roblox tidak punya interstitial | Game sumber punya ±75 titik interstitial, tidak bisa dibawa [SRC 07] |
| 2 | **Pemain gratis tetap bisa sampai L10** dalam ±2,4 jam | Retensi lebih penting daripada monetisasi awal. Algoritma Roblox menilai retensi 28 hari [SRC Analisis S20] |
| 3 | **Beli = lebih cepat, lebih cantik, lebih sosial.** Bukan "bayar untuk bisa main" | Semua request pelanggan selalu bisa dipenuhi dengan bahan gratis |
| 4 | **Gamepass bernilai tinggi + produk kecil berulang** | Payer Roblox makin sedikit tapi belanja per payer naik [SRC Analisis S1] |
| 5 | **Tidak ada paid random item di V1** | Jika ditambah nanti, wajib menampilkan semua hasil dan peluang [SRC Analisis S24] |
| 6 | **Tawaran kontekstual, bukan popup beruntun** | Game sumber punya antrean 11 popup di Home. Kita hanya menampilkan tawaran di tempat yang relevan |

Harga mengacu ke rentang gamepass Fix My Phone: alat 99–149 R$, booster 199–249 R$, VIP 499 R$ [FMP].

---

## 3. Gamepass (9)

| # | Gamepass | Harga | Efek | Kategori draft | Ditawarkan di |
|---|---|---|---|---|---|
| 1 | **VIP Studio** | 449 R$ | +10% cash (masuk bonus sosial, cap jadi +60%), tag VIP di nama & chat, papan nama emas, +1 slot Display Rack, stiker maks 5, set dekor eksklusif "Velvet Lounge" | Buff + dekor | App Store, papan nama toko lain yang VIP |
| 2 | **2x Cash** | 349 R$ | Cash pesanan pemain & karyawan ×2 (lihat rumus [08](08_Ekonomi.md#5-bonus-cash)) | Buff pendapatan | Layar reward (tombol kecil "2x?") |
| 3 | **2x XP** | 249 R$ | XP pesanan ×2 | Buff | Layar level-up |
| 4 | **Wide Spray** | 99 R$ | Base Painting & roller menutup 3×3 sel (bukan 2×2) | Alat | Ikon gembok di tray Paint |
| 5 | **Power Buffer** | 99 R$ | Smoothing mengurangi 2 tingkat kasar per lintasan | Alat | Ikon gembok di tray Smoothing |
| 6 | **Magic Wipe** | 99 R$ | Screen Cleaning: noda besar hilang dalam 1 lintasan, radius kain lebih besar | Alat | Ikon gembok di tray Cleaning |
| 7 | **Golden Tools** | 299 R$ | Semua alat berwarna emas + jejak partikel emas + kata konfirmasi emas. Kosmetik murni | Dekor premium | Tray alat |
| 8 | **Bigger Gallery Rack** | 149 R$ | +4 slot Display Rack (4 → 8) | Buff (AFK) | Slot rak terkunci (terlihat dengan gembok) |
| 9 | **Night Shift** | 149 R$ | Cap Tip Jar 3 jam → 8 jam | Buff (AFK) | Saat Tip Jar penuh |

Alat (4–6) adalah padanan *Wide Squeegee / Power Screwdriver / Magnet Mat* di FMP: mempercepat langkah tanpa melewatinya.

---

## 4. Developer Product

### Gems [DRAFT]
| Paket | Gems | Harga | R$ per 💎 | Label |
|---|---|---|---|---|
| Pouch | 80 💎 | 59 R$ | 0,74 | |
| Stack | 250 💎 | 169 R$ | 0,68 | Popular |
| Box | 650 💎 | 399 R$ | 0,61 | |
| Vault | 1.500 💎 | 849 R$ | 0,57 | Best Value |

### Produk lain
| Produk | Harga | Isi | Catatan |
|---|---|---|---|
| **Starter Pack** (sekali beli, muncul di L3) | 99 R$ | 150 💎 + pola Holo Glitter + Boost 2x Cash 60 menit | Tawaran pertama yang sangat murah, untuk konversi payer pertama |
| **Boost 2x Cash 15 menit** | 39 R$ (atau 25 💎) | Cash ×2 selama 15 menit, bisa ditumpuk durasinya | [DRAFT: buff pendapatan]. Mirip code RELEASE di FMP |
| **Cash Party** (sosial) | 199 R$ | **Semua pemain di server** mendapat 2x Cash 15 menit. Pengumuman: "Mia started a Cash Party! 🎉" | Pembeli mendapat pengakuan sosial, pemain lain mendapat alasan untuk tetap di server |

### Pengerjaan instant [DRAFT]
Dijual lewat Gems (bukan Robux langsung) supaya satu mata uang menangani semua percepatan:

| Fitur | Harga | Efek |
|---|---|---|
| **Instant Finish** | 1 💎 per langkah (4–6 💎) | Pesanan di bench langsung selesai dengan kedua bonus (bayaran penuh ×1,45), **50% XP** |
| **Rush Staff** | 2 💎 per pesanan karyawan | Semua karyawan langsung menyelesaikan pesanannya |

---

## 5. Dekor premium (brand parodi)

Draft meminta dekor premium berupa **plesetan brand besar** [DRAFT].

> ⚠️ **Risiko kebijakan.** Aturan Roblox melarang penggunaan IP dan merek dagang pihak lain tanpa izin. Plesetan yang terlalu mirip (ganti 1 huruf, logo mirip, warna khas sama) bisa diturunkan lewat laporan DMCA/merek, dan dalam kasus terburuk experience diberi moderasi. Game sumber sendiri memakai bentuk "StarBucks" dan "Among-us", dan kita sudah memutuskan tidak meniru itu [SRC 02, SRC 11].

### Aturan aman untuk brand parodi
| Boleh | Jangan |
|---|---|
| Nama orisinal yang **membangkitkan nuansa** kategori brand (kopi mewah, fashion Paris, sneaker) | Nama yang hanya beda 1–2 huruf dari merek nyata |
| Logo dibuat dari nol dengan bentuk berbeda | Meniru logo, maskot, font khas, atau kombinasi warna ikonik |
| Lelucon yang jelas fiksi | Menyiratkan kerja sama resmi dengan brand nyata |
| Review nama oleh lead sebelum aset dibuat | Rilis tanpa review |

### Usulan set dekor premium V1 [USULAN]
| Item | Nama fiksi | Nuansa | Harga |
|---|---|---|---|
| Mesin kopi | **Bean Boss Coffee** | Kedai kopi waralaba | 90 💎 |
| Rak tas mewah | **Maison Glitté** | Rumah mode Paris | 120 💎 |
| Pajangan sepatu | **Nimbus Kicks** | Brand sneaker | 100 💎 |
| Mesin arcade | **Pixel Pop** | Arcade retro | 110 💎 |
| Kulkas minuman | **Fizzly Cola** | Minuman soda | 80 💎 |
| Neon sign | **Glam Gallery** | Fashion | 60 💎 |

Hal yang sama berlaku untuk nama device **Aphone** dan **Samsam** dari draft. Lihat [16](16_Roadmap_KPI_Risiko.md#5-risiko).

---

## 6. Peta penempatan tawaran

| Lokasi | Tawaran | Bentuk |
|---|---|---|
| Tray alat di layar craft | Wide Spray, Power Buffer, Magic Wipe, Golden Tools | Ikon gembok kecil. Tap → kartu info + tombol beli |
| Tray pola | Pola premium (💎) | Kartu dengan ikon 💎 |
| Layar reward pesanan | 2x Cash | Teks kecil "Earn 2x with 2x Cash", tidak menutupi tombol lanjut |
| Layar level-up | 2x XP, Starter Pack (L3) | Satu kartu tawaran, tombol tutup jelas |
| Display Rack | Bigger Gallery Rack, Night Shift | Slot terkunci, ikon bulan saat Tip Jar penuh |
| Bench saat craft | Instant Finish | Tombol ⚡ kecil di pojok, selalu menampilkan harga 💎 |
| App **Store** di HP | Semua produk | Tab: Gems, Passes, Boosts, Premium Decor |
| Toko pemain lain | Dekor premium & VIP yang terlihat | Tidak ada popup. Pemain melihat sendiri ("ingin seperti itu") |

**Batas popup:** maksimal 1 tawaran otomatis per sesi (Starter Pack di L3, atau tawaran 2x XP di level-up), sisanya hanya muncul saat pemain menyentuh item terkunci.

---

## 7. Kepatuhan & usia
- **Pemain di bawah 13 tahun** (±35% pengguna): tidak ada mekanik yang menekan pembelian dengan timer palsu atau FOMO berlebihan.
- **Rewarded video** Roblox hanya untuk 13+ dan pendapatannya kecil [SRC Analisis S18]. **Tidak dipakai di V1.** Dipertimbangkan di V1.1 untuk "Double Tip Jar".
- **ProcessReceipt** harus idempoten. Lihat [14](14_Teknis_Programmer.md#13-monetisasi--processreceipt).
- Semua harga ditampilkan dengan ikon Robux/Gems yang jelas sebelum konfirmasi.

---

## 8. Skenario pendapatan [ASUMSI]

Angka ini hanya patokan perencanaan, belum ada data. Harus diganti dengan data soft launch.

| Asumsi | Nilai |
|---|---|
| Konversi payer (30 hari) | 1,5% |
| Belanja rata-rata payer | 450 R$ |
| DevEx | $0,0038 / R$ [SRC Analisis S17] |

| DAU rata-rata | Payer / bulan | R$ / bulan | Perkiraan DevEx / bulan |
|---|---|---|---|
| 2.000 | ±900 | ±405.000 | ±$1.540 |
| 10.000 | ±4.500 | ±2.025.000 | ±$7.700 |
| 50.000 | ±22.500 | ±10.125.000 | ±$38.500 |

(Payer/bulan = MAU × 1,5%, dengan asumsi kasar MAU ≈ 30 × DAU karena banyak pemain Roblox hanya mencoba sekali. Anggap sebagai urutan besaran, bukan prediksi.)
