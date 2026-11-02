"""Bangun buku dan slide; pakai --help untuk pilihan mesin dan lingkup."""

import argparse
from pathlib import Path
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def run_command(arguments, directory):
  """Jalankan daftar argumen tanpa shell agar jalur berkas tetap aman."""
  print(f"Membangun {directory.relative_to(ROOT)}", flush=True)
  subprocess.run(arguments, cwd=directory, check=True)


def build_document(source, engine, executable):
  """Tangani pustaka dan pengulangan lintas rujukan sesuai mesin yang dipilih."""
  if engine == "tectonic":
    run_command([executable, "--keep-logs", source.name], source.parent)
    return
  command = [executable, "-interaction=nonstopmode", "-halt-on-error", source.name]
  run_command(command, source.parent)
  if source.parent.name == "module":
    bibliography = shutil.which("bibtex")
    if not bibliography:
      raise RuntimeError("BibTeX diperlukan untuk membangun daftar pustaka.")
    run_command([bibliography, source.stem], source.parent)
    run_command(command, source.parent)
  run_command(command, source.parent)


def main():
  """Pilih sumber yang diminta; mesin tidak terpasang menghasilkan pesan jelas."""
  parser = argparse.ArgumentParser(description=__doc__)
  parser.add_argument("--engine", choices=["auto", "xelatex", "tectonic"],
                      default="auto")
  parser.add_argument("--executable", help="Jalur mesin bila tidak ada di PATH")
  parser.add_argument("--scope", choices=["all", "module", "slides"],
                      default="all")
  args = parser.parse_args()
  engine = args.engine
  if engine == "auto":
    engine = "xelatex" if shutil.which("xelatex") else "tectonic"
  executable = args.executable or shutil.which(engine)
  if not executable:
    parser.error("Pasang XeLaTeX/BibTeX atau Tectonic, atau isi --executable.")
  sources = []
  if args.scope in {"all", "module"}:
    sources.append(ROOT / "module/enterprise-architecture-digital-blueprint.tex")
  if args.scope in {"all", "slides"}:
    sources.extend(sorted((ROOT / "slides").glob("session*/session*.tex")))
  for source in sources:
    build_document(source, engine, executable)
  print(f"Selesai membangun {len(sources)} dokumen.")
  return 0


if __name__ == "__main__":
  sys.exit(main())
