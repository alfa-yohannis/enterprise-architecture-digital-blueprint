# Sumber Modul

Berkas pendukung setiap bab mencakup templat, contoh terisi, data sintetis Medikara, model Archi, dan pemeriksa Python opsional. Baca README tiap bab untuk kegunaan berkas dan hasil pemeriksaan yang diharapkan. Salin templat ke folder tim sebelum mengisi.

| Bab | Isi | Tonggak |
| --- | --- | --- |
| [01](chapter01/README.md) | Orientasi dan piagam tim | C1 |
| [02](chapter02/README.md) | Pemangku kepentingan dan ruang lingkup | C1 |
| [03](chapter03/README.md) | Strategi dan visi | C1 |
| [04](chapter04/README.md) | Model ArchiMate | C2 |
| [05](chapter05/README.md) | Kapabilitas dan value stream | C2 |
| [06](chapter06/README.md) | Konsep informasi dan CRUD | C2 |
| [07](chapter07/README.md) | Portofolio aplikasi dan lanskap teknologi | C2 |
| [08](chapter08/README.md) | Pilihan bisnis target | C3 |
| [09](chapter09/README.md) | Data dan aplikasi target | C3 |
| [10](chapter10/README.md) | Standar teknologi, ADR, dan kesiapan AI | C3 |
| [11](chapter11/README.md) | Gap dan paket kerja | C3 |
| [12](chapter12/README.md) | Transisi dan peta jalan | C4 |
| [13](chapter13/README.md) | Business case dan portofolio | C4 |
| [14](chapter14/README.md) | Tata kelola dan presentasi | C4 |

## Hubungan antartonggak

- **C1, Bab 1 sampai 3:** piagam, profil organisasi, ruang lingkup, rantai motivasi, dan visi menjadi dasar penilaian kondisi saat ini.
- **C2, Bab 4 sampai 7:** model, kapabilitas, informasi, aplikasi, dan teknologi membentuk kondisi awal yang dapat ditelusuri ke bukti.
- **C3, Bab 8 sampai 11:** kondisi target dibandingkan dengan C2. Gap dan paket kerja memakai ID yang stabil; contoh P1 sampai P8 mengikuti data jadwal Bab 12.
- **C4, Bab 12 sampai 14:** dependensi menjadi peta jalan, manfaat menjadi business case, dan keputusan serta dispensasi dipelihara oleh forum arsitektur.

CSV memakai UTF-8 dengan pemisah koma. Beberapa CSV baru diawali komentar `#`; hapus baris komentar saat mengimpor ke spreadsheet, lalu pertahankan header. Skrip baru menyaring komentar secara otomatis. Angka tambahan Medikara adalah asumsi latihan, sehingga perlu diganti bukti saat diterapkan ke organisasi nyata.

Periksa satuan setiap sumber: contoh arus kas Bab 13 memakai juta rupiah untuk 2027 sampai 2031, sedangkan biaya portofolionya memakai miliar rupiah. Simpan dokumen bukti yang tidak boleh dibagikan di lokasi berizin dan catat metadatanya dalam lembar kerja.

## Angka bersama lintas bab

Angka berikut dipakai oleh lebih dari satu bab. Bila salah satunya diubah, naskah, slide, gambar, dan sumber yang memakainya ikut diubah.

| Hal | Nilai | Berkas sumber |
| --- | --- | --- |
| Peta kapabilitas | 15 kapabilitas saat ini; target 18, yaitu 3 baru, 8 diperkuat, 5 dipertahankan, 2 dihentikan | [`chapter05/medikara-capability-map.csv`](chapter05/medikara-capability-map.csv), [`chapter08/medikara-capability-map-target.csv`](chapter08/medikara-capability-map-target.csv) |
| Jadwal paket kerja | Bulan 0 = Juli 2026; P3 April 2027 sampai Maret 2028; P6 selesai Maret 2029; P8 mulai Januari 2029; P5 selesai September 2030 | [`chapter12/paket-kerja-medikara.csv`](chapter12/paket-kerja-medikara.csv) |
| Titik keputusan SIMRS | Percontohan Depok Desember 2028; K3 Maret 2029; Bekasi dan Bogor Desember 2029; Jakarta dan Bandung September 2030 | [`chapter12/paket-kerja-medikara.csv`](chapter12/paket-kerja-medikara.csv) |
| Arus kas MPI | 2027 sampai 2031, TCO Rp7.800 juta, NPV Rp2.271 juta | [`chapter13/data-biaya-manfaat-mpi.csv`](chapter13/data-biaya-manfaat-mpi.csv) |
| Lab ulang | 18.000 pemeriksaan per tahun, Rp150.000 per pemeriksaan, turun menjadi 6.000 per tahun | [`chapter13/data-biaya-manfaat-mpi.csv`](chapter13/data-biaya-manfaat-mpi.csv) |
| Biaya SIMRS | Rp29 miliar untuk opsi membeli di Bab 9; Rp48,0 miliar untuk inisiatif I3 di Bab 13, dengan cakupan lebih luas | [`chapter13/templat-matriks-prioritas-portofolio.csv`](chapter13/templat-matriks-prioritas-portofolio.csv) |
| Akun karyawan keluar | 212 akun aktif | [`chapter05/medikara-capability-map.csv`](chapter05/medikara-capability-map.csv), [`chapter11/contoh-gap-medikara.csv`](chapter11/contoh-gap-medikara.csv) |
| Integrasi | Batas model 36 pasangan, 21 pasangan aktif, target 9 koneksi | [`chapter07/README.md`](chapter07/README.md) |
| Pemetaan paket ke inisiatif | P1 ke I2, P2 ke I4, P3 ke I1, P5 ke I3, P6 ke I5, P7 ke I7, P8 ke I6; P4 dibagi ke I3 dan I5; I8 bukan paket kerja | [`chapter13/templat-matriks-prioritas-portofolio.csv`](chapter13/templat-matriks-prioritas-portofolio.csv) |
