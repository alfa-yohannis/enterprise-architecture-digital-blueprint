# Sumber Bab 04

| Berkas | Kegunaan |
| --- | --- |
| [`konvensi-penamaan-model.md`](konvensi-penamaan-model.md) | Petunjuk, contoh terisi, lembar kerja, dan daftar periksa |
| [`lembar-kerja-model-berlapis.md`](lembar-kerja-model-berlapis.md) | Petunjuk, contoh terisi, lembar kerja, dan daftar periksa |
| [`medikara-janji-temu.archimate`](medikara-janji-temu.archimate) | Model contoh yang dibuka melalui Archi |
| [`panduan-instalasi-archi.md`](panduan-instalasi-archi.md) | Petunjuk, contoh terisi, lembar kerja, dan daftar periksa |
| [`periksa-model.py`](periksa-model.py) | Pendalaman opsional: pemeriksaan lokal dengan Python pustaka standar |

| [`medikara-cacat.xml`](medikara-cacat.xml) | Salinan pertukaran dengan dua cacat disengaja untuk mereproduksi listing Bab 4 |

## Pemeriksaan model

Jalankan dari folder ini:

```powershell
python periksa-model.py medikara-janji-temu.archimate
python periksa-model.py medikara-cacat.xml
```

Model Archi awal memiliki 26 elemen, 30 relasi, tanpa kesalahan atau peringatan. Berkas XML latihan memiliki 28 elemen, 31 relasi, satu kesalahan referensi, dan enam peringatan; kode keluar 1 memang diharapkan. Pemeriksa konsistensi ini tidak menggantikan validasi skema XML atau penilaian semantik ArchiMate. Gunakan model `.archimate` sebagai sumber untuk praktik Archi.

## Cara memakai

1. Baca tujuan dan Aktivitas Bab 4.
2. Salin templat ke folder tim dan isi bersama anggota berlatar bisnis serta teknis.
3. Bedakan fakta organisasi, asumsi latihan, dan target yang belum disetujui.
4. Tinjau bukti dan konsistensi ID sebelum digabung ke C2.

CSV memakai UTF-8 dan pemisah koma. Berkas baru memuat komentar `#` pada baris pertama; hapus komentar itu saat impor spreadsheet. Beberapa berkas lama langsung memakai header. Jangan menghapus header kolom. Angka tambahan pada Medikara adalah data sintetis, bukan hasil pengukuran organisasi nyata.

## Batas data

Gunakan data berizin dan dianonimkan. Jangan memasukkan identitas pasien, isi rekam medis, kata sandi, token, atau dokumen rahasia ke repositori. Catat metadata bukti bila dokumen asli tidak boleh dibagikan.
