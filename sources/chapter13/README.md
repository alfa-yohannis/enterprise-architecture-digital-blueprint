# Sumber Bab 13

| Berkas | Kegunaan |
| --- | --- |
| [`analisis-business-case.py`](analisis-business-case.py) | Pendalaman opsional: pemeriksaan lokal dengan Python pustaka standar |
| [`data-biaya-manfaat-mpi.csv`](data-biaya-manfaat-mpi.csv) | Data atau templat terstruktur; baca komentar penggunaan dan nama kolom |
| [`templat-business-case.md`](templat-business-case.md) | Petunjuk, contoh terisi, lembar kerja, dan daftar periksa |
| [`templat-matriks-prioritas-portofolio.csv`](templat-matriks-prioritas-portofolio.csv) | Data atau templat terstruktur; baca komentar penggunaan dan nama kolom |

## Cara memakai

1. Baca tujuan dan Aktivitas Bab 13.
2. Salin templat ke folder tim dan isi bersama anggota berlatar bisnis serta teknis.
3. Bedakan fakta organisasi, asumsi latihan, dan target yang belum disetujui.
4. Tinjau bukti dan konsistensi ID sebelum digabung ke C4.

CSV memakai UTF-8 dan pemisah koma. Berkas baru memuat komentar `#` pada baris pertama; hapus komentar itu saat impor spreadsheet. Beberapa berkas lama langsung memakai header. Jangan menghapus header kolom. Angka tambahan pada Medikara adalah data sintetis, bukan hasil pengukuran organisasi nyata.

## Analisis biaya dan manfaat

Jalankan dari folder ini:

```powershell
python analisis-business-case.py arus-kas data-biaya-manfaat-mpi.csv
python analisis-business-case.py portofolio templat-matriks-prioritas-portofolio.csv
```

Skrip menerima subperintah `arus-kas` atau `portofolio` dan satu berkas CSV. Data arus kas dinyatakan dalam juta rupiah untuk 2027 sampai 2031, karena P3 pada Bab 12 berjalan April 2027 sampai Maret 2028. Tingkat diskonto, waktu arus kas, dan batas manfaat harus dinyatakan saat menafsirkan hasil.

## Batas data

Gunakan data berizin dan dianonimkan. Jangan memasukkan identitas pasien, isi rekam medis, kata sandi, token, atau dokumen rahasia ke repositori. Catat metadata bukti bila dokumen asli tidak boleh dibagikan.
