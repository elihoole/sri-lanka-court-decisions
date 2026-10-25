# Sri Lanka Court Decisions

Academic paper and analysis code for computational text analysis of Sri Lankan court decisions.

- **Paper:** Pandoc-based manuscript with PDF/DOCX output
- **Dataset:** [elihoole/sri-lanka-court-decisions](https://huggingface.co/datasets/elihoole/sri-lanka-court-decisions) on HuggingFace
- **Analysis:** Python code reproducing all paper results

## Quick Start

### Run Analysis

```bash
# Install dependencies
uv sync

# Run all analyses (plots, LDA, chi-square)
uv run python3 code/main.py

# Run specific analysis
uv run python3 code/main.py --plots   # Generate plots only
uv run python3 code/main.py --lda     # LDA topic modeling
uv run python3 code/main.py --text    # Chi-square & mutual info
```

### Build Paper

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
| `build-pdf.sh` | `output/EmpiricalStudies_300526_EH_Settled_25102026.pdf` | A4 PDF with full formatting |
| `build-docx.sh` | `output/EmpiricalStudies_300526_EH_Settled_25102026.docx` | Word document (EB Garamond font) |
| `build-mobile-pdf.sh` | `output/EmpiricalStudies_300526_mobile_EH_Settled_25102026.pdf` | Phone-sized PDF (90mm x 160mm) |

## Prerequisites

- [Pandoc](https://pandoc.org/) (>= 3.1.8, matching the pandoc-crossref build)
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
├── code/              # Analysis code
│   ├── main.py        # Entry point
│   ├── data_loader.py # Load from HuggingFace
│   ├── plots.py       # Plotting functions
│   ├── lda_analysis.py # LDA topic modeling
│   ├── text_analysis.py # Chi-square & MI
│   ├── utils.py       # Shared utilities
│   └── stopwords/     # Custom stopword lists
│
├── content/           # Paper sections (Markdown)
├── figures/           # Plots and images (PNG)
├── config/            # Build configuration
│   ├── chicago.csl    # Citation style
│   ├── reference.docx # Word template
│   └── *.tex          # LaTeX configs
├── output/            # Generated files
│
├── pyproject.toml     # Python dependencies
├── references.bib     # Bibliography (BibTeX)
├── build-pdf.sh       # Build A4 PDF
├── build-docx.sh      # Build Word document
└── build-mobile-pdf.sh # Build mobile PDF
```

## Citation Style

Uses Chicago Manual of Style 18th edition (notes and bibliography).
