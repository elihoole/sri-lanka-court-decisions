## Git Workflow

- **Commit frequently**: After completing a logical unit of work (e.g., fixing a section, adding bib entries, converting citations), commit without prompting
- **Use feature branches**: Create branches for significant changes (e.g., `fix/footnote-renumbering`)
- **Commit message format**: Use clear, descriptive messages with bullet points for multiple changes
- **Don't push without asking**: Commits are local until explicitly asked to push

## About the project

I have been working on this paper for a long time and I want to bring to a conclusion. My colleague returned the final Word document from her end. And I have decomposed the different sections under `sections-final`. You don't have to worry about the content of the paper sitting in any other folder. 

What I now need to do is:

1. Apply proper formatting and consistent numbering such that the errors or inconsistencies introduced by my colleague are removed. 

2. Remove weird artifacts from the .md files such as random "\" etc resulting from back conversion from .docx. 

3. Attach images from `images` correctly into `sections-final/4-analysis.md` section (these are plots)

4. My colleage may have inserted new citations / bibiliography that need to be added to `references.bib`

5. My current build scripts are `build-paper-pdf.sh` and `build-paper-docx.sh`. But in another project, I used EB Garamond font and template based Word document generation which gave better output. You can find those here: `/home/elihoole/Documents/personal-work/puttalam-ilmanite-vs-sl-cement-corporation/build-submission-docx.sh` and `/home/elihoole/Documents/personal-work/puttalam-ilmanite-vs-sl-cement-corporation/build-submission-pdf.sh`. I want you to explore those and align our build scripts more closely to them. 


## Citation System Migration (Completed December 6, 2025)

### Overview

The paper has been migrated from a manual footnote system to a hybrid **bibliography + footnote system** using Pandoc's citation processing with Chicago Manual of Style (18th edition, notes and bibliography). This enables automatic bibliography generation while preserving explanatory footnotes.

### Infrastructure Created

**Files:**
- `references.bib` - BibTeX database with 18 complete entries + 14 placeholders
- `chicago-fullnote-bibliography.csl` - Chicago Manual of Style 18th edition (notes and bibliography) style file
- `oscola.csl` - OSCOLA style file (deprecated, replaced with Chicago)
- `bibliography-formatting.tex` - LaTeX customizations for bibliography appearance
- Modified `build-paper-pdf.sh` - Added `--citeproc`, `--bibliography`, `--csl` flags
- Modified `build-paper-docx.sh` - Added same citation processing flags
- `.instructions/footnote-bibliography-migration.md` - Complete 8-phase migration plan
- `.instructions/citation-tracking.md` - 57-footnote tracking spreadsheet with status
- `.instructions/dinesha-handoff.md` - Comprehensive guide for completing 23 placeholder citations

**Complete Bibliography Entries (18):**
- Suchman & Mertz (2010) - Legal empiricism
- Cane & Kritzer (2010) - Oxford Handbook
- Kritzer (2010) - Forgotten empirical research
- Baldwin & Davis (2010) - Empirical research in law
- Abeywardena (2023) - Reading Supreme Courts from afar
- Epstein & Andrew (2014) - Introduction to empirical legal research
- Lazer et al. (2009) - Computational social science
- Frankenreiter & Livermore (2020) - Computational methods in legal research
- Blei et al. (2003) - Latent Dirichlet Allocation (LDA methodology)
- Shapiro (2008) - Coding complexity
- Supreme Court Database (2024)
- ConCourtStats (online database)
- Sri Lanka Mirror (2024) - Pending cases article
- Parliament Report (2017) - Criminal Justice System
- Judicature Act No 2 of 1978
- Daily FT (2015) - Justice triumphs
- Roar Media (2024) - Colombo courts

### Migration Approach

**Three-Part Citation System:**

1. **Pure Comments (11 total)** → Named footnotes `[^note_X]`
   - Appear at page bottoms as traditional footnotes
   - Examples: Mixed legal systems note, Article 126 explanations, SSL certificate warning
   - Format: `[^note_mixed_systems]: The other two mixed legal systems are Scotland and South Africa.`

2. **Full Bibliographic Citations (34 total)** → Bibliography entries `[@citekey]`
   - Automatically generate numbered in-text citations (superscript)
   - Appear in References section with full OSCOLA formatting
   - Format: `[@suchman2010legal]` or `[@suchman2010legal, p. 563]` for specific pages

3. **Incomplete Citations (23 total)** → Placeholders `[^X]`
   - Marked with "[To be filled by Dinesha]" + context
   - Preserved as footnotes until completion
   - Will be converted to `[@citekey]` format once bibliography entries added

**Example Usage:**

```markdown
Legal empiricism has been defined as research that examines legal phenomena 
using empirical data and methods.[@suchman2010legal, p. 563]

The Sri Lankan legal system is one of three surviving mixed legal 
systems.[^note_mixed_systems]

Historical analysis of judicial appointments remains incomplete.[^38]

[^note_mixed_systems]: The other two mixed legal systems are Scotland and South Africa.

[^38]: [To be filled by Dinesha - CJ appointment procedures]
```

### Migration Statistics

**Completed (34 citations + 11 footnotes = 45 total):**
- Section 2 (Empirical Study): 24 bibliography + 7 named footnotes + 15 placeholders
- Section 4 (Insights): 3 bibliography + 2 named footnotes + 4 placeholders
- All completed citations now auto-generate in References section
- All named footnotes appear at page bottoms

**Pending (23 placeholders):**
- Jayawardene (^8, ^9), Samararatne (^10), Tiruchelvam (^13), Author's work (^14)
- Computational methods (^20, ^24), Court on Trial India (^21, ^25)
- Constitutional amendments (^32, ^40, ^44), CJ impeachment/appointment (^38, ^39)
- Various Sri Lankan legal scholars (^28, ^29, ^42, ^43, ^45, ^47, ^48, ^49, ^54, ^55, ^56)

### Build Process

**PDF Generation:**
```bash
./build-paper-pdf.sh
```
Produces: `SriLankaCourtDecisions-paper-draft.pdf` with:
- Auto-generated Bibliography section (18 entries in Chicago format)
- Numbered bibliography entries with proper spacing
- Superscript in-text citations (¹, ², ³...)
- Page-bottom footnotes for comments
- Clean URLs without angle brackets
- Clean build with no warnings

**DOCX Generation:**
```bash
./build-paper-docx.sh
```
Produces: `SriLankaCourtDecisions-paper-draft.docx` with:
- Same bibliography and citation features
- Compatible with Microsoft Word
- Table of contents (requires F9 refresh in Word)

### Testing Results (Phase 6)

**Verified Working:**
- ✅ Both PDF and DOCX build cleanly (no errors/warnings)
- ✅ Bibliography auto-generates with 18 entries
- ✅ In-text citations render as superscript numbers
- ✅ Footnotes appear at page bottoms
- ✅ All citation types working (articles, books, chapters, online, legislation)
- ✅ Duplicates handled correctly (^1=^12, ^15=^16, ^50-52)
- ✅ Chicago style formatting applied (numbered entries, proper spacing, clean URLs)
- ✅ Bibliography entries numbered and properly spaced (December 6, 2025)

### Next Steps for Dinesha

See `.instructions/dinesha-handoff.md` for:
- Complete list of 23 placeholders with context
- Step-by-step guide to adding BibTeX entries
- Citation key naming conventions
- Testing procedures
- Examples for each entry type (@article, @book, @online, @legislation)

**Quick workflow:**
1. Find bibliographic info for placeholder
2. Add entry to `references.bib` in BibTeX format
3. Replace `[^X]: [To be filled...]` with `[@citekey]` in document
4. Delete old `[^X]:` definition (no longer needed)
5. Test with `./build-paper-pdf.sh`

### Special Notes

- LDA citation (Blei et al. 2003) added per user request for topic modeling methodology
- Some placeholders may be duplicates (e.g., ^32 and ^44 both mention 20th Amendment)
- ^47 may be duplicate of ^11 (Abeywardena) - needs verification
- All named footnote definitions moved to end of respective sections for clarity
- Old manual `7-reference.md` completely replaced with auto-generation note
- **Citation style switched from OSCOLA to Chicago** (December 6, 2025) to fix bibliography formatting issues:
  - Added numbered bibliography entries
  - Improved spacing between entries
  - Removed angle brackets from URLs
Contains footnotes and bibliographic references for the paper.