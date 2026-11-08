# 02. Mekanik Maker & Dekorasi

[← Kembali ke indeks](00_README.md)

**Maker** adalah teknik membuat case. Setiap maker sebenarnya mini-game *satisfying* yang terpisah, dan inilah sumber utama variasi gameplay.

Sumber: `enum Maker` di `dump.cs` [KODE], kolom Feature di `Goods.csv` [DATA].

## Daftar Maker

Hari buka untuk Google Play (iOS sedikit berbeda karena di-A/B, lihat [08_LiveOps_AB.md](08_LiveOps_AB.md)).

| Maker | Buka (GP) | Langkah / mekanik inti | Skor leaderboard |
|---|---|---|---|
| **Spray** | Day 1 | Glue → semprot cat (drag) → hair dryer. 25 warna. | 50 |
| **Marker / BrushPen** | Day 1 | 15 warna spidol untuk menggambar bebas. | — |
| **Acrylic** | Day 2 | Tuang cat akrilik (pouring, `PouringConfig`). 25 warna + 25 palet pouring + palet bundle. | 50 |
| **Pop-It** | Day 3 | Cat → keringkan → mainkan pop-it (tap gelembung). | 150 |
| **Stencil** | Day 4 | Pilih stencil (donat, panda, ikan mas, pizza, unicorn, kupu-kupu, hati) → spray di atasnya. | 150 |
| **Marble** | Day 5 | Simulasi fluida (resolusi 256, `stirForce 500`) → aduk cat di air → celup HP (`DippingConfig`, celup 5 detik). | 200 |
| **Injection** | Day 6 | "HOLD TO INJECT": isi rongga berbentuk (bintang, petir, permen, nanas, air, gem) dengan cairan berwarna. Konfigurasi per bentuk HP. | 200 |
| **Liquid Glitter** | Day 6 | Pilih background → isi air + glitter. | 200 |
| **String Pull** | ? | Pasang benang → tarik (pola di `PullLevelConfig`, 20 level) → palette → heater → buka cover. | — |
| **ComingSoon** | — | Kartu "coming soon" untuk memancing rasa penasaran. | — |

> **Maker premium** (Injection, Liquid Glitter, Pop-It, String Pull) **selalu memberi 3★** (lihat [04_LevelDesign_Pacing.md](04_LevelDesign_Pacing.md#penilaian-bintang)).

## Langkah pendukung
Dari `UiVariants.csv`:

| Step | Fungsi |
|---|---|
| `step_vip_select` | Pilihan khusus pelanggan VIP |
| `step_break_screen` / `step_repair_screen` | Memperbaiki layar retak (dibuka lewat RV) |
| `step_clean_dirty` | Membersihkan case kotor (pelanggan Cleaning) |
| `step_clean_charing` | Membersihkan charging port |
| `step_clean_inside` | Membersihkan bagian dalam |
| `step_crossbody` | Memasang tali selempang |
| `step_glitter` | Menaburkan glitter |

**Catatan iklan:** hampir setiap transisi antar-langkah memanggil interstitial. Lihat [07_Monetisasi.md](07_Monetisasi.md#interstitial).

## Dekorasi

| Jenis | Jumlah | Catatan |
|---|---|---|
| Stiker 2D | 81 | Termasuk 8 "laser" holografik. Tema Superhero, Kpop, Princess, Creatures. |
| Stiker 3D | 37 | |
| Glitter | 15 | |
| Keychain | 12 | Didapat dari chest (lihat [06_Gacha.md](06_Gacha.md#keychain-chest)) |
| Crossbody Strap | 8 | `crossbody_strap_items.csv`, ada yang RV |
| Emoji / teks | — | |

- Interaksi: drag & drop dan skala [KODE `MoveSticker2d`].
- Painting memakai P3D Paint dengan undo / redo / clear [KODE `P3dButtonUndoAll`].

## Bentuk HP & Device [DATA]

| Jenis | Daftar |
|---|---|
| Phone dasar | Normal, Bunny, Among-us-like, Unicorn, Pineapple, Cola, "StarBucks", Foot, Cactus |
| Varian | Flip & Fold (Normal / Bunny) |
| Dari bundle | Cat, Anime, Robot, Cloud, Spaceship, Narwhal |
| Device lain | AirPods case, Earbuds, Headphones (alur sendiri, `HeadSetType`) |

- Model HP dibedakan per platform: `PhoneAssetConfig_iPhone` dan `PhoneAssetConfig_Android`, supaya HP di game mirip HP pemain.
- Jadwal kemunculan bentuk HP baru ada di [04_LevelDesign_Pacing.md](04_LevelDesign_Pacing.md).

> ⚠️ Bentuk "Among-us" dan "StarBucks" memakai IP pihak ketiga. Jangan ditiru untuk game kita.

## Config teknis terkait
Semua ada di `tables/ScriptableObject/`:
`PouringConfig`, `PouringColorConfig`, `MarblePaintingConfig`, `DippingConfig`, `InjectConfigList`, `AllInjectConfig`, `EveryInject`, `StencilConfig`, `PhoneStencilConfig`, `PopItPhoneConfig`, `PullLevelData`, `StringPullColor`, `GlitterConfig`, `GlitterBGConfig`, `StiringConfig`, `PhoneAssetConfig`.
