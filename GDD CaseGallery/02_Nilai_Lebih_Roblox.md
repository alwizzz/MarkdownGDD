# 02. Nilai Lebih di Roblox

[← Kembali ke indeks](00_README.md)

Dokumen ini menjawab: **apa yang membuat Phone Case Gallery lebih bernilai dibanding Phone Case DIY di mobile**, dan apa yang kita pelajari dari Fix My Phone.

## 1. Perbandingan langsung

| Aspek | Phone Case DIY (mobile) [SRC] | Phone Case Gallery (Roblox) | Nilai lebih |
|---|---|---|---|
| **Struktur level** | 1 level = 1 pelanggan, lalu layar hasil + iklan | Toko berjalan terus. Antrean selalu terisi, pemain bebas memilih pesanan | Sesi lebih panjang, tidak ada "titik berhenti" setiap 1 menit |
| **Peran pemain** | Hanya pengrajin | Pengrajin **dan** pemilik toko (kasir, karyawan, ekspansi) | Dua lapis progres: skill craft dan toko |
| **Sosial** | Solo, leaderboard 499 bot | Kota 8 pemain, visit toko, like, bonus teman, Best Case of the Week | Alasan mengajak teman, sesuai algoritma Roblox yang menilai retensi |
| **Hasil craft** | Disimpan di album foto | Dipajang di rak toko, dipegang avatar, masuk galeri kota | Kreasi jadi identitas yang dilihat orang lain |
| **Dekor studio** | Ruang 2D yang hanya dilihat sendiri | Toko 3D yang bisa dimasuki pemain lain | Dekorasi punya nilai pamer |
| **Idle income** | Worker sementara lewat iklan, cap 5 jam | Karyawan permanen saat online, display rack saat offline (cap 3 jam, 8 jam dengan gamepass) | Lebih adil, tidak bergantung iklan |
| **Monetisasi** | ±75 titik interstitial + rewarded video | Tanpa iklan paksa. Gamepass, Gems, Developer Product | Pengalaman bersih, pemain tidak terganggu |
| **Konten setelah habis** | Terkunci di Day 25, reward berhenti naik | Galeri mingguan + update konten level 11+ | Ada tujuan jangka panjang |
| **LiveOps** | Remote CSV dari server publisher | Config di ModuleScript/DataStore, codes, event mingguan | Update rutin yang diharapkan pemain Roblox |
| **Cross-device** | Satu HP | Progres sama di HP, PC, konsol | Pemain bisa lanjut di mana saja |

## 2. Apa yang dipelajari dari Fix My Phone [FMP]

Fix My Phone! (Doubloons, rilis 5 Oktober 2026) adalah acuan terdekat. Dalam ±1 bulan mencapai ±12,4 juta visit dan puncak ±21 ribu CCU.

| Pola Fix My Phone | Bukti | Cara kita memakainya |
|---|---|---|
| **8 pemain per server** | Server size maksimal 8, rata-rata 6,1 pemain | Sama dengan draft kita (8 pemain per lobi) [DRAFT] |
| **Hands-on bertahap dengan step counter** | "Step 1 of 6" untuk HP sendiri, "Step X of 7" untuk pesanan pelanggan | Langkah craft memakai counter "Step X of N" |
| **Kata konfirmasi tiap langkah** | CLEAN!, FRESH!, SPOTLESS, NO BUBBLES, IT WORKS! | Setiap langkah punya kata pujian sendiri |
| **Order card** | Menampilkan device, kerusakan, dan request tambahan (contoh: case pink) | Order card menampilkan device, warna, pola, stiker, finish |
| **Tombol besar berlabel aksi** | I'LL FIX IT!, PUT DOWN, TURN IT ON, LEAVE | Tombol aksi besar: I'LL MAKE IT!, PUT DOWN, TURN IT ON |
| **Panduan lantai** | Panah kuning di lantai dan cincin kuning bercahaya di titik interaksi | Dipakai untuk FTUE dan setiap unlock baru |
| **Next unlock selalu terlihat** | "Next Level: 3 – Parts Cabinet" | HUD menampilkan "Next: Lv 3 – Employee" |
| **In-game phone sebagai menu** | Pesanan, menu, dan Codes ada di HP dalam game | Seluruh menu dikemas sebagai HP dalam game. Cocok dengan tema kita |
| **Teknisi** | Teknisi mengerjakan HP saat pemain sibuk | Sama dengan karyawan di draft kita [DRAFT] |
| **Bonus cash sosial** | +10%/teman (maks 4), +10% join grup, +20% Roblox Plus | Diadopsi dengan angka yang disesuaikan (lihat [08](08_Ekonomi.md#5-bonus-cash)) |
| **Gamepass alat** | Wide Squeegee 99, Power Screwdriver 99, Magnet Mat 99, Heat Gun Pro 149, Golden Toolkit 399, 2X Customers 199, 2X Shop XP 249, VIP 499 | Struktur gamepass kita mengikuti rentang harga yang sama (lihat [09](09_Monetisasi.md)) |
| **Konten mingguan** | Job Lots dengan tema berganti tiap minggu, case terbatas | Best Case of the Week + tema mingguan |
| **Codes** | RELEASE (2x cash 15 menit), item case, kunci | Sistem codes di app HP sejak rilis |

### Celah Fix My Phone yang kita isi
1. **Kreasi masih terbatas.** Makeover di FMP (spray paint, laser engraving, gems) adalah sampingan dari reparasi. Di game kita, **kreasi adalah inti**.
2. **Tidak ada galeri atau voting.** Hasil pemain FMP tidak dinilai pemain lain. Ini celah yang terbukti besar di Roblox (DTI).
3. **Pasar sedang panas.** Pemain yang suka FMP adalah audiens yang sudah siap untuk game kita. Rilis cepat sebelum tren mendingin adalah keuntungan.

## 3. Ringkasan nilai lebih (untuk pitch)
1. **Tidak ada pesaing langsung untuk "custom case" di Roblox.** Game terdekat (FMP) fokus ke reparasi.
2. **Mekanik sudah terbukti di dua tempat:** craft case (314 juta download di mobile [SRC]) dan toko HP hands-on 8 pemain (FMP di Roblox).
3. **Lapisan sosial yang tidak dimiliki keduanya:** galeri kota dan voting.
4. **Model bisnis lebih bersih:** tanpa iklan paksa, Robux yang dibelanjakan untuk percepatan, kosmetik, dan identitas.
