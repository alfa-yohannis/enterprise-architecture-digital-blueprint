# Sumber Bab 14

| Berkas | Kegunaan |
| --- | --- |
| [`periksa-standar-teknologi.py`](periksa-standar-teknologi.py) | Pendalaman opsional: pemeriksaan lokal dengan Python pustaka standar |
| [`rubrik-presentasi-c4.md`](rubrik-presentasi-c4.md) | Petunjuk, contoh terisi, lembar kerja, dan daftar periksa |
| [`standar-teknologi-medikara.csv`](standar-teknologi-medikara.csv) | Data atau templat terstruktur; baca komentar penggunaan dan nama kolom |
| [`templat-daftar-periksa-kepatuhan.md`](templat-daftar-periksa-kepatuhan.md) | Petunjuk, contoh terisi, lembar kerja, dan daftar periksa |
| [`templat-piagam-architecture-board.md`](templat-piagam-architecture-board.md) | Petunjuk, contoh terisi, lembar kerja, dan daftar periksa |

## Cara memakai

1. Baca tujuan dan Aktivitas Bab 14.
2. Salin templat ke folder tim dan isi bersama anggota berlatar bisnis serta teknis.
3. Bedakan fakta organisasi, asumsi latihan, dan target yang belum disetujui.
4. Tinjau bukti dan konsistensi ID sebelum digabung ke C4.

CSV memakai UTF-8 dan pemisah koma. Berkas baru memuat komentar `#` pada baris pertama; hapus komentar itu saat impor spreadsheet. Beberapa berkas lama langsung memakai header. Jangan menghapus header kolom. Angka tambahan pada Medikara adalah data sintetis, bukan hasil pengukuran organisasi nyata.

## Pemeriksaan standar

Jalankan `python periksa-standar-teknologi.py --help` sebelum memilih masukan. Contoh yang dapat diulang: `python periksa-standar-teknologi.py --tanggal 2027-10-30`. Deklarasi proyek bawaan sengaja mencampur komponen yang patuh, berdispensasi, dan melanggar. Kode keluar 1 pada contoh ini merupakan hasil latihan yang diharapkan. Hasil pemeriksaan membantu tinjauan; dispensasi tetap memerlukan pemilik, alasan, masa berlaku, dan persetujuan.

## Batas data

Gunakan data berizin dan dianonimkan. Jangan memasukkan identitas pasien, isi rekam medis, kata sandi, token, atau dokumen rahasia ke repositori. Catat metadata bukti bila dokumen asli tidak boleh dibagikan.
