# Sri Lanka Court Decisions Paper

Academic paper analyzing Sri Lankan court decisions using computational text analysis.

## Quick Start

```bash
# Build PDF
./build-pdf.sh

# Build DOCX
./build-docx.sh

# Build mobile-friendly PDF
./build-mobile-pdf.sh
```

## Outputs

| Script | Output | Description |
|--------|--------|-------------|
| `build-pdf.sh` | `output/paper.pdf` | A4 PDF with full formatting |
| `build-docx.sh` | `output/paper.docx` | Word document (EB Garamond font) |
| `build-mobile-pdf.sh` | `output/paper-mobile.pdf` | Phone-sized PDF (90mm x 160mm) |

## Prerequisites

- [Pandoc](https://pandoc.org/) (>= 2.0)
- [pandoc-crossref](https://github.com/lierdakil/pandoc-crossref)
- LaTeX (pdflatex) with standard packages
- Python 3 (standard library only, no packages needed)

### Ubuntu/Debian
```bash
sudo apt install pandoc texlive-latex-base texlive-fonts-recommended \
    texlive-fonts-extra texlive-latex-extra python3
```

## Project Structure

```
.
├── build-pdf.sh       # Build A4 PDF
├── build-docx.sh      # Build Word document
├── build-mobile-pdf.sh # Build mobile PDF
├── references.bib     # Bibliography (BibTeX)
│
├── content/           # Paper sections (Markdown)
├── figures/           # Plots and images (PNG)
├── config/            # Build configuration
│   ├── chicago.csl    # Citation style
│   ├── reference.docx # Word template
│   └── *.tex          # LaTeX configs
│
└── output/            # Generated files
    └── paper.pdf      # Final PDF
```

## Citation Style

Uses Chicago Manual of Style 18th edition (notes and bibliography).
