#!/bin/bash

# Build script for Mobile-friendly PDF
# Generates a phone-sized PDF (80mm x 150mm) optimized for reading on mobile devices
# Based on the approach used in sharjana-booklet project

set -e  # Exit on error

# Change to the sections directory
cd "$(dirname "$0")/sections-final"

# Get all markdown files and sort them properly
files=(*.md)
IFS=$'\n' sorted=($(printf '%s\n' "${files[@]}" | sort -V))

echo "Building Mobile PDF from the following files:"
printf '  - %s\n' "${sorted[@]}"

# Create temporary combined file with page breaks
echo ""
echo "Combining files with page breaks..."
temp_file="../temp-combined-mobile.md"
> "$temp_file"  # Clear/create temp file

for file in "${sorted[@]}"; do
    # Add page break before each file
    echo -e '\n\\newpage\n' >> "$temp_file"
    cat "$file" >> "$temp_file"
    echo "" >> "$temp_file"  # Add blank line after file content
done

# Build the PDF with pandoc
echo ""
echo "Generating Mobile PDF..."
cd ..
pandoc temp-combined-mobile.md \
    -o SriLankaCourtDecisions-paper-mobile.pdf \
    --pdf-engine=pdflatex \
    --filter pandoc-crossref \
    -M secPrefix="Section" \
    -M tablePrefix="Table" \
    -M figurePrefix="Figure" \
    -M tblPrefix="Table" \
    -M figPrefix="Figure" \
    --citeproc \
    --bibliography=references.bib \
    --csl=chicago-fullnote-bibliography.csl \
    --toc \
    --toc-depth=2 \
    --number-sections \
    -H bibliography-formatting.tex \
    -H text-alignment.tex \
    -H font-config-mobile.tex \
    -H quote-style.tex \
    -H section-breaks.tex \
    -V geometry:paperwidth=90mm \
    -V geometry:paperheight=160mm \
    -V geometry:top=8mm \
    -V geometry:bottom=12mm \
    -V geometry:left=6mm \
    -V geometry:right=6mm \
    -V linkcolor:blue \
    -V toccolor:blue \
    -V urlcolor:blue \
    -V fontsize=9pt \
    -V pagestyle=plain

# Clean up temporary file
rm -f temp-combined-mobile.md

echo ""
echo "✓ Mobile PDF generated successfully: SriLankaCourtDecisions-paper-mobile.pdf"
echo ""
echo "Mobile PDF specifications:"
echo "  - Paper size: 90mm × 160mm (phone-friendly)"
echo "  - Margins: 6-8mm (compact)"
echo "  - Font size: 9pt (readable on small screens)"
echo "  - Line spacing: 1.15 (tighter than desktop)"
echo "  - TOC depth: 2 levels (less clutter)"
echo ""
