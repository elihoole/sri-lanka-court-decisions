#!/bin/bash

# Build script for Mobile-friendly PDF
# Generates a phone-sized PDF (90mm x 160mm) optimized for reading on mobile devices

set -e  # Exit on error

# Change to the content directory
cd "$(dirname "$0")/content"

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
    echo -e '\n\\newpage\n' >> "$temp_file"
    cat "$file" >> "$temp_file"
    echo "" >> "$temp_file"
done

# Build the PDF with pandoc
echo ""
echo "Generating Mobile PDF..."
cd ..
mkdir -p output

pandoc temp-combined-mobile.md \
    -o output/paper-mobile.pdf \
    --pdf-engine=pdflatex \
    --filter pandoc-crossref \
    -M secPrefix="Section" \
    -M tablePrefix="Table" \
    -M figurePrefix="Figure" \
    -M tblPrefix="Table" \
    -M figPrefix="Figure" \
    --citeproc \
    --bibliography=references.bib \
    --csl=config/chicago.csl \
    --toc \
    --toc-depth=2 \
    --number-sections \
    -H config/bibliography.tex \
    -H config/alignment.tex \
    -H config/fonts-mobile.tex \
    -H config/quotes.tex \
    -H config/sections.tex \
    -B config/title-page-mobile.tex \
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
echo "Generated: output/paper-mobile.pdf"
