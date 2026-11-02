<!-- Templat daftar masalah data Bab 06. Salin berkas ini ke folder tim, isi tabel di bagian 2, lalu periksa dengan daftar di bagian 3 sebelum digabung ke dokumen C2. -->

# Daftar Masalah Data

Daftar ini adalah luaran ketiga Aktivitas Bab 06, sesudah peta informasi dan
matriks CRUD. Tiap baris mencatat satu masalah data yang menghambat strategi,
lengkap dengan buktinya. Daftar ini menjadi bahan utama arsitektur data target
di Bab 9.

## 1. Cara mengisi

1. Tulis satu masalah per baris. Masalah yang sama di dua konsep ditulis dua
   baris.
2. Sebut konsep data dengan nama yang sama persis seperti di katalog konsep
   informasi dan matriks CRUD.
3. Pilih satu dimensi kualitas utama: akurasi, kelengkapan, konsistensi,
   ketepatan waktu, atau keunikan. Masalah yang bukan kualitas, misalnya
   pemilik yang tidak jelas atau aliran manual, ditulis "kepemilikan" atau
   "aliran".
4. Bukti wajib berupa angka beserta sumbernya, misalnya "sampel 10.000 nomor
   rekam medis, 11,4 persen duplikat". Dugaan tanpa angka ditandai "perlu
   diukur".
5. Dampak ditulis terhadap strategi organisasi, bukan terhadap sistem.
6. Usulan ditulis sebagai arah, bukan solusi teknis. Rancangan rincinya
   dikerjakan di Bab 9.

Data pribadi pasien atau karyawan tidak boleh disalin ke daftar ini. Yang
dicatat adalah jumlah, persentase, dan contoh yang sudah dianonimkan.

## 2. Tabel masalah

| No | Masalah | Konsep data | Dimensi | Bukti (angka dan sumber) | Dampak pada strategi | Pemilik | Usulan arah kondisi target |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Satu orang punya nomor rekam medis di beberapa rumah sakit | Pasien | Keunikan | Sampel 10.000 nomor rekam medis dari lima SIMRS: 1.140 (11,4 persen) milik orang yang sudah terdaftar di rumah sakit lain | Menghambat "Satu Pasien, Satu Rekam Medis" | Direktur tiap rumah sakit (belum tunggal) | Identitas pasien tunggal dengan satu pemilik korporat |
| 2 | Jumlah kunjungan berbeda antara SIMRS dan laporan direksi | Kunjungan | Konsistensi | Oktober 2025: SIMRS 99.870, spreadsheet 102.640, selisih 2,8 persen | Direksi ragu memakai angka untuk keputusan investasi | Direktur Pelayanan | Satu definisi kunjungan dan satu sumber laporan |
| 3 | Kontrak penjamin hanya ada di spreadsheet | Kontrak Penjamin | Kepemilikan | Matriks CRUD: C hanya di kolom spreadsheet, pemilik kosong | Ekosistem mitra asuransi sulit diperluas | Belum ada | Tetapkan pemilik, pindahkan ke aplikasi yang dikelola |
| 4 | ... | ... | ... | ... | ... | ... | ... |
| 5 | ... | ... | ... | ... | ... | ... | ... |
| 6 | ... | ... | ... | ... | ... | ... | ... |
| 7 | ... | ... | ... | ... | ... | ... | ... |
| 8 | ... | ... | ... | ... | ... | ... | ... |

Baris 1 sampai 3 adalah contoh dari kasus Medikara Health dan boleh dihapus
oleh tim yang memakai organisasi sendiri.

## 3. Daftar periksa sebelum digabung ke C2

- [ ] Katalog konsep informasi berisi 10 sampai 15 konsep, masing-masing
      dengan definisi satu kalimat dan pemilik bisnis.
- [ ] Setiap konsep yang menyimpan data pribadi sudah diberi kategori UU PDP
      (umum atau spesifik) dan tingkat klasifikasi organisasi.
- [ ] Matriks CRUD memuat semua aplikasi yang membuat atau mengubah konsep,
      termasuk spreadsheet dan aplikasi milik vendor.
- [ ] Setiap konsep yang dibuat di lebih dari satu tempat muncul di tabel
      masalah, atau ada catatan mengapa hal itu wajar.
- [ ] Setiap konsep tanpa penghapus sudah dicocokkan dengan aturan masa
      simpan, misalnya 25 tahun untuk rekam medis elektronik.
- [ ] Diagram aliran data tingkat tinggi memperlihatkan aliran manual, bukan
      hanya integrasi resmi.
- [ ] Setiap baris tabel masalah punya bukti berangka atau tanda "perlu
      diukur".
- [ ] Nama konsep sama persis di katalog, matriks CRUD, diagram aliran,
      model Archi, dan tabel masalah.
- [ ] Tidak ada data pribadi pasien atau karyawan yang ikut tersalin ke
      dokumen tim.
