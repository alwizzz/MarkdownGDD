# 06. Pelanggan & Device

[← Kembali ke indeks](00_README.md)

## 1. Tipe pelanggan

Lima tipe dari draft [DRAFT]. Perilaku tiap tipe diadaptasi dari tipe pelanggan game sumber [SRC 03] supaya setiap tipe punya "rasa" berbeda, bukan hanya pengali angka.

| Tipe | Buka | Padanan di game sumber | Peran desain |
|---|---|---|---|
| **Normal** | L1 | Normal | Pesanan standar, pengisi ritme |
| **Fancy Girl/Boy** | L3 | VIP | Pesanan rewel tapi bayaran besar. Momen "spesial" berkala |
| **Thief** | L5 | Revenge | Momen lucu dan kejutan. Mini-event mengejar pencuri |
| **Old Club** | L7 | Couple | Pesanan 2 case serasi (berpasangan) |
| **Rich Kid** | L9 | Auction | Bayaran tertinggi + tawar-menawar |

### Normal (L1)
| | |
|---|---|
| Penampilan | Variasi warga kota (12 kombinasi rambut/baju) |
| Request | 1–2 elemen (warna selalu, kadang pola/stiker) |
| Pengali | Cash ×1,0, XP ×1,0 |
| Dialog contoh | "Pink please!", "Make it cute!", "Surprise me!" |

### Fancy Girl/Boy (L3)
| | |
|---|---|
| Penampilan | Baju modis, kacamata hitam, tas kecil. Berjalan dengan animasi "catwalk" |
| Frekuensi | Kira-kira **1 dari 4** pelanggan (mirip VIP tiap 3 pelanggan di game sumber) |
| Request | 2–3 elemen, **selalu menyebut bentuk** (Bunny/Kitty Ears) dan warna. L6+: sering minta Glossy |
| Pengali | Cash ×1,5, XP ×1,3 |
| Bonus | Jika 3★: pose foto + efek blitz, pemain mendapat **"Style Star"** (+1 ke progres badge "Fashion Favorite") [USULAN] |
| Dialog contoh | "Only the cutest shape for me~", "Glossy. Obviously." |

### Thief (L5)
| | |
|---|---|
| Penampilan | Topi kupluk, topeng mata ala kartun, langkah mengendap-endap. **Gaya komedi, bukan menakutkan** |
| Alur | Memesan seperti biasa. Begitu case selesai, Thief menyambar case dari bench dan **lari ke pintu**. Bayaran ditahan sampai kejar-kejaran selesai. Tombol besar **STOP THIEF!** muncul selama 3 detik (tap / [E] / A). Pemain juga bisa mengejar dan menyentuhnya |
| Berhasil dihentikan | Thief tersandung lucu, membayar penuh ×1,2 + kata **CAUGHT!** + badge "Shop Guardian" (pertama kali) |
| Gagal | Thief lolos tetapi menjatuhkan 50% pembayaran ("He dropped some cash!"). **Tidak ada kerugian di luar itu** |
| Frekuensi | ±12–15% pelanggan di L5+ |
| Pengali | Cash ×1,2 (tertangkap) / ×0,5 (lolos), XP ×1,2 |
| Catatan konten | Tidak ada kekerasan, tidak ada kata "steal phone" yang realistis. Nama tampil: "Sneaky Sam" dkk. Bahan jahil game sumber (poop spray, poison glue) **tidak dipakai** [SRC Analisis P2 #17] |

### Old Club (L7)
| | |
|---|---|
| Penampilan | Pasangan kakek-nenek / anggota klub lansia, topi golf, kardigan |
| Alur | Memesan **2 case serasi** sekaligus (2 device, desain sama atau warna berpasangan). Pemain mengerjakan case pertama, lalu case kedua langsung dimulai di bench yang sama dengan langkah yang sama (Case Shape otomatis terpilih sama) |
| Request | Warna klasik (Cream, Navy, Forest Green, Cocoa), sering "Matching please!" |
| Pengali | Cash ×1,3 **per case** (total ×2,6), XP ×1,6 |
| Sentuhan | Saat menerima, mereka berdansa pelan bersama. Dialog: "Just like the old days!" |

### Rich Kid (L9)
| | |
|---|---|
| Penampilan | Anak dengan jaket bling, kacamata emas, diiringi bodyguard NPC kecil |
| Request | 3–4 elemen, hampir selalu Glossy + pola + stiker. Sering membawa **Tablet atau Macbook** |
| Pengali | Cash ×2,0, XP ×1,5 |
| **Bonus Offer** (adaptasi Auction) | Begitu case selesai, Rich Kid menawarkan tip: kartu **×1,0–1,6** dari bayaran. Pemain bisa **ACCEPT** atau **HAGGLE** sekali: 60% tawaran naik +25%, 40% tawaran tetap (tidak pernah turun) |
| Catatan kebijakan | Tawaran acak ini tidak dibeli dengan Robux, jadi bukan "paid random item" [SRC Analisis S24] |

---

## 2. Device

Dari draft [DRAFT]: 2 phone, 1 tablet, 1 Macbook, 1 Earpod.

| Device | Buka | Gaji dasar | Faktor waktu | Bentuk V1 | Catatan art |
|---|---|---|---|---|---|
| **Aphone 18 Pro Max** | L1 | 14 | 1,0× | Slim, Bumper, Bunny Ears, Kitty Ears | Kamera 3 lensa dalam modul persegi besar di pojok kiri atas. Referensi: [ref_aphone18promax.png](assets/referensi_device/ref_aphone18promax.png) |
| **Samsam X26 Ultra** | L3 | 18 | 1,0× | Slim, Bumper, Bunny Ears, Kitty Ears | Kamera vertikal 3 lensa + 1 lensa pil dalam "pulau" di kiri atas, sudut lebih kotak. Referensi: [ref_samsam_x26ultra.png](assets/referensi_device/ref_samsam_x26ultra.png) |
| **Earpod** | L5 | 10 | 0,7× | Round Shell, Bear Ears | Case kotak kecil membulat. Langkah cepat (level "istirahat" seperti Cleaning di game sumber) |
| **Tablet** | L7 | 28 | 1,4× | Folio, Slim Bumper | Area besar. Grid painting lebih lebar, stiker lebih kecil relatif |
| **Macbook** | L9 | 38 | 1,7× | Hard Shell, Bumper Corners | Shell laptop. Step 6 membersihkan layar dan keyboard |

> ⚠️ Nama dan foto referensi meniru produk nyata. Gambar referensi berisi logo merek (Caudabe, Freewell). **Hanya siluet umum yang boleh dipakai**: jangan menyalin logo, ikon apel/brand, atau bentuk modul kamera yang identik. Lihat risiko nama parodi di [16](16_Roadmap_KPI_Risiko.md#5-risiko).

---

## 3. Pembuatan request (order generator)

Setiap pesanan dibuat di server saat pelanggan muncul.

```
1. Pilih tipe pelanggan  → bobot per level (tabel 3a)
2. Pilih device          → bobot per level (tabel 3b)
3. Tentukan langkah      → Shape, Paint, Smoothing, Cleaning selalu ada
                           + Pattern (70% jika terbuka)
                           + Sticker (60% jika terbuka)
                           + Glossy (40% jika terbuka; Fancy/Rich 70%)
4. Tentukan request      → jumlah elemen sesuai tipe pelanggan,
                           dipilih dari bahan yang SUDAH TERBUKA untuk pemain
5. Hitung gaji dasar & waktu target → rumus di 08_Ekonomi dan 04_Mekanik_HandsOn
```

### 3a. Bobot tipe pelanggan
| Level | Normal | Fancy | Thief | Old Club | Rich Kid |
|---|---|---|---|---|---|
| 1–2 | 100% | — | — | — | — |
| 3–4 | 75% | 25% | — | — | — |
| 5–6 | 60% | 25% | 15% | — | — |
| 7–8 | 50% | 22% | 13% | 15% | — |
| 9–10 | 45% | 20% | 12% | 13% | 10% |

Aturan tambahan [USULAN]:
- Pelanggan pertama setelah level-up yang membuka tipe baru **selalu** tipe baru itu (perkenalan).
- Thief tidak muncul dua kali berturut-turut.
- Fancy dijamin muncul minimal 1× per 5 pelanggan (pity ringan).

### 3b. Bobot device
| Level | Aphone | Samsam | Earpod | Tablet | Macbook |
|---|---|---|---|---|---|
| 1–2 | 100% | — | — | — | — |
| 3–4 | 60% | 40% | — | — | — |
| 5–6 | 45% | 35% | 20% | — | — |
| 7–8 | 35% | 30% | 15% | 20% | — |
| 9–10 | 30% | 25% | 15% | 15% | 15% |

### 3c. Jumlah elemen request
| Tipe | Jumlah elemen | Elemen yang mungkin |
|---|---|---|
| Normal | 1–2 | warna (selalu), pola / stiker |
| Fancy | 2–3 | warna + bentuk (selalu), pola / finish |
| Thief | 1 | warna |
| Old Club | 2 per case | warna + "matching" |
| Rich Kid | 3–4 | warna + finish Glossy + pola + stiker |

- Request "Surprise me!" (tanpa elemen) muncul 10% pada pelanggan Normal. Pemain bebas berkreasi dan otomatis mendapat bonus kesesuaian.
- Request hanya memakai bahan yang sudah dimiliki pemain, sehingga **semua request selalu bisa dipenuhi**.
