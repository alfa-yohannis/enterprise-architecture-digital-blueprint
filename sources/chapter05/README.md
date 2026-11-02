<!-- Daftar berkas pendukung Bab 5 dan cara memakainya. Baca sebelum mengerjakan Aktivitas. -->

# Sumber Bab 05

| Berkas | Kegunaan |
| --- | --- |
| [`templat-capability-map.csv`](templat-capability-map.csv) | Templat peta kapabilitas tim dua tingkat beserta kolom skor, kepentingan, keyakinan, dan bukti |
| [`medikara-capability-map.csv`](medikara-capability-map.csv) | Contoh terisi 15 kapabilitas tingkat 2 Medikara Health, dengan angka yang sama seperti naskah Bab 5 |
| [`templat-value-stream.md`](templat-value-stream.md) | Templat value stream dan pemetaan silang, dengan contoh enam tahap rawat jalan Medikara |
| [`kriteria-heatmap.md`](kriteria-heatmap.md) | Skala kondisi 1 sampai 3, cara menilai, contoh terisi, lembar kerja, dan daftar periksa heatmap |
| [`periksa-kapabilitas.py`](periksa-kapabilitas.py) | Pendalaman opsional: memeriksa struktur peta dan menghitung urutan awal prioritas dengan Python pustaka standar |

## Cara memakai

1. Baca Aktivitas Bab 5, lalu salin templat ke folder tim.
2. Isi bersama anggota berlatar bisnis dan teknis. Bedakan fakta organisasi, pengandaian, dan hal yang belum diketahui.
3. Pakai kode kapabilitas yang sama pada artefak Bab 6, Bab 7, dan Bab 8.
4. Tinjau bukti dan konsistensi kode sebelum digabung ke C2.

Berkas CSV memakai UTF-8 dan pemisah koma. Baris pertama berisi komentar `#`; hapus baris itu saat impor ke spreadsheet. Kolom `skor_kondisi` berisi 1, 2, 3, atau `belum dinilai`. Angka pada contoh Medikara adalah pengandaian, bukan hasil pengukuran organisasi nyata.

## Pemeriksa kapabilitas

```
python periksa-kapabilitas.py
python periksa-kapabilitas.py peta-tim.csv
```

Contoh Medikara harus lolos pemeriksaan struktur. Templat kosong menghasilkan temuan, karena belum ada kapabilitas yang diisi. Lolos pemeriksaan tidak berarti skor benar: skor dan bukti tetap ditinjau tim.

## Batas data

Gunakan data berizin dan dianonimkan. Identitas pasien, isi rekam medis, kata sandi, token, dan dokumen rahasia tidak boleh masuk ke repositori. Bila dokumen asli tidak boleh dibagikan, catat metadata buktinya: jenis dokumen, periode, dan pemiliknya.
