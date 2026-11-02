# Memeriksa konsistensi model ArchiMate. Pakai: python periksa-model.py <berkas>
"""Pemeriksa konsistensi model ArchiMate untuk Aktivitas Bab 4.

Skrip ini membaca dua format: berkas asli Archi (.archimate) dan berkas Open
Exchange Format (.xml) hasil menu File > Export > Model to Open Exchange File.
Keduanya diubah menjadi satu bentuk yang sama, lalu diperiksa dengan aturan
yang sama. Akibatnya, model yang dibuat dengan alat lain pun dapat diperiksa
selama alat itu mampu mengekspor format pertukaran.

Kesalahan (referensi relasi yang putus) membuat skrip keluar dengan status 1.
Peringatan hanya dicetak, karena peringatan sering berarti pekerjaan yang
belum selesai, bukan model yang rusak.
"""

import sys
import xml.etree.ElementTree as ElementTree
from collections import Counter

NAMESPACE_XSI = "http://www.w3.org/2001/XMLSchema-instance"
NAMESPACE_ARCHI = "http://www.archimatetool.com/archimate"
NAMESPACE_PERTUKARAN = "http://www.opengroup.org/xsd/archimate/3.0/"
ATRIBUT_JENIS = "{" + NAMESPACE_XSI + "}type"

# Jenis view di berkas Archi. Sketsa dan kanvas bukan diagram ArchiMate,
# sehingga isinya tidak dihitung sebagai pemakaian elemen.
JENIS_VIEW_ARCHI = {"ArchimateDiagramModel", "SketchModel", "CanvasModel"}

# Elemen bantu yang tidak wajib bernama dan tidak wajib punya relasi sendiri.
JENIS_TANPA_ATURAN_NAMA = {"Junction", "Grouping"}

# Konvensi penamaan tim. Awalan dipakai sebagai pemeriksaan kasar, bukan
# pemeriksaan tata bahasa, sehingga hasilnya berupa peringatan saja.
AWALAN_PROSES = ("Me", "Ber")
AWALAN_FUNGSI = ("Pe",)
AWALAN_LAYANAN = ("Layanan",)
JENIS_LAYANAN = {"BusinessService", "ApplicationService", "TechnologyService"}

# Properti yang wajib diisi per jenis elemen. Katalog aplikasi di Bab 7
# membutuhkan pemilik tiap komponen aplikasi, jadi kekosongannya dicatat
# sejak sekarang.
PROPERTI_WAJIB = {"ApplicationComponent": ("Pemilik",)}

STATUS_BERHASIL = 0
STATUS_ADA_KESALAHAN = 1
STATUS_PEMAKAIAN_SALAH = 2


def buang_awalan_archimate(jenis_mentah):
  """Mengubah 'archimate:BusinessActor' menjadi 'BusinessActor'.

  Berkas Archi menulis jenis dengan awalan, sedangkan format pertukaran
  tidak. Tanpa penyeragaman ini, aturan harus ditulis dua kali.
  """
  return jenis_mentah.split(":")[-1]


def jenis_relasi_archi(jenis_elemen):
  """Mengembalikan nama relasi tanpa akhiran 'Relationship', atau None.

  Archi menyimpan relasi sebagai elemen di folder Relations dengan jenis
  seperti 'ServingRelationship'. Format pertukaran cukup menulis 'Serving'.
  """
  akhiran = "Relationship"
  if jenis_elemen.endswith(akhiran):
    return jenis_elemen[: -len(akhiran)]
  return None


def baca_properti_archi(simpul_elemen):
  """Mengambil pasangan kunci dan nilai properti dari satu elemen Archi."""
  properti = {}
  for simpul_properti in simpul_elemen.findall("property"):
    properti[simpul_properti.get("key", "")] = simpul_properti.get("value", "")
  return properti


def baca_format_archi(akar):
  """Membaca berkas .archimate menjadi elemen, relasi, dan elemen yang tampil.

  Elemen, relasi, dan view sama-sama bertanda 'element' di berkas Archi,
  dan dibedakan lewat atribut xsi:type.
  """
  daftar_elemen = []
  daftar_relasi = []
  id_elemen_tampil = set()
  for simpul in akar.iter("element"):
    jenis = buang_awalan_archimate(simpul.get(ATRIBUT_JENIS, ""))
    if jenis in JENIS_VIEW_ARCHI:
      for anak in simpul.iter("child"):
        if anak.get("archimateElement"):
          id_elemen_tampil.add(anak.get("archimateElement"))
      continue
    jenis_relasi = jenis_relasi_archi(jenis)
    if jenis_relasi is not None:
      daftar_relasi.append({
        "id": simpul.get("id"),
        "jenis": jenis_relasi,
        "sumber": simpul.get("source"),
        "tujuan": simpul.get("target"),
      })
      continue
    daftar_elemen.append({
      "id": simpul.get("id"),
      "jenis": jenis,
      "nama": simpul.get("name", ""),
      "properti": baca_properti_archi(simpul),
    })
  return daftar_elemen, daftar_relasi, id_elemen_tampil


def teks_nama_pertukaran(simpul, namespace):
  """Mengambil teks tag name pertama, atau string kosong bila tidak ada."""
  simpul_nama = simpul.find(namespace + "name")
  if simpul_nama is None or simpul_nama.text is None:
    return ""
  return simpul_nama.text


def baca_definisi_properti(akar, namespace):
  """Memetakan identifier definisi properti ke nama propertinya.

  Format pertukaran tidak menulis nama properti di tiap elemen, hanya
  rujukan ke definisinya, sehingga peta ini dibutuhkan lebih dahulu.
  """
  peta_nama = {}
  jalur = namespace + "propertyDefinitions/" + namespace + "propertyDefinition"
  for simpul_definisi in akar.findall(jalur):
    nama = teks_nama_pertukaran(simpul_definisi, namespace)
    peta_nama[simpul_definisi.get("identifier")] = nama
  return peta_nama


def baca_properti_pertukaran(simpul_elemen, namespace, peta_nama_properti):
  """Mengambil pasangan kunci dan nilai properti dari satu elemen pertukaran."""
  properti = {}
  jalur = namespace + "properties/" + namespace + "property"
  for simpul_properti in simpul_elemen.findall(jalur):
    kunci = peta_nama_properti.get(simpul_properti.get("propertyDefinitionRef"), "")
    simpul_nilai = simpul_properti.find(namespace + "value")
    nilai = "" if simpul_nilai is None else (simpul_nilai.text or "")
    properti[kunci] = nilai
  return properti


def baca_format_pertukaran(akar):
  """Membaca berkas Open Exchange Format menjadi bentuk yang sama dengan Archi."""
  namespace = "{" + NAMESPACE_PERTUKARAN + "}"
  peta_nama_properti = baca_definisi_properti(akar, namespace)
  daftar_elemen = []
  for simpul in akar.findall(namespace + "elements/" + namespace + "element"):
    daftar_elemen.append({
      "id": simpul.get("identifier"),
      "jenis": simpul.get(ATRIBUT_JENIS, ""),
      "nama": teks_nama_pertukaran(simpul, namespace),
      "properti": baca_properti_pertukaran(simpul, namespace, peta_nama_properti),
    })
  daftar_relasi = []
  jalur_relasi = namespace + "relationships/" + namespace + "relationship"
  for simpul in akar.findall(jalur_relasi):
    daftar_relasi.append({
      "id": simpul.get("identifier"),
      "jenis": simpul.get(ATRIBUT_JENIS, ""),
      "sumber": simpul.get("source"),
      "tujuan": simpul.get("target"),
    })
  id_elemen_tampil = set()
  for simpul_node in akar.iter(namespace + "node"):
    if simpul_node.get("elementRef"):
      id_elemen_tampil.add(simpul_node.get("elementRef"))
  return daftar_elemen, daftar_relasi, id_elemen_tampil


def baca_model(jalur_berkas):
  """Mengenali format dari namespace akar, lalu memanggil pembaca yang sesuai."""
  akar = ElementTree.parse(jalur_berkas).getroot()
  if akar.tag == "{" + NAMESPACE_ARCHI + "}model":
    return "Archi", baca_format_archi(akar)
  if akar.tag == "{" + NAMESPACE_PERTUKARAN + "}model":
    return "Open Exchange Format", baca_format_pertukaran(akar)
  raise ValueError("Format tidak dikenali: " + akar.tag)


def nama_bawaan_archi(jenis):
  """Menghasilkan nama bawaan Archi, misalnya 'Business Actor'.

  Archi memberi nama sesuai jenisnya saat elemen baru dibuat. Nama yang
  belum diganti hampir selalu berarti elemen itu lupa diberi nama.
  """
  huruf_bernama = []
  for posisi, huruf in enumerate(jenis):
    if posisi > 0 and huruf.isupper():
      huruf_bernama.append(" ")
    huruf_bernama.append(huruf)
  return "".join(huruf_bernama)


def periksa_referensi_relasi(daftar_elemen, daftar_relasi):
  """Mencari relasi yang ujungnya menunjuk elemen yang tidak ada."""
  id_yang_ada = {elemen["id"] for elemen in daftar_elemen}
  id_yang_ada.update(relasi["id"] for relasi in daftar_relasi)
  kesalahan = []
  for relasi in daftar_relasi:
    for ujung in ("sumber", "tujuan"):
      if relasi[ujung] not in id_yang_ada:
        kesalahan.append(f"Relasi {relasi['id']} ({relasi['jenis']}): {ujung} "
                         f"'{relasi[ujung]}' tidak ditemukan")
  return kesalahan


def periksa_pemakaian_elemen(daftar_elemen, daftar_relasi, id_elemen_tampil):
  """Mencari elemen yang tidak tampil di view atau tidak punya relasi."""
  id_terhubung = set()
  for relasi in daftar_relasi:
    id_terhubung.add(relasi["sumber"])
    id_terhubung.add(relasi["tujuan"])
  peringatan = []
  for elemen in daftar_elemen:
    if elemen["jenis"] in JENIS_TANPA_ATURAN_NAMA:
      continue
    if elemen["id"] not in id_elemen_tampil:
      peringatan.append(f"Belum tampil di view mana pun: {elemen['nama']}")
    if elemen["id"] not in id_terhubung:
      peringatan.append(f"Tidak punya relasi: {elemen['nama']}")
  return peringatan


def periksa_nama(daftar_elemen):
  """Memeriksa nama kosong, nama bawaan, nama ganda, dan awalan konvensi."""
  peringatan = []
  hitungan_nama = Counter((elemen["jenis"], elemen["nama"]) for elemen in daftar_elemen)
  for (jenis, nama), jumlah in sorted(hitungan_nama.items()):
    if jumlah > 1:
      peringatan.append(f"Nama ganda ({jumlah} kali) untuk {jenis}: {nama}")
  for elemen in daftar_elemen:
    jenis = elemen["jenis"]
    nama = elemen["nama"]
    if jenis in JENIS_TANPA_ATURAN_NAMA:
      continue
    if not nama.strip():
      peringatan.append(f"Elemen {elemen['id']} ({jenis}) belum bernama")
      continue
    if nama == nama_bawaan_archi(jenis):
      peringatan.append(f"Nama bawaan Archi belum diganti: {nama}")
    if jenis.endswith("Process") and not nama.startswith(AWALAN_PROSES):
      peringatan.append(f"Proses sebaiknya diawali kata kerja: {nama}")
    if jenis.endswith("Function") and not nama.startswith(AWALAN_FUNGSI):
      peringatan.append(f"Fungsi sebaiknya berupa kata benda pe-an: {nama}")
    if jenis in JENIS_LAYANAN and not nama.startswith(AWALAN_LAYANAN):
      peringatan.append(f"Layanan sebaiknya diawali 'Layanan': {nama}")
  return peringatan


def periksa_properti_wajib(daftar_elemen):
  """Mencari elemen yang belum mengisi properti wajib menurut konvensi tim."""
  peringatan = []
  for elemen in daftar_elemen:
    for kunci in PROPERTI_WAJIB.get(elemen["jenis"], ()):
      if not elemen["properti"].get(kunci, "").strip():
        peringatan.append(f"Properti '{kunci}' kosong: {elemen['nama']}")
  return peringatan


def cetak_ringkasan(nama_format, daftar_elemen, daftar_relasi, id_elemen_tampil):
  """Mencetak jumlah elemen per jenis agar isi model terlihat sekilas."""
  print(f"Format: {nama_format}")
  print(f"Elemen: {len(daftar_elemen)}, relasi: {len(daftar_relasi)}, "
        f"elemen yang tampil di view: {len(id_elemen_tampil)}")
  hitungan_jenis = Counter(elemen["jenis"] for elemen in daftar_elemen)
  for jenis, jumlah in sorted(hitungan_jenis.items()):
    print(f"  {jenis:<24} {jumlah}")


def cetak_daftar(judul, daftar_pesan):
  """Mencetak satu kelompok temuan beserta jumlahnya."""
  print(f"{judul}: {len(daftar_pesan)}")
  for pesan in daftar_pesan:
    print(f"  - {pesan}")


def main():
  """Menjalankan seluruh pemeriksaan dan mengembalikan status keluar."""
  if len(sys.argv) != 2:
    print("Pakai: python periksa-model.py <berkas .archimate atau .xml>")
    return STATUS_PEMAKAIAN_SALAH
  nama_format, (daftar_elemen, daftar_relasi, id_elemen_tampil) = baca_model(
    sys.argv[1])
  cetak_ringkasan(nama_format, daftar_elemen, daftar_relasi, id_elemen_tampil)
  kesalahan = periksa_referensi_relasi(daftar_elemen, daftar_relasi)
  peringatan = periksa_pemakaian_elemen(daftar_elemen, daftar_relasi, id_elemen_tampil)
  peringatan += periksa_nama(daftar_elemen)
  peringatan += periksa_properti_wajib(daftar_elemen)
  cetak_daftar("Kesalahan", kesalahan)
  cetak_daftar("Peringatan", peringatan)
  if kesalahan:
    return STATUS_ADA_KESALAHAN
  return STATUS_BERHASIL


if __name__ == "__main__":
  sys.exit(main())
