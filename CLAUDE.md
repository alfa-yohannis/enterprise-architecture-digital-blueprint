# Aturan Penulisan Modul IT40513 Enterprise Architecture & Digital Blueprint

Aturan ini diturunkan dari aturan penulisan modul `advanced-web-engineering`,
lalu disesuaikan untuk mata kuliah S2 Magister Teknologi Informasi, peminatan
Digital Enterprise Architecture. Keempat mata kuliah peminatan ini
(IT40513, IT40613, IT40713, IT40813) memakai aturan yang sama, sehingga
seluruh modul terbaca sebagai satu suara.

## 1. Bahasa

- Bahasa Indonesia baku yang alami, seperti dosen Indonesia menjelaskan kepada
  mahasiswanya. Susunan kalimat tidak boleh terasa seperti terjemahan bahasa
  Inggris.
- Kalimat pendek, satu gagasan per kalimat. Keterbacaan dan kemudahan dipahami
  didahulukan di atas istilah yang terdengar canggih atau gaya bahasa
  berbunga-bunga.
- Kalimat aktif dengan subjek sistem, organisasi, tim, atau mahasiswa. Hindari
  "dapat dilakukan dengan cara", cukup "dilakukan dengan".
- Tanpa kata pengisi: "sangat", "sebenarnya", "tentu saja", "cukup jelas bahwa".
- Tanpa kata ganti orang pertama dan kedua, tunggal maupun jamak: saya, aku,
  -ku, kami, kita, Anda, kamu, engkau, -mu, kalian. Tanpa sapaan seperti "mari".
  Kata ganti orang ketiga (dia, ia, mereka) boleh.
- Tanpa em dash. Tidak ada karakter "—" dan tidak ada `---` di LaTeX. Pakai
  koma, titik dua, titik, atau tanda kurung. Rentang ditulis "1 sampai 3".
- Istilah asing yang belum punya padanan mapan, atau yang janggal bila
  diterjemahkan, tetap ditulis dalam bahasa Inggris dan dicetak miring:
  `\textit{stakeholder}`, `\textit{capability map}`, `\textit{value stream}`,
  `\textit{risk appetite}`, `\textit{API gateway}`, `\textit{dashboard}`,
  `\textit{tradeoff}`, `\textit{error}`, `\textit{query}`, `\textit{node}`.
  Istilah yang sudah diserap ditulis biasa: server, data, aplikasi, sistem.
  Nama diri (TOGAF, COBIT, Kubernetes, ArchiMate) tidak dimiringkan.
- Judul bab, judul seksi, dan judul slide menulis istilah Inggris tegak.
- Imbuhan bahasa Indonesia pada istilah Inggris memakai tanda hubung:
  di-`\textit{deploy}`, di-`\textit{onboard}`.
- Singkatan dieja penuh saat pertama muncul di bab itu, lalu dipakai
  singkatnya: "Application Programming Interface (API)". Setiap singkatan baru
  wajib ditambahkan ke tabel **Daftar Singkatan** di `README.md`.
- Nama berkas, perintah, dan potongan kode inline memakai `\texttt{}`. Jalur
  berkas memakai `\berkas{}`. Garis bawah di luar `lstlisting` wajib di-escape.
- Pakai kata "Aktivitas", bukan "Praktikum".

## 2. Audiens

- Mahasiswa berlatar belakang campuran: sebagian non-teknis (bisnis,
  manajemen, akuntansi, hukum, kesehatan), sebagian dari ilmu komputer,
  rekayasa perangkat lunak, atau teknologi informasi. Banyak yang sudah bekerja.
- Isi utama bab tidak menganggap mahasiswa bisa memprogram. Setiap konsep
  diawali dari masalah organisasi yang nyata, baru masuk ke konsep dan istilah.
- Materi teknis yang lebih dalam ditaruh di kotak
  `\begin{pendalaman} ... \end{pendalaman}`. Isi utama bab tetap utuh tanpa
  kotak ini.
- Level S2: analisis kritis, keputusan beserta `\textit{tradeoff}`-nya,
  pembacaan laporan industri dan artikel ilmiah, justifikasi tertulis.
- Tatap muka hanya hari Sabtu untuk membahas progres capstone. Modul dan slide
  harus bisa dipelajari mandiri.

## 3. Struktur bab

Urutan seksi tetap:

1. `\section*{Tujuan Pembelajaran}`: tepat tiga butir, tiap butir diawali kata
   kerja terukur (Menjelaskan, Membedakan, Menganalisis, Merancang, Menilai),
   bukan "Memahami" atau "Mengetahui". Isinya sama dengan README.
2. `\section{Pendahuluan}`: dua sampai tiga paragraf. Paragraf terakhir
   menyebut rujukan utama bab dengan `\cite{}`.
3. Seksi materi, tiga sampai delapan buah.
4. `\section{Aktivitas: Judul}`: kerja tim untuk capstone (lihat bagian 7).
5. `\section{Ringkasan}`: empat sampai lima paragraf naratif, bukan daftar
   berbutir. Paragraf terakhir menutup dengan pesan utama bab.
6. `\section{Latihan}`: paling banyak tiga latihan (lihat bagian 8).

## 4. Cara menjelaskan satu konsep

Pola tiga langkah, dipakai berulang:

1. **Pernyataan.** Satu paragraf berisi definisi dan cara kerjanya.
2. **Analogi sehari-hari.** Diambil dari kehidupan biasa atau dunia kerja:
   warung dengan satu kasir, loket pembayaran, gudang cabang, denah gedung,
   rapat RT. Analogi ditulis satu paragraf, lalu ditinggalkan.
3. **Contoh konkret.** Umumnya dua, ditulis sebagai `enumerate` dan diawali
   kalimat pengantar seperti "Dua contoh kasus nyata:". Contohnya memakai
   angka: 18 klinik, 1,2 juta kunjungan, biaya Rp450 juta per tahun.

Transisi antarbagian memakai pertanyaan eksplisit yang langsung dijawab:
"Pertanyaan kemudian muncul: siapa yang memutuskan?". Perbedaan yang sering
tertukar dibereskan lewat seksi khusus: "Dua hal pada X sering tertukar.
Pembagiannya begini." Setiap konsekuensi ditulis eksplisit dan dihitung:
"Keputusan ini punya dua konsekuensi. Pertama, ... Kedua, ...".

## 5. Kasus berjalan: Medikara Health

Keempat mata kuliah memakai satu kasus fiktif yang sama. Fakta dasarnya tidak
boleh diubah:

- PT Medikara Nusa Sehat ("Medikara Health"), organisasi fiktif, jaringan
  layanan kesehatan swasta: 5 rumah sakit (Jakarta, Bekasi, Depok, Bogor,
  Bandung), 18 klinik pratama, 1 laboratorium rujukan, 12 apotek; sekitar
  4.800 karyawan dan sekitar 1,2 juta kunjungan pasien per tahun.
- Kondisi saat ini: SIMRS (Sistem Informasi Manajemen Rumah Sakit) monolitik
  on-premise di tiap rumah sakit dengan versi berbeda karena hasil akuisisi;
  ERP keuangan terpusat; aplikasi pasien "Medikara+" (janji temu dan
  telekonsultasi) buatan vendor; integrasi point-to-point ke BPJS Kesehatan dan
  SATUSEHAT (berbasis HL7 FHIR); data pasien tersebar; banyak laporan
  manajemen masih disusun dengan spreadsheet.
- Strategi 2026 sampai 2030, "Satu Pasien, Satu Rekam Medis": layanan
  terintegrasi lintas fasilitas, ekosistem mitra (klinik mitra, asuransi,
  laboratorium, apotek daring, layanan kesehatan karyawan perusahaan),
  modernisasi ke cloud, kepatuhan pada UU PDP dan aturan rekam medis
  elektronik.
- Pemicu: insiden kebocoran data pasien skala kecil lewat vendor pada 2025,
  temuan audit internal tentang kontrol akses yang lemah, antrean layanan yang
  panjang, biaya integrasi yang tinggi.

Penerapan materi pada kasus ditulis di kotak
`\begin{kasus} ... \end{kasus}` (judul khusus:
`\begin{kasus}[title={Kasus Medikara Health: ...}]`). Detail tambahan boleh
dikarang asalkan tidak bertentangan dengan fakta dasar dan dengan bab lain.
Skenario pengandaian ditandai "Misalkan".

## 6. Gambar dan tabel

- Tiap seksi materi punya minimal satu gambar atau satu tabel.
- Diagram dibuat dengan TikZ dan disimpan sebagai `figures/chNN-nama.tex`
  (hanya satu `tikzpicture`, tanpa preamble), supaya modul dan slide memakai
  gambar yang sama. Modul memanggil `\input{../figures/chNN-nama.tex}`, slide
  memanggil `\input{../../figures/chNN-nama.tex}`.
- Ilustrasi raster (JPG) bersifat opsional; diagram TikZ sudah cukup. Bila
  dipakai, ilustrasi dibuat dengan `codex` atau `agy`, atau diambil dari
  sumber berlisensi Creative Commons dengan atribusi lengkap di caption
  (judul, pembuat, sumber, lisensi). Tanpa teks di dalam gambar, paling banyak
  dua per bab, disimpan sebagai `figures/chNN-nama.jpg`, ukuran berkas paling
  besar sekitar 500 KB. Ilustrasi yang belum ada dipasang bersyarat dengan
  `\IfFileExists` sehingga build tetap bersih.
- Setiap bab juga memuat satu diagram konsep `figures/chNN-diagram-konsep.png`
  (dengan sumber SVG), dibangkitkan `tools/render-diagrams.py` dari
  `figures/chapter-diagrams.json`. Istilah dan urutan di dalamnya wajib sama
  dengan naskah bab.
- Palet TikZ tetap: `blue!8` untuk tahap biasa, `orange!12` untuk tahap yang
  ditekankan, `green!10` untuk hasil akhir, `praditagreen!15` untuk node
  induk, `red!22` dan `gray!35` untuk penanda masalah.
- Gaya panah tetap: `panah/.style={-{Stealth[length=2mm]}, thick}`.
- Font di dalam gambar `\scriptsize` atau `\footnotesize`, keterangan kecil
  memakai `{\tiny\mdseries ...}`. Lebar gambar paling besar sekitar 12 cm.
- Tabel memakai `tabularx` selebar `\textwidth`, dengan `\hline` di setiap
  baris, termasuk sebelum baris judul dan sesudah baris terakhir.
- Tiap gambar dan tabel wajib punya `\caption` dan `\label`, dan dirujuk dari
  naskah dengan `\ref{}` sebelum kemunculannya.
- Label diberi awalan bab: `fig:chNN-nama`, `tab:chNN-nama`, `lst:chNN-nama`.
  Tabel latihan: `tab:chNN-latN-contoh` dan `tab:chNN-latN-hasil`.

## 7. Aktivitas

- Kerja tim campuran latar belakang untuk proyek capstone "Cetak Biru
  Transformasi Digital". Tim memakai organisasi nyata (dengan izin dan data
  yang dianonimkan) atau kasus Medikara Health.
- Isinya: tujuan, pembagian peran dalam tim, langkah kerja, luaran, kaitan
  dengan tonggak capstone, kriteria penilaian singkat, dan berkas pendukung di
  `\berkas{sources/chapterNN/...}`.
- Tonggak bersama: C1 Konteks dan Strategi (Pertemuan 1 sampai 3), C2 Kondisi
  Saat Ini (4 sampai 7, ditinjau menjelang UTS), C3 Kondisi Target (8 sampai
  11), C4 Peta Jalan dan Tata Kelola (12 sampai 14, dipresentasikan menjelang
  UAS).
- Pendalaman teknis opsional dipisahkan dengan jelas.

## 8. Latihan

- Paling banyak tiga latihan, isinya sama dengan README.
- Tiap latihan diberi judul `\subsection*{Latihan N: Judul}`, bernomor urut
  dari 1 dan konsisten dengan penomoran pada caption tabelnya.
- Tiap latihan berisi: kalimat pembuka yang menyebut apa yang dibuktikan,
  langkah kerja sebagai `enumerate`, satu tabel contoh yang sudah terisi, dan
  satu tabel lembar isian kosong berisi `\dots`.
- Langkah kerja ditulis berurutan sesuai waktu pelaksanaan.
- Latihan ditutup dengan dua atau tiga pertanyaan analisis yang jawabannya
  menuntut pembacaan data, bukan hafalan.
- Angka pada tabel contoh diambil dari kasus Medikara atau dari sumber publik
  yang dirujuk. Hasil tiap mahasiswa boleh berbeda; yang dinilai adalah
  penalaran dan perbandingannya.

## 9. Kode

Kode hanya muncul di kotak pendalaman dan di `sources/`.

- Contoh skrip memakai Python. Spesifikasi memakai format aslinya (OpenAPI
  YAML, manifest Kubernetes YAML, JSON).
- Tanpa fungsi bersarang. Setiap modul, kelas, dan fungsi punya komentar yang
  menjelaskan mengapa dan apa akibatnya. Nama menjelaskan isinya, tanpa
  singkatan satu huruf. Angka ajaib diberi nama konstanta.
- Baris maksimum 88 karakter; baris yang dikutip ke listing maksimum 78.
- Tanpa karakter tab. Indentasi dua spasi, termasuk pada berkas `.tex`.
- Setiap `lstlisting` punya `caption` dan `label`, dan captionnya menyebut
  lokasi berkas: `tersedia di \berkas{sources/chapterNN/nama}`.
- Kode di naskah adalah salinan berkas di `sources/chapterNN/`.
- Berkas di `sources/` diberi komentar berbahasa Indonesia di baris pertama:
  kegunaan dan cara memakainya.

## 10. Etika

- Data organisasi nyata yang dipakai mahasiswa wajib seizin organisasi dan
  dianonimkan. Data pribadi pasien atau karyawan tidak boleh dipakai.
- Kegiatan yang membebani sistem milik orang lain (uji beban, pemindaian
  keamanan) hanya untuk sistem sendiri atau yang sudah berizin tertulis.
  Peringatan ditulis di dekat perintahnya.

## 11. Referensi

- Sumber primer lebih dahulu: standar dan spesifikasi resmi, regulasi dari
  JDIH, buku acuan, artikel ilmiah, laporan industri. Blog dan tutorial tidak
  dipakai sebagai rujukan utama.
- Rujukan inti di `module/references.bib`; rujukan khusus satu bab di
  `module/bib/chapterNN.bib` dengan kunci berawalan `cNN-`. Rujukan yang
  dipakai lebih dari satu bab dipindahkan ke `references.bib`.
- Setiap entri punya `url` yang dapat dibuka dan
  `note = {Diakses (tanggal)}` untuk sumber daring.
- Sitasi dipasang pada kalimat yang benar-benar mengambil isinya.

## 12. Struktur repositori

- Naskah bab: `module/chapterNN.tex`, disatukan oleh `module/enterprise-architecture-digital-blueprint.tex`.
- Berkas pendukung: `sources/chapterNN/`, masing-masing punya `README.md`
  berisi tabel daftar berkas dan kegunaannya.
- Slide: `slides/sessionNN/sessionNN.tex`, diawali
  `\documentclass[aspectratio=169, table, 12pt]{beamer}` lalu
  `\input{../preamble}`. Judul slide dua baris:
  `\title{\Huge Baris Satu\\ \vspace{10pt} Baris Dua}`. Isinya ringkasan bab,
  memakai gambar dan tabel yang sama dengan babnya. Angka pada slide wajib sama
  dengan angka pada naskah bab.
- Gambar: `figures/`. `module/fonts`, `slides/theme`,
  `figures/logo_universitas.png`, dan `figures/building.png` adalah berkas asli
  di repo ini, supaya modul dan slide bisa dikompilasi di Windows tanpa symlink.
- Peta pertemuan, kaitan capstone, rujukan utama, dan daftar singkatan:
  `README.md` di akar.
