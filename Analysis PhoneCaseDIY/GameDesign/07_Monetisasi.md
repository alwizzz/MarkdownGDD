# 07. Monetisasi

[← Kembali ke indeks](00_README.md)

**Model bisnis:** ad-first (hybrid-casual). Semua produk IAP non-consumable, dan **tidak ada mata uang premium**. IAP hanya untuk menghapus iklan atau membuka konten.

## IAP
[DATA `StoreItemConfig`], harga USD default:

| Produk | Harga | Hapus iklan? |
|---|---|---|
| noads | $4,99 | ✔ |
| noadstwo | $3,99 | ✔ |
| keychains (beli semua keychain) | $1,99 | |
| premiumdesigns | $1,99 | |
| fullgame | $1,99 | |
| geteverything | $4,99 | ✔ |
| specialoffer | $5,99 | ✔ |
| premiumpack | $7,99 | ✔ |
| allincludedbundle | $12,99 | ✔ |
| unlockmakers / bundle | harga dari store | |

Booster idle permanen dan thematic bundle juga bisa dibeli lewat IAP (lihat [05_Ekonomi.md](05_Ekonomi.md), [08_LiveOps_AB.md](08_LiveOps_AB.md#thematic-bundle)).

## Interstitial
[KODE ✔]

- Ada **sekitar 75 titik pemanggilan** di kode.
- Hampir **setiap transisi langkah maker** memanggil interstitial:
  - setelah glue, paint, dry, acrylic
  - ganti stencil
  - ganti tab dekorasi (×6)
  - injection, pop-it, string pull, crossbody
- Titik lain: akhir level, masuk mode Cleaning, keluar leaderboard, menerima tawaran auction, menolak RV revenge, "No thanks" di layar hasil.
- **Client tidak membatasi frekuensi** (tidak ada cek level / hari / cooldown). Syaratnya hanya: belum beli NoAds dan iklan sudah siap.
- Jadi **frekuensi sebenarnya diatur SDK CrazyLabs dari server**. Game sengaja menyediakan banyak "slot" iklan, dan server yang memutuskan slot mana yang dipakai.
- Iklan akhir level dilewati jika popup Rate Us akan muncul.
- Ada juga **App Open Ads**.

## Rewarded Video (RV)
[KODE ✔]

| Kategori | Titik RV | Nilai |
|---|---|---|
| **Pengali reward** | Claim di layar hasil | ×2 (normal), **×4 (VIP)** |
| | Auction Best Offer / Coins Multiplier | tawaran tertinggi / ×2 |
| **Koin langsung** | Earn Coins / panel Skin | 500 + 25×(day−1) |
| | Extra coins, Mystery Box, float | — |
| **Akses konten** | Mulai level VIP | — |
| | Unlock AirPods | — |
| | "TRY ONCE" item terkunci | — |
| | Item studio `price_rv` (33 item) | 1 RV per item |
| | Klaim item bundle | 1 RV untuk 2 item |
| | Repair / break screen | — |
| **Gacha** | Reroll / reshuffle skin | pengganti 500 koin |
| | Spin wheel | di luar jatah gratis 6 jam |
| | +3 kunci chest | — |
| **Lainnya** | Daily sign | — |
| | Worker & booster idle | — |
| | Bahan Revenge (poop/pepper spray, poison glue/soap) | — |

**Video ticket**: ada di kode tetapi hanya ditampilkan, tidak pernah didapat atau dipakai (fitur sisa).

## Antrean Popup di Home
Urutan prioritas popup:

```
GetEverything → SpecialOrder → No Ads (± tiap 4 level selesai) → Daily
  → Leaderboard → Auction → Weekly → DailyMission → Bundle
  → StudioCategoryUnlock → RateUs
```

- Popup "Get Everything" dan `RvOfferPopup` **dimatikan** di build ini.
- **Rate Us** memberi hadiah gratis setelah rating.

## Catatan untuk tim
- Pengali RV berbeda per konteks (×2 normal, ×4 VIP) membuat iklan paling "worth it" di momen spesial.
- Item RV diselipkan di antara item koin di toko studio, sehingga iklan terasa sebagai jalan pintas yang wajar.
- Hook interstitial di setiap transisi + pacing dari server lebih fleksibel untuk A/B daripada cooldown yang di-hardcode.
