"""Periksa kelengkapan modul; jalankan dari folder mana pun dengan Python 3."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
CHAPTER_COUNT = 14


def inspect_materials():
  """Temukan rujukan putus dan bagian kosong sebelum kompilasi dilakukan."""
  errors = []
  labels = []
  references = []
  citations = set()
  bibliography = "\n".join(
    path.read_text(encoding="utf-8") for path in (ROOT / "module").rglob("*.bib")
  )
  keys = re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", bibliography)
  for key in set(keys):
    if keys.count(key) > 1:
      errors.append(f"Kunci pustaka berulang: {key}")
  master = (ROOT / "module/enterprise-architecture-digital-blueprint.tex").read_text(
    encoding="utf-8"
  )
  for number in range(1, CHAPTER_COUNT + 1):
    chapter = f"chapter{number:02}"
    path = ROOT / "module" / f"{chapter}.tex"
    slide = ROOT / "slides" / f"session{number:02}" / f"session{number:02}.tex"
    sources = ROOT / "sources" / chapter
    if not path.exists() or not slide.exists():
      errors.append(f"Naskah atau slide belum tersedia: {chapter}")
      continue
    text = path.read_text(encoding="utf-8")
    if f"\\include{{{chapter}}}" not in master:
      errors.append(f"Bab belum dimuat berkas induk: {chapter}")
    if re.search(r"\bTODO\b", text):
      errors.append(f"Masih ada penanda bagian kosong: {chapter}")
    objectives = text.split("\\section*{Tujuan Pembelajaran}")[-1].split(
      "\\section{Pendahuluan}"
    )[0]
    if objectives.count("\\item") != 3:
      errors.append(f"Tujuan harus tiga butir: {chapter}")
    exercises = re.findall(r"\\subsection\*\{Latihan ([123]):", text)
    if exercises != ["1", "2", "3"]:
      errors.append(f"Latihan harus berurutan 1 sampai 3: {chapter}")
    if not (sources / "README.md").exists() or len(list(sources.iterdir())) < 2:
      errors.append(f"Berkas pendukung belum lengkap: {chapter}")
    for target in re.findall(r"\\berkas\{(sources/[^}]+)\}", text):
      if not (ROOT / target).exists():
        errors.append(f"Berkas pendukung tidak ditemukan: {target}")
    for figure in re.findall(r"\\input\{(\.\./figures/[^}]+)\}", text):
      if not (path.parent / figure).exists():
        errors.append(f"Diagram tidak ditemukan: {figure}")
    labels.extend(re.findall(r"\\label\{([^}]+)\}", text))
    labels.extend(re.findall(r"(?<!\\)\blabel\s*=\s*\{([^}]+)\}", text))
    references.extend(re.findall(r"\\(?:ref|autoref)\{([^}]+)\}", text))
    for group in re.findall(r"\\cite\w*\{([^}]+)\}", text):
      citations.update(part.strip() for part in group.split(","))
    slide_text = slide.read_text(encoding="utf-8")
    if slide_text.count("\\begin{frame}") < 8:
      errors.append(f"Slide terlalu sedikit untuk satu sesi: {chapter}")
    for figure in re.findall(r"\\input\{(\.\./\.\./figures/[^}]+)\}", slide_text):
      if not (slide.parent / figure).exists():
        errors.append(f"Diagram slide tidak ditemukan: {figure}")
    print(
      f"Bab {number:02}: {len(text.split())} kata sumber, "
      f"{slide_text.count(chr(92) + 'begin{frame}')} frame, "
      f"{len(list(sources.iterdir())) - 1} berkas pendukung"
    )
  for label in set(labels):
    if labels.count(label) > 1:
      errors.append(f"Label berulang: {label}")
  errors.extend(f"Rujukan label tidak ditemukan: {key}"
                for key in sorted(set(references) - set(labels)))
  errors.extend(f"Kunci sitasi tidak ditemukan: {key}"
                for key in sorted(citations - set(keys)))
  return errors


def main():
  """Kembalikan kode gagal agar pemeriksaan dapat dipakai pada alur build."""
  errors = inspect_materials()
  for error in errors:
    print(f"GAGAL: {error}", file=sys.stderr)
  print(f"Pemeriksaan selesai: {len(errors)} masalah.")
  return 1 if errors else 0


if __name__ == "__main__":
  sys.exit(main())
