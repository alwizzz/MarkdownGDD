# 01. Core Loop

[← Kembali ke indeks](00_README.md)

## Genre & Fantasi
- **Genre:** hybrid-casual "DIY / satisfying craft" ditambah simulasi toko.
- **Fantasi pemain:** "Aku punya bengkel custom phone case. Pelanggan datang, aku membuat case sesuai pesanan, dibayar koin, lalu aku mempercantik studio."
- **Fokus pengalaman:** ekspresi diri dan rasa *satisfying*, bukan tantangan. Tidak ada kondisi gagal (lihat [04_LevelDesign_Pacing.md](04_LevelDesign_Pacing.md)).

## Core Loop (1 level = 1 pelanggan)

```
Pelanggan datang (Normal / VIP / Returning / Couple / Revenge / Auction)
  → pilih bentuk HP (phone shape)
  → pilih MAKER (teknik membuat case: Spray, Acrylic, Stencil, Marble, ...)
  → jalankan langkah mini-game (glue → paint → dry → ...)
  → dekorasi (stiker 2D, stiker 3D, glitter, keychain, strap)
  → hasil dinilai 1–3 bintang
  → dapat koin (+ RV ×2) dan peluang 70% dapat kunci chest
  → kemungkinan upsell: "CAN YOU DO MY HEADPHONES CASE TOO?" → level bonus
```

| Tahap | Detail | Dokumen |
|---|---|---|
| Pelanggan | 6 tipe aktif, masing-masing punya aturan sendiri | [03_Pelanggan.md](03_Pelanggan.md) |
| Maker & langkah | 9 maker, masing-masing berisi beberapa mini-game | [02_Mekanik_Maker.md](02_Mekanik_Maker.md) |
| Penilaian | Rumus bintang deterministik, tanpa unsur acak | [04_LevelDesign_Pacing.md](04_LevelDesign_Pacing.md#penilaian-bintang) |
| Reward | Koin linear per pelanggan, pengali RV | [05_Ekonomi.md](05_Ekonomi.md) |

## Meta Loop

```
Hari (Day) → setiap hari ada 1–6 pelanggan
  → naik hari membuka maker, bentuk HP, stiker, dan kategori studio baru
  → koin dipakai untuk dekor studio dan skin alat
  → skor aksi menaikkan rank leaderboard (bot) → hadiah spin premium
  → daily mission, login harian, idle income, dan timer bundle membuat pemain kembali
```

| Sistem meta | Dokumen |
|---|---|
| Studio (dekor toko), skin alat | [05_Ekonomi.md](05_Ekonomi.md), [06_Gacha.md](06_Gacha.md) |
| Leaderboard, daily mission, login, idle | [09_Retensi_Sosial.md](09_Retensi_Sosial.md) |
| Thematic bundle (timer) | [08_LiveOps_AB.md](08_LiveOps_AB.md) |

## Durasi konten
- **25 hari terdesain** (120 pelanggan). Setelah Day 25, tabel dikunci di Day 25 dan 6 pelanggan terakhir diputar ulang. Reward tidak naik lagi.
- Variasi setelah onboarding datang dari bentuk HP baru, stiker baru, VIP item, dan mode spesial (Revenge, Auction, Couple, Cleaning).
