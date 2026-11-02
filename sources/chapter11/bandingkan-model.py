# Membandingkan ekspor CSV model awal dan target, lalu menandai butir yang perlu
# keputusan. Pakai: python bandingkan-model.py [model-awal.csv model-target.csv]
"""Perbandingan struktur model untuk Aktivitas Bab 11.

Skrip hanya membandingkan kode, nama, dan padanan. Makna bisnis tetap ditinjau
manusia, karena kode yang sama tidak membuktikan fungsi yang setara.
"""
import argparse
import csv
from collections import Counter
from pathlib import Path

TANDA_KOMENTAR = "#"
STATUS_TETAP = "dipertahankan"
STATUS_UBAH = "diubah"
STATUS_GANTI = "diganti"
STATUS_HAPUS = "dihapus sengaja"
STATUS_PERIKSA = "PERIKSA"
STATUS_PENERUS = "penerus"
STATUS_BARU = "baru"
URUTAN_STATUS = (
  STATUS_TETAP, STATUS_UBAH, STATUS_GANTI, STATUS_HAPUS,
  STATUS_PERIKSA, STATUS_PENERUS, STATUS_BARU,
)


def baca_model(lokasi):
  """Membaca satu ekspor model menjadi peta kode ke baris.

  Kode ganda ditolak, karena baris yang tertimpa akan menyembunyikan perubahan.
  """
  model = {}
  with lokasi.open(encoding="utf-8-sig", newline="") as berkas:
    baris_data = (baris for baris in berkas if not baris.startswith(TANDA_KOMENTAR))
    for baris in csv.DictReader(baris_data):
      kode = baris.get("id", "").strip()
      if not kode or kode in model:
        raise ValueError(f"Kode kosong atau berulang di {lokasi}: '{kode}'")
      model[kode] = baris
  return model


def golongkan_butir_awal(butir, target):
  """Menentukan status satu butir kondisi awal.

  Butir tanpa padanan dan tanpa alasan diberi status PERIKSA, karena bisa
  jadi fungsi wajib yang terlewat pada target.
  """
  kode = butir["id"].strip()
  padanan = butir.get("padanan_target", "").strip()
  alasan = butir.get("alasan_dihapus", "").strip()
  if kode in target:
    nama_sama = butir["nama"] == target[kode]["nama"]
    return STATUS_TETAP if nama_sama else STATUS_UBAH
  if padanan in target:
    return STATUS_GANTI
  if alasan:
    return STATUS_HAPUS
  return STATUS_PERIKSA


def golongkan_butir_target(kode, awal, daftar_padanan):
  """Membedakan penerus dan elemen baru, karena pekerjaannya berbeda.

  Penerus membawa migrasi data dan fungsi, sedangkan elemen baru tidak.
  Butir yang ada di kedua sisi sudah dihitung dari sisi awal.
  """
  if kode in awal:
    return None
  return STATUS_PENERUS if kode in daftar_padanan else STATUS_BARU


def bandingkan(awal, target):
  """Menghasilkan pasangan kode dan status untuk seluruh butir kedua model."""
  hasil = {}
  for kode, butir in awal.items():
    hasil[kode] = golongkan_butir_awal(butir, target)
  daftar_padanan = {
    butir.get("padanan_target", "").strip() for butir in awal.values()
  }
  for kode in target:
    status = golongkan_butir_target(kode, awal, daftar_padanan)
    if status:
      hasil[kode] = status
  return hasil


def cetak_hasil(hasil, awal, target):
  """Mencetak rincian lalu ringkasan, agar tim membaca butir PERIKSA di akhir."""
  for kode in sorted(hasil):
    sumber = awal.get(kode) or target[kode]
    print(f"{kode:8} {hasil[kode]:16} {sumber['nama']}")
  jumlah = Counter(hasil.values())
  print()
  print(f"Butir awal {len(awal)}, butir target {len(target)}.")
  for status in URUTAN_STATUS:
    print(f"  {status:16} {jumlah[status]}")
  print("Kode yang sama tidak otomatis membuktikan fungsi yang setara.")


def main():
  """Membaca argumen, lalu menjalankan perbandingan dengan pesan galat ringkas."""
  folder = Path(__file__).parent
  parser = argparse.ArgumentParser(description=__doc__)
  parser.add_argument(
    "awal", nargs="?", type=Path, default=folder / "model-awal.csv"
  )
  parser.add_argument(
    "target", nargs="?", type=Path, default=folder / "model-target.csv"
  )
  argumen = parser.parse_args()
  try:
    awal = baca_model(argumen.awal)
    target = baca_model(argumen.target)
  except (OSError, ValueError) as galat:
    parser.error(str(galat))
  cetak_hasil(bandingkan(awal, target), awal, target)


if __name__ == "__main__":
  main()
