# Analisis Kecocokan Adaptasi: Phone Case DIY → Roblox ("Case Craft Studio")

| | |
|---|---|
| Game sumber | **Phone Case DIY** (`com.newnormalgames.phonecasediy` v5.2.0.0, CrazyLabs) |
| Versi kita | **Case Craft Studio**, saat ini masih [Prototype v1](Prototype%20v1/README.md) (browser, Three.js, gaya blocky low-poly) |
| Dasar internal | Teardown di [GameDesign/](GameDesign/00_README.md): data CSV, ScriptableObject, dan kode hasil dekompilasi |
| Dasar eksternal | Laporan keuangan Roblox, dokumentasi resmi Roblox Creator Hub, DevForum, tracker pihak ketiga (lihat [Daftar Sumber](#daftar-sumber)) |
| Tanggal analisis | 4 November 2026 |

### Cara membaca label sumber
| Label | Arti |
|---|---|
| **[GDD-xx]** | Dari dokumen teardown kita, file `GameDesign/xx_*.md`. Angkanya diambil langsung dari APK. |
| **[PROTO]** | Dari [Prototype v1/README.md](Prototype%20v1/README.md). |
| **[S#]** | Sumber eksternal nomor # di [Daftar Sumber](#daftar-sumber). |
| **[DUGAAN]** | Interpretasi kami. Belum ada data yang membuktikan. |

> ⚠️ **Batas data.** Roblox tidak merilis data retensi per genre ([S13]). Kami juga tidak punya data demografi resmi pemain Phone Case DIY. Angka visit dan CCU game Roblox berasal dari tracker pihak ketiga, jadi anggap sebagai perkiraan.

---

## 1. Summary

**Kesimpulan: COCOK DENGAN SYARAT. Skor kecocokan 3,4 / 5.**

Fantasi inti Phone Case DIY ("aku punya bengkel custom case, membuat pesanan, lalu menghias studio") sejalan dengan genre yang kuat di Roblox, yaitu ekspresi diri dan simulasi/tycoon. Masalahnya, **model bisnis dan struktur sosialnya tidak bisa dibawa apa adanya.** Game aslinya single-player, ad-first, dengan sesi pendek. Di Roblox ketiga hal itu justru menjadi kelemahan.

### Yang mendukung adaptasi
| # | Temuan | Sumber |
|---|---|---|
| 1 | Game sumber terbukti di pasar mobile: 314 juta download (2024), judul CrazyLabs dengan download terbanyak. | [S5], [S6] |
| 2 | Genre ekspresi diri sangat besar di Roblox. *Dress to Impress* mencapai ±10,5 miliar visit dan puncak 1,5–1,73 juta CCU. Ada 274 juta update avatar per hari di 2025. | [S10], [S11], [S12] |
| 3 | Game sederhana dan santai bisa meledak di Roblox. *Grow a Garden* mencapai ±21,3 juta CCU (Juni 2025). | [S14] |
| 4 | Basis pengguna Roblox didominasi mobile (±72–80%), sama dengan platform asal game. | [S3], [S4] |
| 5 | Pengguna wanita di Roblox mobile (panel AS) kini melampaui pria. Ini sesuai dengan tema konten game sumber (Kpop, Princess, glitter). | [S7], [GDD-02] |
| 6 | Belum ada pesaing langsung "phone case DIY" di Roblox. Yang paling dekat adalah *Phone Store Tycoon* (±23 juta visit) dan *Make a Cake!* (±226 juta visit). | [S15], [S16] |
| 7 | Desain datanya sudah rapi dan mudah dipindah: semua angka ada di CSV, ada rumus reward linear, dan sink yang terukur. | [GDD-05], [GDD-08] |

### Risiko utama
| # | Risiko | Sumber |
|---|---|---|
| 1 | **Monetisasi asli bergantung pada iklan** (±75 titik interstitial, puluhan titik RV). Roblox tidak punya interstitial. Rewarded video hanya tampil untuk pengguna 13+ dan awalnya hanya ±3% dari pendapatan. | [GDD-07], [S18] |
| 2 | **Single-player, tanpa unsur sosial nyata.** Leaderboard-nya berisi 499 bot. Algoritma Roblox kini menilai retensi 28 hari. | [GDD-09], [S20] |
| 3 | **Sesi pendek.** Hypercasual rata-rata 6m42d per sesi. Di Roblox, sesi di bawah 6 menit berkorelasi dengan D1 sekitar 6%. | [S21], [S13] |
| 4 | **Konten berhenti di Day 25.** Tabel dikunci, reward tidak naik lagi. Pemain Roblox mengharapkan update rutin. | [GDD-04] |
| 5 | **Platform sedang melambat.** DAU Q3 2026 138 juta (−9% YoY), bookings ±$1,7 miliar (−12% YoY). | [S1], [S2] |
| 6 | **Painting di runtime** butuh `EditableImage`, yang masih beta, dibatasi memori client, dan mewajibkan verifikasi umur + ID developer. | [S23] |

### Rekomendasi singkat
Adaptasi **mekanik maker dan meta studio-nya**, lalu **ubah bentuk produknya** menjadi *social crafting tycoon*: studio di server bersama, case bisa dipakai di avatar, ada showcase/voting antar pemain, dan monetisasi Robux. Detail ada di [Bagian 7](#7-perubahan-yang-perlu-dilakukan-untuk-diadaptasi).

---

## 2. Player Behaviour: Mobile vs Roblox

| Aspek | Phone Case DIY (mobile) | Roblox | Implikasi untuk Case Craft Studio | Sumber |
|---|---|---|---|---|
| **Cara menemukan game** | Iklan UA (paid install) dari publisher besar | Home/discovery algoritmik, sort, rekomendasi teman | Kunci pertumbuhannya retensi dan engagement, bukan budget UA | [S20], [S22] |
| **Panjang sesi** | Hypercasual median 6m42d. Satu level = satu pelanggan, sangat singkat | "Core users" rata-rata 37 menit per sesi, "casual users" keluar dalam < 2 menit. Retensi naik tajam setelah ±19 menit | Butuh loop yang membuat pemain bertahan > 15 menit: antrean pelanggan beruntun, event server, showcase | [S21], [S13] |
| **Retensi yang dinilai platform** | Tidak ada. Publisher mengukur sendiri | "Recommended For You" kini memakai jendela **28 hari** (sebelumnya 7 hari), plus play-through rate, D1/D7, play time, dan konversi payer | Day 25 lock membunuh retensi jangka panjang. Wajib ada konten loop dan liveops | [S20], [GDD-04] |
| **Sosial** | Solo. Leaderboard = 499 bot dengan skor tetap. Viral loop hanya lewat share foto | Pemain datang bersama teman, satu server berisi banyak pemain, budaya pamer dan trading | Leaderboard bot diganti leaderboard nyata (global + server). Hasil case dipamerkan ke pemain lain | [GDD-09], [S9] |
| **Ekspektasi konten** | Konten statis 25 hari, perubahan lewat remote CSV | Update mingguan, event, kolaborasi. DTI melonjak ke 651 ribu+ CCU saat kolaborasi Charli XCX | Rencanakan kalender update sejak awal | [GDD-08], [S11] |
| **Kegagalan** | Tidak ada kondisi gagal, minimal 1★ | Genre santai (DTI, Grow a Garden) juga minim kondisi gagal | **Pertahankan.** Desain "no-fail" cocok | [GDD-04], [S14] |
| **Umur** | Tidak ada data resmi. Tema Kpop/Princess/glitter mengarah ke remaja putri [DUGAAN] | Age-checked DAU: <13 = 35%, 13–17 = 38%, 18+ = 27% | ±1/3 pemain di bawah 13: iklan RV tidak tampil untuk mereka, chat dibatasi | [S3], [S18] |
| **Gender** | Tidak ada data resmi [DUGAAN: dominan perempuan] | WAU perempuan di Roblox mobile (panel AS) melampaui laki-laki per Juli 2026, tumbuh 24% YoY vs 5% | Target audiens sejalan dengan tren pertumbuhan Roblox | [S7] |
| **Offline / idle** | Idle income dengan cap 5 jam | *Grow a Garden* membuktikan progres offline bekerja di Roblox (tanaman tumbuh saat offline) | **Pertahankan** idle income, ubah menjadi "toko tetap jalan saat offline" | [GDD-05], [S14] |

**Ringkasan perilaku:** pemain mobile datang untuk *satisfying moment* yang singkat dan sendirian. Pemain Roblox datang untuk **identitas dan teman**. Mekanik yang memuaskan tetap berharga, tetapi harus dibungkus lapisan sosial.

---

## 3. Monetization & Marketing

### 3.1 Model asli vs Roblox

| | Phone Case DIY | Roblox | Sumber |
|---|---|---|---|
| Model | Ad-first hybrid-casual, tanpa mata uang premium | In-experience purchase dengan Robux (Game Pass, Developer Product, subscription) | [GDD-07] |
| Iklan paksa | ±75 titik interstitial + App Open Ads | **Tidak ada interstitial.** Yang tersedia: rewarded video (opt-in) dan immersive ads | [GDD-07], [S18], [S19] |
| Rewarded video | Inti ekonomi: claim ×2, VIP ×4, unlock item, gacha, booster | Ada sejak April 2025. Hanya untuk pengguna **13+**, ada syarat kelayakan experience. Roblox menyebutnya awalnya hanya ±3% dari earnings | [S18] |
| IAP | 10 produk non-consumable, $1,99–$12,99 | Robux. DevEx standar **$0,0038/Robux** (naik dari $0,0035 per 5 Sept 2025). Ada rate +42% untuk belanja pemain 18+ AS yang lolos age check di game R15 | [GDD-07], [S17] |
| Split pendapatan (perkiraan) | IAP 52% / Ads 48% (estimasi AppGoblin, belum terverifikasi) | Mobile = ±80% pengguna, tetapi hanya ±46% pendapatan Robux | [S8], [S4] |
| Gacha | Skin roll dengan koin, tanpa duplikat | **Paid random items wajib menampilkan semua hasil dan peluang numerik**, termasuk jika dibayar dengan mata uang yang bisa dibeli pakai Robux | [GDD-06], [S24] |

### 3.2 Pemetaan monetisasi (RV → Robux)

| Momen di game asli | Versi Roblox yang disarankan | Tipe | Dasar |
|---|---|---|---|
| RV "Claim ×2" di layar hasil | Game Pass **"2× Coins" permanen**, ditambah opsi rewarded video ×2 untuk pemain 13+ | Game Pass + RV | [GDD-07] |
| VIP ×4 (momen RV paling bernilai) | Game Pass **"VIP Studio"**: ×4 reward VIP + antrean VIP lebih sering | Game Pass | [GDD-03] |
| Item studio `price_rv` (33 item) | Dijadikan item koin, atau beberapa diubah menjadi item eksklusif Robux | Dev Product | [GDD-05] |
| Thematic bundle (timer + skip koin) | Bundle musiman berbatas waktu yang dibeli dengan Robux. Timer tetap untuk jalur gratis | Dev Product | [GDD-08] |
| `keychains` $1,99 | Game Pass "All Keychains" | Game Pass | [GDD-06] |
| Spin wheel premium | Dev Product **dengan tabel peluang ditampilkan** | Dev Product | [S24] |
| `noads` $4,99 | Tidak relevan (tidak ada interstitial). Diganti Game Pass "Pro Tools" (semua maker terbuka) | Game Pass | [GDD-07] |
| Booster idle permanen | Game Pass "Auto-Worker" / "Double Income" | Game Pass | [GDD-05] |
| Interstitial di setiap transisi langkah | **Dihapus.** Transisi dibuat cepat dan mulus | — | [S18] |

**Catatan gacha:** skin roll asli memakai peluang seragam tanpa duplikat [GDD-06]. Ini mudah dibuat patuh kebijakan: tampilkan "peluang = 1 / jumlah skin tersisa". Jika koin bisa dibeli dengan Robux, aturan disclosure tetap berlaku [S24].

**Catatan payer:** payer bulanan Roblox turun ke 30 juta (−16% YoY), sedangkan bookings per payer naik 5% [S1]. Artinya pemain yang membayar makin sedikit tetapi makin besar belanjanya. Sediakan beberapa produk bernilai tinggi (Game Pass) selain produk kecil.

### 3.3 Marketing

| Kanal | Mobile (asli) | Roblox | Sumber |
|---|---|---|---|
| Akuisisi | UA berbayar lewat jaringan publisher (CrazyLabs, 7 miliar+ download portofolio) | Discovery algoritmik yang menilai retensi 28 hari dan monetisasi. Ada cold-start problem untuk game baru | [S6], [S20], [S22] |
| Konten kreator | Video iklan "satisfying" [DUGAAN] | YouTuber/TikToker Roblox. Kolaborasi menjadi pemicu lonjakan (DTI × Charli XCX) | [S11] |
| Event | Weekly event, thematic bundle | Update mingguan, event musiman, kode promo, badge | [GDD-08] |
| Iklan dalam platform | — | Sponsored experience / ads manager dan portal ads | [S19] |

**Strategi yang disarankan [DUGAAN, berbasis S20/S22]:** soft launch dengan grup kecil, perbaiki D1/D7 dan play time di Creator Analytics, baru setelah itu beli sponsored ads. Uang iklan untuk game dengan retensi rendah akan terbuang, karena algoritma tidak akan ikut mendorong.

---

## 4. Art and Design Style

| Aspek | Phone Case DIY | Kebutuhan Roblox | Status versi kita | Sumber |
|---|---|---|---|---|
| Gaya umum | Semi-realistis, close-up tangan dan HP, fokus ASMR/satisfying | Stylized, cerah, terbaca di layar kecil. Avatar pemain terlihat di dunia | Prototype v1 sudah memakai 3D low-poly gaya blocky ala Roblox | [GDD-02], [PROTO] |
| Kamera | Close-up statis per langkah | Ada mode dunia (studio + avatar) dan mode crafting (close-up) | Prototype punya 2 view: `craft` dan `studio` | [PROTO] |
| Model HP | Mirip HP asli pemain (`PhoneAssetConfig_iPhone` / `_Android`) | Bentuk generik orisinal, hindari brand nyata | Sudah generik | [GDD-02] |
| Bentuk HP ber-IP | "Among-us" dan "StarBucks" | **Dilarang ditiru** | Sudah diganti **Alien** dan **Kopi** | [GDD-02], [GDD-11], [PROTO] |
| Painting | P3D Paint (Unity) dengan undo/redo, simulasi fluida Marble resolusi 256 | `EditableImage`: beta, memori client dibatasi, maksimal 1 update per frame, developer wajib verifikasi 13+ dan ID | Prototype menyederhanakan Marble menjadi smudge kanvas | [GDD-02], [S23], [PROTO] |
| Stiker & dekorasi | 81 stiker 2D, 37 stiker 3D, 15 glitter, 12 keychain | Decal/MeshPart. Stiker 3D cocok dengan gaya blocky | Konten pengganti orisinal, jumlah lebih sedikit | [GDD-10], [PROTO] |
| Studio | 125 item dalam 10 kategori | Ruang 3D yang bisa dimasuki teman. Ini menjadi lebih bernilai | Ada 125 item, sama dengan data asli | [GDD-05], [PROTO] |

### Arahan art untuk Roblox
1. **Case harus bisa dipakai di avatar** sebagai accessory (dipegang atau dikalungkan). Ini mengubah hasil crafting menjadi identitas, sejalan dengan 274 juta update avatar per hari [S12]. Peluang lanjutan: rilis case populer sebagai UGC [DUGAAN].
2. **Palet pastel dan tekstur bersih.** Siluet HP harus terbaca jelas di layar HP kecil, karena mayoritas pemain memakai mobile [S4].
3. **Efek "satisfying" dengan partikel dan suara**, bukan simulasi fisika berat. Alasannya batas memori `EditableImage` dan keragaman device mobile [S23].
4. **Budget performa.** Uji di device Android murah. Kreasi dari banyak pemain di satu server berarti banyak tekstur unik di memori [DUGAAN, berbasis S23].

---

## 5. Statistik Pendukung: Apakah Worth Diadaptasi?

### 5.1 Data pasar

| Metrik | Nilai | Interpretasi | Sumber |
|---|---|---|---|
| Download Phone Case DIY | 314 juta (2024). Google Play ±325 juta install | Fantasi dan mekanik terbukti sangat luas jangkauannya | [S6], [S8] |
| Estimasi pendapatan Phone Case DIY | $50 ribu+/bulan (satu listing store, tidak terverifikasi) | Monetisasi per user di mobile rendah, wajar untuk ad-first | [S8] |
| DAU Roblox Q3 2026 | 138 juta (−9% YoY, +12% QoQ). DAU 18+ tumbuh 18% | Platform tetap raksasa meski sedang turun dari puncak 2025 | [S1], [S2] |
| Bookings Roblox Q3 2026 | ±$1,7 miliar (−12% YoY). Outlook Q4 −10% s/d −15% | Persaingan pendapatan makin ketat | [S1], [S2] |
| Payer bulanan | 30 juta (−16% YoY), bookings/payer +5% | Butuh produk bernilai tinggi | [S1] |
| Share device | Mobile ±72–80%, desktop ±17–25%, konsol ±3% | Basis input game sumber (touch) cocok | [S3], [S4] |
| Gender mobile (panel AS) | Perempuan > laki-laki sejak Juli 2026 | Audiens game sumber sedang tumbuh di Roblox | [S7] |
| DevEx | $0,0038/Robux (standar) | 1 juta Robux ≈ $3.800 | [S17] |

### 5.2 Benchmark game sejenis di Roblox

| Game | Kemiripan | Angka | Sumber |
|---|---|---|---|
| *Dress to Impress* | Ekspresi diri, kreasi dinilai, audiens dominan perempuan | ±10,5 miliar visit. Puncak 1,5–1,73 juta CCU | [S10], [S11] |
| *Grow a Garden* | Loop santai, tanpa gagal, ada progres offline | Puncak ±21,3 juta CCU | [S14] |
| *Make a Cake!* | Crafting / membuat sesuatu | ±226 juta visit, CCU kecil saat ini (±1 ribu puncak terbaru) | [S16] |
| *Phone Store Tycoon* | Tema HP + tycoon | ±23 juta visit, puncak ±2–10,7 ribu CCU (sumber berbeda) | [S15] |

**Interpretasi:** tema "HP + crafting" **belum pernah dieksekusi dengan baik** di Roblox. Pesaing langsungnya kecil, jadi ada celah pasar. Sebaliknya, belum ada bukti bahwa tema ini sendiri bisa menarik jutaan pemain. Game besar seperti DTI dan Grow a Garden sukses karena **lapisan sosialnya** (voting runway, trading/mencuri), bukan karena temanya saja [S11], [S14].

### 5.3 Scorecard kecocokan

| Dimensi | Bobot | Skor (1–5) | Alasan | Sumber |
|---|---|---|---|---|
| Kecocokan fantasi & genre | 20% | **4,5** | Ekspresi diri + toko sejalan dengan genre top Roblox | [S10], [S12], [S9] |
| Kecocokan audiens | 15% | **4,0** | Mobile-first, tren pemain perempuan naik | [S4], [S7] |
| Kemampuan mekanik dipindah | 15% | **3,0** | Spray/stencil/stiker mudah dibuat. Marble, acrylic pour, dan paint butuh `EditableImage` (beta) | [GDD-02], [S23] |
| Kecocokan monetisasi | 20% | **2,0** | Model ad-first harus dibangun ulang dari nol | [GDD-07], [S18] |
| Potensi retensi & sosial | 15% | **2,5** | Asli single-player dengan konten 25 hari. Butuh desain sosial baru | [GDD-04], [GDD-09], [S20] |
| Persaingan / celah pasar | 10% | **4,0** | Belum ada pesaing langsung yang kuat | [S15], [S16] |
| Risiko IP & kebijakan | 5% | **4,0** | IP sudah diganti. Gacha mudah dibuat patuh | [PROTO], [S24] |
| **Total tertimbang** | 100% | **3,4** | **Worth diadaptasi, asalkan monetisasi dan lapisan sosial didesain ulang** | |

---

## 6. Aksesibilitas dan Kontrol Device

### 6.1 Input yang dipakai game asli
Semua interaksi memakai satu jari: drag untuk spray/paint, tap untuk pop-it, **hold** untuk injection ("HOLD TO INJECT"), drag & scale untuk stiker (`MoveSticker2d`) [GDD-02]. Prototype v1 sudah memakai Pointer Events (mouse dan touch dalam satu jalur) [PROTO].

### 6.2 Pemetaan per device

| Aksi | Mobile (touch) | PC (mouse/keyboard) | Konsol (gamepad) |
|---|---|---|---|
| Spray / paint (drag) | Drag satu jari | Klik kiri + drag | Stik kiri menggerakkan kursor virtual, RT untuk semprot |
| Pop-it (tap) | Tap | Klik | A pada kursor |
| Injection (hold) | Tahan | Tahan klik / Spasi | Tahan RT |
| Stiker: pindah / skala / putar | Drag + pinch + rotasi dua jari | Drag + scroll wheel + Q/E | Stik kiri + LB/RB untuk skala, stik kanan untuk putar |
| Undo / Redo | Tombol UI | Ctrl+Z / Ctrl+Y + tombol UI | X / Y |
| Pindah langkah | Tombol besar di bawah | Tombol + Enter | A / B |
| Jalan di studio | Thumbstick virtual default Roblox | WASD | Stik kiri |

**Dasar teknis:** dokumentasi Roblox mendukung mouse/keyboard, touch, dan gamepad. Developer disarankan mendeteksi input utama memakai `UserInputService.PreferredInput`, bukan `TouchEnabled`, karena laptop touchscreen juga terdeteksi sebagai touch. Gesture swipe/pinch dan haptic tersedia di mobile. `ContextActionService` bisa membuat tombol touch otomatis [S25].

### 6.3 Checklist aksesibilitas
| # | Poin | Alasan |
|---|---|---|
| 1 | Target sentuh besar, terutama palet warna (25 warna spray). Gunakan grid yang bisa di-scroll | Mayoritas pemain di layar HP [S4] |
| 2 | **Jangan hanya mengandalkan warna.** Permintaan pelanggan mewajibkan warna **sama persis (RGBA)** [GDD-04]. Tambahkan nama/ikon/pola pada setiap warna dan tanda ✔ saat cocok | Ramah buta warna [DUGAAN] |
| 3 | Mode "hold" punya alternatif tap-toggle | Pemain dengan keterbatasan motorik |
| 4 | Haptic saat pop-it dan injection | Didukung di iPhone/Pixel/Galaxy [S25]. Memperkuat rasa *satisfying* |
| 5 | Teks pendek + ikon, dukung lokalisasi | Game asli mendukung 16 bahasa [GDD-10]. ±35% pemain di bawah 13 [S3] |
| 6 | Jangan ada UI yang berkedip saat input berganti (touch ↔ gamepad) | Diperingatkan di dokumentasi input Roblox [S25] |
| 7 | Uji di device low-end, siapkan fallback saat `EditableImage` gagal dibuat (API bisa mengembalikan `nil` saat memori habis) | [S23] |

---

## 7. Perubahan yang Perlu Dilakukan untuk Diadaptasi

Diurutkan dari prioritas tertinggi.

### P0: wajib sebelum rilis

| # | Perubahan | Dari → Ke | Alasan / Sumber |
|---|---|---|---|
| 1 | **Rombak monetisasi** | Interstitial + RV → Game Pass, Developer Product, dan RV opsional untuk 13+ | Tidak ada interstitial di Roblox, RV hanya untuk 13+ [S18]. Lihat tabel [3.2](#32-pemetaan-monetisasi-rv--robux) |
| 2 | **Hapus ±75 slot interstitial** | Setiap transisi langkah memanggil iklan → transisi langsung | [GDD-07] |
| 3 | **Lapisan sosial** | Solo → studio di server bersama, pemain bisa mengunjungi studio orang lain, showcase dengan like/voting | Algoritma menilai retensi dan play time [S20]. DTI sukses lewat penilaian antar pemain [S11] |
| 4 | **Leaderboard nyata** | 499 bot dengan skor tetap → `OrderedDataStore` global + leaderboard server, tetap memakai skor per aksi | Leaderboard palsu mudah ketahuan di lingkungan multipemain [GDD-09] |
| 5 | **Case bisa dipakai di avatar** | Hanya disimpan di album foto → accessory di avatar dalam experience | Hook identitas [S12] |
| 6 | **Patuh kebijakan gacha** | Skin roll / spin wheel tanpa info peluang → tampilkan semua hasil + peluang numerik | [S24] |
| 7 | **Painting di Roblox** | P3D Paint + simulasi fluida → `EditableImage` dengan resolusi rendah, plus fallback berbasis decal/pola untuk device lemah | [S23]. Developer pemilik experience wajib verifikasi 13+ dan ID |

### P1: penting untuk retensi

| # | Perubahan | Dari → Ke | Alasan / Sumber |
|---|---|---|---|
| 8 | **Sesi lebih panjang** | 1 level = 1 pelanggan, lalu popup → antrean pelanggan terus-menerus di toko (gaya tycoon), tanpa layar menu di antara pesanan | Sesi < 6 menit ≈ D1 6% [S13] |
| 9 | **Endgame tanpa batas** | Tabel dikunci di Day 25 → pesanan prosedural, rank studio, tema mingguan | [GDD-04], [GDD-11] poin 4 |
| 10 | **Event & liveops** | Remote CSV CrazyLabs → konfigurasi di ModuleScript/DataStore + kalender update mingguan | [GDD-08], [S11] |
| 11 | **Mode spesial jadi momen server** | VIP/Auction privat → Auction dengan penawar = pemain lain atau NPC yang dilihat semua orang di server | [GDD-03] [DUGAAN] |
| 12 | **Couple order jadi co-op** | 2 case serasi dibuat sendiri → 2 pemain berkolaborasi | [GDD-03] [DUGAAN] |
| 13 | **Idle income** | Worker sementara lewat RV → worker permanen dibeli dengan koin, atau booster lewat Game Pass | [GDD-05], [S14] |

### P2: penyesuaian dan polish

| # | Perubahan | Dari → Ke | Alasan / Sumber |
|---|---|---|---|
| 14 | **Kurangi popup** | 11 popup berantrean di Home → satu notifikasi ringan di HUD | [GDD-07]. Popup beruntun memotong sesi [DUGAAN] |
| 15 | **Kontrol multi-device** | Hanya touch → touch + mouse + gamepad, deteksi `PreferredInput` | [S25] |
| 16 | **Konten orisinal penuh** | Placeholder di prototype → set stiker, warna, keychain orisinal. Tetap tanpa IP pihak ketiga | [PROTO], [GDD-11] poin 14 |
| 17 | **Bahan Revenge disesuaikan** | "Poop spray", "poison glue", dan dialog "I STOLE THIS PHONE" → dicek ulang terhadap kebijakan konten dan rating umur | [GDD-03] [DUGAAN] |
| 18 | **Kebijakan chat dan umur** | Tidak relevan di mobile → interaksi sosial memakai fitur bawaan Roblox (emote, like, preset) supaya aman untuk <13 | [S3] |

### Yang sebaiknya **dipertahankan** dari game asli
| Elemen | Alasan | Sumber |
|---|---|---|
| Tanpa kondisi gagal, bintang deterministik | Cocok untuk genre santai di Roblox | [GDD-04], [S14] |
| VIP tiap 3 pelanggan | Ritme "momen spesial" tanpa menaikkan kesulitan | [GDD-03] |
| Reward linear + sink studio ±77% pendapatan | Mudah di-tuning, sudah teruji | [GDD-05] |
| Gacha tanpa duplikat dengan harga naik | Terasa adil dan mudah dibuat patuh kebijakan disclosure | [GDD-06], [S24] |
| Skor leaderboard lebih tinggi untuk maker baru | Mengarahkan pemain mencoba konten yang mahal dibuat | [GDD-09] |
| Semua angka di tabel data | Tuning tanpa rilis ulang | [GDD-08] |

---

## Daftar Sumber

### Internal
| Kode | File |
|---|---|
| GDD-02 | [02_Mekanik_Maker.md](GameDesign/02_Mekanik_Maker.md) |
| GDD-03 | [03_Pelanggan.md](GameDesign/03_Pelanggan.md) |
| GDD-04 | [04_LevelDesign_Pacing.md](GameDesign/04_LevelDesign_Pacing.md) |
| GDD-05 | [05_Ekonomi.md](GameDesign/05_Ekonomi.md) |
| GDD-06 | [06_Gacha.md](GameDesign/06_Gacha.md) |
| GDD-07 | [07_Monetisasi.md](GameDesign/07_Monetisasi.md) |
| GDD-08 | [08_LiveOps_AB.md](GameDesign/08_LiveOps_AB.md) |
| GDD-09 | [09_Retensi_Sosial.md](GameDesign/09_Retensi_Sosial.md) |
| GDD-10 | [10_Konten.md](GameDesign/10_Konten.md) |
| GDD-11 | [11_Pelajaran.md](GameDesign/11_Pelajaran.md) |
| PROTO | [Prototype v1/README.md](Prototype%20v1/README.md) |

### Eksternal
| # | Sumber | Jenis |
|---|---|---|
| S1 | [Gaming.net: Roblox Q3 revenue rises 16% as bookings fall 12% to $1.7B](https://gaming.net/roblox-q3-revenue-rises-16-as-bookings-fall-12-to-1-7-billion) | Berita (laporan Q3 2026) |
| S2 | [Quartr: Roblox Q3 2026 earnings summary](https://quartr.com/events/roblox-rblx-q3-2026_ozGBemPh) | Ringkasan earnings |
| S3 | [Statista: Roblox users by age](https://www.statista.com/statistics/1190869/roblox-games-users-age/), [DemandSage: How many people play Roblox](https://www.demandsage.com/how-many-people-play-roblox/) | Statistik / agregator |
| S4 | [PocketGamer.biz: 80% of Roblox users are on mobile, contributing 46% of Robux revenue](https://www.pocketgamer.biz/80-of-roblox-users-are-on-mobile-contributing-46-of-robux-revenue) | Berita industri |
| S5 | [Mobidictum: Phone Case DIY hits 200 million downloads (Okt 2022)](https://mobidictum.com/crazylabs-phone-case-diy-hits-200-million-downloads/) | Berita industri |
| S6 | [Mobidictum: CrazyLabs celebrates 7 billion downloads](https://mobidictum.com/crazylabs-celebrates-7-billion-downloads/) | Berita industri |
| S7 | [Apptopia: Female WAUs now outnumber male users on Roblox mobile (Jul 2026)](https://apptopia.com/en/insights/female-waus-now-outnumber-male-users-on-roblox-mobile/) | Riset panel device AS |
| S8 | [AppGoblin: Phone Case DIY](https://appgoblin.info/apps/com.newnormalgames.phonecasediy/trends) | Tracker pihak ketiga (estimasi) |
| S9 | [GameDevReports: Newzoo, Roblox as a Platform in 2025](https://gamedevreports.substack.com/p/newzoo-roblox-as-a-platform-in-2025) | Riset (Newzoo) |
| S10 | [RoWatcher: Dress To Impress, 9.7 billion visits](https://rowatcher.com/news/dress-to-impress-how-a-teen-developer-s-fashion-game-hit-9-7-billion-visits), [Rolimons: DTI Group](https://www.rolimons.com/group/17264167) | Tracker pihak ketiga |
| S11 | [Kotaku AU: Dress to Impress](https://kotaku.com.au/?p=1363719), [Pocket Tactics: DTI visits](https://pockettactics.com/dress-to-impress-visits) | Berita |
| S12 | [GamesBeat: Roblox saw 274M daily avatar updates in 2025](https://gamesbeat.com/roblox-saw-274m-daily-avatar-updates-in-2025/) | Berita (data Roblox) |
| S13 | [GameAnalytics: 2025 Roblox Report](https://www.gameanalytics.com/reports/2025-roblox-report), [The 2025 Roblox Benchmark Report](https://gameindustrylibrary.com/documents/the-2025-roblox-benchmark-report), [RoWatcher: Genre dictates retention targets](https://rowatcher.com/news/genre-dictates-retention-targets-stop-benchmarking-wrong) | Laporan benchmark pihak ketiga |
| S14 | [PocketGamer.biz: Grow a Garden hits 21.3M concurrent users](https://www.pocketgamer.biz/robloxs-grow-a-garden-hits-industry-record-213m-concurrent-users-surpassing-pubg-fortnite-and-more), [News4Jax/AP: Grow a Garden](https://www.news4jax.com/business/2025/07/30/millions-are-flocking-to-grow-virtual-gardens-in-viral-roblox-game-created-by-teenager/) | Berita |
| S15 | [Rotrends: Phone Store Tycoon](https://rotrends.com/game/7818137963), [RoWatcher: Phone Store Tycoon](https://rowatcher.com/games/7818137963/phone-store-tycoon) | Tracker pihak ketiga |
| S16 | [RoWatcher: Make a Cake!](https://rowatcher.com/games/26494385/make-a-cake) | Tracker pihak ketiga |
| S17 | [Business Wire: Roblox DevEx increase (Sept 2025)](https://www.businesswire.com/news/home/20250905587466/en), [NetInfluencer: 18+ DevEx rate](https://www.netinfluencer.com/roblox-to-raise-developer-exchange-rate-for-games-aimed-at-18-plus-players-as-adult-cohort-surges/) | Rilis resmi / berita |
| S18 | [DevForum: More Creators Can Now Use Rewarded Video Ads](https://devforum.roblox.com/t/more-creators-can-now-use-rewarded-video-ads/3838678), [MediaPost: Roblox expanded rewarded video placements](https://www.mediapost.com/publications/article/417959/) | Resmi (DevForum) / berita |
| S19 | [Roblox Creator Docs: Immersive ads](https://create.roblox.com/docs/en-us/production/monetization/immersive-ads) | Dokumentasi resmi |
| S20 | [Roblox Newsroom: Optimizing discovery (Jun 2026)](https://about.roblox.com/newsroom/2026/06/optimizing-discovery-great-games-reach-millions-players-roblox), [DevForum: 2025 Discovery Roadmap](https://devforum.roblox.com/t/roblox’s-2025-discovery-roadmap-and-ways-to-reach-and-engage-your-audience/3557533) | Resmi |
| S21 | [Game World Observer: Hyper-casual 167m sessions a year](https://gameworldobserver.com/2019/07/02/hyper-casual-167m-sessions-a-year), [GameDevReports: GameAnalytics hypercasual metrics](https://gamedevreports.substack.com/p/gameanalytics-hypercasual-games-metrics) | Benchmark (data lama 2019 + ringkasan) |
| S22 | [RoWatcher: From zero to 1 million](https://rowatcher.com/news/from-zero-to-1-million-how-long-does-it-actually-take) | Opini komunitas (anekdotal) |
| S23 | [DevForum: In-experience Mesh & Image APIs in published experiences](https://devforum.roblox.com/t/client-beta-in-experience-mesh-image-apis-now-available-in-published-experiences/3267293), [Creator Docs: EditableImage](https://create.roblox.com/docs/en-us/reference/engine/classes/EditableImage.md) | Resmi |
| S24 | [Roblox Creator Docs: Paid random items policy](https://create.roblox.com/docs/en-us/production/monetization/paid-random-items) | Kebijakan resmi |
| S25 | [Roblox Creator Docs: Input](https://create.roblox.com/docs/en-us/input), [Mobile input](https://create.roblox.com/docs/input/mobile.md), [ContextActionService](https://create.roblox.com/docs/reference/engine/classes/ContextActionService) | Dokumentasi resmi |

### Tingkat keyakinan sumber
- **Tinggi:** dokumen resmi Roblox (S18–S20, S23–S25), laporan Q3 2026 (S1–S2), data teardown internal.
- **Sedang:** berita industri (S4–S7, S11, S12, S14, S17), Newzoo (S9).
- **Rendah, hanya indikatif:** tracker pihak ketiga (S8, S10, S15, S16), benchmark lama (S21), opini komunitas (S22).
