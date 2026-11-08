# 11. Pelajaran untuk Game Kita

[← Kembali ke indeks](00_README.md)

## Desain Gameplay
1. **Satu fantasi, banyak "maker".** Core loop tetap (pesanan → buat → dinilai → koin), dan variasi datang dari *cara membuat*. Setiap maker adalah mini-game satisfying yang terpisah. Ini cara murah menambah konten. → [02](02_Mekanik_Maker.md)
2. **Pelanggan spesial tiap 3 level** (VIP) menjaga perhatian tanpa menaikkan kesulitan. → [03](03_Pelanggan.md)
3. **Tanpa kondisi gagal.** Untuk genre "satisfying", hukuman cukup berupa bintang lebih sedikit. → [04](04_LevelDesign_Pacing.md)
4. **Endgame dikunci di Day 25**, dan reward berhenti naik. Untuk game kita, siapkan konten loop atau event setelah konten utama habis. → [04](04_LevelDesign_Pacing.md)

## Ekonomi
5. **Reward linear + sink yang dihitung.** Reward naik +4 koin per pelanggan, dan total harga studio (33,4k) dipatok sekitar 77% pendapatan 25 hari. Gunakan formula sederhana yang mudah di-tuning di spreadsheet. → [05](05_Ekonomi.md)
6. **Tiga jalur unlock** (hari, VIP, chest) membuat setiap jenis aktivitas punya hadiah unik. → [05](05_Ekonomi.md#jalur-unlock-konten)
7. **Gacha dengan harga naik (+200/roll)** adalah sink tanpa batas yang terasa adil karena pemain tidak pernah mendapat duplikat. → [06](06_Gacha.md)

## Monetisasi
8. **Item RV diselipkan di antara item koin** di toko, sehingga iklan terlihat sebagai jalan pintas yang wajar. → [05](05_Ekonomi.md#a-studio-dekor-toko)
9. **Banyak slot iklan di client, frekuensi diatur server.** Pasang hook interstitial di setiap transisi, lalu atur pacing dari remote. Lebih fleksibel untuk A/B daripada cooldown yang di-hardcode. → [07](07_Monetisasi.md)
10. **Pengali RV berbeda per konteks** (normal ×2, VIP ×4, auction ×2 + best offer) membuat iklan paling "worth it" di momen spesial. → [07](07_Monetisasi.md)

## Retensi & LiveOps
11. **Leaderboard bot berbasis aksi** memberi rasa kompetisi tanpa backend multiplayer, sekaligus mengarahkan perilaku (skor tinggi untuk maker baru). → [09](09_Retensi_Sosial.md)
12. **Leaderboard palsu yang linear** (50 poin = 1 rank, hadiah tiap 10 rank) adalah sistem progres termurah dengan rasa sosial. → [09](09_Retensi_Sosial.md)
13. **Semua angka di tabel CSV + flag remote**, sehingga desainer bisa A/B pacing tanpa rilis ulang. → [08](08_LiveOps_AB.md)

## Peringatan
14. ⚠️ **Hindari IP pihak ketiga.** Game ini memakai bentuk "Among-us" dan "StarBucks". Untuk game kita, ganti dengan desain orisinal.
