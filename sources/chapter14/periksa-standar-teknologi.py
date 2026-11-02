# Kegunaan: fitness function yang memeriksa teknologi proyek terhadap katalog standar.
# Cara pakai: python periksa-standar-teknologi.py [--proyek deklarasi.csv]
#   [--tanggal 2027-10-30]. Tanpa --proyek, deklarasi contoh yang diperiksa.
"""Fitness function arsitektur untuk Bab 14.

Skrip ini dijalankan di pipeline Continuous Integration. Tujuannya memindahkan
pemeriksaan yang berulang dari rapat architecture board ke mesin, sehingga board
cukup menilai pengecualian. Status keluar 1 berarti ada pelanggaran, dan pipeline
membaca angka itu untuk memblokir penggabungan perubahan.

Format berkas deklarasi proyek (CSV, baris berawalan # diabaikan):

  kategori,teknologi,nomor_dispensasi,berlaku_sampai
  basis data,PostgreSQL 16,,
  identitas pasien,Basis data pasien lokal aplikasi,DSP-2027-07,2028-04-30

Skrip hanya memakai pustaka standar Python 3.9 atau lebih baru.
"""

import argparse
import csv
import io
import sys
from datetime import date, datetime
from pathlib import Path

# Katalog dicari di folder skrip agar skrip dapat dijalankan dari folder mana pun,
# termasuk dari akar repositori proyek di dalam pipeline.
BERKAS_STANDAR_BAWAAN = Path(__file__).with_name("standar-teknologi-medikara.csv")
PENANDA_KOMENTAR = "#"
FORMAT_TANGGAL = "%Y-%m-%d"
STATUS_DIIZINKAN = ("standar", "dibolehkan")
STATUS_KELUAR_LOLOS = 0
STATUS_KELUAR_GAGAL = 1
HASIL_LOLOS = "lolos"
HASIL_DISPENSASI = "lolos dengan dispensasi"
HASIL_MELANGGAR = "MELANGGAR"
LEBAR_KOLOM_TEKNOLOGI = 44
LEBAR_KOLOM_HASIL = 24

# Deklarasi contoh proyek Layanan Kesehatan Karyawan, dipakai bila tim belum punya
# berkas sendiri. Isinya sengaja mencampur komponen yang patuh, yang memakai
# dispensasi, dan yang melanggar, agar ketiga hasil terlihat dalam satu kali jalan.
CONTOH_DEKLARASI_PROYEK = [
  {"kategori": "identitas pasien", "teknologi": "Basis data pasien lokal aplikasi",
   "nomor_dispensasi": "DSP-2027-07", "berlaku_sampai": "2028-04-30"},
  {"kategori": "identitas pengguna",
   "teknologi": "Layanan identitas terpusat (OpenID Connect)",
   "nomor_dispensasi": "", "berlaku_sampai": ""},
  {"kategori": "integrasi klinis", "teknologi": "HL7 FHIR R4",
   "nomor_dispensasi": "", "berlaku_sampai": ""},
  {"kategori": "integrasi", "teknologi": "Koneksi langsung antarbasis data",
   "nomor_dispensasi": "", "berlaku_sampai": ""},
  {"kategori": "basis data", "teknologi": "MongoDB 7",
   "nomor_dispensasi": "", "berlaku_sampai": ""},
  {"kategori": "laporan manajemen",
   "teknologi": "Spreadsheet sebagai sumber laporan",
   "nomor_dispensasi": "DSP-2027-03", "berlaku_sampai": "2027-09-30"},
]


def baca_baris_csv(jalur_berkas):
  """Membaca berkas CSV menjadi daftar kamus, sambil melewati baris komentar.

  Baris komentar ditulis untuk pembaca manusia. Bila tidak dibuang lebih dahulu,
  pembaca CSV menganggapnya sebagai baris judul dan seluruh kolom bergeser.
  """
  with open(jalur_berkas, encoding="utf-8", newline="") as berkas:
    baris_isi = [
      baris for baris in berkas
      if baris.strip() and not baris.lstrip().startswith(PENANDA_KOMENTAR)
    ]
  return list(csv.DictReader(io.StringIO("".join(baris_isi))))


def buat_kunci(kategori, teknologi):
  """Menyusun kunci pencarian yang tidak peka huruf besar dan spasi di tepi.

  Tanpa penyeragaman ini, "PostgreSQL 16" dan "postgresql 16" dianggap dua
  teknologi berbeda, dan proyek dinyatakan melanggar hanya karena salah ketik.
  """
  return (kategori.strip().casefold(), teknologi.strip().casefold())


def susun_katalog(baris_standar):
  """Mengubah baris katalog menjadi kamus dari kunci teknologi ke statusnya.

  Kamus dipakai agar setiap komponen proyek cukup dicari sekali, berapa pun
  panjang katalognya.
  """
  return {
    buat_kunci(baris["kategori"], baris["teknologi"]): baris["status"].strip()
    for baris in baris_standar
  }


def dispensasi_masih_berlaku(komponen, tanggal_periksa):
  """Memeriksa apakah komponen punya dispensasi yang belum berakhir.

  Dispensasi selalu berbatas waktu. Tanggal berakhir yang kosong dianggap tidak
  berlaku, agar tidak ada pengecualian yang diam-diam menjadi permanen.
  """
  nomor = (komponen.get("nomor_dispensasi") or "").strip()
  berlaku_sampai = (komponen.get("berlaku_sampai") or "").strip()
  if not nomor or not berlaku_sampai:
    return False
  tanggal_berakhir = datetime.strptime(berlaku_sampai, FORMAT_TANGGAL).date()
  return tanggal_periksa <= tanggal_berakhir


def nilai_komponen(komponen, katalog, tanggal_periksa):
  """Menilai satu komponen dan mengembalikan pasangan (hasil, keterangan).

  Teknologi berstatus standar atau dibolehkan langsung lolos. Teknologi
  yang dihentikan atau belum terdaftar hanya lolos bila dispensasinya
  masih berlaku, karena katalog adalah keputusan board, bukan pilihan
  tiap proyek.
  """
  kunci = buat_kunci(komponen["kategori"], komponen["teknologi"])
  status = katalog.get(kunci)
  if status in STATUS_DIIZINKAN:
    return HASIL_LOLOS, f"status {status}"
  if status is None:
    alasan = "tidak terdaftar di katalog"
  else:
    alasan = f"status {status}"
  nomor = (komponen.get("nomor_dispensasi") or "").strip()
  if dispensasi_masih_berlaku(komponen, tanggal_periksa):
    return HASIL_DISPENSASI, f"{nomor} sampai {komponen['berlaku_sampai']}"
  if nomor:
    return HASIL_MELANGGAR, f"{alasan}, {nomor} sudah berakhir"
  return HASIL_MELANGGAR, alasan


def cetak_laporan(daftar_hasil):
  """Mencetak satu baris per komponen agar mudah dibaca di log pipeline."""
  print(f"{'Teknologi':<{LEBAR_KOLOM_TEKNOLOGI}} "
        f"{'Hasil':<{LEBAR_KOLOM_HASIL}} Keterangan")
  for komponen, hasil, keterangan in daftar_hasil:
    teknologi = komponen["teknologi"][:LEBAR_KOLOM_TEKNOLOGI]
    print(f"{teknologi:<{LEBAR_KOLOM_TEKNOLOGI}} "
          f"{hasil:<{LEBAR_KOLOM_HASIL}} {keterangan}")


def baca_argumen():
  """Membaca argumen baris perintah beserta nilai bawaannya.

  Tanggal pemeriksaan dapat diatur agar hasil latihan dapat diulang persis,
  tidak bergantung pada hari saat skrip dijalankan.
  """
  pengurai = argparse.ArgumentParser(description="Fitness function standar teknologi")
  pengurai.add_argument("--standar", default=str(BERKAS_STANDAR_BAWAAN),
                        help="berkas katalog standar teknologi")
  pengurai.add_argument("--proyek", help="berkas deklarasi teknologi proyek")
  pengurai.add_argument("--tanggal", default=date.today().isoformat(),
                        help="tanggal pemeriksaan dengan format TTTT-BB-HH")
  return pengurai.parse_args()


def main():
  """Menjalankan pemeriksaan, lalu keluar dengan status yang dibaca pipeline."""
  argumen = baca_argumen()
  katalog = susun_katalog(baca_baris_csv(argumen.standar))
  if argumen.proyek:
    deklarasi = baca_baris_csv(argumen.proyek)
  else:
    deklarasi = CONTOH_DEKLARASI_PROYEK
  tanggal_periksa = datetime.strptime(argumen.tanggal, FORMAT_TANGGAL).date()
  daftar_hasil = [
    (komponen, *nilai_komponen(komponen, katalog, tanggal_periksa))
    for komponen in deklarasi
  ]
  cetak_laporan(daftar_hasil)
  jumlah_melanggar = sum(
    1 for komponen, hasil, keterangan in daftar_hasil if hasil == HASIL_MELANGGAR
  )
  if jumlah_melanggar:
    print(f"\nGagal: {jumlah_melanggar} komponen melanggar standar.")
    sys.exit(STATUS_KELUAR_GAGAL)
  print("\nLolos: seluruh komponen sesuai standar atau berdispensasi.")
  sys.exit(STATUS_KELUAR_LOLOS)


if __name__ == "__main__":
  main()
