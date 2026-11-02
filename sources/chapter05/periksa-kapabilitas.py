# Memeriksa peta kapabilitas dan menghitung urutan awal prioritas heatmap.
# Pakai: python periksa-kapabilitas.py [peta.csv]
"""Pemeriksa peta kapabilitas dua tingkat untuk Aktivitas Bab 5.

Skrip ini hanya memeriksa hal yang dapat diperiksa mesin: kode ganda, induk
yang hilang, kolom wajib kosong, skor di luar skala, dan warna merah tanpa
bukti berangka. Benar atau tidaknya skor tetap diputuskan tim lewat diskusi,
karena skrip tidak dapat menilai mutu bukti.
"""

import argparse
import csv
from pathlib import Path

# Skala kondisi latihan pada Bab 5. Nilai di luar daftar ini dianggap salah isi.
SKOR_SAH = {"1", "2", "3"}
# Tanda resmi bahwa data belum tersedia. Tidak boleh diganti skor tebakan.
BELUM_DINILAI = "belum dinilai"
# Skor tertinggi pada skala; celah kondisi dihitung dari angka ini.
SKOR_TERTINGGI = 3
# Skor merah. Bab 5 mewajibkan bukti berangka untuk skor ini.
SKOR_MERAH = "1"
# Bobot kepentingan strategis untuk urutan awal prioritas.
BOBOT_KEPENTINGAN = {"tinggi": 3, "sedang": 2, "rendah": 1}
# Kolom yang wajib terisi pada setiap baris tingkat 2.
KOLOM_WAJIB = ("nama", "definisi", "pemilik", "kepentingan", "keyakinan", "bukti")
# Kolom yang wajib terisi pada baris tingkat 1, karena kelompok tidak diberi skor.
KOLOM_WAJIB_INDUK = ("nama", "definisi")


def baca_baris(lokasi_berkas):
  """Membaca CSV dan melewati baris komentar.

  Baris komentar diawali tanda pagar agar petunjuk pemakaian tetap tersimpan
  di dalam berkas. Tanpa penyaringan ini, petunjuk ikut terbaca sebagai data.
  """
  with lokasi_berkas.open(encoding="utf-8-sig", newline="") as berkas:
    baris_data = [baris for baris in berkas if not baris.startswith("#")]
  return list(csv.DictReader(baris_data))


def ambil_nilai(baris, kolom):
  """Mengambil isi kolom tanpa spasi tepi.

  Kolom yang hilang dibaca sebagai teks kosong, sehingga berkas tim yang
  belum lengkap menghasilkan temuan, bukan kegagalan program.
  """
  return (baris.get(kolom) or "").strip()


def kumpulkan_kode(daftar_baris):
  """Mengumpulkan kode kapabilitas dan melaporkan kode ganda.

  Kode ganda membuat pemetaan Bab 6 dan Bab 7 menunjuk dua kapabilitas
  sekaligus, sehingga temuan ini selalu harus diperbaiki lebih dahulu.
  """
  kode_terkumpul = set()
  temuan = []
  for baris in daftar_baris:
    kode = ambil_nilai(baris, "id")
    if not kode:
      continue
    if kode in kode_terkumpul:
      temuan.append(f"Kode ganda: {kode}")
    kode_terkumpul.add(kode)
  if not kode_terkumpul:
    temuan.append("Belum ada kapabilitas yang diisi")
  return kode_terkumpul, temuan


def periksa_kolom_wajib(baris, daftar_kolom):
  """Mencari kolom wajib yang kosong pada satu baris.

  Definisi dan pemilik yang kosong membuat dua tim memakai arti berbeda untuk
  nama yang sama, sehingga kekosongan ini dilaporkan satu per satu.
  """
  kode = ambil_nilai(baris, "id")
  return [
    f"{kode}: kolom {kolom} kosong"
    for kolom in daftar_kolom
    if not ambil_nilai(baris, kolom)
  ]


def periksa_penilaian(baris):
  """Memeriksa skor, kepentingan, dan bukti pada baris tingkat 2.

  Skor merah wajib berbukti angka agar warna tidak menjadi pendapat semata.
  Status belum dinilai diterima, karena data yang tidak ada tidak boleh
  berubah menjadi warna apa pun.
  """
  temuan = []
  kode = ambil_nilai(baris, "id")
  skor = ambil_nilai(baris, "skor_kondisi")
  if skor != BELUM_DINILAI and skor not in SKOR_SAH:
    temuan.append(f"{kode}: skor harus 1, 2, 3, atau '{BELUM_DINILAI}'")
  kepentingan = ambil_nilai(baris, "kepentingan")
  if kepentingan and kepentingan not in BOBOT_KEPENTINGAN:
    temuan.append(f"{kode}: kepentingan harus tinggi, sedang, atau rendah")
  bukti = ambil_nilai(baris, "bukti")
  ada_angka = any(karakter.isdigit() for karakter in bukti)
  if skor == SKOR_MERAH and not ada_angka:
    temuan.append(f"{kode}: skor merah tanpa bukti berangka")
  return temuan


def periksa_baris(baris, kode_terkumpul):
  """Memeriksa satu baris dan mengembalikan daftar temuannya.

  Baris tanpa induk adalah kelompok tingkat 1 dan tidak diberi skor, sehingga
  pemeriksaannya lebih ringan daripada baris tingkat 2.
  """
  kode = ambil_nilai(baris, "id")
  induk = ambil_nilai(baris, "induk")
  if not induk:
    return periksa_kolom_wajib(baris, KOLOM_WAJIB_INDUK)
  temuan = periksa_kolom_wajib(baris, KOLOM_WAJIB)
  if induk not in kode_terkumpul:
    temuan.append(f"{kode}: induk {induk} tidak ditemukan")
  temuan.extend(periksa_penilaian(baris))
  return temuan


def nilai_prioritas(baris):
  """Menghitung nilai prioritas awal: celah kondisi kali bobot kepentingan.

  Rumus ini sengaja sederhana. Nilai yang sama pada beberapa kapabilitas
  justru menjadi tanda bahwa tim harus menimbang risiko dan ketergantungan.
  """
  skor = ambil_nilai(baris, "skor_kondisi")
  kepentingan = ambil_nilai(baris, "kepentingan")
  if skor not in SKOR_SAH or kepentingan not in BOBOT_KEPENTINGAN:
    return None
  celah_kondisi = SKOR_TERTINGGI - int(skor)
  return celah_kondisi * BOBOT_KEPENTINGAN[kepentingan]


def kunci_urutan(butir):
  """Mengurutkan nilai dari besar ke kecil, lalu menurut kode.

  Kode dipakai sebagai penentu kedua agar hasil selalu sama setiap kali skrip
  dijalankan, walaupun beberapa kapabilitas bernilai sama.
  """
  nilai, kode, _nama = butir
  return (-nilai, kode)


def cetak_prioritas(daftar_baris):
  """Mencetak urutan awal prioritas untuk kapabilitas yang sudah dinilai.

  Kapabilitas bernilai nol tidak dicetak, karena kondisinya sudah di skor
  tertinggi dan tidak punya celah yang perlu dibahas.
  """
  peringkat = []
  for baris in daftar_baris:
    nilai = nilai_prioritas(baris)
    if ambil_nilai(baris, "induk") and nilai:
      peringkat.append((nilai, ambil_nilai(baris, "id"), ambil_nilai(baris, "nama")))
  peringkat.sort(key=kunci_urutan)
  print("Urutan awal prioritas (celah kondisi x bobot kepentingan):")
  for nilai, kode, nama in peringkat:
    print(f"  {nilai:>2}  {kode:<8} {nama}")


def main():
  """Menjalankan pemeriksaan agar hasilnya dapat dibandingkan dengan tinjauan tim."""
  pengurai = argparse.ArgumentParser(description=__doc__)
  bawaan = Path(__file__).with_name("medikara-capability-map.csv")
  pengurai.add_argument("berkas", nargs="?", type=Path, default=bawaan)
  argumen = pengurai.parse_args()
  daftar_baris = baca_baris(argumen.berkas)
  kode_terkumpul, temuan = kumpulkan_kode(daftar_baris)
  for baris in daftar_baris:
    if ambil_nilai(baris, "id"):
      temuan.extend(periksa_baris(baris, kode_terkumpul))
  for butir_temuan in temuan:
    print(butir_temuan)
  print(f"Temuan struktur: {len(temuan)}. Lolos struktur belum berarti skor benar.")
  cetak_prioritas(daftar_baris)
  return 1 if temuan else 0


if __name__ == "__main__":
  raise SystemExit(main())
