---
description: readme
---

# Phone Case DIY: Teardown Game Design

Dokumentasi hasil teardown game **Phone Case DIY**, dipecah per segmen supaya tim development bisa langsung membuka bagian yang relevan.

| | |
|---|---|
| Paket | `com.newnormalgames.phonecasediy` v5.2.0.0 (Google Play) |
| Publisher / SDK | CrazyLabs (TTPlugins / CLIK) |
| Engine | Unity 2022.3.62f2, IL2CPP, arm64 |
| Tanggal teardown | 2026-11-04 |

## Daftar Isi

| # | File | Isi | Cocok untuk |
|---|---|---|---|
| 01 | [Core Loop](01_CoreLoop.md) | Fantasi pemain, core loop, meta loop | Semua |
| 02 | [Mekanik Maker & Dekorasi](02_Mekanik_Maker.md) | 9 teknik membuat case, langkah mini-game, dekorasi, bentuk HP | Gameplay programmer, artist |
| 03 | [Tipe Pelanggan](03_Pelanggan.md) | Normal, VIP, Revenge, Auction, Couple, Cleaning, dll. | Gameplay, level designer |
| 04 | [Level Design & Pacing](04_LevelDesign_Pacing.md) | Struktur hari, FTUE, ritme, penilaian bintang, kesulitan | Level designer |
| 05 | [Ekonomi](05_Ekonomi.md) | Mata uang, sumber koin, pemakai koin, jalur unlock | Economy designer |
| 06 | [Gacha & Sistem Acak](06_Gacha.md) | Skin roll, spin wheel, keychain chest, auction | Economy designer, programmer |
| 07 | [Monetisasi](07_Monetisasi.md) | IAP, interstitial, rewarded video, antrean popup | Monetization, programmer |
| 08 | [LiveOps & A/B Testing](08_LiveOps_AB.md) | Thematic bundle, varian UI, remote config | LiveOps, backend |
| 09 | [Retensi & Sosial](09_Retensi_Sosial.md) | Leaderboard bot, daily mission, login, idle income | Product, programmer |
| 10 | [Daftar Konten](10_Konten.md) | Jumlah aset per kategori | Producer, artist |
| 11 | [Pelajaran untuk Game Kita](11_Pelajaran.md) | Poin desain yang bisa ditiru | Semua |
| 12 | [Lokasi File Sumber](12_Sumber_Data.md) | Peta file data, config, dan kode hasil dekompilasi | Programmer |

## Arti label

| Label | Arti |
|---|---|
| **[DATA]** | Angka diambil langsung dari tabel CSV atau ScriptableObject di dalam APK. |
| **[KODE ✔]** | Sudah dikonfirmasi dengan membaca isi method (Cpp2IL ISIL). |
| **[KODE]** | Struktur kelas/method ada, tetapi detail perilaku masih perkiraan dari nama. |
| **[DUGAAN]** | Interpretasi desain, belum terbukti. |

> ⚠️ **Semua angka adalah nilai default.** CrazyLabs bisa mengganti seluruh file CSV dari server (lihat [08_LiveOps_AB.md](08_LiveOps_AB.md)), jadi nilai yang aktif di HP pemain bisa berbeda.

## Yang tidak tercakup
- Nilai remote config yang sedang aktif di server.
- Save data pemain.
- Aset visual dan audio (masih terbungkus di `data.unity3d`, belum diekstrak).
