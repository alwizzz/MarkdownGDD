# 08. LiveOps & A/B Testing

[← Kembali ke indeks](00_README.md)

## Thematic Bundle
[DATA `Bundles.csv`, `Bundle_Items.csv`] [KODE ✔ `BundleService`]

| Bundle | Timer siklus | Harga koin skip / siklus | Isi (3 siklus × 2 item) |
|---|---|---|---|
| Cat | 2 menit | 500 | case, spray, stiker 2D ×2, 3D, charm |
| Anime | 5 menit | 600 | case, spray, 2D, 3D, charm, strap |
| Robot | 5 menit | 700 | case, spray, 2D, 3D, charm, strap |
| Cloud | 10 menit | 800 | case, 2D, 3D, glitter, charm, strap |
| Spaceship | 10 menit | 900 | case, spray, 3D, glitter, charm, strap |
| Narwhal | 10 menit | 1.000 | case, spray, 2D, 3D, glitter, strap |

### Alur
```
Buka di Day 2
  → timer siklus berjalan
  → timer habis: 2 item berikutnya "bisa diklaim" → klaim dengan 1 RV (untuk kedua item)
  → atau bayar 500–1.000 koin untuk melewati timer
  → atau beli seluruh bundle lewat IAP
  → 3 siklus selesai → pindah ke bundle berikutnya
```

- `coins_per_cycle` adalah **harga skip**, bukan hadiah.
- Ada RV per kategori item (`bundle_case_rv`, `bundle_glitter_rv`, …).
- Flag `bundle_timer_reset_on_relaunch=1`: timer di-reset saat app dibuka ulang (bisa diatur dari remote).
- Fungsi desain: timer membuat pemain kembali lagi (sesi berulang).

## Weekly Event
`WeeklyStartPopup` dan keychain `weeklyEvent` [KODE]. Detail isi event tidak ada di tabel.

## A/B Testing
Game ini dibangun sebagai **mesin A/B test**.

| Mekanisme | Isi |
|---|---|
| `UiVariants.csv` | 89 prefab UI yang bisa ditukar (`_V2`, `ResultPanel_V430`, `phoneOrder_440`, …) |
| `RuntimeBehaviorVariants.csv` | 23 flag perilaku |
| Unlock day iOS vs GP | Pacing berbeda antar platform |
| `LeaderboardSO_V470_*` | 4 varian konten leaderboard |
| `Features.csv` | Fitur on/off |

### Contoh flag perilaku
- `all_decoration_tools_unlocked_early`
- `makers_day_lock_removed`
- `phone_selection_available_from_first_day`
- `break_screen_rewarded_unlock`
- `between_level_flow_rework`

### Perbedaan pacing iOS vs Google Play

| Maker | iOS | GP |
|---|---|---|
| Acrylic | Day 4 | Day 2 |
| Stencil | Day 2 | Day 4 |
| Marble | Day 7 | Day 5 |

## Remote Config
[KODE ✔ `CrazyLabs DatabaseController`]

- Game **tidak** membaca key remote satu per satu.
- **Seluruh file CSV bisa diganti dari server** (`fileConfig_*`), atau hanya sel tertentu.
- Artinya semua angka di dokumentasi ini (reward, harga, hari unlock, drop rate) adalah *default* yang bisa di-A/B tanpa update app.

### Flag lama yang di-hardcode di `GameSettingPrefs`

| Flag | Nilai |
|---|---|
| Revenge | ON, menggantikan VIP |
| Auction | ON, bisa di-skip |
| IAP NoAds | ON |
| RV-unlock-offers | OFF |

## Catatan untuk tim
- Simpan semua angka desain di tabel (CSV / spreadsheet), bukan di kode.
- Siapkan pipeline untuk mengganti tabel dari server. Ini memungkinkan desainer men-tuning pacing dan ekonomi tanpa rilis ulang.
