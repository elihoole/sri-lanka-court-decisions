## Git Workflow

- **Commit frequently**: After completing a logical unit of work (e.g., fixing a section, adding bib entries, converting citations), commit without prompting
- **Use feature branches**: Create branches for significant changes (e.g., `fix/footnote-renumbering`)
- **Commit message format**: Use clear, descriptive messages with bullet points for multiple changes
- **Don't push without asking**: Commits are local until explicitly asked to push

## About the project

Paper: *First Steps: Empirical Study of Sri Lanka's Apex Courts with a Focus on Public Law Litigation* (Elijah Hoole, Dinesha Samararatne, Yanitra Kumaraguru), built from Markdown with Pandoc. The Markdown in `content/` is the source of truth; Word documents exchanged with co-authors are review copies.

- `content/` — one Markdown file per section, combined in `sort -V` order (`01-abstract.md` … `9-references.md`)
- `config/` — `chicago.csl`, `reference.docx` (Word template), LaTeX includes (`fonts.tex`, `bibliography.tex`, `title-page*.tex`, …), `title-page.md` (DOCX title page), Lua filters
- `references.bib` — all citations
- `figures/` — plots referenced from `content/4-analysis.md`
- `code/` — analysis code reproducing the figures and tables (see README)
- `review/` — co-author review rounds (decision sheets, CriticMarkup renderings of returned docx files)
- `output/` — built files and the docx files returned by co-authors

## Building

```bash
./build-pdf.sh         # A4 PDF  -> output/EmpiricalStudies_300526_EH_Settled_25102026.pdf
./build-docx.sh        # Word    -> output/EmpiricalStudies_300526_EH_Settled_25102026.docx
./build-mobile-pdf.sh  # Phone   -> output/EmpiricalStudies_300526_mobile_EH_Settled_25102026.pdf
```

- Output names are set by `OUTPUT=` at the top of each script; update the version label when a new draft is settled. Only the A4 PDF is tracked in git.
- Needs pandoc >= 3.1.8 (pandoc-crossref 0.3.17 is built against 3.1.8; installed user-locally in `~/.local/bin`), pandoc-crossref and pdflatex.
- After building, verify: no `??` or raw `@sec:`/`@fig:` in the output, and footnote/figure numbering is continuous.

## Writing conventions

- **Citations**: Chicago 18th notes-bibliography via citeproc. Use `[@citekey, p. 12]` for sources (generates the footnote and a bibliography entry); use named footnotes `[^note_x]` only for explanatory comments. Inside a footnote, citeproc wraps `[@…]` in parentheses, so for a footnote that is just a list of sources use a citation with a prefix: `[Some examples include: @a; @b]`. Give printed page numbers, not e-book page numbers.
- **Cross-references**: `@sec:label`, `@fig:label` (pandoc-crossref). Headings that are referenced need `{#sec:label}`.
- **No raw LaTeX in body text**: the DOCX build drops it silently (this is how `\texttt{…}` once vanished). Write the dataset name as inline code: `` `SriLankaCourtDecisions` ``.
- **Terminology**: "superior courts" for the Supreme Court and Court of Appeal together; "apex court" only for the Supreme Court alone (or the Privy Council before 1971). Spelling "judgment".
- **Corpus completeness**: do not claim that all judgments were published online; the Supreme Court website has a few judgments from 2009, the Court of Appeal from 2011, and from 2012 the volume very likely reflects full output but is unverified.

## Co-author review workflow

1. Convert the returned docx against the last settled baseline: `pandoc X.docx --track-changes=all` (render tracked changes and comments), and diff the baseline with tracked changes accepted against the returned doc to catch untracked (silent) edits. Compare whole paragraphs; truncated line diffs miss edits.
2. Write a decision sheet in `review/` (numbered items, recommendation, tick boxes) and let the user settle it before editing `content/`.
3. Open questions for co-authors go into the Markdown as Word comments:
   `[Dinesha: …]{.comment-start id="901" author="Elijah Hoole" date="…"}anchor text[]{.comment-end id="901"}` (numeric ids). They appear as Word comments in the DOCX; `config/review-comments.lua` strips them from the PDF builds. Remove a comment once it is resolved.

## Open items (as of 25 October 2026)

- Dinesha to confirm the Talagala (2026) citation, including the start page (192), and to supply the publisher for Sunil Cooray, *Principles of Administrative Law in Sri Lanka* (1998). Both are Word comments in `content/5-insights.md`.
