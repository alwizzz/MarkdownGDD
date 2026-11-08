# 10. Sosial & Retensi

[← Kembali ke indeks](00_README.md)

## 1. Kota 8 pemain (Social Tycoon) [DRAFT]

Draft: *player berada di satu wilayah kota dengan 7 player lainnya, total 8 player dalam 1 lobi. Nantinya bisa visit dan lihat perkembangan.*

Fix My Phone juga memakai server 8 pemain (rata-rata 6,1 pemain per server) [FMP].

### Layout kota
```
            ┌──────┐   ┌──────┐   ┌──────┐
            │Plot 1│   │Plot 2│   │Plot 3│
            └──┬───┘   └──┬───┘   └──┬───┘
   ┌──────┐    │  jalan melingkar    │    ┌──────┐
   │Plot 8├────┤  ┌───────────────┐  ├────┤Plot 4│
   └──────┘    │  │ GALLERY SQUARE│  │    └──────┘
               │  │ (bingkai Best │  │
   ┌──────┐    │  │ Case + Hall of│  │    ┌──────┐
   │Plot 7├────┤  │ Fame + papan  │  ├────┤Plot 5│
   └──────┘    │  │ leaderboard)  │  │    └──────┘
               │  └───────────────┘  │
            ┌──┴───┐            ┌───┴──┐
            │Plot 6│  spawn     │ (bus │
            └──────┘  plaza     │ stop)│
                                └──────┘
```
- Setiap pemain mendapat 1 plot saat join (plot kosong di-*reset* saat pemainnya keluar).
- Jarak plot ke Gallery Square ≤ 10 detik jalan kaki.
- Pemain lain bisa masuk ke toko siapa saja. Pemain lain **tidak bisa** mengambil pesanan, membeli, atau mengubah dekor di toko orang lain.

### Interaksi sosial V1
| Fitur | Cara kerja |
|---|---|
| **Visit** | Jalan kaki, atau app **Visit** di HP → daftar 7 toko lain dengan level & jumlah like → teleport ke pintu toko |
| **Like toko** | Tombol ❤ di papan nama toko. 1× per toko per hari |
| **Like case** | Tombol ❤ di setiap case di Display Rack dan bingkai galeri |
| **Bonus teman** | +10% cash per teman di server (maks +30%). Indikator di HUD: "👥 +20%" [FMP] |
| **Equip case** | Case dari Album bisa dipegang avatar (Tool "My Phone"). Pemain lain melihatnya di tangan |
| **Emote foto** | Di Gallery Square ada spot foto: avatar berpose sambil memamerkan case |
| **Pengumuman server** | "Mia reached Level 8!", "Rio started a Cash Party!" di feed kecil kiri bawah |
| Chat | Chat bawaan Roblox (sudah mengikuti aturan umur dari Roblox). Game tidak menambah input teks bebas |

---

## 2. Best Case of the Week [DRAFT, isi USULAN]

Draft hanya menulis judul fitur. Berikut desain lengkapnya.

### Alur
```
Senin 00:00 UTC: minggu baru, tema mingguan diumumkan (contoh: "Pastel Dream")
  → pemain memilih 1 case dari Album → SUBMIT (bisa diganti sampai Jumat, like di-reset saat diganti)
  → case tampil di bingkai Gallery Square server itu + masuk pool global
  → pemain lain memberi ❤ (di Gallery Square, di app Gallery, atau di rak toko)
Minggu 23:59 UTC: peringkat dikunci → hadiah dikirim saat pemain login berikutnya
  → Top 8 global tampil di "Hall of Fame" di SEMUA server selama minggu berikutnya
```

### Aturan like (anti-abuse)
| Aturan | Nilai |
|---|---|
| Syarat pemberi like | Level ≥ 3 dan total main ≥ 10 menit |
| Like per entri | 1 per pemain |
| Like per hari | Maks 30 per pemain |
| Like diri sendiri | Tidak bisa |
| Akun alt | Like dari akun berumur < 7 hari bernilai 0 untuk peringkat global (tetap terlihat di angka lokal) |

### Tempat melihat entri
| Tempat | Isi |
|---|---|
| Gallery Square (server) | 8 bingkai: entri pemain di server ini |
| Hall of Fame (server) | 8 bingkai: Top 8 global minggu lalu + nama pembuat |
| App **Gallery** di HP | Swipe kartu: entri acak dari pool global (20 per sesi), tombol ❤ |

### Hadiah mingguan
| Peringkat | Hadiah |
|---|---|
| Ikut submit | 5 💎 |
| ≥ 10 ❤ | +10 💎 + bingkai "Rising Designer" di Album |
| Top 100 global | +30 💎 |
| Top 10 global | +100 💎 + badge **Gallery Star** + tampil di Hall of Fame |
| #1 global | +250 💎 + patung emas case-nya di tengah Gallery Square semua server selama 1 minggu |

### Keamanan konten
Case dibangun **hanya dari bahan yang disediakan** (warna, pola, stiker yang sudah disetujui). Tidak ada teks bebas atau gambar unggahan. Karena itu tidak perlu moderasi UGC untuk galeri V1.

---

## 3. Leaderboard (nyata, bukan bot)

Game sumber memakai 499 bot dengan skor tetap [SRC 09]. Di Roblox leaderboard palsu mudah ketahuan, jadi kita memakai data nyata.

| Leaderboard | Lingkup | Tampil di |
|---|---|---|
| Level (leaderstats) | Server | Daftar pemain Roblox (Tab) |
| Most Liked This Week | Global (OrderedDataStore) | Papan di Gallery Square + app Gallery |
| Top Shops (total like toko) | Global | Papan di Gallery Square |
| Cases Crafted | Global | Papan di Gallery Square |

---

## 4. Sistem retensi

| Sistem | Pemicu kembali | Horizon |
|---|---|---|
| **AFK Tip Jar** (cap 3 jam) | "Tip Jar sudah penuh" | Beberapa kali sehari |
| **Daily Login** 7 hari | Hadiah naik, hari ke-7 dapat stiker eksklusif | Harian |
| **Daily Quest** (3 per hari) | Quest baru, termasuk quest sosial | Harian |
| **Best Case of the Week** | Hasil & hadiah, tema baru | Mingguan |
| **Level berikutnya** | HUD "Next: Lv X – ..." | Per sesi |
| **Karyawan & dekor** | Sink setelah L10 | Mingguan |
| **Codes** | Diumumkan di grup/Discord/YouTube | Saat update |
| **Experience Notifications** (opt-in) | "Your Tip Jar is full!", "Best Case results are in!" | Harian / mingguan [USULAN, memakai fitur notifikasi Roblox] |
| **Update konten** | L11+, tema baru, device baru | 2 mingguan |

### Badge V1
| Badge | Syarat |
|---|---|
| Open For Business! | Selesaikan pesanan pertama |
| First Sparkle | Pakai Top Pattern pertama kali |
| Team Player | Rekrut karyawan pertama |
| Shop Guardian | Hentikan Thief pertama |
| Fashion Favorite | 3★ untuk 10 pelanggan Fancy |
| Golden Oldies | Selesaikan pesanan Old Club |
| Big Spender's Choice | Haggle berhasil dengan Rich Kid |
| Bigger & Better | Beli Waiting Room Expand |
| Gallery Master | Capai Level 10 |
| Gallery Star | Masuk Top 10 Best Case of the Week |
| Social Butterfly | Kunjungi 10 toko berbeda |

### Codes saat rilis [USULAN]
| Code | Hadiah |
|---|---|
| `RELEASE` | 2x Cash 15 menit (sama dengan pola FMP) |
| `GALLERY` | 20 💎 |
| `SPARKLE` | Stiker eksklusif "Launch Star" |

---

## 5. Target metrik retensi
Lihat [16_Roadmap_KPI_Risiko.md](16_Roadmap_KPI_Risiko.md#3-kpi).
