# Sri Lanka Court Decisions Analysis

Analysis code for the Sri Lanka Court Decisions dataset, reproducing results from the research paper.

## Dataset

The dataset is hosted on HuggingFace: [elihoole/sri-lanka-court-decisions](https://huggingface.co/datasets/elihoole/sri-lanka-court-decisions)

- **8,592 court decisions** (2012-2022)
- Supreme Court: 1,278 decisions
- Court of Appeal: 7,314 decisions

## Setup

```bash
# Install dependencies
uv sync

# Or with pip
pip install datasets pandas matplotlib seaborn scienceplots gensim nltk
```

## Usage

```bash
# Run all analyses
uv run python3 code/main.py

# Run specific analyses
uv run python3 code/main.py --plots   # Generate plots only
uv run python3 code/main.py --lda     # LDA topic modeling only
uv run python3 code/main.py --text    # Chi-square/MI analysis only
```

## Output

### Plots (saved to `images/`)

| File | Description |
|------|-------------|
| `num_decisions_per_year.png` | Decisions per year by court |
| `time_to_decision.png` | Time to decision distribution |
| `image_no_6_fr_delay_distribution.png` | FR delay distribution |
| `image_no_8_sc_fr_vs_ca_writ_delay_distribution.png` | SC FR vs CA Writ comparison |
| `length_of_decision.png` | Decision length histogram |
| `image_no_11_avg_words_by_decision_type.png` | Avg words by type over time |
| `writ_jurisdiction_ratio.png` | SC vs CA writ jurisdiction |

### LDA Topics

Top 3 topics identified:
1. **Land/Property**: defendant, plaintiff, land, district, title, deed, possess
2. **Writs/Service**: decision, writ, office, service, public, board, authority
3. **Criminal**: accused, sentence, trial, witness, police, prosecute, convict

### Text Analysis

- `mutual_info.csv` - Tokens ranked by mutual information
- `chi_square.csv` - Tokens ranked by chi-square statistic

## Key Statistics

| Metric | Value |
|--------|-------|
| SC average word count | 3,646 |
| CA average word count | 1,688 |
| FR mean time to decision | 4.1 years |
| FR median time to decision | 4.0 years |

## Project Structure

```
code_to_push/
├── code/
│   ├── main.py           # Entry point
│   ├── data_loader.py    # Load from HuggingFace
│   ├── plots.py          # Plotting functions
│   ├── lda_analysis.py   # LDA topic modeling
│   ├── text_analysis.py  # Chi-square & mutual info
│   ├── utils.py          # Shared utilities
│   └── stopwords/        # Stopword files
│       ├── englishST.txt
│       ├── stop_words.txt
│       └── legalstopwords.txt
├── images/               # Generated plots
├── pyproject.toml        # Dependencies
└── README.md
```

## License

MIT
