# 09. Retensi & Sosial

[← Kembali ke indeks](00_README.md)

## Ringkasan alasan pemain kembali

| Sistem | Pemicu kembali |
|---|---|
| [Leaderboard bot](#leaderboard-bot) | Naik rank, spin premium tiap 10 rank |
| [Daily Mission](#daily-mission) | Misi baru setiap hari |
| [Daily Login](#daily-login) | Hadiah naik sampai hari ke-7 / 30 |
| [Idle Income](#idle-income) | Koin terkumpul saat offline (cap 5 jam) |
| Spin wheel gratis | Tiap 6 jam (lihat [06_Gacha.md](06_Gacha.md#spin-wheel)) |
| Thematic bundle | Timer 2–10 menit (lihat [08_LiveOps_AB.md](08_LiveOps_AB.md#thematic-bundle)) |
| Weekly event | `WeeklyStartPopup` |
| Push notification | — |
| Photo Album | Semua case tersimpan dan bisa di-share (viral loop) |

## Leaderboard Bot
[KODE ✔ `LeaderBoardData.Init`]

- Berisi **499 NPC** dengan skor tetap: `(500 − rank) × 50`. Rank 1 = 24.950.
- Pemain mulai di **rank 500** dan **naik 1 rank per 50 poin**.
- Skor bot tidak pernah bertambah, dan tidak ditemukan reset mingguan.
- Jadi ini sebenarnya **progress bar yang dibungkus sebagai kompetisi**.
- Nama bot diambil dari `leaderboard_names.csv` (154 nama). Ada 4 varian `LeaderboardSO` (50 avatar/bendera).
- **Hadiah:** setiap 10 rank (490, 480, …) pemain mendapat **spin wheel Premium gratis**.

### Skor per aksi
[DATA `leaderboard_scores.csv`]

| Aksi | Skor |
|---|---|
| Complete VIP level | 400 |
| Complete regular / Revenge / Auction | 200 |
| Choose Glitter / Marble / Injection maker | 200 |
| Choose Pop-It / Stencil maker | 150 |
| Complete Cleaning, Collect key, Place keychain | 100 |
| Upgrade studio (interior / wall / floor) | 80 |
| Choose Spray / Acrylic | 50 |
| Unlock skin | 50 |
| Place sticker / 3D decoration | 20 |

Skor maker lanjutan dibuat lebih tinggi supaya pemain mencoba maker baru, karena maker baru adalah konten yang mahal dibuat.

## Daily Mission
- 27 misi di `DailyMissionData`, dengan grup reward.
- Hadiah 50–150 koin.
- Contoh: "Create 3 Spray cases" (120), "Upgrade your floor once" (50), "Play boxes mini game 2 times" (150).

## Daily Login
- **7 hari:** 250, 500, 750, 1.000, 1.250, 1.500, 1.750 (total 7.000 per siklus) [DATA `DailyLogin.csv`].
- **30 hari** (`ThrityDaySign`, iOS): item eksklusif di hari 1/2/4/5/7/9 (`daily_bonus_order` di `Goods.csv`).
- Ada RV di daily sign.

## Idle Income
Rumus dan booster ada di [05_Ekonomi.md](05_Ekonomi.md). Untuk retensi, poin pentingnya:
- Cap offline **5 jam** mendorong pemain membuka game beberapa kali sehari.
- Worker bersifat sementara dan didapat lewat RV, jadi pemain perlu memperbaruinya.
