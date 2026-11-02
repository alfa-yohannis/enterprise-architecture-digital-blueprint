# Sumber Bab 12

| Berkas | Kegunaan |
| --- | --- |
| [`jalur-kritis.py`](jalur-kritis.py) | Pendalaman opsional: pemeriksaan lokal dengan Python pustaka standar |
| [`paket-kerja-medikara.csv`](paket-kerja-medikara.csv) | Data atau templat terstruktur; baca komentar penggunaan dan nama kolom |
| [`templat-arsitektur-transisi.md`](templat-arsitektur-transisi.md) | Petunjuk, contoh terisi, lembar kerja, dan daftar periksa |
| [`templat-peta-jalan.csv`](templat-peta-jalan.csv) | Data atau templat terstruktur; baca komentar penggunaan dan nama kolom |
| [`templat-rencana-migrasi.md`](templat-rencana-migrasi.md) | Petunjuk, contoh terisi, lembar kerja, dan daftar periksa |

## Cara memakai

1. Baca tujuan dan Aktivitas Bab 12.
2. Salin templat ke folder tim dan isi bersama anggota berlatar bisnis serta teknis.
3. Bedakan fakta organisasi, asumsi latihan, dan target yang belum disetujui.
4. Tinjau bukti dan konsistensi ID sebelum digabung ke C4.

CSV memakai UTF-8 dan pemisah koma. Berkas baru memuat komentar `#` pada baris pertama; hapus komentar itu saat impor spreadsheet. Beberapa berkas lama langsung memakai header. Jangan menghapus header kolom. Angka tambahan pada Medikara adalah data sintetis, bukan hasil pengukuran organisasi nyata.

## Analisis jadwal

Jalankan `python jalur-kritis.py paket-kerja-medikara.csv`. Bulan 0 adalah Juli 2026. Bedakan durasi, prasyarat hasil, tanggal rencana, dan keterbatasan sumber daya. ID P1 sampai P8 sama dengan contoh Bab 11.

## Batas data

Gunakan data berizin dan dianonimkan. Jangan memasukkan identitas pasien, isi rekam medis, kata sandi, token, atau dokumen rahasia ke repositori. Catat metadata bukti bila dokumen asli tidak boleh dibagikan.
