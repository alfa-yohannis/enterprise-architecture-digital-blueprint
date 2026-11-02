# Kegunaan: memeriksa arah TIME serta menghitung pasangan dan biaya integrasi Bab 7.
# Cara memakai: python periksa-portofolio.py [--aplikasi a.csv] [--antarmuka b.csv]
"""Pemeriksa portofolio aplikasi untuk Aktivitas Bab 7.

Keluaran skrip ini usulan pemeriksaan, bukan keputusan. Kewajiban regulator,
ketergantungan, dan penilaian pemilik bisnis tetap harus ditinjau manusia.
"""
import argparse
import csv
from collections import Counter
from pathlib import Path

# Ambang dipilih tim, bukan aturan universal TIME. Ubah di sini agar semua
# aplikasi dinilai dengan ambang yang sama dan perubahannya mudah ditinjau.
AMBANG_TINGGI = 4
SKOR_TERENDAH = 1
SKOR_TERTINGGI = 5

# Asumsi biaya kelas. Tiap angka perlu diganti dengan data organisasi, karena
# biaya integrasi peka terhadap tarif dan lama pengerjaan.
JAM_PER_INSIDEN = 8
JAM_PER_PERUBAHAN = 40
TARIF_PER_JAM_JUTA = 0.25
OPERASI_PER_PASANGAN_JUTA = 18

# Ekspor manual dicatat di katalog, tetapi tidak masuk hitungan pasangan
# otomatis supaya kedua angka tidak dijumlahkan seolah sejenis.
POLA_MANUAL = "Ekspor manual"

DIREKTORI_SKRIP = Path(__file__).parent
BERKAS_APLIKASI = DIREKTORI_SKRIP / "contoh-katalog-medikara.csv"
BERKAS_ANTARMUKA = DIREKTORI_SKRIP / "templat-katalog-antarmuka.csv"


def arah_time(nilai_bisnis, kualitas_teknis):
  """Mengusulkan arah TIME dari dua skor.

  Eliminate selalu ditulis bersyarat, karena skor rendah tidak menghapus
  kewajiban laporan, retensi data, atau pengguna yang masih bergantung.
  """
  for skor in (nilai_bisnis, kualitas_teknis):
    if not SKOR_TERENDAH <= skor <= SKOR_TERTINGGI:
      raise ValueError(f"Skor harus {SKOR_TERENDAH} sampai {SKOR_TERTINGGI}")
  if nilai_bisnis >= AMBANG_TINGGI:
    return "Invest" if kualitas_teknis >= AMBANG_TINGGI else "Migrate"
  if kualitas_teknis >= AMBANG_TINGGI:
    return "Tolerate"
  return "Eliminate bersyarat"


def batas_pasangan(jumlah_sistem):
  """Menghitung batas pasangan tak berarah, n(n-1)/2.

  Hasilnya batas model graf lengkap. Angka ini tidak boleh dilaporkan sebagai
  jumlah antarmuka yang sudah ada, karena hal itu harus dibuktikan katalog.
  """
  return jumlah_sistem * (jumlah_sistem - 1) // 2


def perkiraan_biaya_integrasi(insiden, perubahan, pasangan):
  """Memperkirakan biaya integrasi per tahun, dalam juta rupiah.

  Biaya berasal dari tenaga menangani insiden, tenaga mengerjakan perubahan,
  dan operasi per pasangan. Pemisahan ini menunjukkan komponen yang turun
  bila jumlah pasangan atau frekuensi perubahan berkurang.
  """
  jam_kerja = insiden * JAM_PER_INSIDEN + perubahan * JAM_PER_PERUBAHAN
  biaya_tenaga = jam_kerja * TARIF_PER_JAM_JUTA
  return biaya_tenaga + pasangan * OPERASI_PER_PASANGAN_JUTA


def baca_csv(lokasi_berkas):
  """Membaca CSV dan melewati baris komentar agar templat tetap dapat dipakai."""
  with lokasi_berkas.open(encoding="utf-8-sig", newline="") as aliran:
    baris_data = (baris for baris in aliran if not baris.startswith("#"))
    return [baris for baris in csv.DictReader(baris_data) if baris.get("id")]


def cetak_arah_aplikasi(daftar_aplikasi):
  """Mencetak arah tiap aplikasi supaya pemilik dapat membandingkan skor."""
  print("Arah TIME per aplikasi:")
  jumlah_arah = Counter()
  for aplikasi in daftar_aplikasi:
    arah = arah_time(
      float(aplikasi["nilai_bisnis"]), float(aplikasi["kualitas_teknis"])
    )
    jumlah_arah[arah] += 1
    print(f"  {aplikasi['id']} {aplikasi['nama']}: {arah}")
  print(f"Sebaran contoh ini: {dict(sorted(jumlah_arah.items()))}")


def ringkas_antarmuka(daftar_antarmuka):
  """Menghitung pasangan aktif dari katalog, terpisah dari ekspor manual."""
  otomatis = [
    baris for baris in daftar_antarmuka if baris["pola"] != POLA_MANUAL
  ]
  pasangan = {
    frozenset((baris["pengirim"], baris["penerima"])) for baris in otomatis
  }
  jumlah_manual = len(daftar_antarmuka) - len(otomatis)
  insiden = sum(int(baris["insiden_per_tahun"]) for baris in otomatis)
  perubahan = sum(int(baris["perubahan_per_tahun"]) for baris in otomatis)
  return len(pasangan), len(otomatis), jumlah_manual, insiden, perubahan


def main():
  """Mencetak usulan dan asumsi, sehingga bukti bisnis tetap dapat ditinjau."""
  parser = argparse.ArgumentParser(description=__doc__)
  parser.add_argument("--aplikasi", type=Path, default=BERKAS_APLIKASI)
  parser.add_argument("--antarmuka", type=Path, default=BERKAS_ANTARMUKA)
  parser.add_argument("--sistem", type=int, default=9)
  argumen = parser.parse_args()
  if argumen.sistem < 0:
    parser.error("Jumlah sistem tidak boleh negatif")
  try:
    cetak_arah_aplikasi(baca_csv(argumen.aplikasi))
    ringkasan = ringkas_antarmuka(baca_csv(argumen.antarmuka))
  except (KeyError, ValueError) as kesalahan:
    parser.error(str(kesalahan))
  pasangan, otomatis, manual, insiden, perubahan = ringkasan
  biaya = perkiraan_biaya_integrasi(insiden, perubahan, pasangan)
  batas = batas_pasangan(argumen.sistem)
  print(f"Batas model {argumen.sistem} sistem: {batas} pasangan tak berarah.")
  print(f"Katalog: {pasangan} pasangan aktif, {otomatis} antarmuka otomatis, "
        f"{manual} ekspor manual.")
  print(f"Insiden {insiden} dan perubahan {perubahan} per tahun.")
  print(f"Perkiraan biaya: Rp{biaya:.0f} juta per tahun, "
        f"Rp{biaya / pasangan:.0f} juta per pasangan aktif.")
  print("Arah TIME hanya usulan; kewajiban dan ketergantungan tetap diperiksa.")


if __name__ == "__main__":
  main()
