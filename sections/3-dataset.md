
# **3\. CDTextLK: Court Decision Texts Sri Lanka Dataset**

*CDTextLK dataset at a glance; SD \= standard deviation.*

|  | Number of | Mean token |
| :---- | :---- | :---- |
|  | decisions | count (SD) |
| Supreme Court | 1278 | 3646 (3038) |
| Court of Appeal | 7314 | 1688 (2091) |
| **Full corpus** | **8592** | **1979 (2361)** |

For our Court Decision Texts Sri Lanka Dataset (CDTextLK) we scraped the official websites of the Supreme Court and the Court of Appeal, for the time period starting from 1 January 2012 to 31 December 2022\. The choice of the time period owed entirely to data availability. Although the Supreme Court website lists decisions starting from the year 2009, data is incomplete for the years 2009-2011. This is likely the result of backdated uploading. The Court of Appeal entries start from 2012\.

Scraping the two websites was a relatively straightforward exercise as they are static websites and do not implement rate limiting or IP-blocking. The only challenges worth noting with respect to scraping are the websites’ long downtimes which often crashed scraping routines and their expired SSL certificates which throw up numerous runtime warnings. We converted downloaded PDF files with PDFMiner and ignored the few decisions (\< 10 in the total collection) that required OCR conversion. We found a significant number of duplicate entries in both websites. Upon deduplication based on case number and decision date, we were left with 1278 Supreme Court decisions and 7314 Court of Appeal decisions (see: Table [1](#bookmark=id.scyamhoh91vz)).

The dataset has the following columns: decision date (str), case number (str), court name (str), case filed year (str), judge (str), bench (str), link to original decision (str), and decision text (str). The column ‘judge’ refers to the justice who wrote the decision while ‘bench’ consists of all the justices who constituted the bench during the hearings.

