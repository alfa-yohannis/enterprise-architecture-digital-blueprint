<!-- Indeks berkas pendukung Bab 3. Baca sebelum mengerjakan Aktivitas dan Latihan. -->

# Sumber Bab 03

| Berkas | Kegunaan |
| :-- | :-- |
| [`templat-rantai-motivasi.csv`](templat-rantai-motivasi.csv) | Templat dan contoh rantai motivasi Medikara: 15 elemen dari *driver* sampai *requirement* |
| [`lembar-penilaian-model-operasi.md`](lembar-penilaian-model-operasi.md) | Lembar penilaian integrasi dan standardisasi per lingkup, dengan skala skor dan contoh terisi |
| [`templat-prinsip-arsitektur.md`](templat-prinsip-arsitektur.md) | Templat prinsip dengan nama, pernyataan, alasan, implikasi, uji dua opsi, serta catatan konflik dan dispensasi |
| [`templat-visi-arsitektur.md`](templat-visi-arsitektur.md) | Kerangka delapan bagian untuk visi arsitektur dua sampai tiga halaman |
| [`periksa-keterlacakan.py`](periksa-keterlacakan.py) | Pendalaman opsional: pemeriksaan keterlacakan dengan Python pustaka standar |

## Cara memakai

1. Baca tujuan dan Aktivitas Bab 3.
2. Salin templat ke folder tim dan isi bersama anggota berlatar bisnis serta teknis.
3. Bedakan fakta organisasi, asumsi latihan, dan target yang belum disetujui.
4. Tinjau bukti dan konsistensi nomor elemen sebelum digabung ke C1.

CSV memakai UTF-8 dan pemisah koma. Baris pertama berisi komentar `#`; hapus baris itu saat impor ke *spreadsheet*, dan jangan menghapus nama kolomnya. Angka tambahan pada Medikara adalah data sintetis, bukan hasil pengukuran organisasi nyata.

## Pendalaman keterlacakan

`python periksa-keterlacakan.py` memeriksa CSV bawaan. Contoh sengaja memuat R3 yang tidak memiliki induk, sehingga kode keluar 1 adalah temuan latihan yang diharapkan. Perbaiki pada salinan dengan menambah hubungan yang dapat dibenarkan atau menghapus kebutuhan yang tidak didukung strategi. Lolos struktur tidak membuktikan alasan bisnis benar.

## Batas data

Gunakan data berizin dan dianonimkan. Jangan memasukkan identitas pasien, isi rekam medis, kata sandi, token, atau dokumen rahasia ke repositori. Catat metadata bukti bila dokumen asli tidak boleh dibagikan.
