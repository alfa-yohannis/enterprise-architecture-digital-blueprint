# Kegunaan: menghitung NPV, payback period, sensitivitas, dan indeks portofolio Bab 13.
# Cara memakai, dari folder sources/chapter13:
#   python analisis-business-case.py arus-kas data-biaya-manfaat-mpi.csv
#   python analisis-business-case.py portofolio templat-matriks-prioritas-portofolio.csv
"""Analisis business case sederhana untuk mata kuliah IT40513.

Skrip ini hanya memakai pustaka standar Python, sehingga dapat dijalankan
tanpa memasang paket tambahan. Angka contoh berasal dari kasus fiktif Medikara
Health. Arus kas dinyatakan dalam juta rupiah, biaya portofolio dalam miliar
rupiah. Tim mengganti isi berkas CSV dengan angka organisasinya sendiri, lalu
menjalankan ulang skrip ini tanpa mengubah kodenya.
"""

import csv
import sys

# Tingkat diskonto tahunan. Angka 10 persen adalah asumsi kasus Medikara, bukan
# angka resmi. Tim menggantinya dengan biaya modal yang dipakai bagian keuangan.
TINGKAT_DISKONTO = 0.10

# Kenaikan biaya migrasi yang diuji pada analisis sensitivitas.
KENAIKAN_BIAYA_MIGRASI = 0.30

# Lama penundaan manfaat yang diuji, dalam tahun.
TAHUN_PENUNDAAN_MANFAAT = 1

# Pembengkakan ekstrem yang diuji. Satu dari enam proyek TI dalam sampel
# Flyvbjerg dan Budzier (2011) membengkak rata-rata 200 persen.
PEMBENGKAKAN_EKSTREM = 2.00

# Nama komponen biaya yang dikenai skenario. Harus sama persis dengan isi
# kolom komponen di CSV arus kas, karena dipakai sebagai kunci pencarian.
KOMPONEN_MIGRASI = "Migrasi dan pembersihan data"
KOMPONEN_IMPLEMENTASI = "Implementasi dan integrasi 5 SIMRS"

# Kriteria nilai dan risiko pada CSV portofolio. Nama kolomnya harus sama.
KRITERIA_NILAI = ["strategis", "finansial", "kepatuhan", "fondasi"]
KRITERIA_RISIKO = ["ukuran", "teknologi", "kapasitas", "dampak_gagal"]

# Batas kuadran pada matriks nilai dan risiko, di tengah skala 1 sampai 5.
AMBANG_KUADRAN = 3.0

# Kode baris CSV portofolio yang berisi bobot, bukan inisiatif.
KODE_BARIS_BOBOT = "bobot"

# Baris CSV yang diawali tanda ini dianggap petunjuk dan dilewati.
PENANDA_KOMENTAR = "#"

# Jumlah argumen baris perintah yang diharapkan, termasuk nama skrip.
JUMLAH_ARGUMEN = 3


def baca_baris_csv(nama_berkas):
  """Membaca CSV menjadi daftar kamus, sesudah melewati baris petunjuk.

  Baris petunjuk dipakai sebagai keterangan di dalam templat. Bila tidak
  dilewati, baris itu terbaca sebagai judul kolom dan seluruh isi bergeser.
  """
  with open(nama_berkas, encoding="utf-8", newline="") as berkas:
    baris_isi = [
        baris for baris in berkas if not baris.startswith(PENANDA_KOMENTAR)
    ]
  return list(csv.DictReader(baris_isi))


def baca_arus_kas(nama_berkas):
  """Memisahkan baris biaya dan baris manfaat dari CSV arus kas.

  Pemisahan dibutuhkan karena skenario sensitivitas mengubah biaya dan
  manfaat dengan cara yang berbeda. Mengembalikan daftar tahun, kamus biaya
  per komponen, dan kamus manfaat per komponen.
  """
  daftar_baris = baca_baris_csv(nama_berkas)
  daftar_tahun = [kolom for kolom in daftar_baris[0] if kolom.isdigit()]
  biaya = {}
  manfaat = {}
  for baris in daftar_baris:
    nilai = [float(baris[tahun]) for tahun in daftar_tahun]
    if baris["jenis"] == "biaya":
      biaya[baris["komponen"]] = nilai
    else:
      manfaat[baris["komponen"]] = nilai
  return daftar_tahun, biaya, manfaat


def jumlahkan_per_tahun(kamus_komponen, jumlah_tahun):
  """Menjumlahkan seluruh komponen menjadi satu angka untuk tiap tahun."""
  total = [0.0] * jumlah_tahun
  for nilai in kamus_komponen.values():
    for urutan in range(jumlah_tahun):
      total[urutan] += nilai[urutan]
  return total


def hitung_npv(arus_bersih, tingkat_diskonto):
  """Menghitung NPV dengan tahun pertama sebagai tahun ke-0.

  Tahun ke-0 tidak didiskonto karena uangnya keluar sekarang. Arus tahun
  berikutnya dibagi (1 + tingkat) pangkat urutannya, sehingga manfaat yang
  datang belakangan bernilai lebih kecil.
  """
  return sum(
      arus / (1 + tingkat_diskonto) ** urutan
      for urutan, arus in enumerate(arus_bersih)
  )


def hitung_payback(arus_bersih):
  """Menghitung payback period dalam tahun, atau None bila tidak tercapai.

  Pecahan tahun dihitung dengan anggapan arus kas masuk merata sepanjang
  tahun, sehingga hasilnya dapat berupa 2,29 tahun, bukan hanya 2 atau 3.
  """
  kumulatif = 0.0
  for urutan, arus in enumerate(arus_bersih):
    kumulatif_sebelumnya = kumulatif
    kumulatif += arus
    if kumulatif >= 0:
      if urutan == 0:
        return 0.0
      return (urutan - 1) + (-kumulatif_sebelumnya / arus)
  return None


def ubah_komponen(biaya, nama_komponen, faktor):
  """Mengembalikan salinan biaya dengan satu komponen dikalikan faktor.

  Salinan dibuat agar perubahan pada satu skenario tidak ikut mengubah
  skenario lain yang memakai kamus biaya yang sama.
  """
  biaya_baru = dict(biaya)
  biaya_baru[nama_komponen] = [nilai * faktor for nilai in biaya[nama_komponen]]
  return biaya_baru


def tunda_manfaat(manfaat, jumlah_tahun_tunda):
  """Menggeser seluruh manfaat ke belakang sebanyak jumlah tahun tunda.

  Manfaat yang terdorong melewati akhir horizon hilang dari perhitungan,
  sedangkan biayanya tetap. Itu sebabnya penundaan sering lebih merusak
  daripada kenaikan biaya.
  """
  manfaat_baru = {}
  for komponen, nilai in manfaat.items():
    awal = [0.0] * jumlah_tahun_tunda
    manfaat_baru[komponen] = (awal + nilai)[: len(nilai)]
  return manfaat_baru


def susun_skenario(biaya, manfaat):
  """Menyusun pasangan biaya dan manfaat untuk tiap skenario sensitivitas."""
  faktor_migrasi = 1 + KENAIKAN_BIAYA_MIGRASI
  faktor_ekstrem = 1 + PEMBENGKAKAN_EKSTREM
  biaya_migrasi_naik = ubah_komponen(biaya, KOMPONEN_MIGRASI, faktor_migrasi)
  manfaat_tertunda = tunda_manfaat(manfaat, TAHUN_PENUNDAAN_MANFAAT)
  biaya_ekstrem = ubah_komponen(biaya, KOMPONEN_MIGRASI, faktor_ekstrem)
  biaya_ekstrem = ubah_komponen(
      biaya_ekstrem, KOMPONEN_IMPLEMENTASI, faktor_ekstrem
  )
  return [
      ("Dasar", biaya, manfaat),
      ("Biaya migrasi naik 30 persen", biaya_migrasi_naik, manfaat),
      ("Manfaat tertunda satu tahun", biaya, manfaat_tertunda),
      ("Keduanya sekaligus", biaya_migrasi_naik, manfaat_tertunda),
      ("Implementasi dan migrasi naik 200 persen", biaya_ekstrem, manfaat),
  ]


def format_angka(nilai, jumlah_desimal=1):
  """Menulis angka dengan pemisah ribuan titik dan desimal koma.

  Format ini dipakai agar keluaran skrip dapat disalin langsung ke business
  case berbahasa Indonesia tanpa diubah manual.
  """
  teks = f"{nilai:,.{jumlah_desimal}f}"
  return teks.replace(",", "_").replace(".", ",").replace("_", ".")


def hitung_arus_bersih(biaya, manfaat, jumlah_tahun):
  """Mengurangkan total biaya dari total manfaat untuk tiap tahun."""
  total_biaya = jumlahkan_per_tahun(biaya, jumlah_tahun)
  total_manfaat = jumlahkan_per_tahun(manfaat, jumlah_tahun)
  return [
      masuk - keluar for masuk, keluar in zip(total_manfaat, total_biaya)
  ]


def laporkan_arus_kas(nama_berkas):
  """Mencetak tabel arus kas skenario dasar, lalu ringkasan tiap skenario.

  Tabel dasar dicetak lengkap agar tiap angka NPV dapat diperiksa ulang
  dengan kalkulator. Skenario lain cukup diringkas menjadi NPV dan payback.
  """
  daftar_tahun, biaya, manfaat = baca_arus_kas(nama_berkas)
  jumlah_tahun = len(daftar_tahun)
  total_biaya = jumlahkan_per_tahun(biaya, jumlah_tahun)
  total_manfaat = jumlahkan_per_tahun(manfaat, jumlah_tahun)
  arus_bersih = hitung_arus_bersih(biaya, manfaat, jumlah_tahun)
  print(f"Tingkat diskonto: {format_angka(TINGKAT_DISKONTO * 100, 0)} persen")
  print(f"{'Tahun':<6}{'Biaya':>10}{'Manfaat':>10}{'Bersih':>10}"
        f"{'Kumulatif':>11}{'Faktor':>8}{'Nilai kini':>12}")
  kumulatif = 0.0
  for urutan, tahun in enumerate(daftar_tahun):
    kumulatif += arus_bersih[urutan]
    faktor = 1 / (1 + TINGKAT_DISKONTO) ** urutan
    print(f"{tahun:<6}{format_angka(total_biaya[urutan], 0):>10}"
          f"{format_angka(total_manfaat[urutan], 0):>10}"
          f"{format_angka(arus_bersih[urutan], 0):>10}"
          f"{format_angka(kumulatif, 0):>11}"
          f"{format_angka(faktor, 3):>8}"
          f"{format_angka(arus_bersih[urutan] * faktor):>12}")
  print(f"TCO {jumlah_tahun} tahun: {format_angka(sum(total_biaya), 0)}")
  print()
  print(f"{'Skenario':<42}{'NPV':>10}{'Payback':>16}")
  for nama, biaya_skenario, manfaat_skenario in susun_skenario(biaya, manfaat):
    arus = hitung_arus_bersih(biaya_skenario, manfaat_skenario, jumlah_tahun)
    payback = hitung_payback(arus)
    teks_payback = "tidak tercapai"
    if payback is not None:
      teks_payback = f"{format_angka(payback, 2)} tahun"
    npv = hitung_npv(arus, TINGKAT_DISKONTO)
    print(f"{nama:<42}{format_angka(npv):>10}{teks_payback:>16}")


def hitung_indeks(baris, daftar_kriteria, bobot):
  """Menghitung rata-rata berbobot skor 1 sampai 5 pada beberapa kriteria.

  Pembaginya jumlah bobot, sehingga hasilnya tetap berskala 1 sampai 5
  walaupun bobot tim tidak berjumlah tepat 100.
  """
  total_bobot = sum(bobot[kriteria] for kriteria in daftar_kriteria)
  total_skor = sum(
      float(baris[kriteria]) * bobot[kriteria] for kriteria in daftar_kriteria
  )
  return total_skor / total_bobot


def tentukan_kuadran(indeks_nilai, indeks_risiko):
  """Menerjemahkan posisi pada matriks nilai dan risiko menjadi saran awal.

  Saran ini titik awal diskusi, bukan keputusan. Keputusan akhir tetap
  menimbang dependensi, pagu anggaran, dan kapasitas organisasi.
  """
  if indeks_nilai >= AMBANG_KUADRAN and indeks_risiko < AMBANG_KUADRAN:
    return "kerjakan lebih dahulu"
  if indeks_nilai >= AMBANG_KUADRAN:
    return "pecah dan amankan"
  if indeks_risiko < AMBANG_KUADRAN:
    return "kerjakan bila ada kapasitas"
  return "tunda atau kaji ulang"


def laporkan_portofolio(nama_berkas):
  """Mencetak indeks nilai, indeks risiko, dan biaya kumulatif tiap inisiatif.

  Inisiatif diurutkan menurut indeks nilai. Biaya kumulatif ikut dicetak
  untuk memperlihatkan inisiatif mana yang tidak lagi muat dalam pagu bila
  urutan itu diikuti apa adanya.
  """
  daftar_baris = baca_baris_csv(nama_berkas)
  baris_bobot = [
      baris for baris in daftar_baris if baris["kode"] == KODE_BARIS_BOBOT
  ][0]
  bobot = {
      kriteria: float(baris_bobot[kriteria])
      for kriteria in KRITERIA_NILAI + KRITERIA_RISIKO
  }
  hasil = []
  for baris in daftar_baris:
    if baris["kode"] == KODE_BARIS_BOBOT:
      continue
    indeks_nilai = hitung_indeks(baris, KRITERIA_NILAI, bobot)
    indeks_risiko = hitung_indeks(baris, KRITERIA_RISIKO, bobot)
    biaya = float(baris["biaya_5_tahun_miliar"])
    hasil.append((indeks_nilai, indeks_risiko, biaya, baris))
  hasil.sort(key=lambda isi: isi[0], reverse=True)
  print(f"{'Kode':<5}{'Inisiatif':<40}{'Nilai':>6}{'Risiko':>7}"
        f"{'Biaya':>7}{'Kumulatif':>10}  Saran awal")
  kumulatif = 0.0
  for indeks_nilai, indeks_risiko, biaya, baris in hasil:
    kumulatif += biaya
    saran = tentukan_kuadran(indeks_nilai, indeks_risiko)
    print(f"{baris['kode']:<5}{baris['inisiatif']:<40}"
          f"{format_angka(indeks_nilai, 2):>6}"
          f"{format_angka(indeks_risiko, 2):>7}"
          f"{format_angka(biaya):>7}{format_angka(kumulatif):>10}  {saran}")


def main():
  """Memilih jenis analisis dari argumen baris perintah."""
  if len(sys.argv) != JUMLAH_ARGUMEN or sys.argv[1] not in (
      "arus-kas", "portofolio"):
    print("Pemakaian: python analisis-business-case.py "
          "arus-kas|portofolio <berkas.csv>")
    sys.exit(1)
  if sys.argv[1] == "arus-kas":
    laporkan_arus_kas(sys.argv[2])
  else:
    laporkan_portofolio(sys.argv[2])


if __name__ == "__main__":
  main()
