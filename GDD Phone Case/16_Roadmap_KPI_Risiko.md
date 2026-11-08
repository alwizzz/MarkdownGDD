# 16. Roadmap, KPI & Risiko

[← Kembali ke indeks](00_README.md)

## 1. Scope V1 (MVP)

### Masuk V1
| Area | Isi |
|---|---|
| Core | 6 langkah craft + Glossy, order card, bayaran langsung (gaji + bonus sesuai + bonus cepat), reward, Album, Freestyle |
| Toko | Kasir + dispatch, Waiting Table, backlog, 7 item tycoon, ekspansi L8 |
| Karyawan | 3 karyawan, 3 skill upgrade, Speed & Quality Lv1–5 |
| Konten | 5 device, 16 bentuk, 5 pelanggan, 23 warna, 9 pola, 24+ stiker, L1–L10 |
| Dekor | 7 objek × 3 varian, permukaan, papan nama, mesin kasir, 6 dekor premium |
| AFK | Display Rack + Tip Jar |
| Sosial | Kota 8 pemain, visit, like toko/case, bonus teman/grup/premium, equip case, feed server |
| Galeri | Best Case of the Week + Hall of Fame + app Gallery |
| Retensi | Daily login, daily quest, badge, codes, leaderboard global |
| Monetisasi | 9 gamepass, 4 paket Gems, Starter Pack, Boost, Cash Party, Instant Finish, Rush Staff |
| Platform | Mobile, PC, gamepad. EN + ID |

### Ditunda (V1.1+)
| Fitur | Alasan / asal |
|---|---|
| **Gallery Showdown** (ronde voting real-time setiap ±15 menit di server, gaya DTI) | Momen sosial kuat, tetapi butuh UX & balancing tersendiri |
| Upgrade/penambahan kasir | Draft menyebut "penambahan kasir". V1 cukup 1 kasir |
| Mesin penjual minuman, rak alat, upgrade rak pilihan case | Teks draft, belum ada di tabel level |
| Level 11–20, device & pelanggan baru | Update konten |
| Free-paint (`EditableImage`) | Menunggu API stabil [SRC Analisis S23] |
| Capsule stiker berbayar (dengan tabel peluang) | Kebijakan paid random items [SRC Analisis S24] |
| Rewarded video (13+) | Pendapatan kecil, hanya 13+ |
| Co-op (2 pemain mengerjakan pesanan Old Club bersama) | [SRC Analisis P1 #12] |
| Trading case | Butuh moderasi & anti-scam |
| UGC case accessory | Peluang lanjutan [SRC Analisis 4] |

## 2. Milestone [USULAN]

| Milestone | Durasi | Hasil | Kriteria lulus |
|---|---|---|---|
| **M0 Pre-production** | 1 minggu | Config final, greybox toko & kota, style guide | Desain L1–L10 disetujui |
| **M1 Vertical slice** | 3 minggu | L1–L3 lengkap di 1 plot: 4–5 langkah craft, kasir, waiting table, karyawan #1, reward, level-up | Playtest internal: craft terasa satisfying, ≥ 70% tester bilang "mau main lagi" |
| **M2 Content complete** | 4 minggu | L1–L10, semua langkah, pelanggan, device, tycoon, dekor, AFK, 8 plot | Bisa main L1→L10 tanpa bug blocker |
| **M3 Social & Monetization** | 2 minggu | Visit, like, galeri, leaderboard, gamepass, produk, codes, quest | ProcessReceipt lulus uji idempotensi |
| **M4 Polish & QA** | 2 minggu | Audio lengkap, VFX, FTUE, lokalisasi, optimasi mobile | FPS & memori sesuai [14](14_Teknis_Programmer.md#15-performa--batas) |
| **M5 Soft launch** | 2 minggu | Rilis publik tanpa iklan, grup kecil + kreator kecil | KPI soft launch (bagian 3) |
| **M6 Launch + update** | — | Sponsored ads, update tiap 2 minggu | — |

Total sampai soft launch: **±14 minggu**. Fix My Phone sudah ramai sejak Oktober 2026, jadi rilis lebih cepat lebih baik. Jika perlu dipersingkat, galeri bisa dimulai versi server-only dan Hall of Fame menyusul.

## 3. KPI

| Metrik | Target soft launch | Target setelah tuning | Dasar |
|---|---|---|---|
| D1 retention | ≥ 20% | ≥ 25% | Sesi < 6 menit ≈ D1 6% [SRC Analisis S13]. Target sesi kita jauh di atas itu |
| D7 retention | ≥ 5% | ≥ 8% | [ASUMSI] |
| Rata-rata sesi | ≥ 18 menit | ≥ 25 menit | Retensi naik tajam setelah ±19 menit [SRC Analisis S13] |
| % pemain baru mencapai L3 | ≥ 70% | ≥ 80% | FTUE funnel |
| % pemain baru mencapai L5 di hari pertama | ≥ 35% | ≥ 45% | [SIM] L5 di ±26 menit |
| Median menit ke L10 | 120–180 | — | [SIM] 142 menit |
| Konversi payer (30 hari) | ≥ 1% | ≥ 2% | [ASUMSI] |
| % pemain yang submit ke galeri | ≥ 15% | ≥ 25% | Indikator lapisan sosial |
| Rata-rata pemain per server | ≥ 5 | ≥ 6 | FMP rata-rata 6,1 [FMP] |

## 4. Analytics
Event lengkap di [14](14_Teknis_Programmer.md#14-analytics). Dashboard minimum:
1. Funnel FTUE 10 langkah.
2. Menit main median ke setiap level (bandingkan dengan [07](07_Level_Design.md#3-kurva-pengalaman)).
3. Cash saat level-up dan % pembeli tiap item tycoon/dekor.
4. % pesanan yang mendapat bonus kesesuaian dan bonus kecepatan, per level dan per device. Target: kecepatan ±70%. Jika jauh di bawah, longgarkan `target` di config `Steps`.
5. Thief: % tertangkap. Rich Kid: % haggle.
6. Konversi per titik tawaran (bagian 6 di [09](09_Monetisasi.md#6-peta-penempatan-tawaran)).

## 5. Risiko

| # | Risiko | Dampak | Mitigasi |
|---|---|---|---|
| 1 | **Nama parodi (Aphone, Samsam, dekor brand plesetan) dianggap melanggar merek** | Aset diturunkan, moderasi experience | Ikuti aturan di [09](09_Monetisasi.md#5-dekor-premium-brand-parodi). Siapkan nama cadangan orisinal (contoh: *Pear Phone 18*, *Galaxion X26*) yang bisa diganti lewat config tanpa ubah aset. Tanpa logo. Review sebelum rilis |
| 2 | **Foto referensi device berisi logo merek nyata** | Logo bocor ke aset | Artist hanya memakai siluet. Checklist QA "tanpa logo" |
| 3 | Pasar "toko HP" sudah diisi Fix My Phone | Pemain menganggap kita peniru | Pesan pemasaran fokus ke **kreasi & galeri**, bukan reparasi. Tidak meniru aset/UI FMP secara visual, hanya pola UX |
| 4 | Craft terasa repetitif setelah 50+ pesanan | Sesi pendek setelah L6 | Variasi pelanggan & device, karyawan mengambil pesanan sederhana, Freestyle, galeri |
| 5 | NPC banyak membuat mobile lag | Retensi turun di device murah | NPC client-side, LOD, batas per plot [14](14_Teknis_Programmer.md#15-performa--batas) |
| 6 | Spam like / akun alt di galeri | Peringkat tidak adil | Aturan anti-abuse di [10](10_Sosial_Retensi.md#aturan-like-anti-abuse) |
| 7 | Thief dianggap konten tidak pantas untuk anak | Masalah rating / laporan | Gaya komedi, tanpa kekerasan, tanpa kata pencurian HP nyata. Bisa diganti menjadi "Sneaky Prankster" lewat config |
| 8 | Ekonomi terlalu cepat / lambat | Pemain bosan atau frustrasi | Semua angka di config + script sim + dashboard soft launch |
| 9 | Konten habis di L10 | Churn di minggu 2 | Sink setelah L10 ±4 jam, galeri mingguan, update L11+ dalam 2–3 minggu setelah launch |
| 10 | Platform Roblox melambat (DAU −9% YoY, bookings −12%) | Pertumbuhan lebih sulit | [SRC Analisis 5.1]. Fokus ke retensi sebelum beli iklan |

## 6. Pertanyaan terbuka untuk pemilik desain

| # | Pertanyaan | Asumsi GDD saat ini |
|---|---|---|
| 1 | "Sova" di tabel L5 maksudnya Sofa? | Ya, Sofa |
| 2 | Apakah kasir di L1 sudah ada (NPC), dan "penambahan kasir" di draft berarti kasir ke-2? | NPC kasir ada sejak L1, kasir ke-2 di V1.1 |
| 3 | Urutan langkah Smoothing sebelum Top Pattern sesuai draft. Apakah Glossy boleh jadi sub-step Smoothing? | Ya |
| 4 | Apakah Screen Cleaning termasuk skill bawaan karyawan? | Ya, bawaan |
| 5 | Nama final device & brand parodi: tetap plesetan atau orisinal? | Plesetan ringan tanpa logo, dengan nama cadangan siap |
| 6 | Best Case of the Week: global atau per server saja? | Global + tampilan per server |
| 7 | Apakah 2x XP gamepass boleh mempercepat konten MVP yang hanya 10 level? | Boleh, karena sink setelah L10 cukup panjang |
| 8 | Gems: boleh dipakai untuk Instant Finish dengan XP penuh? | Tidak, XP 50% |
