# Sumber Bab 11

| Berkas | Kegunaan |
| --- | --- |
| [`templat-matriks-gap.csv`](templat-matriks-gap.csv) | Templat perbandingan kondisi saat ini dan target per domain, termasuk kolom asal gap |
| [`templat-daftar-paket-kerja.csv`](templat-daftar-paket-kerja.csv) | Templat batas, prasyarat, pemilik, dan bukti penerimaan tiap paket kerja |
| [`templat-analisis-dampak.csv`](templat-analisis-dampak.csv) | Templat dampak pada orang serta skor kesiapan per paket |
| [`templat-dokumen-c3.md`](templat-dokumen-c3.md) | Templat dokumen Kondisi Target C3 beserta daftar pemeriksaan |
| [`contoh-gap-medikara.csv`](contoh-gap-medikara.csv) | Contoh register 23 gap Medikara, sama dengan tabel register pada Bab 11 |
| [`contoh-paket-kerja-medikara.csv`](contoh-paket-kerja-medikara.csv) | Contoh delapan paket kerja; kode, durasi, dan prasyarat sama dengan `sources/chapter12/paket-kerja-medikara.csv` |
| [`model-awal.csv`](model-awal.csv) | Ekspor sintetis model awal, masukan `bandingkan-model.py` |
| [`model-target.csv`](model-target.csv) | Ekspor sintetis model target, masukan `bandingkan-model.py` |
| [`bandingkan-model.py`](bandingkan-model.py) | Pendalaman opsional: membandingkan dua ekspor model dengan Python pustaka standar |
| [`periksa-dependensi.py`](periksa-dependensi.py) | Pendalaman opsional: mencetak matriks dependensi, mencari lingkaran, dan menyusun lapisan paket |

## Cara memakai

1. Baca tujuan dan Aktivitas Bab 11.
2. Salin templat ke folder tim dan isi bersama anggota berlatar bisnis serta teknis.
3. Bedakan fakta organisasi, asumsi latihan, dan target yang belum disetujui.
4. Tinjau bukti dan konsistensi kode sebelum digabung ke C3.

CSV memakai UTF-8 dan pemisah koma. Baris pertama berisi komentar `#`; hapus baris itu saat impor spreadsheet. Jangan menghapus header kolom. Kode prasyarat dan kode gap dalam satu sel dipisahkan titik koma. Angka tambahan pada Medikara adalah data sintetis, bukan hasil pengukuran organisasi nyata.

## Membandingkan model

Jalankan `python bandingkan-model.py`. Pada data contoh, 15 butir awal dan 9 butir target menghasilkan 2 dipertahankan, 1 diubah, 7 diganti, 3 dihapus sengaja, 2 PERIKSA, 2 penerus, dan 4 baru. Dua butir PERIKSA adalah `APP-10` Surveilans Infeksi Bogor dan `APP-11` Laporan Klaim Lama. Tinjau arti perubahan sebelum mengesahkan gap. Ekspor jArchi merupakan pilihan lanjutan, bukan prasyarat.

## Memeriksa dependensi

Jalankan `python periksa-dependensi.py`. Pada data contoh, hasilnya 11 dependensi, tiga lapisan (P1 dan P2; P3 dan P4; P5 sampai P8), dan tidak ada lingkaran. Untuk melihat peringatan lingkaran, salin CSV contoh lalu tambahkan P5 sebagai prasyarat P3. Tanggal, durasi, dan kapasitas dihitung pada Bab 12 dengan `sources/chapter12/jalur-kritis.py`.

## Kode

Kode paket P1 sampai P8 mengikuti Bab 12. Kode gap memakai huruf domain: `G-B` bisnis, termasuk orang dan proses, `G-D` data, `G-A` aplikasi, dan `G-T` teknologi. Kode aplikasi `APP-01` sampai `APP-11` dan `SPR-01` mengikuti katalog Bab 7. Kode `APP-T01` sampai `APP-T05` dan `CAP-T01` hanya berlaku pada contoh model target di folder ini.

## Batas data

Gunakan data berizin dan dianonimkan. Jangan memasukkan identitas pasien, isi rekam medis, kata sandi, token, atau dokumen rahasia ke repositori. Catat metadata bukti bila dokumen asli tidak boleh dibagikan.
