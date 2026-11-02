# Sumber Bab 07

| Berkas | Kegunaan |
| :-- | :-- |
| [`contoh-katalog-medikara.csv`](contoh-katalog-medikara.csv) | Contoh dan templat katalog aplikasi: 11 aplikasi dan 1 kumpulan spreadsheet, potongan dari katalog 46 aplikasi |
| [`templat-katalog-antarmuka.csv`](templat-katalog-antarmuka.csv) | Contoh dan templat katalog antarmuka: 26 antarmuka otomatis dan 7 ekspor manual |
| [`lembar-penilaian-time.md`](lembar-penilaian-time.md) | Indikator dua sumbu TIME, contoh terisi, lembar kerja, dan daftar periksa |
| [`templat-dokumen-c2.md`](templat-dokumen-c2.md) | Susunan dokumen C2, contoh lima masalah terbesar, lembar kerja, dan daftar periksa |
| [`periksa-portofolio.py`](periksa-portofolio.py) | Pendalaman opsional: pemeriksaan arah TIME, pasangan integrasi, dan biaya integrasi dengan pustaka standar Python |

## Cara memakai

1. Baca tujuan dan Aktivitas Bab 7.
2. Salin kedua berkas CSV ke folder tim, ganti barisnya, dan isi bersama anggota berlatar bisnis serta teknis.
3. Bedakan fakta organisasi, asumsi latihan, dan target yang belum disetujui.
4. Tinjau bukti dan konsistensi kode sebelum digabung ke C2.

CSV memakai UTF-8 dan pemisah koma. Baris pertama berisi komentar `#`; hapus baris itu saat impor ke spreadsheet. Header kolom tidak boleh dihapus. Seluruh angka Medikara adalah data sintetis, bukan hasil pengukuran organisasi nyata.

## Pemeriksa portofolio

Skrip dijalankan dengan `python periksa-portofolio.py`. Ambang tinggi kelas adalah 4 dari skala 1 sampai 5. Nilai 36 merupakan batas pasangan model untuk 9 sistem, bukan jumlah antarmuka aktual. Katalog contoh memuat 21 pasangan aktif dan 26 antarmuka otomatis. Berkas lain dibaca dengan `--aplikasi` dan `--antarmuka`.

## Batas data

Data yang dipakai harus berizin dan dianonimkan. Identitas pasien, isi rekam medis, kata sandi, token, dan dokumen rahasia tidak boleh masuk repositori. Bila dokumen asli tidak boleh dibagikan, cukup catat metadata buktinya.
