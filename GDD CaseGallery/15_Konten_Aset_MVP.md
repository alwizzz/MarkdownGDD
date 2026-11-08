# 15. Daftar Konten & Aset MVP

[← Kembali ke indeks](00_README.md)

Semua yang perlu diproduksi untuk V1 (L1–L10). Bandingkan dengan skala game sumber di [GameDesign/10_Konten.md](../GameDesign/10_Konten.md): V1 sengaja jauh lebih kecil, karena konten akan ditambah lewat update rutin.

## 1. Ringkasan jumlah

| Kategori | V1 | Game sumber [SRC 10] |
|---|---|---|
| Level | 10 | 25 hari (120 pelanggan) |
| Langkah craft | 6 (+ sub-step Glossy) | 9 maker |
| Device | 5 | 9 bentuk HP + 6 bundle + 3 device |
| Bentuk case | 16 (lihat bawah) | — |
| Warna | 23 | 25 spray + 25 acrylic |
| Pola | 7 gratis + 2 premium | 15 glitter |
| Stiker | 24 + 1 eksklusif login + 1 code | 81 2D + 37 3D |
| Tipe pelanggan | 5 | 6 aktif |
| Item tycoon | 7 | — |
| Objek dekor | 7 objek × 3 varian = 21 | 125 item studio |
| Dekor permukaan | ±40 opsi | — |
| Dekor premium brand fiksi | 6 | — |
| Gamepass / Dev Product | 9 / 7 | 10 IAP |

## 2. Model 3D

### Device & case
| Aset | Jumlah | Catatan |
|---|---|---|
| Device (badan + layar depan) | 5 | Aphone, Samsam, Earpod, Tablet, Macbook |
| Mesh case | 16 | Aphone ×4, Samsam ×4, Earpod ×2, Tablet ×2, Macbook ×2, + 2 cadangan |

### Toko & tycoon
| Aset | Jumlah |
|---|---|
| Bangunan toko tahap awal + tahap ekspansi | 2 |
| Kasir counter + mesin kasir default | 1 |
| Waiting Table (2–3 slot) | 1 |
| Craft Bench pemain (papan alat terpasang, slot rak di dinding belakang) | 1 |
| Work bench karyawan | 1 (dipakai ×3) |
| Pattern Shelf, Sticker Stock, Glossy Finish Paint Shelf | 3 |
| Display Rack (8 slot, 4 terkunci) + Tip Jar | 2 |
| Kursi tunggu | 1 (dipakai ×6) |
| Hologram (shader/material umum) | 1 |
| Alat craft: kaleng spray, buffer, kuas glossy, toples glitter, roller, kain, botol cleaner | 7 (+7 versi Golden) |

### Dekor
| Aset | Jumlah |
|---|---|
| Stool, Table, Sofa, Plant Pot, Trash Bin, Statue, Fish Tank × 3 varian | 21 |
| Mesin kasir (Retro, Pastel, Gold) | 3 |
| Hiasan dinding | 6 |
| Papan nama toko | 5 |
| Set VIP "Velvet Lounge" | 2 |
| Dekor premium brand fiksi | 6 |

### Kota
| Aset | Jumlah |
|---|---|
| Plot (tanah + pagar + taman) | 1 template |
| Elemen taman: pohon, semak, bunga, bangku, kolam, bebek | ±10 |
| Gallery Square: air mancur, 16 bingkai, 3 papan leaderboard, spot foto, podium patung | ±6 |
| Jalan, lampu jalan, halte, papan petunjuk | ±6 |

### Karakter
| Aset | Jumlah |
|---|---|
| Set pakaian pelanggan Normal | 12 kombinasi |
| Fancy, Thief, Old Club (pasangan), Rich Kid + bodyguard | 6 rig |
| Karyawan (variasi warna) | 6 |
| Kasir | 1 |
| Animasi NPC: jalan, antre, duduk, reaksi senang/biasa, catwalk, jinjit, lari, jatuh lucu, dansa pelan, kerja di bench (3) | ±15 |
| Animasi pemain: craft di bench, pose foto | 2 |

## 3. Tekstur & 2D

| Aset | Jumlah |
|---|---|
| Decal pola (tileable, grayscale untuk diwarnai) | 9 |
| Stiker 2D | 26 |
| Tekstur noda layar | 6 |
| Tekstur kasar (butiran smoothing) | 1 |
| Wallpaper HP (layar menyala) | 5 |
| Motif lantai & tekstur dinding | ±14 |
| Ikon UI: kartu bentuk untuk list HUD (16), app HP (11), mata uang (2), langkah (7), bahan (warna 23 simbol), badge (11), gamepass (9), produk (7) | ±96 |
| Logo game + thumbnail + ikon experience | 1 + 3 + 1 |

### Daftar stiker V1 [USULAN]
| Buka | Stiker |
|---|---|
| L4 (12) | Strawberry, Boba Tea, Donut, Cherry, Bunny Face, Kitty Face, Bear Face, Rainbow, Cloud, Star, Heart, Smiley |
| L6 (+4) | Planet, Rocket, Alien Cutie, Moon |
| L8 (+4) | Butterfly, Flower Daisy, Sparkle, Lightning |
| L10 (+4) | Crown, Diamond, Sunglasses Emoji, Gold Star |
| Login hari ke-7 | 1 stiker eksklusif per minggu (rotasi) |
| Code `SPARKLE` | Launch Star |

## 4. VFX
Lihat daftar di [12](12_Art_Style_World.md#6-efek-visual-vfx): ±12 efek partikel.

## 5. Audio
Lihat [13](13_Sound_Design.md): ±85 SFX unik (±150 file dengan variasi), 4 musik + 1 jingle, 4 ambience.

## 6. Teks
| Aset | Jumlah perkiraan |
|---|---|
| String UI | ±250 |
| Dialog pelanggan (per tipe 6–10 baris) | ±45 |
| Nama warna, pola, stiker, bentuk, dekor | ±120 |
| Bahasa | English + Bahasa Indonesia |
