## My writing preferences

Based on comparing the AI version to your edited version, here are your writing preferences:
Precision over flourish: You replaced vague phrases with more exact ones. "Constitutes the core of the legal system" became "determine the content of the law"—direct and legally precise. "Highly influential" became simply "influential," trimming unnecessary intensifiers.
Discipline-appropriate terminology: You changed "decisions" to "judgments," which is the more accurate term in common-law usage. "Narrated" became "interpreted"—a more concrete, legally meaningful verb.
Avoiding redundancy: You cut "past both binding precedent and" from the phrase about extending knowledge, streamlining what was a somewhat tangled construction. Similarly, "settled assumptions" became "received assumptions and ingrained perceptions"—you actually expanded here, but to add meaningful nuance rather than padding.
Measured claims: You softened absolute statements. "Makes visible" became "can make visible." This reflects appropriate scholarly caution about what computational methods actually achieve.
Punctuation preferences: You use spaced en-dashes (–) rather than unspaced em-dashes (—) for parenthetical insertions, though you kept the em-dash in the final sentence. You also prefer "judgments" over "decisions" and "rulings" in certain contexts.
Cutting hollow phrases: "How judicial influence operates" was removed entirely—it didn't add substance. You prefer economy where possible.
Overall, you favor prose that is precise, appropriately hedged, terminologically accurate, and free of vague intensifiers or filler phrases. You're comfortable with complex sentences but want each word to earn its place.

## Key things

1. I will have to port this as a docx file -- so very important that footnotes are properly preserved
2. This is an academic paper so writing style should be approriate and must reflect my preferences. 

## About the project

I have been working on this paper for a long time and I want to bring to a conclusion. As it is, most sections are there but several issues persist:

1. Writing is very all over the place because multiple people contributed. We need to bring a consistent style.
2. We need to think about the logical coherence and redundancy in paras and sections. I think organisation overall needs work.
3. We need to write some parts of sections that need to be added.

## Skeleton of the paper

All sections sit within sections/ directory as separate .md files. 

**0. Abstract**
Introduces the empirical study of Sri Lanka's apex courts (Supreme Court and Court of Appeal) from 2012–2022 using computational methods. Presents the CDTextLK corpus (1278 Supreme Court and 7314 Court of Appeal decisions) and describes eight key patterns identified through computational analysis. Argues these insights challenge received wisdom about judicial impact and provide a necessary corrective to knowledge generated through landmark cases.

**1. Introduction**
Explains the dominance of landmark judgments in common-law systems and proposes computational methods as a means to analyse the full corpus of case law beyond this narrow focus. Sets out the article's two main questions: what insights emerge from systematic empirical examination of Sri Lankan appellate judgments, and what are the prospects for such examination given current data availability. Provides roadmap for subsequent sections.

**2. Empirical Study of Sri Lankan Courts**
Situates the study within the tradition of legal empiricism and judicial statistics research, contrasting the rare empirical work in Sri Lanka with more established practices elsewhere. Describes Sri Lanka's mixed legal system shaped by Portuguese, Dutch, and British colonialism, explains the role of case law in developing Roman-Dutch, English Common, and Customary Laws, and details the structure and function of the Superior Courts. Examines the judicial branch from 2012–2022 in the context of constitutional developments (18th, 19th, and 20th Amendments) and discusses limitations in legal system digitisation.

**3. CDTextLK: Court Decision Texts Sri Lanka Dataset**
Describes the compilation of the CDTextLK dataset by scraping official court websites for the period 2012–2022. Details the dataset structure (1278 Supreme Court decisions, 7314 Court of Appeal decisions) and the technical challenges encountered, including duplicates, non-standardised case numbers, and OCR issues. Provides basic descriptive statistics including mean token counts for each court.

**4. Insights from the CDTextLK**
Presents eight empirical patterns identified through exploratory data analysis, mutual information analysis, and topic modelling. Covers: the Court of Appeal's greater numerical contribution; variations in Supreme Court output correlating with judicial independence; time taken to deliver decisions (37% of SC and 48% of CA decisions took over 5 years); length of decisions; proportion of dismissed versus allowed cases; token-level mutual information analysis revealing salient words; and topic modelling identifying land disputes, state employment writs, and criminal proceedings as dominant themes. Discusses implications for understanding judicial impact and access to justice.

**5. Conclusion**
Summarises the contribution of CDTextLK as both a corpus and a preliminary empirical analysis. Acknowledges the findings as preliminary given the nascent stage of legal system digitisation in Sri Lanka, while emphasising that computational methods have already revealed or confirmed trends warranting further investigation and, in some cases, urgent reform. Notes that immediate next steps are clear and will build on the findings already highlighted.

**6. Future Work**
*[Section appears to require development]*

**7. References**

---

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
Produces: `CDTextLK-paper-draft.pdf` with:
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
Produces: `CDTextLK-paper-draft.docx` with:
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