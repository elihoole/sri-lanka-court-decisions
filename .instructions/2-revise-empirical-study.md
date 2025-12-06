# Issues and Improvements for Section 2: Empirical Study

## 1. Terminology and Consistency
- **"Judgment" vs "Judgement":** Per your writing preferences in `CLAUDE.md`, replace all instances of "judgement" and "judgements" with "judgment" and "judgments" (the common-law usage).
- **Spelling of Names:**
  - Fix "Jaywardene" to "Jayawardene" (consistent with previous mention).
  - Fix "Abeywardene" to "Abeyawardene".
  - Fix "Rajapakse" to "Rajapaksa" (standard spelling for Mahinda and Gotabaya Rajapaksa).
- **Case Names:**
  - Ensure consistency between "Plantation Point" and "Plaintain Point".
  - Ensure all case names are italicized consistently (e.g., *Leeda Violet*, *Velasquez Rodriguez v Honduras*).

## 2. Typos and Formatting Errors
- **Backslashes:** Remove backslashes before periods (e.g., `2022\.`, `2011\.`, `1802\.`).
- **Spacing:**
  - Add space after footnotes (e.g., `[^13]Tiruchelvam`).
  - Remove extra spaces before periods (e.g., `1978 .`, `1799 .`).
  - Fix `*The Business of the Supreme Court: A Study in the Federal Judicial System .[^4]*` (move period/footnote inside or outside consistently, remove extra space).
- **Typos:**
  - "goine" -> "gone".
  - "superior during this period" -> "superior courts during this period".
  - "counter factual" -> "counterfactual".
- **Headers:**
  - The header "**Courts**" is just bold text. Convert it to a proper markdown header (e.g., `### Courts`).
  - The final header "3. ## **Limitations**" seems erroneous. It should likely be a subsection or integrated into the previous section.
- **Strikethrough:** Remove the strikethrough text in the "Legal system digitisation" section (`~~There has been...~~`) if it is not meant to be there.

## 3. Writing Style (Precision and Flow)
- **Tighten Wordy Phrases:**
  - *Current:* "It is only recently and exceptionally that the study of jurisprudence of the Sri Lankan apex courts been supplemented with a quantitative analysis of the same."
  - *Suggestion:* "Quantitative analysis of Sri Lankan apex court jurisprudence is a recent and exceptional development."
  - *Current:* "The quantitative and external perspective that we offer here... can be meaningfully interpreted only when combined with a doctrinal analysis..."
  - *Suggestion:* "This quantitative perspective complements, rather than replaces, doctrinal analysis..."
- **Tone:**
  - "purportedly impeached" -> Consider "controversially impeached" or simply "impeached" to maintain a neutral academic tone, unless the legal validity is the specific point being argued.

## 4. Structure and Organization
- **Section Ordering:**
  - The "Use of Computational Methods" section interrupts the flow between the general "Empirical Study" intro and the "Legal System" background. Consider moving it to follow the "Legal System" and "Judicial Branch" sections, immediately before the "CDTextLK" section (Section 3), or integrating it into the Introduction (Section 1) if it's general theory. However, if it frames the *methodology* of this specific empirical study, it can stay, but transition better.
- **Redundancy:**
  - The "Superior Courts" section repeats some historical details found in "The Legal System". Consolidate these to avoid repetition.
- **Tables:**
  - The tables in "Judicial Branch 2012 to 2022" have empty rows for "Writs judgments". Either populate them or remove the rows if data is unavailable/not relevant.

## 5. Specific Content Queries
- **"3. ## Limitations"**: This section needs to be developed (not just a leftover). It must address the scope of judicial outputs:
    - **Variety of Orders:** Courts issue interlocutory orders, interim relief, enjoining orders, and final judgments. A complete picture requires analyzing all of these, but this study is limited to "judgments."
    - **Inconsistent Terminology:** There is inconsistency in how courts distinguish between "orders" and "judgments."
    - **Data Source Limitation:** The Court of Appeal website separates "judgments" and "orders," and often *final* orders are categorized under "orders," meaning they might be missed if only the "judgments" section is scraped. This limitation needs to be woven seamlessly into the discussion on digitization and data availability.
- **Missing Citations:** Check if *Priyani Soysa v Arsecularatne* needs a citation.

## 6. Action Plan for Revision
1.  **Apply Global Replacements:** Fix "judgment", names, and backslashes.
2.  **Refine Prose:** Edit for precision and remove passive/wordy constructions.
3.  **Fix Formatting:** Correct headers and footnote spacing.
4.  **Restructure:** Ensure a logical flow from the history of the legal system to the specific context of the 2012-2022 period.

## 7. Punctuation and Formatting
- **Dashes:** Ensure consistent use of spaced en-dashes (–) for parenthetical insertions, as per your preference.
- **Footnotes:** Ensure all footnotes are preserved and correctly numbered during the revision, as this will be ported to DOCX.
