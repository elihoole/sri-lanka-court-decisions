# The Dataset: \texttt{SriLankaCourtDecisions} {#sec:dataset}

We compiled the \texttt{SriLankaCourtDecisions} dataset by scraping the official websites of Sri Lanka's Supreme Court and Court of Appeal for judgments delivered between 1 January 2012 and 31 December 2022. The resulting corpus comprises 1,278 Supreme Court judgments and 7,314 Court of Appeal judgments. Data availability determined our choice of time period. The dataset is available on HuggingFace.[^note_huggingface] The GitHub repository contains the analysis code to reproduce all figures, tables, LDA topic modelling, and chi-square/mutual information analyses, as well as the source files and build scripts for this paper.[^note_github]

The constitution establishes distinct forums for public law remedies. Article 140 confers on the Court of Appeal jurisdiction to issue prerogative writs—certiorari, mandamus, prohibition, and others—for judicial review of administrative action, tribunal decisions, and jurisdictional errors. Article 126 vests the Supreme Court with exclusive jurisdiction over fundamental rights petitions alleging constitutional violations. The Supreme Court’s original writ jurisdiction, by contrast, is narrowly circumscribed: Article 104H, for instance, limits such jurisdiction to election-related matters.

The empirical distribution confirms this constitutional design. Of the 1,278 Supreme Court decisions in the dataset, only 4 (0.3%) were original writ petitions under Article 104H. The Court of Appeal, by contrast, issued 1,741 writ decisions (23% of its docket) during the same period. In original writ jurisdiction, the Court of Appeal handles 435 times more cases than the Supreme Court. This stark disparity reflects the constitutional allocation of writ jurisdiction to the Court of Appeal as the primary forum for administrative law and judicial review.


## Data Collection and Processing

Scraping the two court websites presented minimal technical barriers, as both are static sites without rate limiting or IP-blocking mechanisms.[^note_court_websites] The primary challenges were extended server downtimes that interrupted scraping routines and expired SSL certificates that generated runtime warnings. We converted the downloaded PDF files using PDFMiner[^note_pdfminer] with default parameters, preserving document structure while extracting text content. A small number of judgments (fewer than 10 across the entire collection) required Optical Character Recognition (OCR) conversion; we excluded these to maintain consistency in text extraction methodology and data quality.

Both websites contained substantial duplicate entries. Following deduplication based on case number and decision date, the corpus comprised 1,278 Supreme Court judgments and 7,314 Court of Appeal judgments, as shown in Table 1. The deduplication process identified duplicates through exact matching of case numbers combined with decision dates; in instances where the same case number appeared with different dates, we retained the entry with the more complete judgment text.

*Table 1: \texttt{SriLankaCourtDecisions} dataset composition and descriptive statistics (SD = standard deviation)*

| Court | Number of judgments | Mean word count (SD) |
|:---- |:---- |:---- |
| Supreme Court | 1,278 | 3,646 (3,038) |
| Court of Appeal | 7,314 | 1,688 (2,091) |
| **Full corpus** | **8,592** | **1,979 (2,361)** |

## Dataset Structure

The dataset contains eight fields for each judgment: decision date (str), case number (str), court name (str), case filed year (str), judge (str), bench (str), link to original decision (str), and decision text (str). The ‘judge’ field identifies the justice who authored the judgment, while ‘bench’ lists all justices who constituted the bench during hearings. These fields enable analysis of individual judicial contribution and bench composition patterns over time.

Extracting structured data from the court websites presented several challenges. Case numbers follow non-standardised formats that vary by court, case type, and year, requiring custom parsing rules. Judge and bench information, while generally present, appears inconsistently across judgments – sometimes in formal headers, sometimes within the judgment text itself. We extracted this information using a combination of regular expressions and manual validation of a sample subset.

## Descriptive Statistics and Characteristics

The word count statistics in Table 1 reveal marked differences between the two courts. Supreme Court judgments average 3,646 words with substantial variation (SD = 3,038), reflecting the court's role in addressing complex constitutional matters and questions of law alongside its appellate functions. Court of Appeal judgments average 1,688 words (SD = 2,091), consistent with a higher-volume appellate court addressing a broader range of routine matters. The high standard deviations in both courts indicate considerable heterogeneity in judgment length, ranging from brief orders to extensive reasoned judgments spanning dozens of pages.

The numerical dominance of Court of Appeal judgments (7,314 versus 1,278) reflects the courts’ different positions in Sri Lanka’s judicial hierarchy and their distinct jurisdictional mandates, as discussed in @sec:empirical. This 5.7:1 ratio has implications for understanding the relative contribution of each court to the development of case law, a pattern we explore further in @sec:insights.

[^note_huggingface]: The dataset is available at [huggingface.co/datasets/elihoole/sri-lanka-court-decisions](https://huggingface.co/datasets/elihoole/sri-lanka-court-decisions).

[^note_github]: The repository is available at [github.com/elihoole/SriLankaCourtDecisions](https://github.com/elihoole/SriLankaCourtDecisions).

[^note_court_websites]: The official websites are available at [supremecourt.lk](https://supremecourt.lk/) and [courtofappeal.lk](https://courtofappeal.lk/). Scraping was conducted between February 2023 and April 2023 using custom Python scripts.

[^note_pdfminer]: PDFMiner.six version 20221105 was used for PDF text extraction.