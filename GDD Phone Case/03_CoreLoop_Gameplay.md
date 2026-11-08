# 03. Core Loop & Alur Sesi

[← Kembali ke indeks](00_README.md)

## 1. Empat lapis loop

```
┌─ LOOP MOMEN (5–20 detik) ─────────────────────────────────┐
│  satu langkah craft: pilih alat → drag/tap → progress     │
│  penuh → kata konfirmasi + suara → langkah berikutnya     │
└───────────────────────────────────────────────────────────┘
┌─ CORE LOOP (60–110 detik) [DRAFT] ────────────────────────┐
│  ambil pesanan dari waiting table → kerjakan di bench     │
│  (4–6 langkah) → case jadi → Cash + XP langsung masuk     │
└───────────────────────────────────────────────────────────┘
┌─ META LOOP (5–40 menit per level) [DRAFT] ────────────────┐
│  Cash + XP → Level Up → buka pelanggan/warna/alat         │
│  → beli tycoon & dekorasi → toko lebih besar & cantik     │
│  → pesanan lebih kompleks & lebih mahal → ulangi          │
└───────────────────────────────────────────────────────────┘
┌─ LOOP SOSIAL & HARIAN [DRAFT + USULAN] ───────────────────┐
│  pajang case di rak (AFK income) → visit toko teman       │
│  → like case di galeri → Best Case of the Week            │
│  → login harian, codes, kembali ambil AFK income          │
└───────────────────────────────────────────────────────────┘
```

## 2. Core loop secara rinci [DRAFT]

Draft: **Create case → Get Money and XP → Level Up → Build Store → Unlock Feature → Repeat.**

| Tahap | Apa yang terjadi | Detail |
|---|---|---|
| **1. Pelanggan datang** | NPC masuk toko, antre di **kasir** | Kasir langsung meng-assign ke karyawan yang cocok. Jika tidak ada, pesanan masuk **waiting table** (maks 2) [DRAFT]. Lihat [05](05_Toko_Tycoon_Karyawan.md#2-kasir--dispatch) |
| **2. Ambil pesanan** | Pemain mendekati waiting table, tekan **[E]**, baca order card, tekan **I'LL MAKE IT!** | Device dibawa ke bench pemain. Slot waiting table langsung terisi pesanan baru [DRAFT] |
| **3. Craft hands-on** | 4–6 langkah di **satu Craft Bench** tanpa berpindah tempat: Case Shape (pilih dari list HUD) → Base Painting → Smoothing → Top Pattern → Sticker → Screen Cleaning | Langkah yang muncul tergantung level dan request. Lihat [04](04_Mekanik_HandsOn.md) |
| **4. Case selesai = langsung dibayar** | Begitu langkah terakhir (Screen Cleaning) selesai, pesanan langsung selesai. **Tidak perlu membawa case ke kasir.** Pelanggan mengambil case sendiri dari bench, bereaksi, lalu pergi | Cash + XP langsung masuk |
| **5. Bayaran** | **Gaji dasar** (pesanan selesai) + **bonus kesesuaian 25%** (semua request terpenuhi) + **bonus kecepatan 20%** (selesai di bawah waktu target). Layar reward merinci ketiganya | Rumus di [08](08_Ekonomi.md#2-rumus-bayaran-pesanan) |
| **6. Level Up** | XP penuh → level naik → unlock baru | Tabel di [07](07_Level_Design.md) |
| **7. Build Store** | Beli item tycoon (fungsional) dan dekorasi (kosmetik) | Hologram biru di toko + app **Build** di HP |
| **8. Unlock Feature** | Pelanggan baru, langkah baru, device baru, warna baru, karyawan | Pesanan menjadi lebih kompleks dan lebih mahal |

### Aturan "selalu ada pekerjaan" [DRAFT]
- Waiting table selalu berisi pesanan. Begitu pemain mengambil satu, pesanan baru dibuat otomatis.
- Pelanggan **tidak pernah pergi karena kesal**. Tidak ada timer kesabaran yang bisa gagal (pilar 5).
- Saat pemain sibuk di bench, kasir terus meng-assign pesanan ke karyawan. Uang tetap masuk.
- **Tidak ada langkah DELIVER.** Kasir hanya menerima pelanggan dan membagi pesanan. Uang masuk saat case selesai, baik dikerjakan pemain maupun karyawan.

## 3. Pembagian kerja pemain vs karyawan

| | Pemain | Karyawan |
|---|---|---|
| Cara kerja | Hands-on, mini-game | Otomatis, timer |
| Kecepatan | ±60–95 detik per pesanan [SIM] | 75 detik base, bisa di-upgrade |
| Cash | 100% | 60% |
| XP | 100% | 25% |
| Bisa mengerjakan | Semua langkah yang sudah terbuka | Hanya pesanan yang sesuai skill-nya |
| Bonus kesesuaian & kecepatan | Tergantung hasil kerja pemain | Peluang dari stat Quality & Speed |

**Desain sengaja:** karyawan memberi cash yang lumayan tetapi XP kecil. Pemain tetap harus craft sendiri untuk naik level, sementara karyawan membiayai ekspansi toko.

## 4. Alur sesi pertama (target 30 menit)

| Menit | Kejadian | Tujuan desain |
|---|---|---|
| 0:00 | Spawn di kota, cutscene singkat kamera menyapu kota, berhenti di plot pemain. Teks "Your shop is ready!" | Orientasi ruang, mirip intro "We're open!" di FMP |
| 0:20 | Pelanggan tutorial "Mia" masuk lewat kasir, panah kuning menunjuk waiting table. Mia datang membawa Aphone 18 Pro Max | Langsung ke aksi, tanpa menu |
| 0:40 | Craft pertama: 4 langkah, request pink | Momen satisfying pertama di bawah 1 menit |
| 1:35 | Screen Cleaning selesai → langsung +45 Cash (gaji 31 + sesuai 8 + cepat 6), +26 XP. Mia mengambil case dari bench. Badge "Open For Business!" | Reward pertama, tanpa jalan ke kasir |
| 2:10 | **Level 2.** Unlock Stool + Pattern Shelf (hologram). Panah ke hologram | Belanja pertama, toko mulai berubah |
| 4–8 | Pesanan dengan Top Pattern. **Level 3** di ±7 menit: Fancy Girl/Boy, Samsam X26 Ultra, hologram Employee | Kebaruan terus-menerus |
| 8–15 | Rekrut karyawan pertama. Tutorial kasir mengassign pesanan ke karyawan | Toko mulai "hidup" |
| 15–20 | **Level 4**: Sticker Stock + Table | Langkah craft paling ekspresif dibuka |
| 20–30 | Tutorial display rack: pajang case terbaik → "Earns cash while you're away!" Tutorial galeri | Hook untuk kembali besok |
| ±26 | **Level 5**: Thief (momen lucu), Earpod, Sofa | Penutup sesi pertama yang memorable |

Detail per level di [07_Level_Design.md](07_Level_Design.md).

## 5. Sesi harian setelah hari pertama

```
Login → popup Daily Reward → ambil AFK income dari display rack
  → lanjutkan pesanan (1–3 level per sesi di L5–L10)
  → beli unlock baru
  → visit toko teman / like galeri
  → ganti case di display rack sebelum logout
```
