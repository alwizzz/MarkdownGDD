# 05. Ekonomi

[← Kembali ke indeks](00_README.md)

Game ini **tidak punya mata uang premium**. Ekonomi berputar pada koin (soft currency), dan RV menjadi jalan pintas utama. Sistem acak (gacha, spin, chest) dibahas terpisah di [06_Gacha.md](06_Gacha.md).

## Mata Uang & Resource

| Resource | Sumber | Dipakai untuk |
|---|---|---|
| **Coin** (soft) | Reward level, VIP, misi, login, chest, idle income, RV | Dekor studio, roll skin alat, skip timer bundle |
| **Key** | Drop **70%** per level (`keychain_settings: key_drop_chance_percent=70`) | Buka keychain chest |
| **Spin Wheel Ticket** | Event / hadiah | Spin wheel (`wheelType: free / ticket / rv`) |
| **Video Ticket** | [KODE `RVPlayerManager.videoTicketCount`] | Pengganti menonton RV. Hanya ditampilkan, tidak pernah didapat atau dipakai (fitur sisa). |
| **Leaderboard Score** | Aksi dalam game | Naik rank (50 poin = 1 rank) |
| **Uang asli (IAP)** | — | No Ads, pack, unlock (lihat [07_Monetisasi.md](07_Monetisasi.md)) |

## Faucet (sumber koin)

### a. Reward level
Linear per pelanggan, dengan n = urutan pelanggan global 1…120 [DATA `level_rewards.csv`].

| Bintang | Rumus | Pelanggan ke-1 | Pelanggan ke-120 |
|---|---|---|---|
| 1★ | `75 + 2(n−1)` | 75 | 313 |
| 2★ | `100 + 3(n−1)` | 100 | 457 |
| 3★ | `125 + 4(n−1)` | 125 | **601** |

**Total koin per hari** (3★, tanpa ×2, tanpa VIP):

| Day | 1 | 2 | 4 | 6 | 9 | 14 | 20 | 25 |
|---|---|---|---|---|---|---|---|---|
| Koin 3★ | 125 | 262 | 447 | 700 | 1.125 | 1.962 | 2.826 | 3.546 |

Total Day 1–25: **43.560** (3★) / 23.280 (1★). Dengan RV ×2 bisa mendekati dua kali lipat.

### b. VIP
- `200 + 30 × (day − 2)` per VIP (Day 25 = 890).
- **×4 dengan RV**, ditambah 8–10 emoji × acak 10–30 koin.
- 30 VIP di Day 1–25.

### c. Daily Login
- 7 hari: 250, 500, 750 … 1.750 (total **7.000** per siklus).
- Varian 30 hari (`ThrityDaySign`, iOS) dengan item eksklusif di hari 1/2/4/5/7/9 (`daily_bonus_order`).

### d. Daily Mission
27 misi, hadiah **50–150 koin**. Contoh: "Create 3 Spray cases" 120, "Upgrade your floor once" 50, "Play boxes mini game 2 times" 150.

### e. Keychain Chest
Koin acak 20–440 per tap. Detail di [06_Gacha.md](06_Gacha.md#keychain-chest).

### f. Free coin RV
Di panel Skin dan tombol "Earn Coins" di HUD: `500 + 25 × (day − 1)` per tayangan (Day 25 = 1.100) [DATA `skin_rv_coins.csv`].

### g. Idle Income [KODE ✔]
```
koin = jam × (jumlah_worker × 50 + shop_income) × (DoubleTime ? 2 : 1)
```
- Tabungan offline dibatasi **5 jam** income worker (15 jam dengan booster *Stretch the Limit*).
- Worker didapat **lewat RV** dan bersifat sementara.

| Booster (RV) | Efek |
|---|---|
| DoubleTime | Income ×2 |
| Stretch the Limit | Cap offline 15 jam |
| Design Discount | Dekor studio −30% |

Booster permanen dijual lewat IAP. Durasi booster tidak terbaca dari kode.

### h. Spin Wheel
Hadiah 100–2.000 koin. Detail di [06_Gacha.md](06_Gacha.md#spin-wheel).

### i. Auction
Tawaran 1.0–3.0 × reward 3★. Detail di [03_Pelanggan.md](03_Pelanggan.md#auction).

### j. Extra Coins RV
Tombol RV koin di HUD, toko, dan float (`extra_coins_rv`, `float_skin_rv`, `MysteryBoxRV`).

## Sink (pemakai koin)

### a. Studio (dekor toko)
10 kategori, 125 item [DATA `Decorations_Categories.csv`, `Decorations_Items.csv`].

| Kategori | Buka Day | Jumlah item |
|---|---|---|
| Walls, Floor, Table | 1 | 15 / 15 / 15 |
| Showcase, Chairs | 3 | 10 / 10 |
| Lamp, Sofa | 4 | 15 / 10 |
| Rug | 5 | 15 |
| Plant | 6 | 10 |
| Left Wall Decor | 7 | 10 |

- Komposisi: **35 gratis (default), 57 berbayar koin, 33 RV-only** (1 iklan per item).
- Harga koin 50 → 1.500. **Total semua item koin = 33.400**, sekitar **77%** dari total pendapatan 3★ Day 1–25. Artinya sink disetel supaya studio "hampir penuh" sekitar Day 25.
- Pola harga per kategori: 2–5 item gratis → item koin naik bertahap → item RV diselipkan di antara item koin (urutan `order`). Pemain yang kekurangan koin melihat RV sebagai jalan pintas.
- Upgrade studio (interior/wall/floor) juga memberi skor leaderboard +80.

### b. Skin Alat (gacha roll)
Total 49.500 koin untuk semua skin. Detail di [06_Gacha.md](06_Gacha.md#skin-alat).

### c. Skip timer bundle
500–1.000 koin per siklus. Detail di [08_LiveOps_AB.md](08_LiveOps_AB.md#thematic-bundle).

## Neraca kasar Day 1–25

| | Koin |
|---|---|
| Faucet level 3★ | ~43.560 |
| + VIP, login, misi, chest, RV, idle | (tergantung perilaku pemain) |
| Sink studio | 33.400 |
| Sink skin alat | 49.500 |
| Sink skip bundle | 3 siklus × (500…1.000) per bundle |

Total sink jauh di atas faucet level. **Kekurangan inilah yang mendorong pemain menonton RV.** [DUGAAN]

## Jalur Unlock Konten
`Goods.csv` memisahkan cara membuka setiap item:

| Jalur | Kolom | Contoh |
|---|---|---|
| 1. Progres hari | `unlock_day_gp` / `unlock_day_ios` | Stiker dibuka bertahap Day 1 → 23 |
| 2. Layani VIP | `unlock_vip_order` 1…54 | 21 stiker 2D, 13 stiker 3D, 10 spray, 10 acrylic, 3 glitter. Diberi tag "VIP ITEM". |
| 3. Chest / daily bonus | `daily_bonus_order`, keychain chest | Keychain lewat chest, item eksklusif lewat login 30 hari |
| 4. Bundle | `Bundle_Items.csv` | Lihat [08_LiveOps_AB.md](08_LiveOps_AB.md) |
| 5. RV "TRY ONCE" | — | Coba item terkunci satu kali dengan menonton iklan |
