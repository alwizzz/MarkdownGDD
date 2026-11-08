# 12. Art Style & World

[← Kembali ke indeks](00_README.md)

## 1. Arah utama [DRAFT]
> **Low poly dengan warna mencolok.** Target market unisex, dengan warna yang lebih condong menarik pemain perempuan.

| Kata kunci | Artinya di produksi |
|---|---|
| **Low poly** | Bentuk sederhana dengan sudut terlihat (faceted), shading datar/halus. Tanpa tekstur foto |
| **Mencolok** | Saturasi tinggi tetapi tidak neon semua: pastel cerah sebagai dasar, aksen jenuh untuk objek penting |
| **Unisex condong feminin** | Pink, lavender, mint, peach dominan. Diimbangi biru, teal, dan hitam supaya pemain laki-laki tetap nyaman |
| **Mudah dibaca di HP** | Siluet jelas, kontras tinggi antara objek interaktif dan latar |

Prototype v1 yang sudah ada juga memakai 3D low-poly gaya blocky [SRC Analisis 4], jadi arah ini melanjutkan yang sudah dibuat.

## 2. Palet dunia

| Peran | Warna | Hex |
|---|---|---|
| Rumput taman | Hijau mint cerah | `#8EE59B` |
| Jalan kota | Abu krem | `#E9E1D6` |
| Dinding toko default | Krem hangat | `#FFF1E0` |
| Atap / awning | Pink + putih belang | `#FF8FC7` / `#FFFFFF` |
| Kayu (bench, rak) | Kayu madu | `#E0A96D` |
| Langit siang | Biru muda gradasi | `#A8DBFF → #E8F6FF` |
| Aksen interaktif | Kuning hangat | `#FFD23F` |
| Bayangan | Ungu lembut (bukan hitam) | `#6B5B95` 30% |

**Pencahayaan:** `Lighting.Technology = Future` di PC, otomatis turun di mobile. Satu waktu tetap (siang cerah) di V1. Atmosphere tipis supaya kota terasa luas.

## 3. Plot & toko

| Bagian | Arahan |
|---|---|
| Plot | ±80 × 80 studs, batas dengan pagar putih rendah dan semak |
| Taman awal (luas) | Rumput, bunga warna-warni (low-poly), 3–4 pohon bulat, bangku, kolam kecil dengan bebek. Taman adalah "hadiah visual" yang perlahan berkurang [DRAFT] |
| Bangunan awal | ±28 × 24 studs. Kaca etalase besar di depan supaya pemain lain bisa melihat isi toko dari jalan |
| Awning & papan nama | Elemen paling terlihat dari jalan. Berubah sesuai dekor papan nama |
| Ekspansi L8 | Dinding depan dan samping maju ke taman, ±44 × 32 studs. Taman tersisa jalur bunga + 2 pohon [DRAFT] |
| Interior | Lantai, dinding, plafon sederhana. Semua objek pada **slot tetap** dengan penanda lantai halus |

## 4. Device & case

| Device | Arahan bentuk | Referensi |
|---|---|---|
| Aphone 18 Pro Max | Persegi panjang tinggi, sudut membulat besar, modul kamera **persegi** besar kiri atas berisi 3 lensa segitiga | [ref_aphone18promax.png](assets/referensi_device/ref_aphone18promax.png) |
| Samsam X26 Ultra | Sudut lebih tegas/kotak, kamera **pulau vertikal** kiri atas (3 lensa bulat + 1 lensa pil) | [ref_samsam_x26ultra.png](assets/referensi_device/ref_samsam_x26ultra.png) |
| Earpod | Kotak kecil membulat seperti kerikil | — |
| Tablet | Persegi besar, bezel tipis, 1 lensa | — |
| Macbook | Laptop tertutup, shell atas adalah area kreasi | — |

**Aturan IP:** jangan memasukkan logo, tulisan merek, atau ikon apa pun dari foto referensi (Caudabe, Freewell, logo MagSafe, dll.). Siluet dibuat sedikit lebih "kartun" (lebih tebal, sudut lebih bulat) daripada HP asli.

### Case
- Setiap bentuk case = 1 MeshPart dengan **UV back-face rapi** dalam satu area persegi (untuk grid painting dan stiker).
- Bentuk "telinga" (Bunny, Kitty, Bear) menempel di atas case, ikut warna dasar.
- Bahan: Matte = `SmoothPlastic` dengan reflectance 0. Glossy = `SmoothPlastic` reflectance 0,15 + highlight decal.
- Pola = Decal/Texture semi-transparan yang diberi warna lewat `Color3`. Glitter = decal titik-titik + `Sparkles`/ParticleEmitter kecil saat dilihat dekat.

## 5. Karakter

| Karakter | Arahan |
|---|---|
| Pemain | Avatar Roblox sendiri. Saat craft, avatar memakai celemek toko (accessory sementara) |
| NPC pelanggan | Rig R15 dengan pakaian low-poly yang dibuat tim. Proporsi sedikit chibi (kepala lebih besar) supaya berbeda dari avatar pemain dan terlihat ramah |
| Normal | 12 kombinasi rambut/baju kasual |
| Fancy Girl/Boy | Pakaian modis, kacamata hitam, tas kecil. Warna pastel + aksen emas |
| Thief | Kupluk garis-garis, topeng mata kartun, karung kecil. Lucu, tidak seram |
| Old Club | Kardigan, topi golf, kacamata bulat. Selalu berpasangan |
| Rich Kid | Jaket bling, kacamata emas, sepatu kets mahal. Diikuti bodyguard mini |
| Karyawan | Celemek pink + topi pet. Variasi warna kulit, rambut, dan nama |
| Kasir | Celemek + headset |

## 6. Efek visual (VFX)

| Momen | Efek |
|---|---|
| Spray | Kabut partikel sesuai warna, sedikit "splat" di tepi |
| Smoothing | Debu putih halus, kilau menyapu |
| Glossy | Garis kilau diagonal melintas case |
| Glitter | Partikel bintang kecil berkilau, jatuh dan menempel |
| Stiker menempel | Kilat putih + bounce |
| Kata konfirmasi | Teks 3D/2D besar + bintang meletup |
| Case selesai 3★ | Konfeti kecil di bench + koin melayang ke HUD + hati dari pelanggan saat mengambil case |
| Level-up | Konfeti layar penuh + cahaya dari papan nama toko |
| Build tycoon | Kardus jatuh, "poof" asap pastel, item muncul dengan bounce |
| Ekspansi toko | Debu, dinding naik, lantai tumbuh ke depan |
| Cash masuk | Koin melayang ke ikon cash di HUD |

## 7. Batas performa (mobile low-end)
| Item | Batas |
|---|---|
| Part per plot (toko penuh L10) | ≤ 1.500 |
| Tekstur unik per case | 0 (case dibangun dari decal bersama + warna), lihat [14](14_Teknis_Programmer.md#1-keputusan-teknis-kunci) |
| NPC dengan animasi penuh per plot | ≤ 10 (pelanggan + karyawan + kasir) |
| ParticleEmitter aktif | Hanya di plot pemain sendiri dan saat dekat (≤ 60 stud) |
| StreamingEnabled | Aktif. Plot lain dimuat sesuai jarak |
