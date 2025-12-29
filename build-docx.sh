#!/bin/bash

# Build script for Sri Lanka Court Decisions DOCX
# Generates DOCX with EB Garamond font, proper styling, and page breaks

set -e  # Exit on error

# Change to the content directory
cd "$(dirname "$0")/content"

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

for file in "${sorted[@]}"; do
    cat "$file" >> "$temp_file"
    echo "" >> "$temp_file"
done

# Build the DOCX with pandoc
echo ""
echo "Generating DOCX..."
cd ..
mkdir -p output

# Prepare title page with current date
python3 - <<'PY'
from pathlib import Path
from datetime import datetime
title = Path("config/title-page.md").read_text()
today_str = datetime.now().strftime("%B %-d, %Y")
Path("temp-title-page.md").write_text(title.replace("${TODAY}", today_str))
PY

# Add page breaks before each top-level section
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

pandoc temp-combined-docx.md \
    -o output/paper.docx \
    --reference-doc=config/reference.docx \
    --lua-filter=config/format.lua \
    --filter pandoc-crossref \
    --include-before-body=temp-title-page.md \
    -M secPrefix=Section \
    -M tablePrefix=Table \
    -M figurePrefix=Figure \
    -M tblPrefix=Table \
    -M figPrefix=Figure \
    --citeproc \
    --bibliography=references.bib \
    --csl=config/chicago.csl \
    --toc \
    --toc-depth=3 \
    --number-sections \
    -V linkcolor:blue \
    -V toccolor:blue \
    -V urlcolor:blue \
    --highlight-style=tango

# Clean up temporary files
rm -f temp-combined-docx.md temp-title-page.md

echo ""
echo "Generated: output/paper.docx"
echo ""
echo "To update the Table of Contents in Word:"
echo "  1. Open the document in Microsoft Word"
echo "  2. Click anywhere in the TOC"
echo "  3. Press F9 and choose 'Update entire table'"
