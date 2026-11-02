# Memeriksa keterlacakan rantai motivasi. Pakai: python periksa-keterlacakan.py [csv]
"""Pemeriksa keterlacakan rantai motivasi untuk Bab 3.

Setiap elemen rantai motivasi wajib menunjuk induknya, sehingga setiap
requirement dapat ditelusuri ke atas sampai driver. Skrip ini menemukan elemen
yang tidak berinduk, induk yang jenisnya salah, outcome yang belum dapat
diukur, dan goal yang belum punya outcome. Skrip keluar dengan status 1 bila ada
temuan, sehingga dapat dipasang sebagai pemeriksaan otomatis saat dokumen visi
arsitektur ditinjau. Hanya pustaka standar Python 3 yang dipakai.
"""

import csv
import sys
from pathlib import Path

BERKAS_BAWAAN = Path(__file__).with_name("templat-rantai-motivasi.csv")

# Pemisah bila satu elemen punya lebih dari satu induk, misalnya "O1;PA1".
PEMISAH_INDUK = ";"

# Jenis induk yang sah untuk tiap jenis elemen. Aturan ini mengikuti arah
# rantai: driver, assessment, goal, outcome, lalu prinsip dan requirement.
# Driver tidak berinduk karena driver adalah ujung atas rantai.
INDUK_YANG_SAH = {
  "driver": set(),
  "assessment": {"driver"},
  "goal": {"assessment"},
  "outcome": {"goal"},
  "prinsip": {"goal"},
  "requirement": {"outcome", "prinsip"},
}

# Kolom yang wajib terisi agar sebuah outcome dapat diukur dan ditagih.
KOLOM_UKURAN_OUTCOME = (
  "ukuran", "baseline", "target", "batas_waktu", "pemilik",
)

# Penanda baris komentar pada CSV. Baris ini berisi petunjuk bagi manusia, jadi
# harus dilewati agar tidak terbaca sebagai nama kolom.
PENANDA_KOMENTAR = "#"

# Batas langkah penelusuran ke atas. Rantai yang wajar tidak lebih dari enam
# tingkat, jadi angka ini hanya mencegah putaran tanpa akhir bila ada induk
# yang saling menunjuk.
LANGKAH_PENELUSURAN_MAKSIMUM = 10

STATUS_LOLOS = 0
STATUS_ADA_TEMUAN = 1


def baca_elemen(jalur_berkas):
  """Membaca berkas CSV menjadi kamus id elemen ke baris datanya.

  Spasi di awal dan akhir sel dibuang, sehingga sel yang hanya berisi spasi
  dianggap kosong dan ikut terdeteksi sebagai data yang belum diisi. Baris
  komentar dibuang lebih dahulu, karena baris pertama CSV berisi petunjuk pakai.
  """
  with open(jalur_berkas, newline="", encoding="utf-8") as berkas:
    baris_data = (baris for baris in berkas
                  if not baris.startswith(PENANDA_KOMENTAR))
    pembaca = csv.DictReader(baris_data)
    elemen_per_id = {}
    for baris in pembaca:
      baris_bersih = {kunci: (nilai or "").strip() for kunci, nilai in baris.items()}
      elemen_per_id[baris_bersih["id"]] = baris_bersih
  return elemen_per_id


def daftar_induk(elemen):
  """Mengembalikan daftar id induk sebuah elemen, kosong bila tidak berinduk."""
  return [bagian.strip() for bagian in elemen["induk"].split(PEMISAH_INDUK)
          if bagian.strip()]


def periksa_induk(elemen_per_id):
  """Memeriksa bahwa tiap elemen berinduk dan jenis induknya sah.

  Elemen tanpa induk berarti pekerjaan yang tidak didorong strategi, sedangkan
  induk berjenis salah berarti rantainya melompati satu tingkat penalaran.
  """
  temuan = []
  for id_elemen, elemen in elemen_per_id.items():
    jenis = elemen["jenis"]
    if jenis not in INDUK_YANG_SAH:
      temuan.append(f"{id_elemen}: jenis '{jenis}' tidak dikenal.")
      continue
    induk = daftar_induk(elemen)
    if INDUK_YANG_SAH[jenis] and not induk:
      temuan.append(f"{id_elemen}: {jenis} tanpa induk, tidak dapat ditelusuri"
                    " ke strategi.")
    for id_induk in induk:
      if id_induk not in elemen_per_id:
        temuan.append(f"{id_elemen}: induk '{id_induk}' tidak ada di berkas.")
      elif elemen_per_id[id_induk]["jenis"] not in INDUK_YANG_SAH[jenis]:
        temuan.append(f"{id_elemen}: {jenis} tidak boleh berinduk "
                      f"{elemen_per_id[id_induk]['jenis']} ({id_induk}).")
  return temuan


def periksa_ukuran_outcome(elemen_per_id):
  """Memeriksa bahwa tiap outcome punya ukuran, baseline, target, waktu, pemilik.

  Outcome yang kehilangan salah satunya tidak pernah dapat dinyatakan tercapai
  atau gagal, sehingga tidak ada yang dapat dimintai pertanggungjawaban.
  """
  temuan = []
  for id_elemen, elemen in elemen_per_id.items():
    if elemen["jenis"] != "outcome":
      continue
    kosong = [kolom for kolom in KOLOM_UKURAN_OUTCOME if not elemen.get(kolom)]
    if kosong:
      temuan.append(f"{id_elemen}: outcome belum lengkap, kolom kosong: "
                    f"{', '.join(kosong)}.")
  return temuan


def periksa_goal_tanpa_outcome(elemen_per_id):
  """Menemukan goal yang belum diwujudkan oleh satu outcome pun.

  Goal seperti itu hanya berupa niat: tidak ada hasil terukur yang menandai
  bahwa goal tersebut sudah tercapai.
  """
  goal_berwujud = set()
  for elemen in elemen_per_id.values():
    if elemen["jenis"] == "outcome":
      goal_berwujud.update(daftar_induk(elemen))
  return [f"{id_elemen}: goal belum punya outcome."
          for id_elemen, elemen in elemen_per_id.items()
          if elemen["jenis"] == "goal" and id_elemen not in goal_berwujud]


def telusuri_ke_driver(id_awal, elemen_per_id):
  """Menelusuri satu elemen ke atas lewat induk pertamanya sampai driver.

  Hanya induk pertama yang diikuti agar jejaknya tetap satu baris. Induk
  lainnya sudah diperiksa oleh periksa_induk.
  """
  jejak = [id_awal]
  id_sekarang = id_awal
  for _ in range(LANGKAH_PENELUSURAN_MAKSIMUM):
    induk = daftar_induk(elemen_per_id[id_sekarang])
    if not induk or induk[0] not in elemen_per_id:
      break
    id_sekarang = induk[0]
    jejak.append(id_sekarang)
  return jejak


def cetak_jejak_requirement(elemen_per_id):
  """Mencetak jejak tiap requirement, agar pembaca melihat alasan bisnisnya."""
  print("Jejak requirement sampai driver:")
  for id_elemen, elemen in elemen_per_id.items():
    if elemen["jenis"] != "requirement":
      continue
    jejak = telusuri_ke_driver(id_elemen, elemen_per_id)
    if len(jejak) == 1:
      print(f"  {id_elemen} -> (tidak berinduk)")
    else:
      print("  " + " -> ".join(jejak))


def main():
  """Menjalankan seluruh pemeriksaan dan mengembalikan status keluar."""
  jalur_berkas = Path(sys.argv[1]) if len(sys.argv) > 1 else BERKAS_BAWAAN
  elemen_per_id = baca_elemen(jalur_berkas)
  print(f"Berkas: {jalur_berkas.name} ({len(elemen_per_id)} elemen)\n")
  cetak_jejak_requirement(elemen_per_id)

  temuan = (periksa_induk(elemen_per_id)
            + periksa_ukuran_outcome(elemen_per_id)
            + periksa_goal_tanpa_outcome(elemen_per_id))
  if not temuan:
    print("\nLolos: seluruh elemen dapat ditelusuri.")
    return STATUS_LOLOS
  print("\nTemuan:")
  for satu_temuan in temuan:
    print(f"  {satu_temuan}")
  print(f"\nGagal: {len(temuan)} temuan.")
  return STATUS_ADA_TEMUAN


if __name__ == "__main__":
  sys.exit(main())
