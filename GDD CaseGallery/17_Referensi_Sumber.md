# 17. Referensi & Sumber

[← Kembali ke indeks](00_README.md)

## 1. Internal

| Label | Dokumen | Dipakai untuk |
|---|---|---|
| [DRAFT] | [GDD Draft Phone Case Gallery.docx](../GDD%20Draft%20Phone%20Case%20Gallery.docx) | Core loop, mekanik kasir/karyawan, tycoon vs dekor, 6 langkah, 5 device, tabel L1–L10, art direction, monetisasi |
| [SRC] | [Analisis_PhoneCaseDIY.md](../Analisis_PhoneCaseDIY.md) | Kecocokan Roblox, perilaku pemain, monetisasi Roblox, aksesibilitas, daftar perubahan P0–P2 |
| [SRC 01–12] | [GameDesign/](../GameDesign/00_README.md) (teardown Phone Case DIY v5.2.0.0) | Core loop, maker, tipe pelanggan, rumus bintang, ekonomi, gacha, monetisasi, liveops, retensi, konten |
| — | [assets/referensi_device/](assets/referensi_device/) | Foto referensi bentuk device dari draft (hanya siluet, **jangan pakai logo**) |
| [SIM] | [tools/economy_sim.py](tools/economy_sim.py) | Semua angka waktu dan timeline ekonomi |

Sumber eksternal yang dikutip lewat Analisis (S1–S25: data Roblox Q3 2026, demografi, DevEx, rewarded video, kebijakan paid random items, `EditableImage`, input) tercantum lengkap di [Daftar Sumber Analisis](../Analisis_PhoneCaseDIY.md#daftar-sumber).

## 2. Riset Fix My Phone! [FMP]

Diakses 8 November 2026.

| Sumber | Isi yang dipakai | Keyakinan |
|---|---|---|
| [Rolimons: Fix My Phone!](https://www.rolimons.com/game/139165770588984) | ±12,4 juta visit, puncak 20.979 CCU, 8 pemain per server (rata-rata 6,1), developer Doubloons, 9 gamepass dan harganya (Wide Squeegee 99, Power Screwdriver 99, Magnet Mat 99, Heat Gun Pro 149, 2X Customers 199, 2X Candy 199, 2X Shop XP 249, Golden Toolkit 399, VIP 499) | Sedang (tracker pihak ketiga) |
| [AllThingsHow: Roblox Fix My Phone How to Play](https://allthings.how/roblox-fix-my-phone-how-to-play-full-guide/) | Kontrol [E]/[R], tombol aksi (I'LL FIX IT!, PUT DOWN, TURN IT ON, LEAVE), step counter "Step X of 6/7", kata konfirmasi, order card, reward screen, "Next Level" readout, panah & cincin kuning, unlock awal (Case Shelf $25, Parts Cabinet, Bench 2), reward pertama $39 + 17 XP | Sedang (panduan) |
| [BloxGamer: Fix My Phone beginner guide](https://bloxgamer.com/guides/fix-my-phone-beginner-guide-repairs-shop-growth-job-lots-and-cash-bonuses/) | Langkah reparasi, makeover (spray, laser, gems), trade-in, teknisi, showroom/makeover studio/refurb room, 100+ furnitur, Job Lots mingguan, bonus cash (+10%/teman maks 4, +10% grup, +20% Roblox Plus), codes | Sedang (panduan) |
| [Fix My Phone Wiki (fan)](https://fixmyphone.wiki/) | Konfirmasi tombol TURN IT ON / LEAVE, stage counter, friend perk | Rendah (wiki fan) |
| [FreshGameRadar: Fix My Phone!](https://freshgameradar.com/games/fix-my-phone/) | Alasan sukses: loop taktil low-stress, before/after, cocok untuk short ASMR, tanpa PvP | Rendah (opini) |
| [Sportskeeda: beginner's guide](https://www.sportskeeda.com/roblox-news/fix-my-phone-a-beginner-s-guide), [Dexerto: codes](https://www.dexerto.com/roblox/fix-my-phone-codes-3420625/) | Konfirmasi umum core loop dan sistem codes | Sedang |

### Catatan batas riset
- Tidak ada data resmi tentang ekonomi internal FMP (kurva XP, harga lengkap). Pola yang diambil adalah **struktur UX dan rentang harga gamepass**, bukan angka ekonominya.
- Angka visit/CCU berubah cepat karena game baru rilis 5 Oktober 2026.
- Tampilan visual FMP **tidak** ditiru. GDD ini hanya mengadopsi pola interaksi yang umum di genre.
