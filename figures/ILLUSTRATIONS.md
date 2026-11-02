# Diagram Bab

Gambar aktif pada modul dan slide adalah diagram PNG berlabel. Setiap panah menyatakan alur atau relasi yang tertulis pada labelnya. Diagram disusun dari konsep, batasan, dan kasus pada naskah masing-masing bab, bukan hanya dari judul bab. Seluruh diagram ini dibuat tanpa TikZ.

PNG dipakai oleh LaTeX; SVG menyimpan versi vektor. Spesifikasi komponen, hubungan, catatan batas, dan dasar pemilihan terdapat pada [chapter-diagrams.json](chapter-diagrams.json). Kotak memakai notasi generik, bukan klaim konformansi ArchiMate atau reproduksi gambar standar.

| Bab | Isi diagram | PNG | SVG |
| --- | --- | --- | --- |
| 01 | Lima sudut pandang untuk satu perubahan organisasi | [gambar](ch01-diagram-konsep.png) | [vektor](ch01-diagram-konsep.svg) |
| 02 | Concern menentukan view; metode mengatur penyusunannya | [gambar](ch02-diagram-konsep.png) | [vektor](ch02-diagram-konsep.svg) |
| 03 | Keterlacakan pendorong, sasaran, dan kebutuhan arsitektur | [gambar](ch03-diagram-konsep.png) | [vektor](ch03-diagram-konsep.svg) |
| 04 | Satu model bersama menghasilkan beberapa view | [gambar](ch04-diagram-konsep.png) | [vektor](ch04-diagram-konsep.svg) |
| 05 | Kapabilitas mendukung tahap value stream | [gambar](ch05-diagram-konsep.png) | [vektor](ch05-diagram-konsep.svg) |
| 06 | Identitas pasien menjadi pangkal hubungan informasi | [gambar](ch06-diagram-konsep.png) | [vektor](ch06-diagram-konsep.svg) |
| 07 | Menelusuri masalah layanan sampai ketergantungan teknologi | [gambar](ch07-diagram-konsep.png) | [vektor](ch07-diagram-konsep.svg) |
| 08 | Target bisnis menyatukan backbone dan platform digital | [gambar](ch08-diagram-konsep.png) | [vektor](ch08-diagram-konsep.svg) |
| 09 | MPI menautkan identitas; rekam medis tetap pada sumbernya | [gambar](ch09-diagram-konsep.png) | [vektor](ch09-diagram-konsep.svg) |
| 10 | Target teknologi dan pengawasan AI melintasi domain | [gambar](ch10-diagram-konsep.png) | [vektor](ch10-diagram-konsep.svg) |
| 11 | Gap lintas domain diubah menjadi paket kerja terukur | [gambar](ch11-diagram-konsep.png) | [vektor](ch11-diagram-konsep.svg) |
| 12 | Keadaan transisi menjadi pijakan migrasi yang dapat dijalankan | [gambar](ch12-diagram-konsep.png) | [vektor](ch12-diagram-konsep.svg) |
| 13 | Manfaat memerlukan perubahan kerja yang dimiliki bisnis | [gambar](ch13-diagram-konsep.png) | [vektor](ch13-diagram-konsep.svg) |
| 14 | Tata kelola arsitektur menghubungkan rilis dan peninjauan target | [gambar](ch14-diagram-konsep.png) | [vektor](ch14-diagram-konsep.svg) |

## Membuat ulang

Jalankan dari akar repositori dengan Python, Matplotlib, dan Pillow:

```powershell
python tools/render-diagrams.py
python tools/render-diagrams.py --chapter 1 5
```

Font Titillium Web dibaca dari `module/fonts/`. PNG RGB maksimum 500 KiB; SVG menyimpan huruf sebagai path agar tampilannya tetap sama. Ubah `chapter-diagrams.json` untuk mengubah komponen atau relasi.

JPG ilustrasi terdahulu dan `illustration-prompts.json` disimpan sebagai arsip dan tidak lagi dirujuk pada gambar bab aktif. Diagram TikZ pendukung yang sudah ada tetap menjadi bagian materi. Daftar semua berkas dan tempat pemakaiannya ada di [README.md](README.md).

## Catatan keselarasan dengan naskah

Teks pada PNG diperiksa terhadap naskah bab. Sebagian besar sejalan. Tiga hal belum sama dan perlu diubah lewat `chapter-diagrams.json` lalu dirender ulang:

- Bab 05: urutan tahap pada gambar "Pasien dikenali, Janji diperoleh, Pasien dilayani", sedangkan Bab 5 memakai urutan "Memesan layanan, Hadir dan terverifikasi, Diperiksa dan didiagnosis". Nama kapabilitas "Pengelolaan data pasien" dan "Pengelolaan jadwal" juga tidak ada pada peta 15 kapabilitas Bab 5, yang memakai Pengelolaan Rekam Medis dan Penjadwalan Layanan.
- Bab 06: gambar menghubungkan Kunjungan langsung ke Klaim, sedangkan naskah Bab 6 menempatkan Tagihan di antara keduanya.
- Bab 13: manfaat "Identitas ganda berkurang" tidak ada pada lima manfaat Tabel Bab 13, karena ukuran itu berasal dari *outcome* Bab 3.
