# Sumber Bab 06: Arsitektur Data dan Informasi Saat Ini

| Berkas | Kegunaan |
| --- | --- |
| `templat-katalog-konsep-informasi.csv` | Templat katalog 10 sampai 15 konsep informasi: definisi, pemilik bisnis, *steward*, jenis data, aplikasi pembuat, klasifikasi, dan kategori UU PDP. Dipakai pada langkah 1, 2, dan 5 Aktivitas |
| `templat-matriks-crud.csv` | Templat matriks CRUD antara konsep data dan aplikasi, termasuk kolom spreadsheet. Dipakai pada langkah 3 Aktivitas dan Latihan 2 |
| `medikara-matriks-crud.csv` | Contoh matriks CRUD Medikara Health yang sama dengan tabel di naskah bab. Kolom `simrs` mewakili lima SIMRS |
| `templat-daftar-masalah-data.md` | Templat daftar masalah data beserta contoh Medikara dan daftar periksa sebelum digabung ke dokumen C2 |
| `periksa-matriks-crud.py` | Pendalaman teknis (opsional): skrip Python yang menandai konsep tanpa pemilik, konsep yang dibuat di banyak tempat, dan konsep yang dibuat di spreadsheet |

Baris pertama tiap berkas CSV diawali `#` dan berisi keterangan pemakaian.
Saat dibuka di aplikasi spreadsheet, baris itu tampil sebagai baris biasa dan
boleh dihapus. Skrip pemeriksa melewatinya secara otomatis.

## Menjalankan pemeriksa matriks CRUD

Skrip hanya memakai pustaka standar Python 3, tanpa paket tambahan.

```bash
cd sources/chapter06
python periksa-matriks-crud.py medikara-matriks-crud.csv
```

Keluarannya untuk contoh Medikara:

```
Pasien
  - dibuat di 2 tempat: simrs, medikara_plus
Kunjungan
  - dibuat di 2 tempat: simrs, medikara_plus
Rekam Medis
  - dibuat di 2 tempat: simrs, medikara_plus
Klaim
  - dibuat di 2 tempat: simrs, spreadsheet
  - dibuat di spreadsheet, di luar aplikasi yang dikelola
Kontrak Penjamin
  - belum punya pemilik bisnis
  - dibuat di spreadsheet, di luar aplikasi yang dikelola

Ditandai: 5 dari 10 konsep.
Tanpa penghapus, cocokkan dengan aturan masa simpan:
  Pasien, Kunjungan, Rekam Medis, Hasil Laboratorium, Resep, Tagihan, Klaim
```

Matriks milik tim diperiksa dengan cara yang sama setelah templatnya diisi.
Nama kolom aplikasi boleh diganti bebas, asalkan kolom `konsep`,
`pemilik_bisnis`, dan `spreadsheet` tetap ada.

## Etika

Berkas di folder ini hanya memuat konsep, jumlah, dan persentase. Data pribadi
pasien atau karyawan tidak boleh dimasukkan. Tim yang memakai organisasi nyata
wajib memperoleh izin tertulis dan menganonimkan semua contoh.
