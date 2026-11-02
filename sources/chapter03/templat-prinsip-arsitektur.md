<!-- Templat prinsip arsitektur Bab 3. Salin ke folder tim, tulis lima sampai delapan prinsip, lalu uji tiap prinsip pada dua opsi. -->

# Prinsip Arsitektur

Tulis lima sampai delapan prinsip dengan format nama, pernyataan, alasan, dan implikasi. Uji tiap prinsip pada dua opsi nyata. Catat konflik dan dispensasi yang dibutuhkan.

## Cara memakai

1. Tetapkan lingkup, versi artefak, tanggal, dan penanggung jawab.
2. Turunkan prinsip dari `goal` pada rantai motivasi.
3. Isi satu baris per prinsip. Implikasi wajib menyebut pekerjaan, biaya, atau wewenang.
4. Uji prinsip pada dua opsi. Bila kedua opsi sama-sama lolos, pertajam pernyataannya.
5. Tulis urutan pertimbangan untuk prinsip yang dapat berkonflik.

## Contoh terisi

Contoh mengikuti Bab 3, dengan rincian yang merupakan pengandaian pembelajaran.

| Nama | Pernyataan | Alasan | Implikasi | Uji dua opsi |
| :-- | :-- | :-- | :-- | :-- |
| PA1 Satu sumber kebenaran untuk data pasien | Tiap atribut data pasien punya satu sistem acuan dan satu jalur resmi untuk mengubahnya | Keputusan klinis tidak boleh memakai data yang usang atau ganda | Pemilik data ditunjuk; sistem lain membaca dari acuan; salinan diberi tanda waktu | Medikara+ membaca jadwal dari SIMRS lewat antarmuka: lolos. Salinan jadwal diunggah manual: ditolak |
| PA2 Akses berdasarkan kebutuhan | Akses data pasien diberikan menurut tugas dan dibatasi waktu | Insiden 2025 dan temuan audit; data hanya dibuka pihak yang berhak | Peran ditinjau tiap tiga bulan; akun vendor berakhir bersama kontrak; akses darurat dicatat | Akun bersama untuk tim vendor: ditolak. Akun per orang dengan kedaluwarsa: lolos |

## Lembar kerja tim

| Nama | Pernyataan | Alasan | Implikasi | Uji dua opsi |
| :-- | :-- | :-- | :-- | :-- |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |

## Konflik dan dispensasi

| Prinsip yang berkonflik | Urutan pertimbangan | Pemilik dispensasi | Masa berlaku | Rencana kembali |
| :-- | :-- | :-- | :-- | :-- |
| ... | ... | ... | ... | ... |

## Pemeriksaan sebelum pengumpulan

- [ ] Mudah dipahami: anggota nonteknis dapat menjelaskannya dengan kata sendiri.
- [ ] Kokoh: dua opsi nyata dinilai berbeda.
- [ ] Lengkap: keputusan penting pada strategi sudah tercakup.
- [ ] Konsisten: konflik antarprinsip punya aturan.
- [ ] Stabil: prinsip tetap berlaku saat produk diganti.
- [ ] Tidak memuat data pribadi, rahasia akses, atau salinan produksi.
