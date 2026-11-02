# Sumber Bab 09

| Berkas | Kegunaan |
| --- | --- |
| [`contoh-aturan-identitas-pasien.md`](contoh-aturan-identitas-pasien.md) | Petunjuk, contoh terisi, lembar kerja, dan daftar periksa |
| [`contoh-patient-fhir.json`](contoh-patient-fhir.json) | Contoh struktur data sintetis untuk pendalaman |
| [`lembar-kerja-aktivitas.md`](lembar-kerja-aktivitas.md) | Petunjuk, contoh terisi, lembar kerja, dan daftar periksa |
| [`templat-matriks-bangun-beli-langganan.csv`](templat-matriks-bangun-beli-langganan.csv) | Data atau templat terstruktur; baca komentar penggunaan dan nama kolom |
| [`templat-tabel-rasionalisasi-aplikasi.csv`](templat-tabel-rasionalisasi-aplikasi.csv) | Data atau templat terstruktur; baca komentar penggunaan dan nama kolom |

## Cara memakai

1. Baca tujuan dan Aktivitas Bab 9.
2. Salin templat ke folder tim dan isi bersama anggota berlatar bisnis serta teknis.
3. Bedakan fakta organisasi, asumsi latihan, dan target yang belum disetujui.
4. Tinjau bukti dan konsistensi ID sebelum digabung ke C3.

CSV memakai UTF-8 dan pemisah koma. Berkas baru memuat komentar `#` pada baris pertama; hapus komentar itu saat impor spreadsheet. Beberapa berkas lama langsung memakai header. Jangan menghapus header kolom. Angka tambahan pada Medikara adalah data sintetis, bukan hasil pengukuran organisasi nyata.

## Batas data

Gunakan data berizin dan dianonimkan. Jangan memasukkan identitas pasien, isi rekam medis, kata sandi, token, atau dokumen rahasia ke repositori. Catat metadata bukti bila dokumen asli tidak boleh dibagikan.
