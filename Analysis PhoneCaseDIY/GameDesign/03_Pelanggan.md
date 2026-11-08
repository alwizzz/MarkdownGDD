# 03. Tipe Pelanggan

[← Kembali ke indeks](00_README.md)

Sumber: `enum CustomerType` [KODE], `level_rewards.csv`, `vip_customer.csv`, `ReturningClients.csv`, `couple_phone_requests.csv` [DATA].

## Ringkasan

| Tipe | Status | Frekuensi | Skor leaderboard |
|---|---|---|---|
| Normal | Aktif | Default | 200 |
| VIP | Aktif | Tiap 3 pelanggan mulai Day 2 | 400 |
| Revenge | Aktif | Menggantikan slot VIP (dengan syarat) | 200 |
| Auction | Aktif | Setelah level VIP | 200 |
| Returning (Cleaning) | Aktif | 13 kejadian, Day 2–15 | 100 |
| Couple | Aktif | 8 pesanan | — |
| Headphone/AirPods upsell | Aktif | Setelah case selesai | — |
| Boss / "Picky Boss" | **Mati** | — | — |
| Unhappy customer | **Mati** | — | — |

## Normal
Pesanan biasa. Reward mengikuti tabel `level_rewards.csv` (lihat [05_Ekonomi.md](05_Ekonomi.md#a-reward-level)).

## VIP
- Muncul **tiap 3 pelanggan** mulai Day 2 (`vip_interval=3`, `first_appear_day=2`).
- Reward VIP **menggantikan** reward bintang dengan koin tetap per hari: **200 + 30 × (day − 2)**, jadi Day 25 = 890.
- RV "Claim" mengalikan **×4** (`magnification`) [KODE ✔]. Ini momen RV paling bernilai di game.
- Ada 8–10 emoji yang bisa di-tap, masing-masing memberi 10–30 koin acak.
- Melayani VIP **membuka VIP item** (`unlock_vip_order` 1…54). Lihat [05_Ekonomi.md](05_Ekonomi.md#jalur-unlock-konten).
- Mulai level VIP lewat RV (`VipStart`), bisa di-skip.
- Total 30 VIP di Day 1–25.

## Revenge
- **Menggantikan slot VIP** jika level itu bukan auction / couple / cleaning / weekly dan revenge belum selesai [KODE ✔ `LevelRevengeEnable`].
- Ada 4 pelanggan jahat, contoh dialog: "I STOLE THIS PHONE…", "MAKE ME A CASE, BUT I'M NOT PAYING!".
- Bahan jahil:
  - poop spray & pepper spray → RV "TRY IT"
  - poison glue & poison soap → popup RV, menolak = interstitial
- Warna cat otomatis menjadi permintaan wajib.

## Auction
- Muncul **setelah menyelesaikan level VIP** (bisa di-skip).
- **4 penawar.** Tawaran tiap penawar = `acak(1.0–3.0) × reward 3★ slot itu`, dan semua tawaran dibuat berbeda [KODE ✔].
- RV "Best Offer" = langsung ambil tawaran tertinggi.
- RV "Coins Multiplier" = tawaran yang diterima ×2.
- Ada 25 kata pujian (AMAZING … WONDROUS) untuk efek.

## Returning Client (Cleaning)
- 13 kejadian Day 2–15 (`ReturningClients.csv`).
- Mode: bersihkan **case kotor** atau **charging port**.
- Cerita singkat, contoh: "HP jatuh di lumpur", "ketemu di mangkuk makan anjing".
- Berfungsi sebagai level "istirahat" yang pendek.

## Couple
- 8 pesanan pasangan (`couple_phone_requests.csv`).
- Membuat **2 case serasi**, masing-masing dengan kombinasi 1–3 maker yang ditentukan.

## Headphone / AirPods upsell
- Setelah case selesai pelanggan bertanya "CAN YOU DO MY HEADPHONES CASE TOO?".
- Masuk ke level bonus Earbuds / Headphones. Unlock AirPods memakai RV.

## Fitur yang dimatikan
| Fitur | Bukti |
|---|---|
| Boss / "Picky Boss" | Kode dan teks ada, tapi tidak ada baris Boss di tabel [KODE ✔] |
| Unhappy customer | `isUnhappy` selalu `false` [KODE ✔] |
