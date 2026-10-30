# Enterprise Architecture & Digital Blueprint

IT40513 · Magister Teknologi Informasi, peminatan Digital Enterprise Architecture, Universitas Pradita.

Mata kuliah ini membahas cara organisasi memahami dirinya secara utuh, dari strategi, proses bisnis, data, dan aplikasi sampai teknologi. Pemahaman itu lalu dipakai untuk merencanakan perubahan. Praktik ini disebut arsitektur *enterprise* atau EA (*Enterprise Architecture*). Hasil akhirnya adalah cetak biru transformasi digital (*digital blueprint*), yaitu dokumen yang menjelaskan kondisi saat ini, kondisi yang dituju, selisih di antara keduanya, dan urutan langkah untuk menutup selisih itu. Rujukan utamanya adalah TOGAF (*The Open Group Architecture Framework*) Standard, bahasa pemodelan ArchiMate dengan alat gratis Archi, dan panduan arsitektur bisnis BIZBOK (*Business Architecture Body of Knowledge*). Mata kuliah ini juga membahas EA di sektor publik Indonesia melalui Arsitektur SPBE (Sistem Pemerintahan Berbasis Elektronik), serta peran EA dalam transformasi digital dan pemanfaatan AI (*Artificial Intelligence*). Pengampu: Alfa Yohannis.

Mahasiswa datang dari dua kelompok latar belakang. Sebagian dari bisnis, manajemen, akuntansi, hukum, kesehatan, dan bidang lain. Sebagian lagi dari ilmu komputer, rekayasa perangkat lunak, atau teknologi informasi. Karena itu setiap pertemuan dimulai dari masalah organisasi yang nyata, baru kemudian masuk ke konsep dan istilah. Kemampuan memprogram tidak dibutuhkan. Materi teknis yang lebih dalam disediakan sebagai pendalaman opsional bagi mahasiswa berlatar CS (*Computer Science*), SE (*Software Engineering*), atau TI (Teknologi Informasi). Mata kuliah ini dijalankan sebagai satu proyek *capstone* bersama tiga mata kuliah lain: [IT40613 Digital Platform & API Economy](https://github.com/alfa-yohannis/digital-platform-api-economy), [IT40713 Cloud-Native & Microservices Architecture](https://github.com/alfa-yohannis/cloud-native-microservices-architecture), dan [IT40813 IT Governance, Risk & Compliance](https://github.com/alfa-yohannis/it-governance-risk-compliance). Di dalam proyek itu, mata kuliah ini memegang peta besarnya. Tatap muka hanya berlangsung hari Sabtu untuk membahas progres proyek, sehingga modul dan slide disusun agar dapat dipelajari secara mandiri.

## Peta Pertemuan

Urutan pertemuan mengikuti empat tonggak *capstone* sekaligus alur ADM (*Architecture Development Method*) dalam TOGAF. Tim lebih dahulu memahami konteks dan strategi organisasi, lalu memotret kondisi saat ini, merancang kondisi target, dan terakhir menyusun peta jalan beserta tata kelolanya. Setiap pertemuan menghasilkan satu artefak yang langsung masuk ke cetak biru tim, sehingga tatap muka hari Sabtu dipakai untuk membahas artefak, bukan mengulang materi. Tonggak C2 ditinjau menjelang UTS (Ujian Tengah Semester), dan tonggak C4 dipresentasikan menjelang UAS (Ujian Akhir Semester). Kolom terakhir menunjukkan luaran untuk tonggak yang sedang berjalan.

| # | Pertemuan | Aktivitas | Luaran Capstone |
| --- | --- | --- | --- |
| 1 | **Orientasi Mata Kuliah dan Dasar Arsitektur Enterprise** | Membentuk tim campuran, memilih organisasi, dan membagi peran | C1: piagam tim, profil organisasi, dan glosarium bersama |
| 2 | Kerangka Kerja Arsitektur: TOGAF, Zachman, dan Arsitektur SPBE | Memetakan pemangku kepentingan dan menetapkan ruang lingkup kerja arsitektur | C1: peta pemangku kepentingan dan *Statement of Architecture Work* |
| 3 | Strategi, Model Operasi, dan Visi Arsitektur | Menurunkan strategi menjadi rantai motivasi, model operasi, dan prinsip arsitektur | C1: visi arsitektur |
| 4 | Pemodelan Arsitektur dengan ArchiMate dan Archi | Memodelkan satu layanan inti dari pasien sampai *server* | C2: model ArchiMate awal |
| 5 | Arsitektur Bisnis Saat Ini: Capability Map dan Value Stream | Menyusun *capability map*, *value stream*, dan *heatmap* berbasis bukti | C2: arsitektur bisnis saat ini |
| 6 | Arsitektur Data dan Informasi Saat Ini | Menelusuri lokasi dan aliran data penting, lalu menandai data pribadi | C2: peta informasi, matriks data dan aplikasi, daftar masalah data |
| 7 | Arsitektur Aplikasi dan Teknologi Saat Ini | Menilai portofolio aplikasi dan memetakan integrasi | C2: dokumen kondisi saat ini untuk tinjauan UTS |
| 8 | Arsitektur Bisnis Target untuk Transformasi Digital | Membandingkan opsi kondisi target bisnis, lalu memilih satu beserta alasannya | C3: arsitektur bisnis target |
| 9 | Arsitektur Data dan Aplikasi Target | Merancang identitas pasien tunggal dan rasionalisasi aplikasi | C3: arsitektur data dan aplikasi target |
| 10 | Arsitektur Teknologi Target dan Kesiapan AI | Menulis catatan keputusan arsitektur dan menilai kesiapan AI | C3: arsitektur teknologi target dan catatan keputusan |
| 11 | Gap Analysis dan Paket Kerja | Menyusun matriks gap, lalu mengelompokkannya menjadi paket kerja | C3: dokumen kondisi target dan *gap analysis* |
| 12 | Arsitektur Transisi, Peta Jalan, dan Perencanaan Migrasi | Menyusun arsitektur transisi dan peta jalan 2026 sampai 2030 | C4: peta jalan dan rencana migrasi |
| 13 | Business Case dan Portofolio Inisiatif | Menyusun *business case* dan memprioritaskan portofolio inisiatif | C4: *business case* dan portofolio berprioritas |
| 14 | Tata Kelola Arsitektur dan Praktik Arsitektur yang Lincah | Merancang tata kelola arsitektur dan mempresentasikan cetak biru | C4: rancangan tata kelola dan presentasi akhir |

Pertemuan dikelompokkan ke dalam empat Bagian yang sejajar dengan tonggak *capstone*. Bagian I (1 sampai 3) menyamakan kosakata, memperkenalkan kerangka kerja, dan menghasilkan visi arsitektur. Bagian ini setara dengan fase *Preliminary* dan *Architecture Vision* dalam ADM. Bagian II (4 sampai 7) membekali tim dengan bahasa pemodelan, lalu memotret kondisi saat ini domain demi domain: bisnis, data, aplikasi, dan teknologi. Ini adalah fase B, C, dan D untuk *baseline*. Bagian III (8 sampai 11) mengulang ketiga fase itu untuk kondisi target, lalu menutupnya dengan *gap analysis*. Bagian IV (12 sampai 14) mencakup fase E sampai H: arsitektur transisi, peta jalan, *business case*, dan tata kelola arsitektur.

**Pembagian materi dengan tiga mata kuliah lain.** Topik milik mata kuliah lain hanya disinggung singkat, dengan keterangan bahwa topik itu dibahas rinci di mata kuliah yang bersangkutan. Model bisnis platform, desain API (*Application Programming Interface*), dan SATUSEHAT dari sisi integrasi dibahas di IT40613. Strategi migrasi 7R, *microservices*, dan operasi *cloud* dibahas di IT40713. COBIT, manajemen risiko, keamanan informasi, dan UU PDP (Undang-Undang Pelindungan Data Pribadi) dibahas di IT40813. Mata kuliah ini memegang gambaran utuhnya, yaitu bagaimana semua bagian itu saling terkait dan perubahan mana yang dikerjakan lebih dahulu.

---

## Rencana Pertemuan

### Bagian I. Fondasi dan Konteks Strategis (1 sampai 3)

Bagian ini menyamakan bahasa di dalam tim campuran dan menghasilkan tonggak C1.

#### Pertemuan 01 · Orientasi Mata Kuliah dan Dasar Arsitektur Enterprise

**Tujuan.**

1. Menjelaskan masalah organisasi yang dijawab EA dan nilai yang dapat diharapkan darinya, dengan merujuk bukti empiris.
2. Mendeskripsikan sebuah organisasi memakai lima sudut pandang bersama: strategi, bisnis, data, aplikasi, dan teknologi.
3. Menyusun piagam tim dan profil organisasi sebagai titik awal *capstone*.

**Topik.** Gejala organisasi yang tumbuh tanpa arsitektur. Pengertian *enterprise*, arsitektur, dan EA. Perbedaan EA, arsitektur solusi, dan arsitektur perangkat lunak. Lima sudut pandang atas organisasi. Penyetaraan istilah teknis bagi latar non-teknis, misalnya aplikasi, basis data, integrasi, dan *cloud*. Penyetaraan istilah bisnis bagi latar teknis, misalnya strategi, model bisnis, model operasi, dan *stakeholder*. Bukti empiris tentang nilai EA. Peran arsitek *enterprise*. Proyek *capstone* bersama empat mata kuliah. Kasus Medikara Health.

**Aktivitas.** Tim dibentuk dengan 4 sampai 5 anggota berlatar campuran. Tim memilih satu organisasi nyata, sebaiknya tempat kerja salah satu anggota, dengan izin tertulis dan data yang dianonimkan. Tim yang tidak punya akses memakai kasus Medikara Health. Empat peran dibagi dan digilir pada tiap tonggak: koordinator, analis bisnis, analis teknologi, dan pemodel. Analis bisnis menyusun profil satu halaman tentang layanan, pelanggan, struktur, dan masalah utama organisasi. Analis teknologi mendaftar sistem yang dipakai sehari-hari. Koordinator menulis piagam tim berisi tujuan, peran, aturan kerja, dan jadwal sinkronisasi dengan tiga mata kuliah lain. Pemodel menyusun glosarium bersama agar istilah bisnis dan teknis dipakai dengan arti yang sama. Luarannya adalah piagam tim, profil organisasi, dan glosarium untuk C1. *Pendalaman teknis (opsional):* membaca Kotusev (2019) tentang artefak EA yang benar-benar dipakai di 27 organisasi, lalu membandingkannya dengan dokumentasi arsitektur perangkat lunak yang biasa dibuat tim pengembang.

**Latihan.**

1. Sebuah rumah sakit memakai tiga aplikasi pendaftaran pasien yang berbeda. Jelaskan dua kerugian bisnis dari kondisi itu dan cara EA membantu mencegahnya.
2. Seorang manajer berkata, "EA hanya menghasilkan diagram yang tidak dibaca orang." Tanggapi pernyataan itu dengan merujuk minimal satu temuan penelitian.
3. Ambil satu contoh keputusan di sebuah organisasi yang gagal karena bagian bisnis dan bagian TI memakai istilah dengan arti berbeda. Uraikan istilah yang disalahpahami dan dampaknya.

#### Pertemuan 02 · Kerangka Kerja Arsitektur: TOGAF, Zachman, dan Arsitektur SPBE

**Tujuan.**

1. Menjelaskan struktur TOGAF Standard edisi ke-10 dan urutan fase ADM.
2. Membandingkan TOGAF, Zachman Framework, dan Arsitektur SPBE dari sisi tujuan, cakupan, dan cara pakai.
3. Menyusun peta pemangku kepentingan beserta *concern* dan ruang lingkup kerja arsitektur.

**Topik.** Masalah dokumen arsitektur yang tidak dapat dibandingkan satu sama lain. Konsep *stakeholder*, *concern*, *view*, dan *viewpoint* menurut ISO/IEC/IEEE 42010:2022. Struktur TOGAF Standard edisi ke-10 beserta pembaruan 2025. *Fundamental Content* dan *Series Guides*. Fase ADM dari *Preliminary* sampai *Architecture Change Management*. Perbedaan *deliverable*, artefak, dan *building block*. Zachman Framework sebagai ontologi, bukan metode. Arsitektur SPBE dan enam domainnya. Regulasi SPBE dan percepatan transformasi digital pemerintah. Penyesuaian (*tailoring*) kerangka untuk organisasi menengah.

**Aktivitas.** Tim memetakan pemangku kepentingan organisasi ke matriks kekuasaan dan kepentingan, lalu menuliskan *concern* utama tiap kelompok. Analis bisnis memimpin identifikasi pemangku kepentingan dan *concern* bisnis. Analis teknologi melengkapi *concern* teknis dan regulasi. Pemodel memilih fase ADM dan artefak minimum yang akan dipakai tim. Koordinator merangkum ruang lingkup (unit organisasi, horizon waktu, domain, dan batasan) dalam *Statement of Architecture Work* yang ringkas. Tim yang memilih instansi pemerintah juga memetakan domain TOGAF ke domain Arsitektur SPBE. Luarannya adalah peta pemangku kepentingan dan *Statement of Architecture Work* untuk C1. *Pendalaman teknis (opsional):* memetakan sel Zachman ke jenis model yang lazim di rekayasa perangkat lunak, misalnya model data, diagram komponen, dan diagram *deployment*, lalu menilai sel mana yang paling sering kosong di organisasi nyata.

**Latihan.**

1. Direktur keuangan dan kepala TI menilai proyek yang sama. Tuliskan dua *concern* yang mungkin untuk masing-masing, lalu tentukan *view* yang cocok untuk tiap *concern*.
2. Jelaskan mengapa Zachman disebut ontologi, sedangkan ADM disebut metode. Apa akibatnya bila keduanya dipakai bersama dalam satu proyek?
3. Bandingkan enam domain Arsitektur SPBE dengan empat domain arsitektur TOGAF. Tunjukkan domain yang tidak punya padanan langsung dan jelaskan cara menanganinya.

#### Pertemuan 03 · Strategi, Model Operasi, dan Visi Arsitektur

**Tujuan.**

1. Menurunkan pemicu, tujuan, dan *outcome* organisasi menjadi kebutuhan arsitektur yang dapat ditelusuri.
2. Menentukan model operasi organisasi berdasarkan tingkat integrasi dan standardisasi proses bisnisnya.
3. Merumuskan visi arsitektur dan prinsip arsitektur lengkap dengan alasan dan implikasinya.

**Topik.** Masalah strategi yang tidak pernah sampai ke keputusan sistem. Elemen motivasi: *driver*, *assessment*, *goal*, *outcome*, prinsip, dan *requirement*. Rantai keterlacakan dari strategi ke kebutuhan. Model operasi menurut Ross, Weill, dan Robertson: diversifikasi, koordinasi, replikasi, dan unifikasi. *Core diagram* sebagai gambaran satu halaman. Fase *Preliminary* dan *Architecture Vision*. Format prinsip arsitektur: nama, pernyataan, alasan, dan implikasi. Visi arsitektur sebagai kesepakatan awal dengan direksi.

**Aktivitas.** Tim menyusun rantai motivasi organisasi, dari pemicu seperti insiden kebocoran data atau antrean yang panjang, sampai tujuan dan *outcome* yang terukur. Analis bisnis memimpin telaah dokumen strategi dan wawancara singkat dengan pemangku kepentingan. Analis teknologi menilai pemicu yang berasal dari sistem, misalnya biaya integrasi atau kontrol akses yang lemah. Seluruh tim menentukan model operasi saat ini dan model operasi yang diinginkan, lalu menulis 5 sampai 8 prinsip arsitektur. Koordinator merangkai semuanya menjadi visi arsitektur dua sampai tiga halaman yang dapat dibaca direksi. Luarannya adalah visi arsitektur yang melengkapi C1. *Pendalaman teknis (opsional):* menurunkan satu prinsip menjadi aturan desain yang dapat diperiksa, misalnya prinsip "satu sumber kebenaran untuk data pasien" menjadi kriteria tinjauan rancangan integrasi.

**Latihan.**

1. Turunkan strategi "Satu Pasien, Satu Rekam Medis" menjadi satu *goal*, dua *outcome* terukur, dan satu *requirement*.
2. Jaringan 12 apotek menjalankan proses yang sama di semua cabang, tetapi pelanggan di tiap kota berbeda dan jarang berpindah cabang. Model operasi mana yang paling cocok, dan apa akibatnya bagi aplikasi dan data?
3. Kritik prinsip "Semua sistem harus memakai teknologi terbaru." Tulis ulang menjadi prinsip yang baik lengkap dengan alasan dan implikasi.

### Bagian II. Memotret Kondisi Saat Ini (4 sampai 7)

Bagian ini membekali tim dengan bahasa pemodelan, lalu memotret organisasi domain demi domain. Hasilnya adalah tonggak C2 yang ditinjau menjelang UTS.

#### Pertemuan 04 · Pemodelan Arsitektur dengan ArchiMate dan Archi

**Tujuan.**

1. Menjelaskan kerangka inti ArchiMate: lapisan, aspek, elemen, dan relasi.
2. Membangun model berlapis di Archi yang menghubungkan layanan bisnis, proses, aplikasi, dan teknologi.
3. Memilih *viewpoint* yang sesuai dengan *concern* pemangku kepentingan tertentu.

**Topik.** Masalah diagram kotak dan panah yang dibaca berbeda oleh tiap orang. Perbedaan model, diagram, dan repositori. Kerangka inti ArchiMate: lapisan bisnis, aplikasi, dan teknologi. Aspek struktur aktif, perilaku, dan struktur pasif. Elemen strategi, motivasi, serta implementasi dan migrasi. Relasi struktural, dependensi, dan dinamis. *Viewpoint* dan *view*. Archi sebagai alat pemodelan gratis. ArchiMate 4 yang terbit April 2026 dan bedanya dengan ArchiMate 3.2 yang masih dipakai Archi.

**Aktivitas.** Setiap anggota memasang Archi. Tim memodelkan satu layanan inti dari ujung ke ujung, misalnya janji temu rawat jalan Medikara: pasien, layanan bisnis, proses, aplikasi Medikara+ dan SIMRS (Sistem Informasi Manajemen Rumah Sakit), sampai *server*. Analis bisnis dan analis teknologi bekerja berpasangan. Satu memodelkan lapisan bisnis, satu lagi lapisan aplikasi dan teknologi, lalu keduanya menyepakati titik sambungnya. Pemodel menyiapkan struktur folder, konvensi penamaan, dan berkas model bersama. Rantai motivasi dari C1 dipindahkan ke *motivation view*. Luarannya adalah model ArchiMate awal berisi *layered view* dan *motivation view* sebagai fondasi C2. *Pendalaman teknis (opsional):* memeriksa konsistensi model secara otomatis dengan skrip jArchi, atau mengekspor model ke format pertukaran model ArchiMate (*Open Exchange Format*) lalu membaca strukturnya.

**Latihan.**

1. Uraikan rantai elemen dan relasi dari "Pasien" sampai "*server* basis data SIMRS" untuk layanan pendaftaran. Sebutkan jenis relasi pada tiap langkah.
2. Seorang direktur hanya ingin tahu aplikasi mana yang mendukung tiap layanan pasien. *Viewpoint* apa yang cocok, dan elemen apa yang sengaja tidak ditampilkan?
3. ArchiMate 4 menggabungkan elemen perilaku lintas lapisan. Jelaskan satu keuntungan dan satu kerugian perubahan itu bagi organisasi yang sudah punya model ArchiMate 3.2.

#### Pertemuan 05 · Arsitektur Bisnis Saat Ini: Capability Map dan Value Stream

**Tujuan.**

1. Membedakan kapabilitas bisnis, proses bisnis, dan unit organisasi.
2. Menyusun *capability map* dua tingkat dan satu *value stream* utama untuk organisasi *capstone*.
3. Menilai kondisi kapabilitas dalam *heatmap* yang didukung bukti.

**Topik.** Masalah organisasi yang hanya dipahami lewat bagan struktur dan SOP (*Standard Operating Procedure*). Kapabilitas bisnis: apa yang dilakukan, bukan bagaimana atau oleh siapa. *Capability map* bertingkat. Model referensi industri kesehatan dari BIZBOK versi 15 sebagai titik awal. *Value stream* dari sudut pandang pelanggan. Pemetaan silang *value stream* ke kapabilitas. Peta organisasi. *Heatmap* kapabilitas berdasarkan kematangan, kepentingan strategis, dan keluhan.

**Aktivitas.** Analis bisnis memimpin penyusunan *capability map* tingkat 1 dan 2 dengan bahan dari wawancara, SOP, dan laporan manajemen. Analis teknologi memeriksa dukungan sistem untuk tiap kapabilitas. Tim menyusun satu *value stream* utama, misalnya "Pasien menerima layanan rawat jalan", lalu memetakan tiap tahapnya ke kapabilitas. *Heatmap* disusun dengan skala 1 sampai 3. Setiap warna merah wajib disertai bukti seperti angka antrean, jumlah keluhan, atau temuan audit. Pemodel memasukkan kapabilitas dan *value stream* ke Archi. Luarannya adalah *capability map*, *value stream*, dan *heatmap* untuk C2. *Pendalaman teknis (opsional):* menghubungkan satu kapabilitas ke ukuran yang dapat diambil dari sistem, misalnya waktu tunggu dari catatan sistem pendaftaran, lalu menilai apakah data itu cukup andal untuk dipakai.

**Latihan.**

1. Apakah "Pendaftaran pasien di loket" sebuah kapabilitas, proses, atau unit organisasi? Ubah menjadi nama kapabilitas yang tepat dan jelaskan alasannya.
2. Susun tahapan *value stream* "Klaim asuransi dibayar" dari sudut pandang perusahaan asuransi, lalu pasangkan satu kapabilitas dengan tiap tahap.
3. Dua kapabilitas berwarna merah, tetapi anggaran hanya cukup untuk satu. Tentukan kriteria pemilihan dan bukti yang dibutuhkan.

#### Pertemuan 06 · Arsitektur Data dan Informasi Saat Ini

**Tujuan.**

1. Mengidentifikasi konsep informasi bisnis utama beserta pemiliknya.
2. Memetakan lokasi dan aliran data penting di antara aplikasi dengan matriks CRUD (*Create, Read, Update, Delete*).
3. Menganalisis masalah kualitas, duplikasi, dan klasifikasi data yang menghambat strategi.

**Topik.** Masalah data pasien yang tersebar dan laporan yang disusun dengan *spreadsheet*. Data, informasi, dan konsep bisnis. Model data konseptual dalam bahasa bisnis. Data induk (*master data*), data referensi, dan data transaksi. Kepemilikan data dan *data stewardship*. Lokasi dan aliran data tingkat tinggi. Matriks CRUD antara data dan aplikasi. Klasifikasi data, termasuk data pribadi dan data kesehatan menurut UU PDP, yang dibahas rinci di IT40813. Kewajiban rekam medis elektronik menurut Peraturan Menteri Kesehatan Nomor 24 Tahun 2022. Dimensi kualitas data.

**Aktivitas.** Tim menyusun daftar 10 sampai 15 konsep informasi utama, misalnya Pasien, Kunjungan, Rekam Medis, Resep, Tagihan, dan Klaim. Analis bisnis menentukan pemilik bisnis dan pemakai tiap konsep. Analis teknologi menelusuri di aplikasi mana data itu dibuat, dibaca, diubah, dan dihapus. Hasilnya disusun sebagai matriks CRUD dan diagram aliran data tingkat tinggi. Tim menandai data pribadi dan data kesehatan, lalu mencatat masalah seperti identitas pasien ganda, angka yang berbeda di dua laporan, dan laporan manual. Pemodel memodelkan *business object* dan *data object* di Archi. Luarannya adalah peta informasi, matriks CRUD, dan daftar masalah data untuk C2. *Pendalaman teknis (opsional):* menyusun model data logis untuk entitas Pasien dan Kunjungan, lalu membandingkannya dengan *resource* Patient dan Encounter pada HL7 (*Health Level Seven*) FHIR (*Fast Healthcare Interoperability Resources*) yang dipakai SATUSEHAT.

**Latihan.**

1. Tiga rumah sakit Medikara memberi nomor rekam medis sendiri-sendiri. Jelaskan dampaknya pada layanan pasien, laporan manajemen, dan kepatuhan.
2. Bagaimana matriks CRUD membantu menemukan data yang tidak punya pemilik jelas? Berikan satu contoh.
3. Tentukan klasifikasi untuk jadwal praktik dokter, hasil laboratorium, dan nomor rekening karyawan. Jelaskan alasannya.

#### Pertemuan 07 · Arsitektur Aplikasi dan Teknologi Saat Ini

**Tujuan.**

1. Menyusun katalog aplikasi dan menilainya dengan model TIME (*Tolerate, Invest, Migrate, Eliminate*).
2. Memetakan integrasi antaraplikasi dan menunjukkan titik rawan pola *point-to-point*.
3. Merangkum lanskap teknologi tingkat tinggi beserta utang teknis dan risikonya.

**Topik.** Masalah aplikasi yang bertambah tanpa rencana. Katalog aplikasi: fungsi, pemilik, pengguna, vendor, umur, dan biaya. Pemetaan aplikasi ke kapabilitas. Penilaian portofolio aplikasi dengan model TIME. Katalog antarmuka. Pola integrasi *point-to-point* dan akibatnya. Integrasi dengan BPJS (Badan Penyelenggara Jaminan Sosial) Kesehatan dan SATUSEHAT dilihat dari sisi arsitektur, sedangkan desain API-nya dibahas rinci di IT40613. Lanskap teknologi tingkat tinggi: lokasi, *hosting*, jaringan, dan platform. Utang teknis (*technical debt*). Merangkai dokumen kondisi saat ini.

**Aktivitas.** Analis teknologi memimpin penyusunan katalog aplikasi dan katalog antarmuka. Analis bisnis menilai nilai bisnis tiap aplikasi bersama penggunanya. Kedua penilaian digabung ke dalam kuadran TIME. Pemodel menggambar *application cooperation view* dan *technology view* di Archi. Koordinator merangkai artefak Pertemuan 4 sampai 7 menjadi dokumen kondisi saat ini, lengkap dengan ringkasan lima masalah terbesar. Luarannya adalah katalog aplikasi, diagram integrasi, ringkasan teknologi, dan dokumen C2 yang siap ditinjau menjelang UTS. *Pendalaman teknis (opsional):* menghitung jumlah koneksi pada pola *point-to-point* dengan rumus n(n-1)/2, lalu memperkirakan biaya pemeliharaan integrasi per tahun dari data insiden dan permintaan perubahan.

**Latihan.**

1. Aplikasi bernilai bisnis tinggi tetapi berkualitas teknis rendah masuk kuadran TIME yang mana? Langkah apa yang wajar untuknya?
2. Medikara punya lima SIMRS berbeda versi, satu ERP (*Enterprise Resource Planning*), satu aplikasi pasien, dan dua sistem eksternal. Berapa koneksi maksimum bila semuanya saling terhubung *point-to-point*? Mengapa angka ini penting bagi direksi?
3. Sebutkan tiga pertanyaan untuk vendor guna menilai risiko sebuah aplikasi lama, dan jelaskan alasan tiap pertanyaan.

### Bagian III. Merancang Kondisi Target (8 sampai 11)

Bagian ini mengulang domain yang sama untuk kondisi yang dituju, lalu membandingkannya dengan kondisi saat ini. Hasilnya adalah tonggak C3.

#### Pertemuan 08 · Arsitektur Bisnis Target untuk Transformasi Digital

**Tujuan.**

1. Menganalisis pilihan transformasi digital memakai kerangka *Designed for Digital*.
2. Merumuskan model operasi target dan kapabilitas yang perlu dibangun, diperkuat, atau dihentikan.
3. Merancang *value stream* target beserta ukuran keberhasilannya.

**Topik.** Masalah transformasi digital yang dimulai dari membeli teknologi. Digitisasi, digitalisasi, dan transformasi digital. Lima blok bangunan *Designed for Digital*: *shared customer insights*, *operational backbone*, *digital platform*, *accountability framework*, dan *external developer platform*. Model operasi target. Opsi kondisi target dan *business scenario*. Kapabilitas target dan peta perubahan kapabilitas. Ekosistem mitra sebagai kapabilitas, yang dibahas rinci di IT40613. *Value stream* target.

**Aktivitas.** Tim menyusun dua sampai tiga opsi kondisi target bisnis, misalnya sentralisasi penuh layanan pasien atau inti yang distandarkan dengan keleluasaan lokal. Analis bisnis memimpin perumusan opsi dan kriteria penilaiannya. Analis teknologi menilai kelayakan tiap opsi dari kondisi saat ini. Tim memilih satu opsi dan menuliskan alasannya, termasuk hal yang dikorbankan. Pemodel menandai kapabilitas yang baru, diperkuat, dan dihentikan pada *capability map*. Luarannya adalah arsitektur bisnis target untuk C3: model operasi target, *capability map* target, dan *value stream* target. *Pendalaman teknis (opsional):* memilih kapabilitas yang layak dijadikan layanan bersama (*shared service*) dan menuliskan antarmuka bisnisnya, sebagai bahan desain API di IT40613.

**Latihan.**

1. Jelaskan perbedaan *operational backbone* dan *digital platform* dengan contoh dari Medikara.
2. Sentralisasi layanan pasien memberi efisiensi tetapi mengurangi keleluasaan rumah sakit di daerah. Tuliskan *trade-off* ini dalam tiga kalimat yang dapat dibaca direksi.
3. Mengapa kapabilitas pengelolaan kemitraan muncul di kondisi target tetapi tidak di kondisi saat ini? Apa syarat agar kapabilitas itu berjalan?

#### Pertemuan 09 · Arsitektur Data dan Aplikasi Target

**Tujuan.**

1. Merancang arsitektur data target yang menjamin satu identitas dan satu rekam medis untuk tiap pasien.
2. Menyusun lanskap aplikasi target beserta keputusan rasionalisasi untuk tiap aplikasi.
3. Mengevaluasi pilihan membangun sendiri, membeli, atau berlangganan SaaS (*Software as a Service*) dengan kriteria yang eksplisit.

**Topik.** Masalah satu pasien dengan banyak identitas. MPI (*Master Patient Index*) dan manajemen data induk. Arsitektur data untuk analitik dan laporan manajemen. Prinsip satu sumber kebenaran. Lanskap aplikasi target. Rasionalisasi aplikasi: pertahankan, ganti, gabungkan, atau hentikan. Pola integrasi target pada tingkat konsep, yaitu *hub*, platform integrasi, dan API, yang dibahas rinci di IT40613. Hubungan dengan SATUSEHAT dan BPJS Kesehatan sebagai pihak eksternal. Keputusan membangun, membeli, atau berlangganan.

**Aktivitas.** Analis teknologi memimpin rancangan data dan aplikasi target. Analis bisnis memastikan setiap keputusan mengacu pada kapabilitas target dan prinsip dari C1. Tim menyusun tabel rasionalisasi yang memberi satu keputusan untuk tiap aplikasi saat ini. Untuk satu keputusan besar, misalnya pengganti lima SIMRS, tim membandingkan minimal dua opsi dengan kriteria berbobot. Pemodel menggambar *application cooperation view* target dan *information structure view*. Luarannya adalah arsitektur data dan aplikasi target untuk C3. *Pendalaman teknis (opsional):* merancang aturan pencocokan identitas pasien secara deterministik dan probabilistik, lalu membandingkan risiko salah gabung dan salah pisah pada kedua pendekatan.

**Latihan.**

1. Jelaskan tanpa istilah teknis mengapa MPI dibutuhkan sebelum laporan manajemen terpadu dapat dipercaya.
2. Susun lima kriteria untuk memilih antara membangun sendiri dan membeli SIMRS baru. Beri bobot dan jelaskan alasannya.
3. Sebuah aplikasi dinilai *Eliminate*, tetapi masih dipakai satu unit kecil untuk laporan ke regulator. Apa yang perlu diperiksa sebelum aplikasi itu dihentikan?

#### Pertemuan 10 · Arsitektur Teknologi Target dan Kesiapan AI

**Tujuan.**

1. Merumuskan arah teknologi target tingkat tinggi beserta standar teknologi organisasi.
2. Mendokumentasikan keputusan arsitektur penting sebagai ADR (*Architecture Decision Record*) lengkap dengan *trade-off*-nya.
3. Menilai kesiapan organisasi memanfaatkan AI dari sisi kapabilitas, data, dan tata kelola.

**Topik.** Masalah keputusan teknologi yang diambil per proyek. Arsitektur teknologi tingkat tinggi dalam fase D. Katalog standar teknologi dan *technology reference model*. Pilihan lokasi penerapan: *on-premise*, *private cloud*, *public cloud*, dan *hybrid*, yang dibahas rinci di IT40713. Keamanan sebagai *concern* lintas domain, yang dibahas rinci di IT40813. Struktur ADR: konteks, opsi, keputusan, dan konsekuensi. AI sebagai kapabilitas baru. Kesiapan data untuk AI. Inventaris model dan agen AI. Peran EA dalam tata kelola AI.

**Aktivitas.** Analis teknologi menyusun arah teknologi target dan daftar standar. Tim menulis minimal tiga ADR, misalnya tentang lokasi penyimpanan rekam medis, pola integrasi, dan identitas pengguna terpusat. Analis bisnis memimpin identifikasi dua sampai tiga peluang AI yang terkait langsung dengan kapabilitas target, misalnya prediksi antrean atau ringkasan rekam medis untuk dokter. Kedua analis lalu menilai kesiapan data dan risiko tiap peluang. Pemodel memperbarui *technology view* target. Luarannya adalah arsitektur teknologi target, kumpulan ADR, dan penilaian kesiapan AI untuk C3. *Pendalaman teknis (opsional):* memetakan satu kasus AI ke komponen teknisnya, yaitu sumber data, *pipeline*, model, antarmuka, dan pemantauan, lalu menandai titik kendali yang dibutuhkan.

**Latihan.**

1. Tulis satu ADR singkat untuk keputusan menyimpan rekam medis di pusat data sendiri atau di *cloud*. Sertakan minimal dua opsi beserta konsekuensinya.
2. Mengapa peluang AI sebaiknya dipetakan dulu ke kapabilitas, bukan langsung ke produk atau vendor? Berikan satu contoh kegagalan bila urutannya dibalik.
3. Survei industri 2026 menunjukkan banyak organisasi belum tahu agen AI apa saja yang berjalan di dalamnya. Artefak EA apa yang dapat menutup celah itu, dan siapa yang memeliharanya?

#### Pertemuan 11 · Gap Analysis dan Paket Kerja

**Tujuan.**

1. Menyusun *gap analysis* lintas domain dengan membandingkan kondisi saat ini dan kondisi target.
2. Mengelompokkan gap menjadi paket kerja (*work package*) dengan ruang lingkup yang jelas.
3. Menganalisis dependensi antarpaket kerja dan dampaknya pada pemangku kepentingan.

**Topik.** Masalah daftar keinginan yang tidak pernah menjadi rencana. Teknik *gap analysis* dalam TOGAF: elemen yang dipertahankan, ditambahkan, dan dihapus. Gap yang tidak disengaja. Gap lintas domain bisnis, data, aplikasi, dan teknologi. Konsolidasi gap menjadi paket kerja dalam fase E. Matriks dependensi. Analisis dampak dan kesiapan perubahan. Merangkai dokumen kondisi target.

**Aktivitas.** Tim membuat matriks gap untuk tiap domain. Analis bisnis memimpin gap bisnis dan dampak perubahan pada unit kerja. Analis teknologi memimpin gap data, aplikasi, dan teknologi. Tim mengelompokkan gap menjadi 6 sampai 10 paket kerja dan memetakan dependensinya. Pemodel memakai elemen *gap* dan *work package* di Archi. Koordinator merangkai kondisi target, ADR, dan *gap analysis* menjadi dokumen C3. Luarannya adalah matriks gap, daftar paket kerja beserta dependensinya, dan dokumen C3. *Pendalaman teknis (opsional):* memakai skrip jArchi untuk menemukan elemen target yang belum punya padanan di model *baseline*, lalu membandingkan hasilnya dengan matriks gap yang disusun manual.

**Latihan.**

1. Apa arti sel "ada di *baseline*, tidak ada di target" dalam matriks gap? Berikan contoh dari Medikara dan tindakan yang dibutuhkan.
2. Paket kerja MPI dan paket kerja penggantian SIMRS saling bergantung. Mana yang didahulukan, dan apa risikonya bila urutannya dibalik?
3. Jelaskan mengapa gap yang paling mahal belum tentu gap yang paling penting.

### Bagian IV. Peta Jalan, Investasi, dan Tata Kelola (12 sampai 14)

Bagian ini mengubah rancangan menjadi rencana yang dapat didanai dan dijaga. Hasilnya adalah tonggak C4 yang dipresentasikan menjelang UAS.

#### Pertemuan 12 · Arsitektur Transisi, Peta Jalan, dan Perencanaan Migrasi

**Tujuan.**

1. Merancang dua sampai tiga arsitektur transisi yang masing-masing memberi nilai bisnis.
2. Menyusun peta jalan 2026 sampai 2030 berdasarkan dependensi, nilai, risiko, dan kapasitas organisasi.
3. Menyusun rencana migrasi tingkat tinggi beserta asumsi dan titik keputusannya.

**Topik.** Masalah transformasi besar yang dikerjakan sekaligus. Arsitektur transisi (*transition architecture*) dan *plateau*. Kriteria pengurutan: dependensi, nilai, risiko, dan kapasitas. Fase E dan F dalam ADM. Peta jalan untuk pembaca yang berbeda: direksi, unit bisnis, dan tim TI. Strategi migrasi aplikasi tingkat tinggi, sedangkan strategi 7R dibahas rinci di IT40713. Asumsi, titik keputusan, dan rencana mundur. *Migration view* di ArchiMate.

**Aktivitas.** Tim menetapkan arsitektur transisi. Contohnya, tahun pertama berfokus pada identitas pasien dan kontrol akses, tahap berikutnya pada konsolidasi SIMRS, lalu pada ekosistem mitra. Analis bisnis memastikan tiap transisi menghasilkan manfaat yang terlihat oleh pasien atau manajemen. Analis teknologi memeriksa kelayakan urutan teknisnya. Pemodel membuat *migration view* di Archi. Koordinator menyelaraskan jadwal dengan rencana migrasi *cloud* di IT40713, rencana API di IT40613, dan rencana kendali di IT40813. Luarannya adalah arsitektur transisi, peta jalan, dan rencana migrasi untuk C4. *Pendalaman teknis (opsional):* menyusun jadwal dengan analisis jalur kritis (*critical path*) sederhana dari matriks dependensi Pertemuan 11.

**Latihan.**

1. Mengapa setiap arsitektur transisi harus tetap bernilai bila proyek berikutnya ditunda? Berikan contoh transisi yang tidak memenuhi syarat itu.
2. Ringkas peta jalan tim menjadi satu halaman untuk direksi. Informasi apa yang dihilangkan, dan mengapa?
3. Tim TI Medikara hanya sanggup menangani dua proyek besar per tahun. Bagaimana batasan ini mengubah urutan peta jalan?

#### Pertemuan 13 · Business Case dan Portofolio Inisiatif

**Tujuan.**

1. Menyusun *business case* untuk inisiatif prioritas dengan manfaat, biaya, risiko, dan asumsi yang eksplisit.
2. Memetakan manfaat ke perubahan bisnis dan pemungkinnya dengan *benefits dependency network*.
3. Memprioritaskan portofolio inisiatif dengan kriteria berbobot dan menjustifikasi hasilnya.

**Topik.** Masalah proyek TI yang disetujui tanpa ukuran manfaat. Manajemen manfaat menurut Ward dan Daniel. *Benefits dependency network*. Komponen biaya dan TCO (*Total Cost of Ownership*). Ukuran finansial sederhana: *payback period* dan NPV (*Net Present Value*). Manfaat yang sulit diukur, seperti keselamatan pasien dan kepatuhan. Portofolio inisiatif dan prioritas berbasis kapabilitas. Kaitan dengan keputusan investasi di tingkat direksi, yang dibahas rinci di IT40813.

**Aktivitas.** Analis bisnis memimpin penyusunan *business case* untuk satu atau dua inisiatif prioritas. Analis teknologi menyusun perkiraan biaya lisensi, implementasi, migrasi, dan operasional, lengkap dengan sumber angkanya. Tim menyusun *benefits dependency network* dan matriks prioritas portofolio. Koordinator memastikan angka biaya selaras dengan perkiraan di IT40713 dan daftar risiko di IT40813. Luarannya adalah *business case* dan portofolio inisiatif berprioritas untuk C4. *Pendalaman teknis (opsional):* membuat analisis sensitivitas sederhana untuk melihat perubahan NPV bila biaya migrasi naik 30 persen atau manfaat tertunda satu tahun.

**Latihan.**

1. Sebuah inisiatif menjanjikan "efisiensi meningkat". Tulis ulang menjadi manfaat terukur lengkap dengan pemilik manfaat dan cara mengukurnya.
2. Inisiatif A punya NPV lebih tinggi, tetapi inisiatif B menutup temuan audit tentang kontrol akses. Bagaimana memutuskan di antara keduanya?
3. Jelaskan mengapa manfaat sering tidak tercapai walaupun proyeknya selesai tepat waktu dan sesuai anggaran.

#### Pertemuan 14 · Tata Kelola Arsitektur dan Praktik Arsitektur yang Lincah

**Tujuan.**

1. Merancang mekanisme tata kelola arsitektur: *architecture board*, tinjauan kepatuhan, dispensasi, dan repositori.
2. Membandingkan praktik EA tradisional dengan praktik yang lincah, termasuk tata kelola arsitektur di sektor publik.
3. Mempresentasikan dan mempertahankan cetak biru transformasi digital di hadapan pemangku kepentingan.

**Topik.** Masalah cetak biru yang berhenti sebagai dokumen. Fase G dan H dalam ADM: *implementation governance* dan *architecture change management*. *Architecture board*. Tinjauan kepatuhan, kontrak arsitektur, dan dispensasi. Repositori arsitektur dan pemeliharaannya. Tata kelola Arsitektur SPBE dan evaluasi Pemerintah Digital. Praktik arsitektur yang lincah menurut Open Agile Architecture Standard versi 2.0. Ukuran nilai praktik EA.

**Aktivitas.** Tim merancang tata kelola arsitektur untuk organisasinya: susunan dan mandat *architecture board*, daftar periksa kepatuhan yang diturunkan dari prinsip C1, alur dispensasi, dan cara memelihara repositori. Analis bisnis merancang keanggotaan dan alur keputusan. Analis teknologi merancang daftar periksa kepatuhan. Koordinator menyelaraskan rancangan ini dengan struktur tata kelola TI di IT40813. Tim lalu mempresentasikan seluruh cetak biru dari C1 sampai C4. Luarannya adalah rancangan tata kelola arsitektur dan presentasi akhir C4 menjelang UAS. *Pendalaman teknis (opsional):* merancang *fitness function* arsitektur, yaitu pemeriksaan otomatis atas kepatuhan pada standar teknologi di *pipeline* CI (*Continuous Integration*), lalu membandingkannya dengan tinjauan manual oleh *architecture board*.

**Latihan.**

1. Sebuah proyek mendesak meminta pengecualian dari prinsip "satu sumber data pasien". Rancang alur dispensasi yang tidak menghambat proyek, tetapi tetap menjaga arah arsitektur.
2. Bandingkan peran *architecture board* di perusahaan swasta dengan Tim Koordinasi SPBE di instansi pemerintah.
3. Pilih tiga ukuran untuk menilai apakah praktik EA memberi nilai dalam dua tahun pertama. Jelaskan mengapa "jumlah diagram yang dibuat" bukan ukuran yang baik.

---

## Kaitan dengan Capstone

Proyek *capstone* menghasilkan satu dokumen bersama, yaitu Cetak Biru Transformasi Digital. Tiap mata kuliah menyumbang bagian yang berbeda pada tiap tonggak. Tabel berikut merinci sumbangan IT40513.

| Tonggak | Pertemuan | Luaran dari mata kuliah ini |
| --- | --- | --- |
| C1 Konteks dan Strategi | 1 sampai 3 | Piagam tim, profil organisasi, glosarium bersama, peta pemangku kepentingan beserta *concern*, *Statement of Architecture Work*, dan visi arsitektur yang memuat rantai motivasi, model operasi, serta prinsip arsitektur |
| C2 Kondisi Saat Ini | 4 sampai 7 | Model ArchiMate *baseline*, *capability map* dan *heatmap*, *value stream*, peta informasi, matriks CRUD, katalog aplikasi dengan penilaian TIME, diagram integrasi, dan ringkasan teknologi. Ditinjau menjelang UTS |
| C3 Kondisi Target | 8 sampai 11 | Model operasi dan *capability map* target, arsitektur data dan aplikasi target, arsitektur teknologi target, kumpulan ADR, penilaian kesiapan AI, matriks gap, dan daftar paket kerja |
| C4 Peta Jalan dan Tata Kelola | 12 sampai 14 | Arsitektur transisi, peta jalan 2026 sampai 2030, rencana migrasi, *business case*, portofolio inisiatif berprioritas, dan rancangan tata kelola arsitektur. Dipresentasikan menjelang UAS |

Artefak mata kuliah ini menjadi acuan bagi tiga mata kuliah lain. *Capability map* dan *value stream* dipakai IT40613 untuk menentukan produk API dan mitra ekosistem. Katalog aplikasi, arsitektur teknologi target, dan peta jalan dipakai IT40713 untuk merencanakan migrasi ke *cloud*. Prinsip arsitektur, klasifikasi data, dan rancangan *architecture board* dipakai IT40813 untuk merancang kendali dan struktur tata kelola. Karena itu nama kapabilitas, aplikasi, dan konsep data harus sama di seluruh dokumen. Pemodel tim bertugas menjaga konsistensi ini.

## Kasus Berjalan: Medikara Health

PT Medikara Nusa Sehat ("Medikara Health") adalah organisasi fiktif yang dipakai bersama oleh keempat mata kuliah. Medikara adalah jaringan layanan kesehatan swasta dengan 5 rumah sakit (Jakarta, Bekasi, Depok, Bogor, dan Bandung), 18 klinik pratama, 1 laboratorium rujukan, dan 12 apotek. Jumlah karyawannya sekitar 4.800 orang, dengan sekitar 1,2 juta kunjungan pasien per tahun.

**Kondisi saat ini.** Tiap rumah sakit menjalankan SIMRS monolitik *on-premise* dengan versi yang berbeda karena berasal dari akuisisi. Keuangan memakai ERP terpusat. Aplikasi pasien Medikara+ untuk janji temu dan telekonsultasi dibuat oleh vendor. Integrasi ke BPJS Kesehatan dan ke SATUSEHAT milik Kementerian Kesehatan, yang berbasis HL7 FHIR, dibangun secara *point-to-point*. Data pasien tersebar, dan banyak laporan manajemen masih disusun dengan *spreadsheet*.

**Strategi 2026 sampai 2030.** Strategi berjudul "Satu Pasien, Satu Rekam Medis" punya empat arah. Pertama, layanan terintegrasi lintas fasilitas. Kedua, ekosistem mitra yang terbuka bagi klinik mitra, asuransi, laboratorium, apotek daring, dan layanan kesehatan karyawan perusahaan. Ketiga, modernisasi ke *cloud*. Keempat, kepatuhan pada UU PDP dan aturan rekam medis elektronik.

**Pemicu tambahan.** Insiden kebocoran data pasien skala kecil lewat vendor pada 2025. Temuan audit internal tentang kontrol akses yang lemah. Antrean layanan yang panjang. Biaya integrasi yang tinggi.

**Pemakaian di mata kuliah ini.** Medikara menjadi contoh kerja di setiap bab. Bagian I memakai strategi dan pemicunya untuk menyusun visi arsitektur. Bagian II memotret kondisi saat ini: kapabilitas, data pasien yang tersebar, lima SIMRS, dan integrasi *point-to-point*. Bagian III merancang kondisi target "Satu Pasien, Satu Rekam Medis". Bagian IV menyusun peta jalan 2026 sampai 2030 beserta tata kelola arsitekturnya. Tim yang memakai organisasi sendiri menjadikan Medikara sebagai pembanding, lalu menerapkan langkah yang sama pada organisasinya. Contoh artefak Medikara disediakan bertahap di folder `sources`. Semua angka dan fakta Medikara wajib sama dengan yang dipakai tiga mata kuliah lain.

## Struktur Repositori

| Folder | Isi |
| --- | --- |
| `figures` | Gambar bersama untuk modul dan slide. |
| `module` | Naskah modul: berkas utama `enterprise-architecture-digital-blueprint.tex`, `titlepage.tex`, `chapter01.tex` sampai `chapter14.tex`, `references.bib` untuk rujukan inti, dan `bib/chapterNN.bib` untuk rujukan khusus tiap bab. |
| `slides` | Slide Beamer: `preamble.tex` yang dipakai bersama, dan satu folder `sessionNN` untuk tiap pertemuan yang dibuat bertahap. |
| `sources` | Berkas pendukung tiap bab di `sources/chapterNN`: templat, lembar kerja, data kasus Medikara, dan contoh model Archi. |

Modul dikompilasi dengan XeLaTeX dari folder `module`.

```
cd module
xelatex enterprise-architecture-digital-blueprint
bibtex enterprise-architecture-digital-blueprint
xelatex enterprise-architecture-digital-blueprint
xelatex enterprise-architecture-digital-blueprint
```

Slide dikompilasi dua kali dari folder sesinya, misalnya untuk Pertemuan 1:

```
cd slides/session01
xelatex session01
xelatex session01
```

Selama bab masih berupa kerangka, BibTeX melaporkan "I found no \citation commands". Pesan ini wajar dan akan hilang setelah bab mulai mengutip rujukan.

**Symlink.** `module/fonts`, `slides/theme`, `figures/logo_universitas.png`, dan `figures/building.png` adalah *symlink* ke repo `advanced-software-engineering`. Di Windows, *symlink* ini dapat muncul sebagai berkas teks berisi jalur tujuannya. Bila itu terjadi, aset aslinya perlu disalin dari repo tersebut sebelum kompilasi.

## Rujukan Utama

Versi standar dan status regulasi di bawah ini diperiksa pada 30 Oktober 2026.

**Standar dan kerangka kerja**

- The Open Group. [*The TOGAF Standard, 10th Edition*](https://www.opengroup.org/togaf). Pembaruan Juni 2025 memuat *Technical Corrigendum 1*. Standar ini terdiri atas *Fundamental Content* dan *Series Guides*.
- The Open Group. [*ArchiMate 3.2 Specification*](https://publications.opengroup.org/standards/archimate/c226), dokumen C226, Oktober 2022. Versi yang dipakai di mata kuliah ini karena didukung Archi.
- The Open Group. [*ArchiMate 4 Specification*](https://publications.opengroup.org/standards/archimate/c260), dokumen C260, 27 April 2026. Versi terbaru: istilah lapisan diganti domain, elemen perilaku lintas lapisan digabung, dan relasi dapat diberi multiplisitas. Modul menjelaskan perbedaannya dengan versi 3.2.
- [Archi 5.10.0](https://www.archimatetool.com/download/), 3 September 2026. Alat pemodelan gratis yang mendukung ArchiMate 3.2, belum ArchiMate 4.
- Business Architecture Guild. [*BIZBOK Guide* versi 15](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/bizbok15/BIZBOKv15_introduction.pdf), April 2026. Memuat panduan *capability map*, *value stream*, portofolio aplikasi, dan model referensi industri kesehatan.
- The Open Group. [*Open Agile Architecture Standard, Version 2.0*](https://www.vanharen.net/store/open-agile-architecturetm-standard-version-2-0), April 2026.
- [ISO/IEC/IEEE 42010:2022](https://www.iso.org/standard/74393.html) *Software, systems and enterprise: Architecture description*.
- Zachman, J. A. (1987). [A framework for information systems architecture](https://doi.org/10.1147/sj.263.0276). *IBM Systems Journal*, 26(3), 276 sampai 292.

**Buku**

- Ross, J. W., Weill, P., dan Robertson, D. C. (2006). *Enterprise Architecture as Strategy: Creating a Foundation for Business Execution*. Harvard Business School Press.
- Ross, J. W., Beath, C. M., dan Mocker, M. (2019). *Designed for Digital: How to Architect Your Business for Sustained Success*. MIT Press.
- Kotusev, S. (2021). *The Practice of Enterprise Architecture: A Modern Approach to Business and IT Alignment*, edisi ke-2. SK Publishing.
- Lankhorst, M. (2017). [*Enterprise Architecture at Work: Modelling, Communication and Analysis*](https://doi.org/10.1007/978-3-662-53933-0), edisi ke-4. Springer.
- Ward, J. dan Daniel, E. (2012). *Benefits Management: How to Increase the Business Value of Your IT Projects*, edisi ke-2. Wiley.

**Artikel ilmiah**

- Tamm, T., Seddon, P. B., Shanks, G., dan Reynolds, P. (2011). [How does enterprise architecture add value to organisations?](https://doi.org/10.17705/1CAIS.02810) *Communications of the Association for Information Systems*, 28.
- Lange, M., Mendling, J., dan Recker, J. (2016). [An empirical analysis of the factors and measures of Enterprise Architecture Management success](https://doi.org/10.1057/ejis.2014.39). *European Journal of Information Systems*, 25(5), 411 sampai 431.
- Kotusev, S. (2019). [Enterprise architecture and enterprise architecture artifacts: Questioning the old concept in light of new findings](https://doi.org/10.1177/0268396218816273). *Journal of Information Technology*, 34(2), 102 sampai 128.

**Regulasi Indonesia**

- [Peraturan Presiden (Perpres) Nomor 95 Tahun 2018](https://peraturan.bpk.go.id/Details/96913/perpres-no-95-tahun-2018) tentang Sistem Pemerintahan Berbasis Elektronik. Masih berlaku. Revisinya menjadi satu Perpres tentang Pemerintah Digital masih dalam penyusunan.
- [Perpres Nomor 132 Tahun 2022](https://peraturan.bpk.go.id/Details/233483/perpres-no-132tahun-2022) tentang Arsitektur SPBE Nasional. Masih berlaku dan memuat enam domain arsitektur: proses bisnis, data dan informasi, infrastruktur, aplikasi, keamanan, dan layanan. Periode yang dimuatnya adalah 2020 sampai 2024, dan penggantinya untuk periode berikutnya belum ditemukan.
- [Perpres Nomor 82 Tahun 2023](https://peraturan.bpk.go.id/Details/273981) tentang Percepatan Transformasi Digital dan Keterpaduan Layanan Digital Nasional. Masih berlaku.
- [Perpres Nomor 83 Tahun 2025](https://peraturan.bpk.go.id/Details/329002/perpres-no-83-tahun-2025) tentang Komite Percepatan Transformasi Digital Pemerintah, ditetapkan 29 Juli 2025.
- [Peraturan Menteri PANRB (Pendayagunaan Aparatur Negara dan Reformasi Birokrasi) Nomor 8 Tahun 2026](https://pasal.id/peraturan/permen/permenpanrb-no-8-tahun-2026) tentang Evaluasi Kinerja Pemerintah Digital, ditetapkan 1 Juni 2026. Peraturan ini mencabut Permen PANRB Nomor 59 Tahun 2020 tentang pemantauan dan evaluasi SPBE.
- [Undang-Undang Nomor 27 Tahun 2022](https://peraturan.bpk.go.id/Details/229798/uu-no-27-tahun-2022) tentang Pelindungan Data Pribadi. Dibahas rinci di IT40813.
- [Peraturan Menteri Kesehatan Nomor 24 Tahun 2022](https://peraturan.bpk.go.id/Details/245544) tentang Rekam Medis. Mewajibkan rekam medis elektronik.

**Laporan industri**

- SAP LeanIX. [*SAP LeanIX EA Insights 2025*](https://www.leanix.net/en/download/sap-leanix-ea-insights-2025). Survei terhadap 360 arsitek *enterprise*. Sebanyak 92 persen menyatakan EA masih dipandang, seluruhnya atau sebagian, sebagai fungsi administratif TI.
- SAP LeanIX. [*SAP LeanIX Agentic AI Survey 2026*](https://www.leanix.net/en/download/agentic-ai-survey-2026). Sebagian besar organisasi berencana memakai agen AI, tetapi hanya sebagian kecil yang punya visibilitas atas kinerjanya.
- Betz, C. (21 Januari 2026). [*The State of Enterprise Architecture (EA), 2026*](https://www.forrester.com/report/the-state-of-enterprise-architecture-2025/RES190870). Forrester.
- Thorogood, A. dan Woerner, S. L. (18 Desember 2025). [*Enterprise IT Operating Models in the AI Era*](https://cisr.mit.edu/publication/2025_1201_EntITOperatingModels_ThorogoodWoerner). MIT CISR (*Massachusetts Institute of Technology Center for Information Systems Research*) Research Briefing XXV-12.

**Kurikulum pembanding**

- Penn State World Campus. [Master of Enterprise Architecture, Enterprise Architecture and Business Transformation](https://bulletins.psu.edu/graduate/programs/majors/enterprise-architecture-business-transformation/). Urutan intinya: fondasi EA, arsitektur bisnis strategis, pemodelan *enterprise*, arsitektur TI (aplikasi, data, dan teknologi), arsitektur keamanan dan risiko, lalu kepemimpinan EA dengan proyek *capstone* tim.
- Boston University. [MET CS 783 Enterprise Architecture](https://www.bu.edu/csmet/files/2025/01/Course-SyllabusCS783_OL_Spring2_2025.pdf), Spring 2 2025. Memakai *Enterprise Architecture as Strategy* sebagai buku utama: model operasi, *core diagram*, *IT engagement model*, dan tahap kematangan arsitektur, ditambah proyek bertahap yang dipresentasikan.
- Université de Namur. [ELOIM432 Enterprise Architecture](https://unamur.be/en/enterprise-architecture-3), Master in Business Engineering 2024 sampai 2025. Mencakup proses EA dan peran arsitek, TOGAF, pendekatan ilmiah dalam merancang EA, dan pemodelan ArchiMate. Penilaiannya berupa tugas pemodelan dan ujian lisan.

Ketiga kurikulum memakai pola yang sama: fondasi dan kerangka kerja, pemodelan, domain arsitektur, lalu proyek bertahap yang dipresentasikan. Pola itu dipakai di sini, dengan dua penyesuaian. Pertama, setiap topik dikaitkan langsung dengan tonggak *capstone* lintas mata kuliah. Kedua, setiap pertemuan dimulai dari masalah organisasi agar dapat diikuti mahasiswa tanpa latar teknis.

## Daftar Singkatan

| Singkatan | Kepanjangan |
| --- | --- |
| ADM | Architecture Development Method |
| ADR | Architecture Decision Record |
| AI | Artificial Intelligence |
| API | Application Programming Interface |
| BIZBOK | Business Architecture Body of Knowledge |
| BPJS | Badan Penyelenggara Jaminan Sosial |
| CI | Continuous Integration |
| CRUD | Create, Read, Update, Delete |
| CS | Computer Science |
| EA | Enterprise Architecture |
| ERP | Enterprise Resource Planning |
| FHIR | Fast Healthcare Interoperability Resources |
| HL7 | Health Level Seven |
| IEC | International Electrotechnical Commission |
| IEEE | Institute of Electrical and Electronics Engineers |
| ISO | International Organization for Standardization |
| MIT CISR | Massachusetts Institute of Technology Center for Information Systems Research |
| MPI | Master Patient Index |
| NPV | Net Present Value |
| PANRB | Pendayagunaan Aparatur Negara dan Reformasi Birokrasi |
| PDP | Pelindungan Data Pribadi |
| Perpres | Peraturan Presiden |
| SaaS | Software as a Service |
| SE | Software Engineering |
| SIMRS | Sistem Informasi Manajemen Rumah Sakit |
| SOP | Standard Operating Procedure |
| SPBE | Sistem Pemerintahan Berbasis Elektronik |
| TCO | Total Cost of Ownership |
| TI | Teknologi Informasi |
| TIME | Tolerate, Invest, Migrate, Eliminate |
| TOGAF | The Open Group Architecture Framework |
| UAS | Ujian Akhir Semester |
| UTS | Ujian Tengah Semester |
| UU | Undang-Undang |
