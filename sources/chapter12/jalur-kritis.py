# Menghitung jalur kritis dan beban proyek besar per tahun dari daftar paket kerja.
# Cara pakai: python jalur-kritis.py paket-kerja-medikara.csv
"""Analisis jalur kritis sederhana untuk peta jalan arsitektur.

Skrip membaca daftar paket kerja beserta durasi dan dependensinya, lalu menghitung
kapan tiap paket paling awal dapat dimulai, kapan paling lambat boleh dimulai tanpa
menggeser tanggal selesai, dan berapa kelonggarannya. Paket berkelonggaran nol
membentuk jalur kritis: keterlambatan di sana langsung menggeser target.

Skrip juga menghitung jumlah proyek besar yang berjalan pada tiap tahun kalender,
karena kapasitas tim TI Medikara dinyatakan per tahun, bukan per bulan.
"""

import csv
import sys

# Baris data yang diawali tanda ini dianggap komentar dan dilewati.
PENANDA_KOMENTAR = "#"
# Beberapa pendahulu ditulis dalam satu sel, dipisah tanda ini.
PEMISAH_DEPENDENSI = ";"
# Hanya paket berukuran ini yang menghabiskan kapasitas proyek besar.
UKURAN_BESAR = "besar"
# Bulan nomor 0 pada data adalah Juli 2026.
TAHUN_MULAI = 2026
BULAN_MULAI = 7
BULAN_PER_TAHUN = 12
# Bulan nomor 54 adalah Januari 2031, jadi target harus selesai sebelumnya.
BATAS_AKHIR_BULAN = 54
KAPASITAS_PROYEK_BESAR_PER_TAHUN = 2
NAMA_BULAN = (
    "Jan", "Feb", "Mar", "Apr", "Mei", "Jun",
    "Jul", "Agu", "Sep", "Okt", "Nov", "Des",
)


def baca_paket_kerja(jalur_berkas):
  """Membaca berkas CSV paket kerja menjadi kamus berkunci kode paket.

  Baris komentar dilewati, sehingga berkas data boleh membawa penjelasan di
  baris pertama tanpa merusak pembacaan kolom.
  """
  with open(jalur_berkas, encoding="utf-8", newline="") as berkas:
    baris_data = [
        baris for baris in berkas if not baris.startswith(PENANDA_KOMENTAR)
    ]
  daftar_paket = {}
  for rekaman in csv.DictReader(baris_data):
    teks_dependensi = rekaman["bergantung_pada"].strip()
    pendahulu = teks_dependensi.split(PEMISAH_DEPENDENSI) if teks_dependensi else []
    daftar_paket[rekaman["kode"]] = {
        "nama": rekaman["nama"],
        "ukuran": rekaman["ukuran"],
        "durasi": int(rekaman["durasi_bulan"]),
        "mulai_rencana": int(rekaman["mulai_rencana_bulan"] or 0),
        "pendahulu": pendahulu,
    }
  return daftar_paket


def periksa_kode_pendahulu(daftar_paket):
  """Menghentikan skrip bila ada pendahulu yang tidak terdaftar.

  Salah ketik kode pendahulu membuat paket tidak pernah siap dijadwalkan, dan
  pesan yang jelas lebih berguna daripada laporan dependensi melingkar.
  """
  for kode, paket in daftar_paket.items():
    for pendahulu in paket["pendahulu"]:
      if pendahulu not in daftar_paket:
        sys.exit(f"Paket {kode} bergantung pada {pendahulu} yang tidak terdaftar.")


def urutkan_menurut_dependensi(daftar_paket):
  """Mengurutkan paket sehingga tiap paket muncul sesudah seluruh pendahulunya.

  Hitungan maju dan mundur membutuhkan urutan ini. Bila dependensinya melingkar,
  tidak ada urutan yang sah, dan skrip berhenti agar kesalahan data terlihat.
  """
  sisa_pendahulu = {
      kode: set(paket["pendahulu"]) for kode, paket in daftar_paket.items()
  }
  urutan = []
  while sisa_pendahulu:
    siap = sorted(kode for kode, sisa in sisa_pendahulu.items() if not sisa)
    if not siap:
      sys.exit("Dependensi melingkar pada: " + ", ".join(sorted(sisa_pendahulu)))
    for kode in siap:
      urutan.append(kode)
      del sisa_pendahulu[kode]
    for sisa in sisa_pendahulu.values():
      sisa.difference_update(siap)
  return urutan


def hitung_maju(daftar_paket, urutan):
  """Menghitung bulan mulai dan selesai paling awal untuk tiap paket.

  Paket baru boleh mulai sesudah pendahulu terakhirnya selesai, dan tidak lebih
  awal dari bulan mulai rencana, misalnya karena batas kapasitas.
  """
  jadwal = {}
  for kode in urutan:
    paket = daftar_paket[kode]
    selesai_pendahulu = [
        jadwal[pendahulu]["selesai"] for pendahulu in paket["pendahulu"]
    ]
    mulai = max(selesai_pendahulu + [paket["mulai_rencana"]])
    jadwal[kode] = {"mulai": mulai, "selesai": mulai + paket["durasi"]}
  return jadwal


def hitung_mundur(daftar_paket, urutan, selesai_proyek):
  """Menghitung bulan mulai paling lambat tanpa menggeser selesainya proyek.

  Hitungan berjalan dari paket terakhir ke paket pertama. Batas selesai sebuah
  paket adalah mulai paling lambat milik penerusnya yang paling mendesak.
  """
  mulai_paling_lambat = {}
  for kode in reversed(urutan):
    penerus = [
        lain for lain, paket in daftar_paket.items() if kode in paket["pendahulu"]
    ]
    batas_selesai = min(
        [mulai_paling_lambat[lain] for lain in penerus] + [selesai_proyek]
    )
    mulai_paling_lambat[kode] = batas_selesai - daftar_paket[kode]["durasi"]
  return mulai_paling_lambat


def ke_kalender(nomor_bulan):
  """Mengubah nomor bulan sejak awal peta jalan menjadi nama bulan dan tahun."""
  bulan_absolut = BULAN_MULAI - 1 + nomor_bulan
  tahun = TAHUN_MULAI + bulan_absolut // BULAN_PER_TAHUN
  return f"{NAMA_BULAN[bulan_absolut % BULAN_PER_TAHUN]} {tahun}"


def tahun_yang_disentuh(mulai, selesai):
  """Mengembalikan tahun kalender yang dilalui paket dari mulai sampai selesai.

  Nomor bulan selesai tidak ikut dihitung, karena paket sudah rampung sebelum
  bulan itu dimulai.
  """
  tahun_awal = TAHUN_MULAI + (BULAN_MULAI - 1 + mulai) // BULAN_PER_TAHUN
  tahun_akhir = TAHUN_MULAI + (BULAN_MULAI - 1 + selesai - 1) // BULAN_PER_TAHUN
  return range(tahun_awal, tahun_akhir + 1)


def hitung_beban_tahunan(daftar_paket, jadwal):
  """Mengelompokkan proyek besar menurut tahun kalender tempat proyek berjalan."""
  beban = {}
  for kode, paket in daftar_paket.items():
    if paket["ukuran"] != UKURAN_BESAR:
      continue
    waktu = jadwal[kode]
    for tahun in tahun_yang_disentuh(waktu["mulai"], waktu["selesai"]):
      beban.setdefault(tahun, []).append(kode)
  return beban


def cetak_jadwal(daftar_paket, urutan, jadwal, mulai_paling_lambat):
  """Mencetak jadwal dan kelonggaran tiap paket, lalu jalur kritisnya."""
  print(f"{'Kode':<6}{'Mulai':<10}{'Selesai':<10}{'Bulan':>8}{'Longgar':>9}  Nama")
  for kode in urutan:
    mulai = jadwal[kode]["mulai"]
    selesai = jadwal[kode]["selesai"]
    longgar = mulai_paling_lambat[kode] - mulai
    print(
        f"{kode:<6}{ke_kalender(mulai):<10}{ke_kalender(selesai - 1):<10}"
        f"{mulai:>4}-{selesai:<3}{longgar:>9}  {daftar_paket[kode]['nama']}"
    )
  kritis = [
      kode for kode in urutan if mulai_paling_lambat[kode] == jadwal[kode]["mulai"]
  ]
  print("\nJalur kritis: " + " -> ".join(kritis))


def cetak_beban_tahunan(beban):
  """Mencetak proyek besar per tahun dan menandai tahun yang melewati kapasitas."""
  print(f"\nProyek besar per tahun (kapasitas {KAPASITAS_PROYEK_BESAR_PER_TAHUN}):")
  for tahun in sorted(beban):
    daftar_kode = beban[tahun]
    melebihi = len(daftar_kode) > KAPASITAS_PROYEK_BESAR_PER_TAHUN
    tanda = "MELEBIHI" if melebihi else "aman"
    print(f"  {tahun}: {len(daftar_kode)} ({', '.join(daftar_kode)}) {tanda}")


def main():
  """Menjalankan seluruh hitungan untuk berkas yang disebut di baris perintah."""
  if len(sys.argv) != 2:
    sys.exit("Cara pakai: python jalur-kritis.py paket-kerja-medikara.csv")
  daftar_paket = baca_paket_kerja(sys.argv[1])
  periksa_kode_pendahulu(daftar_paket)
  urutan = urutkan_menurut_dependensi(daftar_paket)
  jadwal = hitung_maju(daftar_paket, urutan)
  selesai_proyek = max(waktu["selesai"] for waktu in jadwal.values())
  mulai_paling_lambat = hitung_mundur(daftar_paket, urutan, selesai_proyek)
  cetak_jadwal(daftar_paket, urutan, jadwal, mulai_paling_lambat)
  cadangan = BATAS_AKHIR_BULAN - selesai_proyek
  print(
      f"Selesai: {ke_kalender(selesai_proyek - 1)}, "
      f"cadangan {cadangan} bulan terhadap batas Des 2030"
  )
  cetak_beban_tahunan(hitung_beban_tahunan(daftar_paket, jadwal))


if __name__ == "__main__":
  main()
