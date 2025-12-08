#!/bin/bash

# Build script for Final Written Defense DOCX
# Generates DOCX with automatic table of contents and page number cross-references
# Each markdown file starts on a new page

set -e  # Exit on error

# Change to the sections directory
cd "$(dirname "$0")/sections"

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
    # Note: If you have a separate title page file (0-0-title-page.md), uncomment below to skip it
    # if [ "$file" = "0-0-title-page.md" ]; then
    #     continue
    # fi

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

# Prepare title page with current date (avoid sed delimiter issues)
python - <<'PY'
from pathlib import Path
from datetime import datetime
title = Path("title-page-docx.md").read_text()
today_str = datetime.now().strftime("%B %-d, %Y")
Path("title-page-docx-temp.md").write_text(title.replace("${TODAY}", today_str))
PY

# Add page breaks before each top-level section (# heading) using pandoc's pagebreak block
python - <<'PY'
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

# Build pandoc command with optional reference doc
PANDOC_CMD="pandoc temp-combined-docx.md \
    -o SriLankaCourtDecisions-paper-draft.docx \
    --filter pandoc-crossref \
    --include-before-body=title-page-docx-temp.md \
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
    --highlight-style=tango"

# Add reference doc if specified
if [ -n "${REFERENCE_DOC:-}" ]; then
    PANDOC_CMD="$PANDOC_CMD --reference-doc=$REFERENCE_DOC"
fi

# Execute the command
eval $PANDOC_CMD

# Clean up temporary file
rm -f temp-combined-docx.md title-page-docx-temp.md

echo ""
echo "✓ DOCX generated successfully: SriLankaCourtDecisions-paper-draft.docx"
echo ""
echo "The DOCX includes:"
echo "  - Custom title page (DOCX-friendly layout)"
echo "  - Table of contents (requires Word to update - see below)"
echo "  - Numbered sections (1, 2, 3, etc.)"
echo "  - Internal cross-references"
echo "  - Each top-level section (# heading) starts on a new page"
echo "  - Professional formatting"
echo "  - Footnotes"
echo ""
echo "⚠ IMPORTANT - To see the Table of Contents in Word:"
echo "  1. Open SriLankaCourtDecisions-paper-draft.docx in Microsoft Word"
echo "  2. Click anywhere in the TOC area (near the top)"
echo "  3. Press F9 (or right-click and select 'Update Field')"
echo "  4. Choose 'Update entire table'"
echo "  5. The TOC will now show all sections with page numbers"
echo ""
echo "Alternative: The --toc flag creates a TOC that should appear automatically,"
echo "but some Word versions may need manual refresh."
echo ""
echo "Note: To customize formatting, you can create a reference document:"
echo "  1. Generate a basic DOCX with pandoc"
echo "  2. Open it in Word and modify styles (headings, fonts, etc.)"
echo "  3. Save it as reference.docx"
echo "  4. Run: REFERENCE_DOC=reference.docx ./build-paper-docx.sh"
