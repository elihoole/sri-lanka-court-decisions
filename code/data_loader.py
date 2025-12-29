"""
Data loader for Sri Lanka Court Decisions dataset.
Loads from HuggingFace and derives analysis columns.
"""

from typing import Optional

import pandas as pd
from datasets import load_dataset

from utils import tokenize_simple


def extract_casefiled_year(standard_casenumber: Optional[str]) -> Optional[int]:
    """Extract the year case was filed from standard_casenumber.

    e.g., "sc-fr-123/2015" -> 2015
    """
    if pd.isna(standard_casenumber) or not standard_casenumber:
        return None
    try:
        year_str = standard_casenumber.split('/')[-1]
        year = int(year_str)
        if 1900 <= year <= 2100:
            return year
        return None
    except (ValueError, IndexError):
        return None


def load_court_decisions() -> pd.DataFrame:
    """Load dataset from HuggingFace and derive analysis columns.

    Returns:
        pd.DataFrame with columns:
        - court: 'SC' or 'CA'
        - standard_casenumber: standardized case number
        - link: URL to PDF
        - text: full decision text
        - decision_year: year decision was published
        - is_fr: True if SC Fundamental Rights case
        - is_writ: True if writ application
        - casefiled_year: year case was filed
        - time_to_decision: years between filing and decision
        - word_count: number of words in decision
    """
    print("Loading dataset from HuggingFace...")
    dataset = load_dataset("elihoole/sri-lanka-court-decisions", split="train")
    df = dataset.to_pandas()
    print(f"Loaded {len(df)} decisions")

    # Derive is_fr (Fundamental Rights cases)
    df['is_fr'] = df['standard_casenumber'].apply(
        lambda x: 'fr' in x.lower() if pd.notna(x) and x else False
    )

    # Derive is_writ (Writ applications)
    df['is_writ'] = df['standard_casenumber'].apply(
        lambda x: 'writ' in x.lower() if pd.notna(x) and x else False
    )

    # Extract casefiled_year from case number
    df['casefiled_year'] = df['standard_casenumber'].apply(extract_casefiled_year)

    # Calculate time_to_decision
    df['time_to_decision'] = df['decision_year'] - df['casefiled_year']
    # Clamp negative values to 0
    df['time_to_decision'] = df['time_to_decision'].apply(
        lambda x: max(0, x) if pd.notna(x) else None
    )

    # Calculate word_count
    df['word_count'] = df['text'].apply(lambda x: len(tokenize_simple(x)))

    # Print summary
    print(f"\nDataset Summary:")
    print(f"  SC cases: {len(df[df['court'] == 'SC'])}")
    print(f"  CA cases: {len(df[df['court'] == 'CA'])}")
    print(f"  FR cases (SC): {df['is_fr'].sum()}")
    print(f"  Writ cases: {df['is_writ'].sum()}")
    print(f"  Decision years: {int(df['decision_year'].min())} - {int(df['decision_year'].max())}")
    print(f"  Avg word count (SC): {df[df['court'] == 'SC']['word_count'].mean():.0f}")
    print(f"  Avg word count (CA): {df[df['court'] == 'CA']['word_count'].mean():.0f}")

    return df


def get_sc_cases(df: pd.DataFrame) -> pd.DataFrame:
    """Filter to Supreme Court cases only."""
    return df[df['court'] == 'SC'].copy()


def get_ca_cases(df: pd.DataFrame) -> pd.DataFrame:
    """Filter to Court of Appeal cases only."""
    return df[df['court'] == 'CA'].copy()


def get_fr_cases(df: pd.DataFrame) -> pd.DataFrame:
    """Filter to Fundamental Rights cases only (SC)."""
    return df[df['is_fr'] == True].copy()


def get_writ_cases(df: pd.DataFrame) -> pd.DataFrame:
    """Filter to writ application cases."""
    return df[df['is_writ'] == True].copy()


if __name__ == "__main__":
    # Test the data loader
    df = load_court_decisions()
    print(f"\nColumns: {list(df.columns)}")
    print(f"\nSample SC case:")
    print(df[df['court'] == 'SC'].iloc[0][['court', 'standard_casenumber', 'decision_year',
                                           'is_fr', 'casefiled_year', 'time_to_decision', 'word_count']])
    print(f"\nSample CA case:")
    print(df[df['court'] == 'CA'].iloc[0][['court', 'standard_casenumber', 'decision_year',
                                           'is_writ', 'casefiled_year', 'time_to_decision', 'word_count']])
