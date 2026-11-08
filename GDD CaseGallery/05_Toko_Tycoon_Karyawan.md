# 05. Toko, Tycoon, Karyawan & AFK

[← Kembali ke indeks](00_README.md)

Draft membedakan dua jenis pembelian [DRAFT]:
- **Tycoon:** upgrade **fungsional** (bench karyawan, ruang tunggu, rak bahan, dll.). Mengubah apa yang bisa dilakukan toko.
- **Dekorasi:** **full kosmetik** (kursi, cat tembok, warna meja, hiasan dinding, keramik lantai, model mesin kasir, dll.). Tidak mempengaruhi angka ekonomi.

---

## 1. Isi toko di Level 1 (gratis)

| Objek | Fungsi |
|---|---|
| Pintu masuk + papan nama toko | Nama toko = nama pemain (contoh: "Mia's Case Gallery"). Terlihat dari jalan kota |
| **Kasir** (counter + NPC kasir) | Menerima pelanggan dan meng-assign pesanan. **Tidak** menerima penyerahan case: case yang selesai langsung dibayar dan diambil pelanggan dari bench |
| **Waiting Table** (2 slot) | Antrean pesanan untuk pemain [DRAFT] |
| **Craft Bench** (pemain) | **Satu-satunya** tempat pemain mengerjakan semua 6 langkah. Papan alat (spray, buffer, kuas, roller, kain) terpasang di bench. Bentuk, warna, pola, dan stiker dipilih dari tray HUD |
| Dinding belakang bench | Slot tempat Pattern Shelf, Sticker Stock, dan Glossy Finish Paint Shelf dipasang setelah dibeli (pajangan visual, tidak perlu didatangi) |
| **Display Rack** (4 slot) | Pajangan case = AFK farm [DRAFT] |
| Kursi tunggu (3) | Tempat pelanggan menunggu |
| **Hologram unlock** | Kerangka biru transparan + label harga dan level di lokasi item tycoon/dekor berikutnya |

---

## 2. Kasir & dispatch

Aturan dari draft: *"Kasir akan langsung meng-assign employee yang tersedia, berdasarkan skill yang dimiliki employee. Jika employee dalam pengerjaan atau tidak memiliki skill untuk request customer tsb, maka akan ditambahkan ke waiting table."* [DRAFT]

```
Pelanggan baru tiba di kasir
  └─ Ada karyawan IDLE yang skill-nya mencakup semua langkah pesanan?
       ├─ YA  → assign ke karyawan (pilih yang skill-nya PALING SEDIKIT tapi cukup,
       │        supaya karyawan serba-bisa tetap tersedia untuk pesanan sulit)
       └─ TIDAK → Waiting Table punya slot kosong?
                   ├─ YA  → taruh di Waiting Table (untuk pemain)
                   └─ TIDAK → pelanggan duduk di kursi tunggu (backlog)

Karyawan selesai / jadi idle
  └─ ambil pesanan dari BACKLOG yang cocok skill-nya (bukan dari Waiting Table)

Pemain mengambil pesanan dari Waiting Table
  └─ slot kosong → kasir langsung menarik pelanggan berikutnya dari backlog,
     atau memanggil pelanggan baru jika backlog kosong [DRAFT: "auto create new antrian"]
```

| Aturan | Nilai | Catatan |
|---|---|---|
| Kapasitas Waiting Table | **2** (3 setelah Waiting Room Expand L8) | [DRAFT] maks 2 di versi ini |
| Kursi tunggu (backlog) | 3 (6 setelah L8) | [USULAN] |
| Interval kedatangan pelanggan | 6–10 detik, hanya jika ada kapasitas | [USULAN] |
| Waiting Table hanya untuk pemain | Karyawan tidak mengambil dari Waiting Table | [USULAN] Supaya pesanan pemain tidak "dicuri" karyawan |
| Pelanggan pergi karena kesal | **Tidak pernah** | Pilar tanpa gagal |
| Kasir dikerjakan oleh | NPC kasir sejak L1 | Draft menyebut "penambahan kasir" per level. V1 memakai 1 kasir, upgrade kasir di V1.1 (lihat [16](16_Roadmap_KPI_Risiko.md)) |

---

## 3. Karyawan (Employee)

Draft: *pemain bisa merekrut 3 employee yang dibangun berdasarkan progres tycoon, lalu meningkatkan skill dengan membayar cash. Setiap employee punya basic skill Case Shape, Basic Painting, Smoothing.* [DRAFT]

### Rekrut
| Karyawan | Buka | Harga | Termasuk |
|---|---|---|---|
| #1 | L3 | 350 | Work bench + NPC karyawan |
| #2 | L7 | 2.200 | Work bench + NPC karyawan |
| #3 | L10 | 6.500 | Work bench + NPC karyawan |

NPC karyawan dibuat dari daftar penampilan dan nama (contoh: Jules, Nara, Bo). Pemain bisa mengganti nama di app Staff.

### Skill
| Skill | Status awal | Biaya belajar | Syarat |
|---|---|---|---|
| `shape` Case Shape | ✔ bawaan | — | — |
| `paint` Basic Painting | ✔ bawaan | — | — |
| `smooth` Smoothing | ✔ bawaan | — | — |
| `clean` Screen Cleaning | ✔ bawaan [USULAN] | — | — |
| `pattern` Top Pattern | Belajar | 300 | Pattern Shelf sudah dibeli |
| `sticker` Sticker | Belajar | 700 | Sticker Stock sudah dibeli |
| `glossy` Glossy Finish | Belajar | 1.200 | Glossy Finish Paint Shelf sudah dibeli |

### Stat
| Stat | Lv1 | Lv2 | Lv3 | Lv4 | Lv5 |
|---|---|---|---|---|---|
| **Speed**: waktu per pesanan | 75 dtk | 67 dtk | 60 dtk | 53 dtk | 45 dtk |
| Peluang bonus kecepatan (+20%) | 20% | 40% | 60% | 80% | 100% |
| Biaya upgrade Speed | — | 250 | 600 | 1.200 | 2.200 |
| **Quality**: peluang bonus kesesuaian (+25%) | 30% | 45% | 60% | 75% | 90% |
| Biaya upgrade Quality | — | 300 | 700 | 1.400 | 2.500 |

| Hasil kerja karyawan | Nilai |
|---|---|
| Cash | 60% × (gaji dasar + bonus kesesuaian jika lolos roll Quality + bonus kecepatan jika lolos roll Speed). Dibayar **langsung saat karyawan selesai** |
| XP | 25% |
| Visual | Karyawan memakai animasi kerja di bench (spray, buffer, tempel). Progress bar melayang di atas kepala. Saat selesai, cash langsung masuk (koin melayang ke HUD) dan pelanggan mengambil case dari work bench karyawan |

**Desain sengaja:** pesanan di L4+ sering meminta pola dan stiker. Karyawan yang hanya punya skill bawaan hanya bisa mengambil sebagian pesanan. Upgrade skill adalah sink cash yang terasa langsung manfaatnya [USULAN].

---

## 4. Tycoon fungsional (V1)

| Level | Item | Harga | Efek |
|---|---|---|---|
| L2 | **Pattern Shelf** | 120 | Membuka Step 4 Top Pattern (bahan pola muncul di tray HUD) dan skill `pattern` untuk karyawan. Rak dipasang di dinding belakang Craft Bench |
| L3 | **Employee +1** | 350 | Karyawan #1 + work bench |
| L4 | **Sticker Stock** | 600 | Membuka Step 5 Sticker (stiker muncul di tray HUD) dan skill `sticker`. Dipasang di dinding belakang Craft Bench |
| L6 | **Glossy Finish Paint Shelf** | 1.500 | Membuka sub-step Glossy, request finish, dan skill `glossy`. Pesanan Glossy menambah gaji dasar +10. Dipasang di dinding belakang Craft Bench |
| L7 | **Employee +1** | 2.200 | Karyawan #2 + work bench |
| L8 | **Waiting Room Expand** | 3.000 | Bangunan toko melebar ke taman. Kursi tunggu 3→6, Waiting Table 2→3, slot dekor baru (Statue, Fish Tank) |
| L10 | **Employee +1** | 6.500 | Karyawan #3 + work bench |

Sumber item dan level: tabel draft [DRAFT]. Harga: [SIM].

**Cara membeli:** hologram di lokasi item (untuk rak bahan: di dinding belakang Craft Bench, terlihat dari posisi kerja pemain), tekan [E] untuk melihat harga dan tekan **BUILD**. Bisa juga lewat app **Build** di HP. Animasi build: kotak kardus jatuh, terbuka dengan "poof", item muncul dengan bounce [USULAN].

**Item tycoon dari teks draft yang belum masuk tabel level** (disimpan untuk V1.1): mesin penjual minuman, rak alat (tool rack), upgrade rak pilihan case. Lihat [16](16_Roadmap_KPI_Risiko.md).

---

## 5. Dekorasi (kosmetik)

Dekorasi tidak mengubah angka ekonomi [DRAFT]. Nilainya adalah ekspresi diri dan pamer saat toko dikunjungi.

### 5a. Objek dekor dari tabel level [DRAFT]

Setiap objek memiliki **slot tetap** di toko (bukan penempatan bebas, supaya UI mudah di HP). Setiap objek punya 3 varian.

| Level | Objek | Varian Basic (cash) | Varian Cute (cash) | Varian Premium (Gems) |
|---|---|---|---|---|
| L2 | Stool | 60 | 110 | 40 💎 |
| L4 | Table | 180 | 320 | 60 💎 |
| L5 | Sofa | 400 | 720 | 80 💎 |
| L6 | Plant Pot | 300 | 540 | 60 💎 |
| L7 | Trash Bin | 250 | 450 | 50 💎 |
| L8 | Statue | 900 | 1.600 | 120 💎 |
| L10 | Fish Tank | 2.000 | 3.600 | 150 💎 |

> Draft menulis "Sova". GDD ini menganggapnya **Sofa**.

### 5b. Permukaan & peralatan [DRAFT teks, harga USULAN]

| Kategori | Buka | Pilihan V1 | Harga |
|---|---|---|---|
| Cat tembok | L1 | 8 warna | 80–300 cash |
| Keramik lantai | L1 | 6 motif | 100–400 cash |
| Warna meja/bench | L2 | 6 warna | 60–200 cash |
| Hiasan dinding | L3 | 6 (poster, jam, neon sign) | 150–500 cash |
| Model mesin kasir | L5 | 3 model (Retro, Pastel, Gold) | 400 / 800 / 90 💎 |
| Papan nama toko | L1 | 5 gaya | 100–600 cash, 2 gaya premium Gems |

Item premium di sini termasuk **dekor brand parodi** dari draft. Aturannya ada di [09](09_Monetisasi.md#5-dekor-premium-brand-parodi).

---

## 6. AFK Farm: Display Rack

Draft: *"Menjual hasil buatan casing yang dapat menghasilkan passive income ketika player tidak online. Ada limit max."* [DRAFT]

| Aturan | Nilai |
|---|---|
| Slot | 4 (+4 dengan gamepass *Bigger Gallery Rack*, +1 VIP) |
| Isi slot | Case apa saja dari **Album** pemain (30 case terakhir yang dibuat sendiri, termasuk Freestyle) |
| Nilai case | `nilai_case` = bayaran penuh pesanan Normal (gaji dasar + kedua bonus) untuk case itu (device + langkah yang ada di case). Rumus di [08](08_Ekonomi.md#4-afk-income-display-rack) |
| Income | **2% × nilai_case per menit** untuk setiap case yang dipajang. Berjalan online dan offline |
| Penampung | Uang masuk ke **Tip Jar** di rak. Pemain menekan [E] untuk mengambil (bunyi koin) |
| Batas (cap) | Tip Jar penuh setelah **3 jam** income (8 jam dengan gamepass *Night Shift*) |
| Case tidak hilang | Case yang dipajang tetap ada. Yang dijual adalah "replika pesanan" [USULAN] |

**Mengapa dikaitkan ke case buatan sendiri:** pemain terdorong membuat case bernilai tinggi (device mahal + banyak langkah) untuk dipajang. Pengunjung juga melihat dan memberi like ke case di rak, jadi rak ini juga "galeri pribadi" toko.

---

## 7. Ekspansi plot & taman

Draft: *tanah toko pertama kecil, dikelilingi taman. Saat toko diekspansi (mulai upgrade waiting room), bangunan diperluas dan taman menjadi lebih sempit.* [DRAFT]

| Tahap | Ukuran bangunan | Taman | Pemicu |
|---|---|---|---|
| Awal (L1) | ±28 × 24 studs | Luas: rumput, bunga, pohon, bangku, kolam kecil | — |
| Setelah Employee #1/#2 | Sama, bench karyawan mengisi area dalam | Sama | L3, L7 |
| **Waiting Room Expand** | ±44 × 32 studs (sisi depan dan samping maju ke taman) | Menyempit menjadi jalur bunga dan 2 pohon | L8 |
| V1.1+ | Lantai 2 / galeri atap | Taman jadi teras | Level 11+ |

Plot total ±80 × 80 studs. Animasi ekspansi: dinding lama "lepas" ke atas, lantai baru tumbuh ke depan, tanaman taman masuk tanah dengan efek debu [USULAN].
