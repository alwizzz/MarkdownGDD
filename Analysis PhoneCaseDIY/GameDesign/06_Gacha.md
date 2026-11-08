# 06. Gacha & Sistem Acak

[← Kembali ke indeks](00_README.md)

Ada empat sistem acak di game ini. Semuanya **ramah pemain**: tanpa duplikat, ada pity, atau hasil awal di-*rig* ke hadiah bagus.

| Sistem | Bayar dengan | Hadiah | Proteksi |
|---|---|---|---|
| [Skin Alat](#skin-alat) | Koin (500 +200/roll) | Skin kosmetik | Tanpa duplikat |
| [Spin Wheel](#spin-wheel) | Gratis 6 jam / RV / tiket | Koin, stiker, 3D, keychain | Spin premium pertama di-rig |
| [Keychain Chest](#keychain-chest) | Kunci (drop 70%) | Koin acak + keychain | Pity `default_count` |
| [Auction](#auction) | — | Koin 1.0–3.0× | RV "Best Offer" |

---

## Skin Alat
[DATA `skin_items.csv`, `skin_roll_prices.csv`] [KODE ✔ `SkinManager`]

### Isi
- 3 jenis alat: **Table, Glue, Hair Dryer**.
- Masing-masing 12 skin: 6 Common, 3 Rare, 3 Legendary. Total 36 skin.

### Harga
- Tombol "UNLOCK RANDOM": harga awal **500**, naik **+200 per roll** [KODE ✔ `SkinManager.GetCostCoin`].

```
harga_roll(k) = 500 + 200 × k     (k = jumlah roll yang sudah dilakukan untuk alat itu)
```

| Roll ke- | 1 | 2 | 3 | … | 11 |
|---|---|---|---|---|---|
| Harga | 500 | 700 | 900 | … | 2.500 |

- Satu set penuh (11 roll, 1 skin default) = **16.500 koin**. Tiga alat = **49.500 koin**.

### Aturan acak
- **Tanpa duplikat, tanpa bobot rarity.** Skin dipilih *uniform random* dari yang masih terkunci [KODE ✔].
- Label Common / Rare / Legendary **hanya kosmetik**, tidak mempengaruhi peluang.
- Animasi "spin" berputar 4–9 kali sebelum berhenti, murni untuk efek.

### Reshuffle
- Popup "RESHUFFLE CHOICES" (`PopSkinPanel`) memakai shuffle bag tanpa pengulangan.
- Biaya reshuffle: **500 koin atau 1 RV**.

### Fungsi
Kosmetik, ditambah skor leaderboard +50 per skin.

---

## Spin Wheel
[KODE ✔ `SpinWheelBase`]

| | Regular | Premium |
|---|---|---|
| Segmen | 6 | 6 |
| Hadiah | 3D, stiker, 100 / 150 / 250 / 300 koin | keychain, stiker, 3D, 1.000 / 1.500 / 2.000 koin |
| Cara dapat | Gratis tiap **6 jam**, selebihnya RV | IAP atau reward leaderboard (tiap 10 rank) |

- `wheelType`: free / ticket / rv.
- **Spin premium pertama di-*rig*** ke hadiah atas (roll dipaksa 96), supaya kesan pertama bagus.

---

## Keychain Chest
[DATA `keychain_chests.csv`, `keychain_settings.csv`] [KODE ✔]

### Alur
```
Selesaikan level → peluang 70% dapat 1 kunci (hanya jika masih ada keychain terkunci)
  → kunci maksimal 3 → chest terbuka saat kunci penuh
  → 1 tap = 1 kunci → koin acak min_coin–max_coin
  → setelah default_count kali dibuka (pity) → keychain diberikan
```

| Parameter | Nilai |
|---|---|
| Drop kunci per level | 70% |
| Kapasitas kunci | 3 |
| Koin per tap | 20–240 (chest awal) sampai 120–440 (chest akhir) |
| Jumlah chest | 11 (untuk 12 keychain) |
| RV | +3 kunci |
| IAP | "keychains" $1,99 = beli semua keychain |

- Skor leaderboard: collect key 100, place keychain 100.

---

## Auction
Lihat [03_Pelanggan.md](03_Pelanggan.md#auction). Ringkasnya: 4 tawaran acak `1.0–3.0 × reward 3★`, RV Best Offer langsung mengambil tawaran tertinggi, RV Multiplier ×2.

---

## Catatan untuk tim
- Semua sistem acak ini **bisa dibuat deterministik di server** karena konfigurasinya ada di CSV yang bisa diganti remote.
- Harga gacha yang naik linear (+200) membuat sink tidak terbatas tapi terasa adil karena tidak ada duplikat.
