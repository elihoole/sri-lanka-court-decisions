

# **CDTextLK: Court Decision Texts Sri Lanka Dataset**

We compiled the CDTextLK dataset by scraping the official websites of Sri Lanka's Supreme Court and Court of Appeal for judgments delivered between 1 January 2012 and 31 December 2022. The resulting corpus comprises 1278 Supreme Court judgments and 7314 Court of Appeal judgments. Data availability determined our choice of time period. Although the Supreme Court website lists judgments from 2009 onwards, the years 2009–2011 contain incomplete data, likely due to retrospective uploading practices. The Court of Appeal entries begin in 2012.

## Data Collection and Processing

Scraping the two court websites presented minimal technical barriers, as both are static sites without rate limiting or IP-blocking mechanisms.[^scraping-note] The primary challenges were extended server downtimes that interrupted scraping routines and expired SSL certificates that generated runtime warnings. We converted the downloaded PDF files using PDFMiner[^pdfminer] with default parameters, preserving document structure while extracting text content. A small number of judgments (fewer than 10 across the entire collection) required OCR conversion; we excluded these to maintain consistency in text extraction methodology and data quality.

[^scraping-note]: The official websites are available at [Supreme Court URL] and [Court of Appeal URL]. Scraping was conducted between [dates] using [tool/library name].

[^pdfminer]: PDFMiner.six version [X.X] was used for PDF text extraction.

Both websites contained substantial duplicate entries. Following deduplication based on case number and decision date, the corpus comprised 1278 Supreme Court judgments and 7314 Court of Appeal judgments, as shown in @tbl:dataset-composition. The deduplication process identified duplicates through exact matching of case numbers combined with decision dates; in instances where the same case number appeared with different dates, we retained the entry with the more complete judgment text.

: CDTextLK dataset composition and descriptive statistics (SD = standard deviation) {#tbl:dataset-composition}

|  | Number of | Mean token |
| :---- | :---- | :---- |
|  | judgments | count (SD) |
| Supreme Court | 1278 | 3646 (3038) |
| Court of Appeal | 7314 | 1688 (2091) |
| **Full corpus** | **8592** | **1979 (2361)** |

## Dataset Structure

The dataset contains eight fields for each judgment: decision date (str), case number (str), court name (str), case filed year (str), judge (str), bench (str), link to original decision (str), and decision text (str). The 'judge' field identifies the justice who authored the judgment, while 'bench' lists all justices who constituted the bench during hearings. These fields enable analysis of individual judicial contribution and bench composition patterns over time.

Extracting structured data from the court websites presented several challenges. Case numbers follow non-standardised formats that vary by court, case type, and year, requiring custom parsing rules. Judge and bench information, while generally present, appears inconsistently across judgments – sometimes in formal headers, sometimes within the judgment text itself. We extracted this information using a combination of regular expressions and manual validation of a sample subset.

## Descriptive Statistics and Characteristics

The token count statistics in Table 1 reveal marked differences between the two courts. Supreme Court judgments average 3646 tokens with substantial variation (SD = 3038), reflecting the court's role in addressing complex constitutional matters and questions of law alongside its appellate functions. Court of Appeal judgments average 1688 tokens (SD = 2091), consistent with a higher-volume appellate court addressing a broader range of routine matters. The high standard deviations in both courts indicate considerable heterogeneity in judgment length, ranging from brief orders to extensive reasoned judgments spanning dozens of pages.

The numerical dominance of Court of Appeal judgments (7314 versus 1278) reflects the courts' different positions in Sri Lanka's judicial hierarchy and their distinct jurisdictional mandates, as discussed in Section 2. This 5.7:1 ratio has implications for understanding the relative contribution of each court to the development of case law, a pattern we explore further in Section 4.

## Limitations and Scope

Several limitations warrant acknowledgement. First, the dataset's temporal scope (2012–2022) represents only a fraction of Sri Lankan legal history and excludes significant earlier periods that shaped the country's jurisprudence. Second, the corpus captures only those judgments that the courts chose to publish on their official websites; unpublished judgments, orders, and procedural decisions remain beyond our scope. Third, our exclusion of OCR-requiring documents, while maintaining data quality, may introduce slight bias if these judgments differ systematically from those successfully converted.

Fourth, the dataset reflects the limitations of the courts' digitisation practices discussed in Section 2. Missing metadata fields, non-standardised case numbering, and inconsistent formatting constrain certain types of analysis. Fifth, our scraping captured judgments as they appeared at the time of collection; subsequent corrections or amendments to published judgments would not be reflected in the dataset. Finally, while we conducted deduplication and quality checks, we cannot guarantee that all duplicates were identified or that all extracted text perfectly represents the original PDF documents.

Despite these limitations, CDTextLK represents the most comprehensive corpus of Sri Lankan appellate judgments assembled to date and provides sufficient coverage for meaningful empirical analysis of recent trends in the Superior Courts.

