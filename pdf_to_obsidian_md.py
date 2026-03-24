import argparse
from pathlib import Path
from pdf2image import convert_from_path

def safe_slug(name: str) -> str:
    """Gør et filnavn mappe-venligt."""
    out = []
    for ch in name.strip():
        if ch.isalnum() or ch in ("-", "_"):
            out.append(ch)
        elif ch.isspace():
            out.append("_")
        # alt andet droppes
    slug = "".join(out).strip("_")
    return slug if slug else "slides"

def unique_path(path: Path) -> Path:
    """
    Hvis path findes, lav en ny med suffix _2, _3, ...
    fx Note.md -> Note_2.md
    """
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    i = 2
    while True:
        candidate = parent / f"{stem}_{i}{suffix}"
        if not candidate.exists():
            return candidate
        i += 1

def main():
    p = argparse.ArgumentParser()
    p.add_argument("pdf", help="Sti til PDF")
    p.add_argument("--out", default="obsidian_slides", help="Output-mappe")
    p.add_argument("--dpi", type=int, default=200, help="DPI til billeder")
    p.add_argument("--title", default=None, help="Titel i markdown (valgfri)")
    p.add_argument("--overwrite", action="store_true",
                   help="Overskriv .md og billeder hvis de allerede findes (IKKE anbefalet)")
    args = p.parse_args()

    pdf_path = Path(args.pdf).expanduser().resolve()
    out_dir = Path(args.out).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    # ✅ Unik undermappe pr PDF: images/<pdf-navn>/
    pdf_slug = safe_slug(pdf_path.stem)
    img_dir = out_dir / "images" / pdf_slug
    img_dir.mkdir(parents=True, exist_ok=True)

    # Markdown filnavn (beskyt noter mod overwrite)
    md_title = args.title or pdf_path.stem
    md_path = out_dir / f"{pdf_path.stem}.md"
    if not args.overwrite:
        md_path = unique_path(md_path)

    # Hvis du ikke overwriter, men billedmappen allerede indeholder billeder,
    # så laver vi automatisk en ny "run" undermappe for at undgå overskrivning.
    if not args.overwrite:
        existing_pngs = list(img_dir.glob("slide_*.png"))
        if existing_pngs:
            # lav images/<pdf>/run_2, run_3, ...
            run_dir = img_dir / "run_2"
            k = 2
            while run_dir.exists():
                k += 1
                run_dir = img_dir / f"run_{k}"
            img_dir = run_dir
            img_dir.mkdir(parents=True, exist_ok=True)

    # Konverter sider til billeder
    pages = convert_from_path(str(pdf_path), dpi=args.dpi)

    image_files = []
    for i, page in enumerate(pages, start=1):
        fname = f"slide_{i:03d}.png"
        fpath = img_dir / fname
        if fpath.exists() and not args.overwrite:
            # Burde ikke ske pga run_* logik, men ekstra sikkerhed:
            fpath = unique_path(fpath)
        page.save(str(fpath), "PNG")
        image_files.append(fpath)

    # Skriv markdown (uden "Slide X" og uden "Noter:" overskrift, men med ---)
    lines = []
    lines.append(f"# {md_title}\n")
    lines.append(f"*Kilde:* `{pdf_path.name}`\n")
    lines.append("---\n\n")

    for fpath in image_files:
        rel = fpath.relative_to(out_dir)
        lines.append(f"![[{rel.as_posix()}]]\n\n")
        lines.append("- \n\n")
        lines.append("---\n\n")

    md_path.write_text("".join(lines), encoding="utf-8")
    print(f"✅ Skrev: {md_path}")
    print(f"🖼️  Billeder i: {img_dir}")

if __name__ == "__main__":
    main()
