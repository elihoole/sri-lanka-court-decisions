#!/bin/bash

# Build script for Sri Lanka Court Decisions PDF
# Generates PDF with automatic table of contents and page number cross-references

set -e  # Exit on error

# Change to the content directory
cd "$(dirname "$0")/content"

# Get all markdown files and sort them properly
files=(*.md)
IFS=$'\n' sorted=($(printf '%s\n' "${files[@]}" | sort -V))

echo "Building PDF from the following files:"
printf '  - %s\n' "${sorted[@]}"

# Create temporary combined file with page breaks
echo ""
echo "Combining files with page breaks..."
temp_file="../temp-combined.md"
> "$temp_file"  # Clear/create temp file

for file in "${sorted[@]}"; do
    echo -e '\n\\newpage\n' >> "$temp_file"
    cat "$file" >> "$temp_file"
    echo "" >> "$temp_file"
done

# Build the PDF with pandoc
echo ""
echo "Generating PDF..."
cd ..
mkdir -p output

pandoc temp-combined.md \
    -o output/paper.pdf \
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
    --toc-depth=3 \
    --number-sections \
    -H config/bibliography.tex \
    -H config/alignment.tex \
    -H config/front-matter.tex \
    -B config/title-page.tex \
    -H config/fonts.tex \
    -H config/quotes.tex \
    -H config/sections.tex \
    -V geometry:a4paper \
    -V geometry:margin=1in \
    -V linkcolor:blue \
    -V toccolor:blue \
    -V urlcolor:blue \
    -V fontsize=12pt \
    -V pagestyle=plain

# Clean up temporary file
rm -f temp-combined.md

echo ""
echo "Generated: output/paper.pdf"
