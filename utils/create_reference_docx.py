#!/usr/bin/env python3
"""
Creates a properly styled reference.docx template for academic papers.
This template is used by pandoc to style the output DOCX.

Styles configured:
- Body Text: EB Garamond 12pt, 1.5 line spacing, justified
- Heading 1: Bold, 14pt, page break before
- Heading 2: Bold, 12pt
- Heading 3: Bold italic, 12pt
- Block Quote: Italic, indented left/right
- Footnotes: EB Garamond 10pt

Usage:
    uv run utils/create_reference_docx.py [output_path]
"""

from pathlib import Path

try:
    from docx import Document
    from docx.shared import Pt, Inches, Mm
    from docx.enum.style import WD_STYLE_TYPE
    from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
except ImportError:
    print("Error: python-docx not installed. Install with: uv add python-docx")
    exit(1)


def set_style_font(style, name='EB Garamond', size=12, bold=False, italic=False):
    """Set font properties for a style."""
    font = style.font
    font.name = name
    font.size = Pt(size)
    font.bold = bold
    font.italic = italic
    # Set font for East Asian text as well
    r = style.element
    rPr = r.get_or_add_rPr()
    rFonts = rPr.get_or_add_rFonts()
    rFonts.set(qn('w:ascii'), name)
    rFonts.set(qn('w:hAnsi'), name)
    rFonts.set(qn('w:eastAsia'), name)
    rFonts.set(qn('w:cs'), name)


def set_paragraph_format(style, space_before=0, space_after=6, line_spacing=1.5,
                         first_line_indent=None, left_indent=None, right_indent=None,
                         alignment=None, page_break_before=False):
    """Set paragraph formatting for a style."""
    pf = style.paragraph_format
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    pf.line_spacing = line_spacing

    if first_line_indent is not None:
        pf.first_line_indent = Inches(first_line_indent)
    if left_indent is not None:
        pf.left_indent = Inches(left_indent)
    if right_indent is not None:
        pf.right_indent = Inches(right_indent)
    if alignment is not None:
        pf.alignment = alignment
    if page_break_before:
        pf.page_break_before = True


def create_academic_reference_docx(output_path: Path):
    """Create a reference DOCX with academic paper styling."""
    doc = Document()

    # === SET PAGE SIZE TO A4 ===
    section = doc.sections[0]
    section.page_width = Mm(210)
    section.page_height = Mm(297)
    # Academic margins: 1 inch all around
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)

    # === ADD PAGE NUMBERS TO FOOTER ===
    footer = section.footer
    footer.is_linked_to_previous = False
    footer_para = footer.paragraphs[0]
    footer_para.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

    # Add page number field
    run = footer_para.add_run()
    fld_char_begin = OxmlElement('w:fldChar')
    fld_char_begin.set(qn('w:fldCharType'), 'begin')
    run._r.append(fld_char_begin)

    instr_text = OxmlElement('w:instrText')
    instr_text.text = 'PAGE'
    run._r.append(instr_text)

    fld_char_end = OxmlElement('w:fldChar')
    fld_char_end.set(qn('w:fldCharType'), 'end')
    run._r.append(fld_char_end)

    # Style the page number
    run.font.name = 'EB Garamond'
    run.font.size = Pt(11)

    # Get styles
    styles = doc.styles

    # === BODY TEXT (Normal) ===
    normal = styles['Normal']
    set_style_font(normal, 'EB Garamond', 12)
    set_paragraph_format(normal, space_after=6, line_spacing=1.5,
                         alignment=WD_PARAGRAPH_ALIGNMENT.JUSTIFY)

    # === HEADINGS ===
    # Heading 1 - Major sections (page break before)
    h1 = styles['Heading 1']
    set_style_font(h1, 'EB Garamond', 14, bold=True)
    set_paragraph_format(h1, space_before=12, space_after=6, line_spacing=1.5,
                         page_break_before=True)

    # Heading 2 - Subsections
    h2 = styles['Heading 2']
    set_style_font(h2, 'EB Garamond', 12, bold=True)
    set_paragraph_format(h2, space_before=12, space_after=6, line_spacing=1.5)

    # Heading 3 - Sub-subsections
    h3 = styles['Heading 3']
    set_style_font(h3, 'EB Garamond', 12, bold=True, italic=True)
    set_paragraph_format(h3, space_before=6, space_after=6, line_spacing=1.5)

    # === BLOCK QUOTE ===
    try:
        quote_style = styles['Quote']
    except KeyError:
        quote_style = styles.add_style('Quote', WD_STYLE_TYPE.PARAGRAPH)
    set_style_font(quote_style, 'EB Garamond', 11, italic=True)
    set_paragraph_format(quote_style, space_before=6, space_after=6,
                         line_spacing=1.5, left_indent=0.5, right_indent=0.5)

    # Block Text (alternative block quote style)
    try:
        block_text = styles['Block Text']
    except KeyError:
        block_text = styles.add_style('Block Text', WD_STYLE_TYPE.PARAGRAPH)
    set_style_font(block_text, 'EB Garamond', 11, italic=True)
    set_paragraph_format(block_text, space_before=6, space_after=6,
                         line_spacing=1.5, left_indent=0.5, right_indent=0.5)

    # === FOOTNOTE TEXT ===
    try:
        footnote = styles['Footnote Text']
        set_style_font(footnote, 'EB Garamond', 10)
        set_paragraph_format(footnote, space_after=3, line_spacing=1.0)
    except KeyError:
        pass  # Style may not exist in base template

    # === TOC STYLES ===
    for i in range(1, 4):
        toc_style_name = f'TOC {i}'
        try:
            toc = styles[toc_style_name]
        except KeyError:
            toc = styles.add_style(toc_style_name, WD_STYLE_TYPE.PARAGRAPH)
        set_style_font(toc, 'EB Garamond', 12)
        set_paragraph_format(toc, space_after=3, line_spacing=1.0,
                             left_indent=0.25 * (i - 1))

    # === TABLE STYLES ===
    try:
        table_style = styles['Table Grid']
        # Tables use slightly smaller font
    except KeyError:
        pass

    # === CAPTION STYLE ===
    try:
        caption = styles['Caption']
        set_style_font(caption, 'EB Garamond', 11, italic=True)
        set_paragraph_format(caption, space_before=6, space_after=12, line_spacing=1.0)
    except KeyError:
        pass

    # === Add sample content for reference ===
    doc.add_heading('Sample Heading 1', level=1)
    doc.add_paragraph('This is normal body text in EB Garamond 12pt with 1.5 line spacing and justified alignment. Academic papers typically use this formatting for readability.')

    doc.add_heading('Sample Heading 2', level=2)
    doc.add_paragraph('Subsection content demonstrating the heading hierarchy and paragraph spacing used throughout the document.')

    doc.add_heading('Sample Heading 3', level=3)
    doc.add_paragraph('Sub-subsection content with bold italic heading style.')

    # Add a block quote
    quote_para = doc.add_paragraph()
    quote_para.style = quote_style
    quote_para.add_run('"This is a sample block quote showing how citations and quoted material should appear - indented and in italics with slightly smaller font."')

    doc.add_paragraph('Regular paragraph continuing after the quote, demonstrating proper spacing.')

    # Save
    doc.save(str(output_path))
    print(f"Created reference document: {output_path}")


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        output = Path(sys.argv[1])
    else:
        output = Path(__file__).parent / 'reference.docx'

    create_academic_reference_docx(output)
    print("\nTo use this template, run pandoc with:")
    print(f"  pandoc input.md -o output.docx --reference-doc={output}")
