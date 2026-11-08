# 08. Ekonomi

[← Kembali ke indeks](00_README.md)

Prinsip yang diambil dari game sumber [SRC 05]:
- **Reward linear, mudah di-tuning.** Semua angka di tabel config, bukan di kode.
- **Sink dihitung terhadap faucet.** Di game sumber, total harga studio ±77% dari pendapatan 25 hari.
- **Tanpa kondisi gagal.** Pesanan yang selesai selalu dibayar gaji dasar. Bonus hanya menambah.

Perbedaan utama: game sumber memakai iklan sebagai jalan pintas. Di sini jalan pintasnya adalah **Gems** dan **Gamepass**, dan pemain gratis tetap bisa mencapai L10 dengan nyaman (±2,4 jam).

Semua angka [SIM] berasal dari [tools/economy_sim.py](tools/economy_sim.py).

---

## 1. Mata uang & resource

| Resource | Jenis | Didapat dari | Dipakai untuk |
|---|---|---|---|
| **Cash** 💵 | Soft currency | Pesanan, karyawan, AFK, login, quest | Tycoon, dekor Basic/Cute, upgrade karyawan |
| **XP** | Progres | Pesanan (pemain 100%, karyawan 25%) | Naik level |
| **Gems** 💎 | Premium (bisa didapat gratis dalam jumlah kecil) | Level-up, login hari ke-3/7, Best Case of the Week, codes, **dibeli dengan Robux** | Dekor & bahan premium, Instant Finish, Rush Staff, boost [DRAFT: "gems"] |
| **Likes** ❤ | Skor sosial | Pemain lain menyukai case/toko kita | Peringkat Best Case of the Week, badge |
| **Prestige Stars** ⭐ | Kosmetik | XP setelah L10 (1 bintang per 1.500 XP) | Bintang di papan nama toko (sementara sampai L11+ rilis) |

---

## 2. Rumus bayaran pesanan

Pesanan **langsung dibayar saat case selesai**. Tidak ada DELIVER ke kasir. Bayaran terdiri dari tiga bagian:

| Bagian | Syarat | Nilai |
|---|---|---|
| **Gaji dasar** | Pesanan selesai | 100% |
| **Bonus kesesuaian** | Semua request pelanggan terpenuhi | +25% gaji dasar |
| **Bonus kecepatan** | Selesai ≤ waktu target ([04](04_Mekanik_HandsOn.md#waktu-target)) | +20% gaji dasar |

```
gaji_dasar = round((gaji_device + Σ gaji_langkah) × pengali_cash_pelanggan)
bayaran    = gaji_dasar
           + (semua request terpenuhi ? round(gaji_dasar × 0,25) : 0)
           + (waktu_kerja ≤ waktu_target ? round(gaji_dasar × 0,20) : 0)
cash_akhir = round(bayaran × (1 + bonus_sosial) × pengali_boost)
xp         = round((6 + 5 × jumlah_langkah_utama) × pengali_xp_pelanggan × pengali_xp_pass)
```
- Bayaran maksimal = **1,45 × gaji dasar**.
- **XP tidak terpengaruh bonus.** Setiap pesanan selesai memberi XP penuh, supaya kecepatan naik level tetap stabil dan bisa diprediksi.
- `jumlah_langkah_utama` tidak menghitung sub-step Glossy.
- Bonus Offer Rich Kid mengalikan `bayaran` sebelum bonus sosial.
- `round` = pembulatan setengah ke atas (`math.round` di Luau).

### Nilai komponen
| Device | Gaji dasar | | Langkah | Gaji dasar |
|---|---|---|---|---|
| Aphone 18 Pro Max | 14 | | Case Shape | 4 |
| Samsam X26 Ultra | 18 | | Base Painting | 6 |
| Earpod | 10 | | Smoothing | 4 |
| Tablet | 28 | | Top Pattern | 8 |
| Macbook | 38 | | Sticker | 8 |
| | | | Glossy (sub-step) | 10 |
| | | | Screen Cleaning | 3 |

Nilai ini disetel supaya **bayaran penuh (×1,45) setara dengan harga 3★ di draft GDD sebelumnya**, sehingga kurva ekonomi tidak berubah.

| Pelanggan | Pengali cash | Pengali XP |
|---|---|---|
| Normal | 1,0 | 1,0 |
| Fancy Girl/Boy | 1,5 | 1,3 |
| Thief | 1,2 (tertangkap) / 0,5 (lolos) | 1,2 |
| Old Club | 1,3 per case (2 case) | 1,6 |
| Rich Kid | 2,0 × Bonus Offer (1,0–1,6, +25% jika haggle berhasil) | 1,5 |

### Contoh hitungan
| Pesanan | Gaji dasar | + Sesuai 25% | + Cepat 20% | Bayaran | XP |
|---|---|---|---|---|---|
| L1, Normal, Aphone, 4 langkah | 14+4+6+4+3 = **31** | 8 | 6 | **45** | 6+20 = **26** |
| L4, Fancy, Samsam, 6 langkah | (18+4+6+4+8+8+3) × 1,5 = 76,5 → **77** | 19 | 15 | **111** | (6+30) × 1,3 = **47** |
| Sama, tapi terlambat | 77 | 19 | — | **96** | 47 |
| Sama, warna salah & terlambat | 77 | — | — | **77** | 47 |
| L9, Rich Kid, Macbook, 6 langkah + Glossy, tip ×1,3 | (38+4+6+4+8+8+10+3) × 2,0 = **162** | 41 | 32 | 235 × 1,3 = **306** | (6+30) × 1,5 = **54** |

---

## 3. Hasil simulasi per level [SIM]

Asumsi rata-rata pemain: **90% pesanan sesuai request**, **70% pesanan dapat bonus kecepatan** (pengali rata-rata 1,365 × gaji dasar). Bobot pelanggan & device dari [06](06_Pelanggan_Device.md#3-pembuatan-request-order-generator).

| Lv | Cash/pesanan | XP/pesanan | Detik/pesanan | Cash/menit | XP/menit |
|---|---|---|---|---|---|
| 1 | 42 | 26 | 62 | 41 | 25,2 |
| 2 | 50 | 29,5 | 72 | 42 | 24,7 |
| 3 | 59 | 31,7 | 72 | 49 | 26,5 |
| 4 | 66 | 34,9 | 83 | 48 | 25,4 |
| 5 | 66 | 35,9 | 79 | 50 | 27,4 |
| 6 | 73 | 35,9 | 80 | 54 | 26,9 |
| 7 | 92 | 38,4 | 87 | 64 | 26,6 |
| 8 | 92 | 38,4 | 87 | 64 | 26,6 |
| 9 | 101 | 39,4 | 92 | 66 | 25,6 |
| 10 | 101 | 39,4 | 92 | 66 | 25,6 |

Detik/pesanan lebih cepat dari draft awal karena (1) tidak ada DELIVER ke kasir, (2) semua langkah dikerjakan di satu Craft Bench, dan (3) Case Shape cukup memilih dari list HUD (±4 detik). Karyawan menambah cash: per karyawan ±0,8 pesanan/menit × 60% cash pada Speed Lv1.

### Timeline pemain gratis, solo, tanpa bonus sosial
| Menit | Kejadian | Cash saat itu |
|---|---|---|
| 2,1 | **L2** | 85 |
| 3,3 | Beli Pattern Shelf (120) | |
| 4,5 | Beli Stool (60) | |
| 6,9 | **L3** | 104 |
| 12,8 | Beli Employee #1 (350) | |
| 15,2 | **L4** | 232 |
| 20,7 | Beli Sticker Stock (600) | |
| 22,1 | Beli Table (180) | |
| 26,2 | **L5** | 330 |
| 27,6 | Beli Sofa (400) | |
| 40,7 | **L6** | 1.117 |
| 46,0 | Beli Glossy Finish Paint Shelf (1.500) | |
| 48,7 | Beli Plant Pot (300) | |
| 60,7 | **L7** | 1.103 |
| 72,3 | Beli Employee #2 (2.200) | |
| 73,7 | Beli Trash Bin (250) | |
| 83,8 | **L8** | 1.642 |
| 93,9 | Beli Waiting Room Expand (3.000) | |
| 99,7 | Beli Statue (900) | |
| 109,8 | **L9** | 1.676 |
| 142,0 | **L10** | 6.906 → langsung cukup untuk Employee #3 (6.500) |

**Bacaan:** setiap item tycoon bisa dibeli 1–12 menit setelah level yang membukanya. Tidak ada "tembok" cash yang memaksa grinding. Sisa cash di L9 (±1.700) dirancang untuk upgrade skill karyawan (tidak dihitung di simulasi).

**Sensitivitas bonus:** pemain yang tidak pernah mendapat bonus apa pun memperoleh ±27% lebih sedikit cash (1,0 vs 1,365) tetapi naik level dengan kecepatan yang sama, karena XP tidak bergantung bonus. Pemain yang selalu sempurna memperoleh ±6% lebih banyak (1,45 vs 1,365).

---

## 4. AFK income (Display Rack)

```
nilai_case       = (gaji_device + Σ gaji_langkah yang ada di case) × 1,45   (pelanggan Normal, bayaran penuh)
income_per_menit = Σ (nilai_case × 0,02)  untuk semua case di rak
tip_jar_cap      = income_per_menit × 180 menit   (480 menit dengan gamepass Night Shift)
```

| Lv | Nilai case terbaik | AFK penuh 3 jam, 4 slot [SIM] | Setara main aktif |
|---|---|---|---|
| 1 | 45 | 647 | ±16 menit |
| 4 | 74 | 1.065 | ±22 menit |
| 6 | 88 | 1.274 | ±24 menit |
| 7 | 103 | 1.482 | ±23 menit |
| 9–10 | 117 | 1.691 | ±26 menit |

AFK 3 jam bernilai ±16–26 menit main aktif. Cukup terasa sebagai hadiah kembali, tidak cukup untuk menggantikan bermain [USULAN]. Game sumber memakai cap 5 jam [SRC 05]. Cap 3 jam mendorong 2–3 sesi per hari.

---

## 5. Bonus cash

Diadaptasi dari Fix My Phone (+10%/teman maks 4, +10% grup, +20% Roblox Plus) [FMP], dengan angka diturunkan sedikit supaya tidak merusak kurva [USULAN].

| Bonus | Nilai |
|---|---|
| Per teman Roblox di server yang sama | +10% (maks 3 teman = +30%) |
| Join grup Roblox studio | +10% |
| Langganan Roblox Premium/Plus | +10% |
| **Total bonus sosial maks** | **+50%** |

```
pengali_boost = 1 + (punya gamepass 2x Cash ? 1 : 0) + (boost 2x Cash aktif ? 1 : 0)      → maks ×3
cash_akhir    = bayaran × (1 + bonus_sosial) × pengali_boost                          → maks ×4,5
```
Bonus berlaku untuk cash pesanan pemain dan karyawan. **Tidak berlaku** untuk AFK income (supaya AFK tetap bisa diprediksi).

---

## 6. Faucet lain

### Daily Login (siklus 7 hari) [USULAN]
| Hari | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| Hadiah | 100 💵 | 150 💵 | 5 💎 | 250 💵 | 300 💵 | 400 💵 | 15 💎 + stiker eksklusif mingguan |

Cash login dikali `(1 + 0,15 × (level − 1))` supaya tetap berarti di level tinggi.

### Daily Quest [USULAN]
3 quest per hari, diambil dari pool 15. Contoh:

| Quest | Hadiah |
|---|---|
| Craft 5 cases | 15 menit income |
| Get 3★ from a Fancy customer | 15 menit income |
| Use Glitter 3 times | 10 menit income |
| Like 3 cases in the Gallery | 3 💎 |
| Visit a friend's shop | 3 💎 |
| Collect your Tip Jar | 10 menit income |

"N menit income" = `N × cash_per_menit_pemain_di_level_itu` (tabel bagian 3). Selesaikan ketiganya = bonus 5 💎.

### Gems gratis per minggu (perkiraan pemain aktif)
| Sumber | 💎 |
|---|---|
| Level-up L2–L10 (sekali) | 65 total |
| Login (hari 3 + 7) | 20 |
| Daily quest (sosial + bonus 3/3) | ±50 |
| Best Case of the Week (ikut submit) | 5 |
| Codes saat rilis | ±25 |
| **Minggu pertama** | **±165 💎** |

Cukup untuk 1–2 dekor premium atau 1 pola premium. Ini memperkenalkan nilai Gems tanpa menghilangkan alasan membeli.

---

## 7. Sink

| Sink | Total sampai L10 (cash) | Catatan |
|---|---|---|
| Tycoon (7 item) | 14.270 | 120 + 350 + 600 + 1.500 + 2.200 + 3.000 + 6.500 |
| Dekor objek varian Basic | 4.090 | 7 objek |
| Dekor objek varian Cute | 7.340 | Opsional |
| Permukaan & peralatan (cat, lantai, meja, dinding, kasir, papan nama) | ±6.000 | Opsional |
| Skill karyawan (×3 karyawan) | 6.600 | 300 + 700 + 1.200 per karyawan |
| Speed karyawan Lv2–5 (×3) | 12.750 | 4.250 per karyawan |
| Quality karyawan Lv2–5 (×3) | 14.700 | 4.900 per karyawan |
| **Total sink cash V1** | **±65.750** | |

**Faucet sampai L10 ≈ 17.000 cash** [SIM]. Sisa sink ±48.000 cash menjadi tujuan setelah L10. Dengan pemain + 3 karyawan (±210 cash/menit) ini setara **±4 jam** konten tambahan, ditambah Best Case of the Week, sampai update L11+ rilis.

### Sink Gems
| Item | Harga |
|---|---|
| Dekor objek varian Premium | 40–150 💎 |
| Model kasir Gold, papan nama premium | 90 💎 |
| Pola premium (Holo Glitter, Neon Grid) | 60 💎 masing-masing |
| **Instant Finish** (pesanan selesai langsung dengan bonus kesesuaian & kecepatan) | 1 💎 per langkah (4–6 💎) |
| **Rush Staff** (semua karyawan selesai sekarang) | 2 💎 per pesanan yang sedang dikerjakan |
| Boost 2x Cash 15 menit | 25 💎 |

Instant Finish memberi **100% cash dan 50% XP** [USULAN]. Pemain yang membayar mendapat uang lebih cepat, tetapi tidak bisa melewati seluruh konten level hanya dengan Gems.

---

## 8. Aturan tuning
1. Ubah angka di [tools/economy_sim.py](tools/economy_sim.py), jalankan, lalu perbarui tabel di dokumen ini dan [07](07_Level_Design.md).
2. Target yang dijaga:
   - L5 tercapai di 25–35 menit (akhir sesi pertama).
   - L10 tercapai di 2–3 jam untuk pemain gratis solo.
   - Setiap item tycoon terbeli maksimal 15 menit setelah level-nya.
3. Setelah soft launch, bandingkan dengan data nyata: median menit ke tiap level, cash saat level-up, dan % pemain yang membeli tiap item (lihat [16](16_Roadmap_KPI_Risiko.md#4-analytics)).
