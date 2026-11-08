---
description: readme
---

# GDD Case Gallery Roblox

Game Design Document untuk **Phone Case Gallery** (judul kerja: *Case Gallery*), adaptasi Roblox dari game mobile **Phone Case DIY** (CrazyLabs). Cakupan dokumen ini adalah **V1 / MVP rilis awal, Level 1–10**.

| | |
|---|---|
| Judul game | **Phone Case Gallery** |
| Platform | Roblox (mobile-first, juga PC dan konsol) |
| Genre | Social crafting tycoon (craft hands-on + bangun toko + pamer di galeri) |
| Server | 8 pemain per server, masing-masing punya 1 toko di satu kota |
| Target MVP | Level 1–10, sekitar 2,4 jam main aktif sampai L10 |
| Versi dokumen | V1 Draft, 8 November 2026 |
| Dasar dokumen | [Draft desain (docx)](../GDD%20Draft%20Phone%20Case%20Gallery.docx), [Analisis adaptasi](../Analisis_PhoneCaseDIY.md), [Teardown GameDesign](../GameDesign/00_README.md), riset game Roblox *Fix My Phone!* |

---

## Daftar isi

| # | File | Isi | Pembaca utama |
|---|---|---|---|
| 01 | [Visi & Pilar](01_Visi_Pilar.md) | High concept, pilar desain, target audiens, posisi pasar | Semua |
| 02 | [Nilai Lebih di Roblox](02_Nilai_Lebih_Roblox.md) | Apa yang lebih baik dibanding versi mobile, dan apa yang diambil dari Fix My Phone | Semua, stakeholder |
| 03 | [Core Loop & Alur Sesi](03_CoreLoop_Gameplay.md) | Loop momen, core, meta, sosial, alur sesi pertama | Semua |
| 04 | [Mekanik Hands-On](04_Mekanik_HandsOn.md) | 6 langkah craft (Case Shape → Screen Cleaning), kontrol, penilaian & bayaran (gaji + bonus) | Gameplay programmer, designer |
| 05 | [Toko, Tycoon, Karyawan & AFK](05_Toko_Tycoon_Karyawan.md) | Kasir, waiting table, karyawan, tycoon fungsional, dekorasi, AFK farm | Gameplay programmer, designer |
| 06 | [Pelanggan & Device](06_Pelanggan_Device.md) | 5 tipe pelanggan, 5 device, pembuatan request | Designer, programmer, artist |
| 07 | [Level Design L1–L10](07_Level_Design.md) | Tabel unlock per level, FTUE, ritme, detail tiap level | Level designer |
| 08 | [Ekonomi](08_Ekonomi.md) | Mata uang, rumus, faucet/sink, kurva XP, hasil simulasi | Economy designer |
| 09 | [Monetisasi](09_Monetisasi.md) | Gamepass, Developer Product, Gems, harga Robux, kebijakan | Product, monetization |
| 10 | [Sosial & Retensi](10_Sosial_Retensi.md) | Kota 8 pemain, visit, Best Case of the Week, daily, codes | Product, programmer |
| 11 | [UI/UX](11_UI_UX.md) | Arahan UI mengikuti pola Fix My Phone, HUD, phone menu, layar craft | UI designer, UI programmer |
| 12 | [Art Style & World](12_Art_Style_World.md) | Low-poly, palet, plot & taman, device, karakter | Artist, environment |
| 13 | [Sound Design](13_Sound_Design.md) | Daftar SFX lengkap, musik, aturan mixing | Sound designer |
| 14 | [Dokumen Teknis Programmer](14_Teknis_Programmer.md) | Arsitektur, data, remote, state machine, DataStore, performa | Programmer |
| 15 | [Daftar Konten & Aset MVP](15_Konten_Aset_MVP.md) | Semua aset yang perlu dibuat untuk V1 | Producer, artist |
| 16 | [Roadmap, KPI & Risiko](16_Roadmap_KPI_Risiko.md) | Scope MVP, milestone, metrik, analytics, risiko, pertanyaan terbuka | Producer, lead |
| 17 | [Referensi & Sumber](17_Referensi_Sumber.md) | Daftar sumber internal dan eksternal | Semua |

Pendukung:
- [tools/economy_sim.py](tools/economy_sim.py): script simulasi ekonomi L1–L10. Ubah angka di sini dulu sebelum mengubah tabel di dokumen.
- [assets/referensi_device/](assets/referensi_device/): foto referensi bentuk case dari draft.

---

## Cara membaca label

| Label | Arti |
|---|---|
| **[DRAFT]** | Diambil dari draft desain (docx). Ini keputusan pemilik desain, jangan diubah tanpa diskusi. |
| **[SRC]** | Dari teardown Phone Case DIY ([GameDesign/](../GameDesign/00_README.md)) atau [Analisis](../Analisis_PhoneCaseDIY.md). |
| **[FMP]** | Dari riset game Roblox *Fix My Phone!* (Doubloons). Dipakai sebagai acuan UI dan pola tycoon. |
| **[USULAN]** | Usulan GDD ini untuk melengkapi bagian yang belum ada di draft. Boleh diubah. |
| **[SIM]** | Angka hasil simulasi [tools/economy_sim.py](tools/economy_sim.py). Perlu divalidasi saat playtest. |

---

## Ringkasan satu halaman

**Fantasi:** "Aku punya toko custom case di kota. Pelanggan datang, aku membuat case dengan tanganku sendiri, karyawanku membantu, tokoku makin besar dan cantik, dan karyaku dipajang di galeri kota."

**Core loop [DRAFT]:**
```
Create Case → Dapat Cash + XP → Level Up → Build Store → Unlock Feature → ulangi
```

**Yang membuat V1 berbeda dari versi mobile:**
1. **Hands-on + tycoon dalam satu ruang.** Pemain membuat case sendiri di bench, sementara karyawan dan kasir menjalankan toko di sekitarnya. Mobile hanya punya satu pelanggan per layar.
2. **Kota 8 pemain.** Toko pemain lain terlihat, bisa dikunjungi, dan ada bonus cash untuk main bersama teman.
3. **Best Case of the Week.** Case terbaik dipajang di galeri kota dan dipilih lewat like antar pemain.
4. **Tanpa iklan paksa.** Monetisasi lewat Gamepass, Gems, dan Developer Product.
5. **Case jadi identitas.** Case buatan sendiri bisa dipegang avatar dan dipajang di rak toko (sekaligus menjadi sumber AFK income).

**Scope V1 (MVP):** 6 langkah hands-on, 5 device, 5 tipe pelanggan, 3 karyawan, 7 item tycoon, 7 kategori dekorasi, 23 warna, AFK farm, Best Case of the Week, 9 Gamepass, paket Gems. Detail di [16_Roadmap_KPI_Risiko.md](16_Roadmap_KPI_Risiko.md).
