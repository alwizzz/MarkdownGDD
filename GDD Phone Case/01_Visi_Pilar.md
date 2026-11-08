# 01. Visi & Pilar

[← Kembali ke indeks](00_README.md)

## High concept
> **Phone Case Gallery** adalah tycoon toko custom case di Roblox. Pemain membuat case dengan tangan sendiri lewat mini-game yang *satisfying*, memperbesar toko bersama karyawan, lalu memamerkan karya terbaiknya di galeri kota bersama 7 pemain lain.

**Elevator pitch (1 kalimat untuk store page):** *Craft cute phone cases by hand, grow your shop, and get your best design into the Gallery!*

## Asal-usul desain

| Sumber | Yang diambil | Yang ditinggalkan |
|---|---|---|
| **Phone Case DIY** (mobile) [SRC] | Fantasi bengkel case, langkah craft yang satisfying, pelanggan dengan request, tanpa kondisi gagal, tipe pelanggan spesial, reward linear + sink terukur, idle income dengan cap | Iklan paksa, 1 level = 1 pelanggan, leaderboard bot, konten berhenti di Day 25, IP pihak ketiga |
| **Fix My Phone!** (Roblox) [FMP] | Pola UI (phone menu, step counter, kata konfirmasi, order card), langkah hands-on dengan tombol besar, toko tycoon 8 pemain per server, teknisi, bonus cash teman/grup, gamepass alat | Tema reparasi (kita fokus ke kustomisasi), trade-in / haggle sebagai loop utama |
| **Draft desain (docx)** [DRAFT] | Core loop, kasir + waiting table, 3 karyawan, tycoon vs dekorasi, 5 device, 6 langkah, tabel L1–L10, art low-poly, 8 pemain per lobi, AFK farm, Best Case of the Week, monetisasi | — |

## Pilar desain

| # | Pilar | Artinya | Contoh keputusan |
|---|---|---|---|
| 1 | **Satisfying di tangan** | Setiap langkah craft harus terasa enak: visual berubah langsung, suara jelas, kata konfirmasi muncul. | Setiap langkah punya progress bar, partikel, dan kata pujian (SMOOTH!, SPARKLY!). Lihat [04](04_Mekanik_HandsOn.md). |
| 2 | **Toko yang hidup** | Pemain tidak pernah menunggu tanpa kerjaan. Selalu ada pesanan, karyawan bekerja di sekitar pemain. | Waiting table otomatis terisi lagi [DRAFT]. Lihat [05](05_Toko_Tycoon_Karyawan.md). |
| 3 | **Karyaku dilihat orang** | Hasil craft bukan hanya angka. Case dipajang, dipegang avatar, dan dinilai pemain lain. | Display rack, Best Case of the Week, equip case. Lihat [10](10_Sosial_Retensi.md). |
| 4 | **Selalu ada yang baru di depan** | Setiap level membuka sesuatu yang terlihat (pelanggan, dekorasi, mesin, warna). | Tabel unlock L1–L10 [DRAFT]. Lihat [07](07_Level_Design.md). |
| 5 | **Ramah dan tanpa gagal** | Tidak ada kondisi kalah. Hukuman terburuk adalah tidak mendapat bonus. | Gaji dasar selalu dibayar, bonus kesesuaian & kecepatan hanya menambah. |

## Target audiens

| Aspek | Target | Dasar |
|---|---|---|
| Usia | Inti 9–15 tahun, aman untuk semua umur | ±35% pemain Roblox di bawah 13 tahun [SRC Analisis S3] |
| Gender | Unisex, dengan visual yang lebih condong menarik pemain perempuan | [DRAFT]. Pengguna perempuan Roblox mobile kini melampaui laki-laki [SRC Analisis S7] |
| Device | Mobile dulu (±72–80% pengguna), lalu PC, lalu konsol | [SRC Analisis S3/S4] |
| Motivasi | Ekspresi diri (kreasi), progres (toko tumbuh), sosial (pamer, main bareng teman) | Genre DTI dan tycoon [SRC Analisis 5.2] |
| Sesi | 15–40 menit per sesi, 2–3 sesi per hari | Retensi Roblox naik tajam setelah ±19 menit [SRC Analisis S13] |

## Posisi pasar

| Game | Kesamaan | Pembeda kita |
|---|---|---|
| *Fix My Phone!* (Doubloons) [FMP] | Toko HP, hands-on, tycoon, 8 pemain per server. ±12,4 juta visit, puncak ±21 ribu CCU dalam ±1 bulan sejak rilis 5 Okt 2026 | Fokus pada **kreasi dan ekspresi diri** (case unik buatan pemain), bukan reparasi. Ada galeri dan voting. |
| *Phone Store Tycoon* [SRC] | Tema HP + tycoon | Ada hands-on craft yang satisfying, bukan hanya klik tombol |
| *Make a Cake!* [SRC] | Craft membuat sesuatu | Ada meta toko yang tumbuh dan lapisan sosial |
| *Dress to Impress* [SRC] | Kreasi dinilai pemain lain | Kreasi asinkron lewat galeri mingguan (V1), mode showdown real-time di V1.1 |

**Kesimpulan:** Fix My Phone membuktikan bahwa "toko HP hands-on, 8 pemain per server" sedang laku di Roblox **saat ini** (November 2026). Phone Case Gallery mengambil pola yang sudah terbukti itu, lalu menambahkan sisi kreasi dan galeri yang tidak dimiliki Fix My Phone.

## Non-goal V1
- Trading antar pemain.
- Free-paint (menggambar bebas pixel). Butuh `EditableImage` yang masih beta [SRC Analisis S23]. Lihat [14](14_Teknis_Programmer.md#1-keputusan-teknis-kunci).
- Gacha berbayar. Ditunda ke V1.1 dengan tabel peluang.
- Level di atas 10.
