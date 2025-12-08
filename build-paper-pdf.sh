#!/bin/bash

# Build script for Final Written Defense PDF
# Generates PDF with automatic table of contents and page number cross-references
# Each markdown file starts on a new page

set -e  # Exit on error

# Change to the sections directory
cd "$(dirname "$0")/sections"

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
    # Note: If you have a separate title page file (0-0-title-page.md), uncomment below to skip it
    # if [ "$file" = "0-0-title-page.md" ]; then
    #     continue
    # fi

    # Add page break before each file
    echo -e '\n\\newpage\n' >> "$temp_file"
    cat "$file" >> "$temp_file"
    echo "" >> "$temp_file"  # Add blank line after file content
done

# Build the PDF with pandoc
echo ""
echo "Generating PDF..."
cd ..
pandoc temp-combined.md \
    -o SriLankaCourtDecisions-paper-draft.pdf \
    --pdf-engine=xelatex \
    --filter pandoc-crossref \
    -M tablePrefix="Table" \
    -M figurePrefix="Figure" \
    -M tblPrefix="Table" \
    -M figPrefix="Figure" \
    --citeproc \
    --bibliography=references.bib \
    --csl=chicago-fullnote-bibliography.csl \
    --toc \
    --toc-depth=3 \
    --number-sections \
    -H bibliography-formatting.tex \
    -H text-alignment.tex \
    -B title-page.tex \
    -H font-config.tex \
    -H quote-style.tex \
    -H section-breaks.tex \
    -V geometry:a4paper \
    -V geometry:margin=1in \
    -V linkcolor:blue \
    -V toccolor:blue \
    -V urlcolor:blue \
    -V fontsize=11pt \
    -V pagestyle=plain
    # Note: Uncomment the lines below if you create additional custom LaTeX templates:
    # -B title-page.tex \
    # -H font-config.tex \
    # -H quote-style.tex \
    # -H section-breaks.tex

# Clean up temporary file
rm -f temp-combined.md

echo ""
echo "✓ PDF generated successfully: SriLankaCourtDecisions-paper-draft.pdf"
echo ""
echo "The PDF includes:"
echo "  - Automatic table of contents with page numbers"
echo "  - Numbered sections (1, 2, 3, etc.)"
echo "  - Internal cross-references"
echo "  - Each markdown file starts on a new page"
echo "  - Professional formatting"
echo "  - Footnotes"
echo ""
echo "Note: To add a custom title page and styling, create LaTeX template files and uncomment"
echo "      the relevant lines in this build script (lines 61-64)."
