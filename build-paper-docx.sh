#!/bin/bash

# Build script for Academic Paper DOCX
# Generates DOCX with EB Garamond font, proper styling, and page breaks
# Uses a reference template for consistent formatting

set -e  # Exit on error

# Change to the sections directory
cd "$(dirname "$0")/sections-final"

# Get all markdown files and sort them properly
files=(*.md)
IFS=$'\n' sorted=($(printf '%s\n' "${files[@]}" | sort -V))

echo "Building DOCX from the following files:"
printf '  - %s\n' "${sorted[@]}"

# Create temporary combined file with page breaks
echo ""
echo "Combining files with page breaks..."
temp_file="../temp-combined-docx.md"
> "$temp_file"  # Clear/create temp file

first=true
for file in "${sorted[@]}"; do
    if [ "$first" = true ]; then
        first=false
    fi
    cat "$file" >> "$temp_file"
    echo "" >> "$temp_file"  # Add blank line after file content
done

# Build the DOCX with pandoc
echo ""
echo "Generating DOCX..."
cd ..

# Prepare title page with current date
python3 - <<'PY'
from pathlib import Path
from datetime import datetime
title = Path("title-page-docx.md").read_text()
today_str = datetime.now().strftime("%B %-d, %Y")
Path("title-page-docx-temp.md").write_text(title.replace("${TODAY}", today_str))
PY

# Add page breaks before each top-level section (# heading) using pandoc's pagebreak block
python3 - <<'PY'
from pathlib import Path
path = Path("temp-combined-docx.md")
lines = path.read_text().splitlines()
out = []
first_heading = True
for line in lines:
    if line.startswith("# "):
        if first_heading:
            first_heading = False
        else:
            out.append("::: pagebreak")
            out.append(":::")
            out.append("")
    out.append(line)
path.write_text("\n".join(out) + "\n")
PY

# Build pandoc command with reference doc and lua filter
pandoc temp-combined-docx.md \
    -o SriLankaCourtDecisions-paper-draft.docx \
    --reference-doc=utils/reference.docx \
    --lua-filter=utils/academic-docx-format.lua \
    --filter pandoc-crossref \
    --include-before-body=title-page-docx-temp.md \
    -M secPrefix=Section \
    -M tablePrefix=Table \
    -M figurePrefix=Figure \
    -M tblPrefix=Table \
    -M figPrefix=Figure \
    --citeproc \
    --bibliography=references.bib \
    --csl=chicago-fullnote-bibliography.csl \
    --toc \
    --toc-depth=3 \
    --number-sections \
    -V linkcolor:blue \
    -V toccolor:blue \
    -V urlcolor:blue \
    --highlight-style=tango

# Clean up temporary file
rm -f temp-combined-docx.md title-page-docx-temp.md

echo ""
echo "DOCX generated successfully: SriLankaCourtDecisions-paper-draft.docx"
echo ""
echo "The DOCX includes:"
echo "  - EB Garamond font throughout"
echo "  - Custom title page"
echo "  - Table of contents (update with F9 in Word)"
echo "  - Numbered sections"
echo "  - Internal cross-references"
echo "  - Each section starts on a new page"
echo "  - Chicago-style footnotes and bibliography"
echo "  - Professional academic formatting"
echo ""
echo "To update the Table of Contents in Word:"
echo "  1. Open the document in Microsoft Word"
echo "  2. Click anywhere in the TOC"
echo "  3. Press F9 and choose 'Update entire table'"
echo ""
