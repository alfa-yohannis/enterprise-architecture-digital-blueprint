# Memeriksa daftar paket kerja: mencetak matriks, mencari lingkaran, menyusun lapisan.
# Pakai: python periksa-dependensi.py [contoh-paket-kerja-medikara.csv]
"""Pemeriksaan dependensi paket kerja untuk Aktivitas Bab 11.

Skrip hanya membaca kolom id dan prasyarat. Hasilnya bahan diskusi, bukan jadwal:
durasi, kapasitas, dan tanggal baru dihitung pada Bab 12.
"""
import argparse
import csv
from pathlib import Path

BERKAS_BAWAAN = "contoh-paket-kerja-medikara.csv"
PEMISAH_PRASYARAT = ";"
TANDA_KOMENTAR = "#"
TANDA_ADA = "x"
TANDA_KOSONG = "."


def baca_prasyarat(lokasi):
  """Membaca peta paket ke himpunan prasyaratnya.

  Prasyarat yang tidak ada di daftar ditolak, karena salah ketik kode akan
  membuat satu paket tampak bebas dependensi.
  """
  peta = {}
  with lokasi.open(encoding="utf-8-sig", newline="") as berkas:
    baris_data = (baris for baris in berkas if not baris.startswith(TANDA_KOMENTAR))
    for baris in csv.DictReader(baris_data):
      daftar = baris["prasyarat"].split(PEMISAH_PRASYARAT)
      peta[baris["id"].strip()] = {kode.strip() for kode in daftar if kode.strip()}
  tidak_dikenal = set().union(*peta.values()) - set(peta)
  if tidak_dikenal:
    raise ValueError(f"Prasyarat tidak dikenal: {sorted(tidak_dikenal)}")
  return peta


def susun_lapisan(peta):
  """Menyusun paket menjadi lapisan; sisanya adalah anggota lingkaran.

  Satu lapisan berisi paket yang seluruh prasyaratnya sudah selesai. Bila
  tidak ada paket yang siap, batas paket atau asumsinya perlu ditinjau.
  """
  selesai = set()
  sisa = dict(peta)
  lapisan = []
  while sisa:
    siap = sorted(kode for kode, butuh in sisa.items() if butuh <= selesai)
    if not siap:
      return lapisan, sorted(sisa)
    lapisan.append(siap)
    selesai.update(siap)
    for kode in siap:
      del sisa[kode]
  return lapisan, []


def cetak_matriks(peta):
  """Mencetak matriks dependensi: baris membutuhkan kolom, plus jumlah tiap baris."""
  daftar_kode = sorted(peta)
  print("Baris membutuhkan kolom")
  print("    " + " ".join(f"{kode:>2}" for kode in daftar_kode) + "  Jumlah")
  for kode in daftar_kode:
    sel = [TANDA_ADA if lain in peta[kode] else TANDA_KOSONG for lain in daftar_kode]
    isi = " ".join(f"{tanda:>2}" for tanda in sel)
    print(f"{kode:<4}{isi}  {len(peta[kode]):>6}")


def main():
  """Membaca argumen, lalu mencetak matriks, jumlah dependensi, dan lapisan."""
  folder = Path(__file__).parent
  parser = argparse.ArgumentParser(description=__doc__)
  parser.add_argument(
    "daftar", nargs="?", type=Path, default=folder / BERKAS_BAWAAN
  )
  argumen = parser.parse_args()
  try:
    peta = baca_prasyarat(argumen.daftar)
  except (OSError, ValueError, KeyError) as galat:
    parser.error(str(galat))
  cetak_matriks(peta)
  print(f"Jumlah dependensi: {sum(len(butuh) for butuh in peta.values())}")
  lapisan, lingkaran = susun_lapisan(peta)
  for nomor, isi in enumerate(lapisan, start=1):
    print(f"Lapisan {nomor}: {', '.join(isi)}")
  if lingkaran:
    print(f"Lingkaran atau terhalang lingkaran: {', '.join(lingkaran)}")
  else:
    print("Tidak ada lingkaran.")


if __name__ == "__main__":
  main()
