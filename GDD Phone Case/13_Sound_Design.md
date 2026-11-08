# 13. Sound Design

[← Kembali ke indeks](00_README.md)

## 1. Arah suara
- **ASMR ringan + kartun ceria.** Langkah craft harus terdengar *satisfying* (desis spray, gosokan halus, "pop" stiker). Game sumber dan FMP sama-sama menjual rasa ini [SRC 02], [FMP].
- **UI dan reward** memakai bunyi kartun yang bulat dan bernada (marimba, glockenspiel, pluck).
- **Tidak menusuk telinga.** Pemain bisa mendengar ratusan kali per sesi, jadi frekuensi tinggi dikurangi dan setiap SFX berulang punya variasi.

## 2. Aturan teknis

| Aturan | Nilai |
|---|---|
| Format | OGG, mono untuk SFX 3D, stereo untuk musik & UI |
| SoundGroup | `Music`, `SFX_Craft`, `SFX_UI`, `SFX_World`, `SFX_Voice` (volume masing-masing di Settings) |
| Variasi | SFX yang sering diputar punya 3–4 variasi + random pitch ±5% |
| Loop | SFX kontinu (spray, buffer, wipe) adalah loop yang fade in 0,05 dtk / fade out 0,1 dtk saat drag dimulai/berhenti |
| Spasial | SFX dunia (pelanggan, karyawan, build) 3D dengan `RollOffMaxDistance` 60 stud. SFX craft & UI 2D |
| Ducking | Musik turun −6 dB saat layar craft aktif, −10 dB saat level-up jingle |
| Batas bersamaan | Maks 3 instance per SFX yang sama (cegah suara menumpuk dari 3 karyawan) |
| Sumber | Library berlisensi / dibuat sendiri, diunggah sebagai aset milik grup. Jangan memakai audio publik tanpa izin |

---

## 3. Daftar SFX

Prioritas: **P0** wajib untuk MVP, **P1** penting, **P2** polish.

### 3a. Craft: Step 1 Case Shape
| ID | Nama | Pemicu | Deskripsi | Var | Prio |
|---|---|---|---|---|---|
| CR_SHAPE_BROWSE | Geser list bentuk | Scroll list bentuk di HUD | Klik halus | 1 | P2 |
| CR_SHAPE_SELECT | Pilih bentuk | Tap kartu bentuk di list HUD | "Tok" plastik ringan | 2 | P0 |
| CR_SHAPE_POP | Case muncul | Setelah bentuk dipilih | "Pop" plastik + bounce kecil | 2 | P0 |

### 3b. Craft: Step 2 Base Painting
| ID | Nama | Pemicu | Deskripsi | Var | Prio |
|---|---|---|---|---|---|
| CR_PAINT_PICK | Pilih warna | Tap warna | "Klik" tutup kaleng + bunyi cat bergoyang | 3 | P0 |
| CR_SPRAY_LOOP | Semprot | Selama drag | Desis aerosol lembut | 1 loop | P0 |
| CR_SPRAY_RATTLE | Kocok kaleng | Mulai drag pertama kali di langkah ini | Bola kaleng bergemerincing | 2 | P1 |
| CR_PAINT_FULL | Cat penuh | Coverage 100% | Kilau "shing" pendek | 1 | P1 |

### 3c. Craft: Step 3 Smoothing + Glossy
| ID | Nama | Pemicu | Deskripsi | Var | Prio |
|---|---|---|---|---|---|
| CR_BUFFER_LOOP | Buffer | Selama drag | Dengung mesin kecil + gosokan halus, nada turun saat permukaan makin halus | 1 loop | P0 |
| CR_BUFFER_CELL | Sel jadi halus | Sel mencapai kasar 0 (dibatasi 6/dtk) | "Tik" sangat halus | 3 | P2 |
| CR_GLOSS_DIP | Celup kuas | Mulai sub-step Glossy | Celup cairan kental | 1 | P1 |
| CR_GLOSS_STROKE | Sapuan glossy | Tiap sapuan | Usapan basah panjang | 3 | P0 |
| CR_GLOSS_SHINE | Kilau | Sapuan ke-3 selesai | "Tiiing" kilau bernada tinggi lembut | 1 | P0 |

### 3d. Craft: Step 4 Top Pattern
| ID | Nama | Pemicu | Deskripsi | Var | Prio |
|---|---|---|---|---|---|
| CR_GLITTER_SHAKE | Goyang glitter | Tiap goyangan | Shaker berisi butiran halus | 4 | P0 |
| CR_GLITTER_LAND | Glitter menempel | Setelah goyangan | Bunyi kristal kecil berkelip | 3 | P1 |
| CR_ROLLER_LOOP | Roller | Selama sapuan roller | Gulungan karet di atas cat basah | 1 loop | P0 |
| CR_ROLLER_REVEAL | Pola muncul | Tiap 1/3 pola terbuka | "Swish" pendek | 3 | P1 |

### 3e. Craft: Step 5 Sticker
| ID | Nama | Pemicu | Deskripsi | Var | Prio |
|---|---|---|---|---|---|
| CR_STICKER_PEEL | Kelupas | Mulai drag stiker dari tray | Kertas stiker dikelupas | 3 | P0 |
| CR_STICKER_PLACE | Tempel | Lepas jari di case | "Pap" lengket + pop kecil | 3 | P0 |
| CR_STICKER_SCALE | Skala/putar | Saat pinch/scroll (dibatasi) | Klik halus | 2 | P2 |
| CR_STICKER_DELETE | Hapus | Tombol 🗑 | Kertas diremas | 1 | P1 |

### 3f. Craft: Step 6 Screen Cleaning
| ID | Nama | Pemicu | Deskripsi | Var | Prio |
|---|---|---|---|---|---|
| CR_DEVICE_FLIP | Balik device | Mulai Step 6 | Whoosh pendek + taruh di matras | 1 | P1 |
| CR_CLEANER_SPRAY | Semprot cairan | Awal langkah | 2× semprotan pump | 1 | P1 |
| CR_WIPE_LOOP | Lap | Selama drag | Kain mikrofiber di atas kaca ("squeak" halus) | 1 loop | P0 |
| CR_SMUDGE_GONE | Noda hilang | Tiap noda bersih | "Ding" kecil | 3 | P0 |
| CR_TURN_ON | Nyalakan | Tombol TURN IT ON | Chime startup HP orisinal (3 nada naik) | 1 | P0 |
| CR_PHOTO_FLASH | Foto album | Turntable selesai | Shutter kamera + "fwip" | 1 | P1 |

### 3g. Craft: umum
| ID | Nama | Pemicu | Deskripsi | Var | Prio |
|---|---|---|---|---|---|
| CR_STEP_START | Masuk langkah | Tiap langkah baru (case berputar di bench) | Whoosh putar lembut | 2 | P1 |
| CR_SPEED_WARN | Bar waktu kuning | Sisa waktu bonus 25% | Tik-tok lembut 2× (tidak menekan) | 1 | P2 |
| CR_CONFIRM_WORD | Kata konfirmasi | PERFECT FIT!, COLORFUL!, dst. | Stinger ceria 0,6 dtk. Nada naik sesuai urutan langkah (Step 1 nada paling rendah) supaya terasa "menuju selesai" | 6 (1 per langkah) | P0 |
| CR_UNDO | Undo | Tombol ↶ | Rewind pendek | 1 | P2 |
| CR_REQUEST_MET | Request terpenuhi | Item order card dicentang | Pluck bernada | 1 | P0 |
| CR_INSTANT | Instant Finish | Tombol ⚡ | Sweep ajaib + semua langkah "pop" cepat | 1 | P1 |

### 3h. Pelanggan & toko (dunia, 3D)
| ID | Nama | Pemicu | Deskripsi | Var | Prio |
|---|---|---|---|---|---|
| WD_DOOR_BELL | Bel pintu | Pelanggan masuk | Bel toko "ding-ding" | 2 | P0 |
| WD_TAKE_ORDER | Ambil pesanan | I'LL MAKE IT! | Kertas order disobek + whoosh | 1 | P0 |
| WD_ORDER_COMPLETE | Pesanan selesai | Langkah terakhir selesai | "Ta-da" kecil + kantong belanja | 1 | P0 |
| WD_CASH_REGISTER | Dibayar | Bayaran masuk saat pesanan selesai (pemain & karyawan) | "Cha-ching" | 3 | P0 |
| WD_CUST_HAPPY | Reaksi 3★ | Bintang 3 | Vokal gibberish senang (bukan kata nyata) | 4 per gender | P1 |
| WD_CUST_OK | Reaksi 1–2★ | Bintang 1–2 | Gumaman "hmm, okay" gibberish | 2 per gender | P1 |
| WD_FANCY_ENTER | Fancy masuk | Fancy tiba | Stinger glamor singkat + flash kamera | 1 | P1 |
| WD_THIEF_GRAB | Thief menyambar | Thief kabur | "Yoink!" kartun + langkah cepat jinjit | 1 | P0 |
| WD_THIEF_CAUGHT | Thief tertangkap | STOP THIEF! berhasil | Terpeleset kartun + "boing" | 1 | P0 |
| WD_THIEF_ESCAPE | Thief lolos | Gagal | Langkah menjauh + koin jatuh | 1 | P1 |
| WD_OLDCLUB_DANCE | Old Club senang | Pesanan Old Club selesai | Musik swing pendek 2 dtk | 1 | P2 |
| WD_RICH_OFFER | Tawaran Rich Kid | Kartu tawaran muncul | Kartu dikocok + "bling" | 1 | P1 |
| WD_HAGGLE_WIN | Haggle berhasil | +25% | Fanfare kecil | 1 | P1 |
| WD_HAGGLE_SAME | Haggle tetap | Tawaran tetap | "Tsk" ringan, tetap positif | 1 | P2 |
| WD_EMPLOYEE_WORK | Karyawan bekerja | Loop selama kerja | Versi pelan & jauh dari spray/buffer (3D) | 2 | P1 |
| WD_EMPLOYEE_DONE | Karyawan selesai | Pesanan karyawan selesai | "Ding" bel meja | 1 | P0 |
| WD_TIPJAR_COLLECT | Ambil Tip Jar | [E] di Tip Jar | Koin berjatuhan banyak, makin panjang jika makin penuh | 2 | P0 |
| WD_TIPJAR_FULL | Tip Jar penuh | Saat penuh (dekat) | Koin terakhir "clink" | 1 | P2 |

### 3i. Tycoon & dekor
| ID | Nama | Pemicu | Deskripsi | Var | Prio |
|---|---|---|---|---|---|
| TY_HOLO_APPEAR | Hologram muncul | Unlock baru | Shimmer digital lembut | 1 | P0 |
| TY_BUILD | Beli/build | BUILD | Kardus jatuh "thud" + "poof" + pop item | 2 | P0 |
| TY_HIRE | Rekrut karyawan | Employee +1 | Pintu + "Hi!" gibberish + jingle singkat | 1 | P0 |
| TY_UPGRADE | Upgrade karyawan | Speed/Quality/Skill | Power-up naik nada | 1 | P1 |
| TY_EXPAND | Ekspansi toko | Waiting Room Expand | Gemuruh ringan + dinding bergeser + fanfare | 1 | P0 |
| DC_PLACE | Pasang dekor | Pilih varian dekor | Pop + kilau | 2 | P0 |
| DC_PREVIEW | Ganti pratinjau | Geser varian | Klik lembut | 1 | P2 |

### 3j. UI & progres (2D)
| ID | Nama | Pemicu | Deskripsi | Var | Prio |
|---|---|---|---|---|---|
| UI_TAP | Tap tombol | Semua tombol | "Bloop" lembut | 3 | P0 |
| UI_BACK | Tutup/kembali | ✕ | Bloop turun | 1 | P0 |
| UI_PHONE_OPEN | Buka HP | Tombol HP | Getar HP + unlock "click" | 1 | P0 |
| UI_PHONE_CLOSE | Tutup HP | Tutup HP | Kunci layar "click" | 1 | P0 |
| UI_APP_OPEN | Buka app | Tap app | Swoosh mini | 1 | P1 |
| UI_ERROR | Tidak bisa | Cash kurang / terkunci | Buzz lembut (bukan keras) | 1 | P0 |
| UI_CASH_TICK | Cash bertambah | Angka naik | Koin tick, dibatasi 10/dtk | 3 | P0 |
| UI_GEM_GAIN | Gems bertambah | Gems masuk | Kristal "ting" | 2 | P0 |
| UI_STAR_1/2/3 | Bintang muncul | Layar reward | 3 nada naik (do-mi-sol) | 3 | P0 |
| UI_BONUS_MATCH | Baris bonus kesesuaian | Layar reward | Pluck naik + kilau | 1 | P0 |
| UI_BONUS_SPEED | Baris bonus kecepatan | Layar reward | Whoosh cepat + kilau | 1 | P0 |
| UI_XP_FILL | Bar XP terisi | XP masuk | Swell naik pendek | 1 | P1 |
| UI_LEVEL_UP | Naik level | Level up | Jingle 2,5 dtk + konfeti pop | 1 | P0 |
| UI_UNLOCK_CARD | Kartu unlock | Tiap kartu di layar level-up | Kartu dibalik + kilau | 1 | P0 |
| UI_BADGE | Dapat badge | Badge | Stinger "achievement" | 1 | P1 |
| UI_PURCHASE_OK | Pembelian Robux berhasil | ProcessReceipt sukses | Fanfare mewah 1,5 dtk | 1 | P0 |
| UI_QUEST_DONE | Quest selesai | Quest | Centang + chime | 1 | P1 |
| UI_LOGIN_CLAIM | Klaim login | Login harian | Hadiah dibuka | 1 | P1 |
| UI_ARROW_PING | Panah panduan | Panah kuning baru muncul | Ping lembut | 1 | P1 |

### 3k. Sosial
| ID | Nama | Pemicu | Deskripsi | Var | Prio |
|---|---|---|---|---|---|
| SO_LIKE | Beri like | ❤ | Pop hati | 2 | P0 |
| SO_LIKE_RECEIVED | Dapat like | Notifikasi like | Chime manis kecil | 1 | P1 |
| SO_FRIEND_JOIN | Teman join | Teman masuk server | "Hey!" jingle + bonus naik | 1 | P1 |
| SO_CASH_PARTY | Cash Party | Dev product dibeli siapa pun | Terompet pesta + konfeti seluruh server | 1 | P0 |
| SO_GALLERY_SUBMIT | Submit galeri | SUBMIT | Bingkai dipasang + kamera flash | 1 | P1 |
| SO_HALL_OF_FAME | Masuk Hall of Fame | Notifikasi hasil mingguan | Fanfare besar | 1 | P1 |

**Total SFX unik:** ±85 (P0: ±45). Dengan variasi: ±150 file.

---

## 4. Musik

| ID | Track | Tempat | Arahan | Durasi loop | Prio |
|---|---|---|---|---|---|
| MU_SHOP | Shop Day | Di dalam toko sendiri | Lo-fi pop ceria, 95–105 BPM, ukulele/kalimba + beat lembut. Tidak mengganggu fokus craft | 2–3 menit | P0 |
| MU_TOWN | Town Stroll | Di jalan & Gallery Square | Bubblegum pop instrumental, sedikit lebih ramai | 2–3 menit | P0 |
| MU_CRAFT | Craft Focus | Opsional: layer musik saat bench | Versi MU_SHOP tanpa drum (crossfade 1 dtk) | sama | P1 |
| MU_GALLERY | Gallery Night | App Gallery / Hall of Fame | Synth lembut, kesan "pameran" | 1,5 menit | P2 |
| MU_LEVELUP | Level-up jingle | Level up | Lihat UI_LEVEL_UP | 2,5 dtk | P0 |

- Crossfade 1,5 detik saat berpindah zona (toko ↔ jalan).
- Semua musik bebas lisensi atau komposisi sendiri. **Tidak boleh** memakai lagu populer meskipun sebagai plesetan.

## 5. Ambience
| ID | Isi | Tempat |
|---|---|---|
| AM_TOWN | Burung, angin pelan, suara kota jauh | Jalan & taman |
| AM_SHOP | Dengung toko lembut, suara pelanggan samar | Dalam toko |
| AM_FISHTANK | Gelembung air pelan | Dekat Fish Tank (L10) |
| AM_FOUNTAIN | Air mancur | Gallery Square |

## 6. Haptic (mobile & gamepad)
| Momen | Pola |
|---|---|
| Case muncul (Step 1) | 1 pulse sedang |
| Goyang glitter | Pulse ringan tiap goyangan |
| Stiker menempel | 1 pulse ringan |
| Kata konfirmasi | 2 pulse ringan |
| Level-up | 3 pulse naik |
