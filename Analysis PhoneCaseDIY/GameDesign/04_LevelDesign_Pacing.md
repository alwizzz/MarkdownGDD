# 04. Level Design & Pacing

[← Kembali ke indeks](00_README.md)

Sumber utama: `level_rewards.csv` [DATA], `MissionManager` [KODE ✔].

## Struktur Hari
- Progres dibagi per **Day**. Day 1–25 ditulis manual, totalnya **120 pelanggan**.
- **Setelah Day 25, tabel dikunci di Day 25** [KODE ✔ `GameSettingPrefs.get_GLDDayIndex = min(day, 25)`]. Setiap hari berikutnya memutar ulang 6 baris Day 25 (reward 3★ 581–601, VIP di slot 4). Endgame tidak lagi menaikkan reward.

### Jumlah pelanggan per hari

| Day | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9–13 | 14–25 |
|---|---|---|---|---|---|---|---|---|---|---|
| Pelanggan | 1 | 2 | 2 | 3 | 3 | 4 | 4 | 4 | 5 | 6 |

### Kolom per pelanggan di `level_rewards.csv`

| Kolom | Fungsi |
|---|---|
| `phone_type_source` | Bentuk HP yang dipakai |
| `prepare_type` | Maker utama (Spray 63×, Acrylic 56×, Marble 1×) |
| `lock_type` | Fitur yang diperkenalkan hari itu |
| `item_require_count` | Jumlah permintaan pelanggan |
| `one/two/three_star_reward` | Reward koin per bintang |
| `customer_type` | Normal / VIP / dll. |
| `vip_emoji_face_min/max` | Jumlah emoji VIP |

## Jadwal Bentuk HP & Fitur Baru

| Day | Bentuk HP baru | Fitur dikenalkan (`lock_type`) |
|---|---|---|
| 1 | Normal | — (tutorial Spray) |
| 2 | Bunny | Chain (keychain / rantai) |
| 3 | — | Acrylic |
| 4 | — | Decoration (stiker) |
| 5 | Among-us-like | Glitter |
| 6 | — | Marble (1× paksa) |
| 8 | Unicorn | |
| 11 | Pineapple | |
| 15 | Cola | |
| 20 | "StarBucks" | |
| 23 | Foot | |
| 25 | Cactus | |

## Kurva Onboarding (FTUE)

| Day | Pelanggan | Hal baru |
|---|---|---|
| 1 | 1 | Spray, HP Normal. Tanpa pilihan supaya pemain langsung paham. |
| 2 | 2 | VIP pertama, keychain, HP Bunny, Bundle, pelanggan Cleaning pertama, Acrylic terbuka (GP) |
| 3 | 2 | Pesanan Acrylic pertama, Pop-It, kategori studio Showcase & Chairs |
| 4 | 3 | Stencil, Decoration (stiker), Lamp & Sofa |
| 5 | 3 | Glitter, Marble, Rug |
| 6 | 4 | Injection, Liquid Glitter, Plant |
| 7 | 4 | Left Wall Decor (kategori studio terakhir) |
| 8–25 | 4→6 | Bentuk HP baru kira-kira tiap 3–5 hari, stiker baru tiap 2–3 hari |

**Pola:** sampai Day 7 hampir **setiap hari membuka sesuatu** (maker atau kategori studio). Setelah itu kebaruan datang dari bentuk HP baru, stiker baru, VIP item, dan mode spesial (lihat [03_Pelanggan.md](03_Pelanggan.md)).

## Ritme dalam Satu Hari
- VIP tiap 3 pelanggan, jadi hampir setiap hari ada 1–2 momen "spesial".
- `prepare_type` diselang-seling Spray / Acrylic supaya maker berganti terus.
- Returning / Cleaning disisipkan sebagai level "istirahat" yang pendek (skor leaderboard 100, bukan 200).

## Penilaian Bintang
[KODE ✔ `MissionManager.GetStarNum`]

```
bintang = (Day <= 3 ? 2 : 1)
        + (semua permintaan terpenuhi ? 1 : 0)
        + (ada dekorasi / marker ? 1 : 0)
jika maker = Injection / LiquidGlitter / PopIt / StringPull → bintang = 3
maks 3
```

- Tidak ada unsur acak.
- Day 1–3 minimal 2★.
- Maker premium **selalu 3★**.
- Paling jelek 1★. Tidak ada kondisi gagal.

### Permintaan pelanggan (`InitMission`)
- Diambil acak dari {warna cat, glitter, stiker 2D, stiker 3D, marker, acrylic}, lalu disaring menurut maker dan hari.
- Jumlah ditentukan `item_require_count`:

| Nilai | Arti |
|---|---|
| −1 | Tanpa permintaan |
| 1 | Satu permintaan |
| 0 | Acak 1…N |

- **Cek kecocokan:** warna harus **sama persis** (RGBA). Stiker yang diminta harus benar-benar ditempel.

### Hasil
- 1★ / 2★ / 3★ membayar kolom reward yang sesuai.
- **RV "Claim"** = koin ×2 untuk pelanggan normal, ×4 untuk VIP.
- "No thanks" membayar koin dasar, lalu muncul interstitial.

## Kesulitan
- **Tidak ada kondisi gagal sama sekali** [KODE ✔]. Fitur Boss dan Unhappy customer dimatikan.
- Satu-satunya "hukuman" adalah bintang lebih sedikit, dan itu pun hanya jika pemain mengabaikan warna/stiker yang diminta atau tidak mendekorasi.
- **Insentif tersembunyi:** maker premium selalu 3★ dan skor leaderboard-nya lebih tinggi, sehingga pemain terdorong mencoba maker baru.
