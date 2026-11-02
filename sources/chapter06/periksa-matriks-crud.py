# Menandai konsep data yang perlu diselidiki dari matriks CRUD berformat CSV.
# Cara memakai: python periksa-matriks-crud.py medikara-matriks-crud.csv
"""Pemeriksa matriks CRUD untuk Aktivitas dan Latihan Bab 06.

Matriks CRUD memetakan konsep data (baris) ke aplikasi (kolom). Pada matriks
yang besar, pola yang penting mudah terlewat bila dibaca dengan mata. Skrip ini
menandai empat pola: konsep tanpa pemilik bisnis, konsep tanpa pembuat, konsep
yang dibuat di lebih dari satu tempat, dan konsep yang dibuat di spreadsheet.
Konsep yang tidak pernah dihapus dicatat terpisah, karena pada data kesehatan
hal itu sering justru diwajibkan aturan masa simpan. Hasilnya bahan diskusi,
bukan putusan: tiap tanda tetap harus dijelaskan oleh pemilik bisnisnya.
"""

import csv
import sys

# Baris yang diawali tanda ini adalah komentar dan tidak ikut dibaca, sehingga
# berkas CSV boleh memuat keterangan di baris pertamanya.
AWALAN_KOMENTAR = "#"

# Kolom yang bukan nama aplikasi. Kolom lain dianggap satu aplikasi.
KOLOM_KONSEP = "konsep"
KOLOM_PEMILIK = "pemilik_bisnis"
KOLOM_BUKAN_APLIKASI = (KOLOM_KONSEP, KOLOM_PEMILIK)

# Spreadsheet diperlakukan khusus karena data yang dibuat di sana berada di
# luar aplikasi yang dikelola, tanpa kontrol akses dan riwayat perubahan.
KOLOM_SPREADSHEET = "spreadsheet"

# Satu konsep idealnya dibuat di satu tempat saja. Lebih dari itu berarti ada
# beberapa versi kebenaran yang harus disatukan belakangan.
BATAS_JUMLAH_PEMBUAT = 1

# Status keluar bila argumen tidak lengkap, agar dapat dibaca skrip lain.
STATUS_SALAH_PAKAI = 2
JUMLAH_ARGUMEN = 2


def baca_matriks(jalur_berkas):
  """Membaca berkas CSV dan mengembalikan daftar baris sebagai kamus.

  Baris komentar dan baris tanpa nama konsep dilewati, sehingga templat yang
  belum terisi penuh tetap dapat diperiksa tanpa menghasilkan tanda palsu.
  """
  with open(jalur_berkas, newline="", encoding="utf-8") as berkas:
    baris_teks = [
        baris for baris in berkas if not baris.startswith(AWALAN_KOMENTAR)
    ]
  daftar_baris = list(csv.DictReader(baris_teks))
  return [
      baris for baris in daftar_baris
      if (baris.get(KOLOM_KONSEP) or "").strip()
  ]


def daftar_aplikasi(baris):
  """Mengembalikan nama kolom aplikasi, yaitu kolom selain konsep dan pemilik."""
  return [kolom for kolom in baris if kolom not in KOLOM_BUKAN_APLIKASI]


def aplikasi_dengan_huruf(baris, huruf):
  """Mengembalikan aplikasi yang selnya memuat huruf CRUD tertentu.

  Huruf dibandingkan tanpa membedakan besar kecil, agar isian "cru" dan "CRU"
  dibaca sama.
  """
  return [
      aplikasi for aplikasi in daftar_aplikasi(baris)
      if huruf in (baris.get(aplikasi) or "").upper()
  ]


def periksa_satu_konsep(baris):
  """Mengembalikan tanda untuk satu konsep, kosong bila tidak ada."""
  tanda = []
  if not (baris.get(KOLOM_PEMILIK) or "").strip():
    tanda.append("belum punya pemilik bisnis")

  pembuat = aplikasi_dengan_huruf(baris, "C")
  if not pembuat:
    tanda.append("tidak ada aplikasi yang membuatnya")
  elif len(pembuat) > BATAS_JUMLAH_PEMBUAT:
    tanda.append(f"dibuat di {len(pembuat)} tempat: {', '.join(pembuat)}")

  if KOLOM_SPREADSHEET in pembuat:
    tanda.append("dibuat di spreadsheet, di luar aplikasi yang dikelola")
  return tanda


def tanpa_penghapus(baris):
  """Menyatakan apakah tidak ada satu aplikasi pun yang menghapus konsep ini.

  Pola ini tidak otomatis salah. Rekam medis, misalnya, memang wajib disimpan
  lama, tetapi keputusan itu harus tercatat dan disengaja.
  """
  return not aplikasi_dengan_huruf(baris, "D")


def main():
  """Membaca jalur berkas dari argumen, lalu mencetak tanda untuk tiap konsep."""
  if len(sys.argv) != JUMLAH_ARGUMEN:
    print("Pemakaian: python periksa-matriks-crud.py <berkas-matriks.csv>")
    sys.exit(STATUS_SALAH_PAKAI)

  daftar_baris = baca_matriks(sys.argv[1])
  jumlah_ditandai = 0
  konsep_tanpa_penghapus = []
  for baris in daftar_baris:
    if tanpa_penghapus(baris):
      konsep_tanpa_penghapus.append(baris[KOLOM_KONSEP])
    tanda = periksa_satu_konsep(baris)
    if not tanda:
      continue
    jumlah_ditandai += 1
    print(baris[KOLOM_KONSEP])
    for satu_tanda in tanda:
      print(f"  - {satu_tanda}")

  print(f"\nDitandai: {jumlah_ditandai} dari {len(daftar_baris)} konsep.")
  print("Tanpa penghapus, cocokkan dengan aturan masa simpan:")
  print("  " + ", ".join(konsep_tanpa_penghapus))


if __name__ == "__main__":
  main()
