<!-- Lembar penilaian model operasi Bab 3. Salin ke folder tim, nilai tiap lingkup, lalu rangkum hasilnya di visi arsitektur. -->

# Penilaian Model Operasi

Nilai integrasi dan standardisasi secara terpisah per lingkup. Satu organisasi boleh memiliki model berbeda untuk lingkup berbeda, asalkan batasnya dinyatakan.

## Cara memakai

1. Tetapkan lingkup, versi artefak, tanggal, dan penanggung jawab.
2. Tulis bukti integrasi: apakah pasien, transaksi, dan keputusan benar-benar melintasi batas unit?
3. Tulis bukti standardisasi: apakah unit mengikuti cara kerja yang sama?
4. Beri skor tiap dimensi, lalu tentukan model saat ini dan model yang diinginkan.
5. Tulis akibatnya bagi aplikasi dan data, serta satu kondisi yang dapat mengubah pilihan.

## Skala skor

| Skor | Arti |
| :-- | :-- |
| 1 | Rendah, didukung bukti |
| 2 | Bukti belum cukup, perlu dicari lagi sebelum disimpulkan |
| 3 | Tinggi, didukung bukti |

## Pembacaan model

| Integrasi | Standardisasi | Model |
| :-- | :-- | :-- |
| Rendah | Rendah | Diversifikasi |
| Tinggi | Rendah | Koordinasi |
| Rendah | Tinggi | Replikasi |
| Tinggi | Tinggi | Unifikasi |

## Contoh terisi

Angka pada contoh merupakan pengandaian pembelajaran.

| Lingkup | Bukti integrasi (skor) | Bukti standardisasi (skor) | Model awal | Akibat bagi aplikasi dan data |
| :-- | :-- | :-- | :-- | :-- |
| Permintaan dan hasil laboratorium rujukan | 1.500 permintaan per hari dari 23 fasilitas; hasil kembali ke rekam medis asal (3) | Cara pengambilan sampel dan formulir berbeda di tiap fasilitas (1) | Koordinasi | Data permintaan dan hasil dibagi lewat antarmuka baku; formulir lokal boleh tetap |
| Layanan dasar 18 klinik pratama | 93 persen pasien hanya berkunjung ke satu klinik (1) | SOP sama di 18 klinik (3) | Replikasi | Satu konfigurasi aplikasi dipakai berulang; rujukan ke rumah sakit tetap perlu integrasi |

## Lembar kerja tim

| Lingkup | Bukti integrasi (skor) | Bukti standardisasi (skor) | Model saat ini | Model yang diinginkan | Akibat bagi aplikasi dan data | Kondisi pengubah |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| ... | ... | ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... | ... | ... |

## Pemeriksaan sebelum pengumpulan

- [ ] Skor 2 sudah dicarikan bukti tambahan atau dicatat sebagai asumsi.
- [ ] Banyaknya cabang atau jumlah server tidak dipakai sebagai satu-satunya bukti.
- [ ] Pemilik definisi data bersama dan mekanisme keputusan dicatat.
- [ ] Istilah dan nomor elemen sama dengan artefak mata kuliah lain.
- [ ] Tidak memuat data pribadi, rahasia akses, atau salinan produksi.
