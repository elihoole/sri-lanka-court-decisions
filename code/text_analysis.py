"""
Chi-Square and Mutual Information analysis for Sri Lanka Court Decisions.
Ported from 1_chi_mutual.ipynb.
"""

from typing import Any, Dict, Tuple

import numpy as np
import pandas as pd
from nltk.corpus import words
import nltk

from utils import load_stopwords, preprocess_text

# Download NLTK words if needed
try:
    words.words()
except LookupError:
    nltk.download('words')


def count_words_in_corpus(corpus_df: pd.DataFrame) -> Dict[str, Dict[str, int]]:
    """Count word occurrences per document in corpus."""
    word_count_dict = {}
    for doc_id, doc_tokens in enumerate(corpus_df['tokens']):
        doc_id = str(doc_id)
        for token in doc_tokens:
            if token in word_count_dict:
                if doc_id in word_count_dict[token]:
                    word_count_dict[token][doc_id] += 1
                else:
                    word_count_dict[token][doc_id] = 1
            else:
                word_count_dict[token] = {doc_id: 1}

    # Remove words appearing in fewer than 3 documents
    for token in list(word_count_dict.keys()):
        if len(word_count_dict[token]) < 3:
            word_count_dict.pop(token)

    return word_count_dict


def make_N_token_class_df(corpus_word_count_dict: Dict[str, Dict[str, int]]) -> Tuple[pd.DataFrame, int]:
    """Create N11/N01 dataframe from word counts."""
    data = []
    for token, doc_counts in corpus_word_count_dict.items():
        data.append({'token': token, 'doc_count': len(doc_counts)})

    df = pd.DataFrame(data)
    num_docs = max(int(d) for token_counts in corpus_word_count_dict.values()
                   for d in token_counts.keys()) + 1

    df = df.rename(columns={'doc_count': 'N_11'})
    df['N_01'] = num_docs - df['N_11']
    return df, num_docs


def calculate_mutual_information(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate mutual information for each token."""
    df = df.copy()
    df['sum_1'] = (df['N11']/df['N']) * np.log2(
        (df['N']*df['N11']) / ((df['N11'] + df['N10']) * (df['N01'] + df['N11']))
    )
    df['sum_2'] = (df['N01']/df['N']) * np.log2(
        (df['N']*df['N01']) / ((df['N01'] + df['N00']) * (df['N01'] + df['N11']))
    )
    df['sum_3'] = (df['N10']/df['N']) * np.log2(
        (df['N']*df['N10']) / ((df['N11'] + df['N10']) * (df['N00'] + df['N10']))
    )
    df['sum_4'] = (df['N00']/df['N']) * np.log2(
        (df['N']*df['N00']) / ((df['N01'] + df['N00']) * (df['N00'] + df['N10']))
    )

    for col in ['sum_1', 'sum_2', 'sum_3', 'sum_4']:
        df[col] = df[col].fillna(0)

    df['Mutual_Info'] = df['sum_1'] + df['sum_2'] + df['sum_3'] + df['sum_4']
    return df


def calculate_chi_squared(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate chi-squared statistic for each token."""
    df = df.copy()
    numerator = (df['N11'] + df['N10'] + df['N01'] + df['N00']) * \
                (df['N11']*df['N00'] - df['N10']*df['N01'])**2
    denominator = (df['N11'] + df['N01']) * (df['N11'] + df['N10']) * \
                  (df['N10'] + df['N00']) * (df['N01'] + df['N00'])

    df['Chi_Square'] = numerator / denominator
    return df


def run_text_analysis(df: pd.DataFrame) -> Dict[str, Any]:
    """Run chi-square and mutual information analysis.

    Args:
        df: DataFrame with 'text' and 'court' columns

    Returns:
        dict with analysis results
    """
    print("\nRunning Chi-Square and Mutual Information Analysis...")
    print("=" * 50)

    # Load stopwords and English word list
    stop_tokens = load_stopwords()
    english_words = set(words.words())
    print(f"Loaded {len(stop_tokens)} stopwords")
    print(f"English word list: {len(english_words)} words")

    # Preprocess texts
    print("Preprocessing texts...")
    df_analysis = df[['text', 'court']].copy()
    df_analysis['tokens'] = df_analysis['text'].apply(
        lambda x: preprocess_text(x, stop_tokens)
    )

    # Split by court
    sc_df = df_analysis[df_analysis['court'] == 'SC'].reset_index(drop=True)
    ca_df = df_analysis[df_analysis['court'] == 'CA'].reset_index(drop=True)

    print(f"SC documents: {len(sc_df)}")
    print(f"CA documents: {len(ca_df)}")

    # Count words
    print("Counting words...")
    sc_word_count = count_words_in_corpus(sc_df)
    ca_word_count = count_words_in_corpus(ca_df)

    # Create N matrices
    sc_N, num_docs_sc = make_N_token_class_df(sc_word_count)
    ca_N, num_docs_ca = make_N_token_class_df(ca_word_count)

    # Merge SC and CA
    sc_ca = pd.merge(sc_N, ca_N, how='outer', on='token')
    sc_ca = sc_ca.rename(columns={
        'N_11_x': 'N11', 'N_01_x': 'N10',
        'N_11_y': 'N01', 'N_01_y': 'N00'
    })

    # Fill NaN values
    sc_ca['N11'] = sc_ca['N11'].fillna(1)
    sc_ca['N01'] = sc_ca['N01'].fillna(1)
    sc_ca['N10'] = sc_ca['N10'].fillna(num_docs_sc - 1)
    sc_ca['N00'] = sc_ca['N00'].fillna(num_docs_ca - 1)

    # Filter to English words only
    sc_ca_filtered = sc_ca[sc_ca['token'].isin(english_words)].copy().reset_index(drop=True)
    print(f"Tokens after English filtering: {len(sc_ca_filtered)}")

    # Set N
    sc_ca_filtered['N'] = num_docs_sc + num_docs_ca

    # Calculate metrics
    mutual_info = calculate_mutual_information(sc_ca_filtered)
    chi_square = calculate_chi_squared(sc_ca_filtered)

    # Sort and get top results
    mi_sorted = mutual_info.sort_values(by='Mutual_Info', ascending=False).reset_index(drop=True)
    chi_sorted = chi_square.sort_values(by='Chi_Square', ascending=False).reset_index(drop=True)

    # Print results
    print("\n" + "=" * 50)
    print("TOP 20 TOKENS BY MUTUAL INFORMATION")
    print("=" * 50)
    for i, row in mi_sorted.head(20).iterrows():
        print(f"  {row['token']:15} MI: {row['Mutual_Info']:.6f}")

    print("\n" + "=" * 50)
    print("TOP 20 TOKENS BY CHI-SQUARE")
    print("=" * 50)
    for i, row in chi_sorted.head(20).iterrows():
        print(f"  {row['token']:15} Chi²: {row['Chi_Square']:.2f}")

    return {
        'mutual_info': mi_sorted,
        'chi_square': chi_sorted,
        'num_docs_sc': num_docs_sc,
        'num_docs_ca': num_docs_ca,
    }


if __name__ == "__main__":
    from data_loader import load_court_decisions

    df = load_court_decisions()
    results = run_text_analysis(df)

    # Save results
    results['mutual_info'].to_csv('mutual_info.csv', index=False)
    results['chi_square'].to_csv('chi_square.csv', index=False)
    print("\nResults saved to mutual_info.csv and chi_square.csv")
