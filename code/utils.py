"""
Shared utilities for Sri Lanka Court Decisions analysis.
"""

import re
from pathlib import Path
from typing import List, Set

import pandas as pd
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import nltk

# Download NLTK data if needed
try:
    stopwords.words('english')
except LookupError:
    nltk.download('stopwords')

# Constants
STOPWORDS_DIR = 'stopwords'
STOPWORD_FILES = ['englishST.txt', 'stop_words.txt', 'legalstopwords.txt']
FIGURE_DPI = 600
FIGURE_SIZE_DEFAULT = (8, 6)
FIGURE_SIZE_WIDE = (10, 6)

# Plot colors
COLORS = {
    'sc': '#f1935d',       # Orange - Supreme Court
    'ca': '#53a2d0',       # Blue - Court of Appeal
    'sc_fr': '#f1935d',    # Orange - SC FR cases
    'ca_writ': '#e74c3c',  # Red - CA Writ cases
    'sc_all': '#9b59b6',   # Purple - SC All
    'ca_all': '#2ecc71',   # Green - CA All
}

# Global stemmer (reused across calls)
_stemmer = PorterStemmer()
_token_pattern = re.compile(r'[a-z]+')


def get_code_dir() -> Path:
    """Get the directory containing the code files."""
    return Path(__file__).parent


def load_stopwords() -> Set[str]:
    """Load all stopword lists and return as a set.

    Combines NLTK English stopwords with custom stopword files.

    Returns:
        Set of stopword strings.
    """
    code_dir = get_code_dir()

    # NLTK stopwords
    stop_tokens = set(stopwords.words('english'))

    # Load custom stopword files from stopwords/ directory
    for filename in STOPWORD_FILES:
        filepath = code_dir / STOPWORDS_DIR / filename
        if filepath.exists():
            with open(filepath, 'r', encoding='utf-8') as f:
                tokens = {line.strip() for line in f.readlines() if line.strip()}
                stop_tokens.update(tokens)

    return stop_tokens


def preprocess_text(
    text: str,
    stop_tokens: Set[str] = None,
    stem: bool = True,
    min_token_length: int = 3
) -> List[str]:
    """Preprocess text: lowercase, tokenize, remove stopwords, optionally stem.

    Args:
        text: Input text to preprocess.
        stop_tokens: Set of stopwords to remove. If None, loads default stopwords.
        stem: Whether to apply Porter stemming.
        min_token_length: Minimum token length to keep.

    Returns:
        List of preprocessed tokens.
    """
    if pd.isna(text) or not text:
        return []

    if stop_tokens is None:
        stop_tokens = load_stopwords()

    text = text.lower()
    tokens = _token_pattern.findall(text)
    tokens = [t for t in tokens if len(t) >= min_token_length and t not in stop_tokens]

    if stem:
        tokens = [_stemmer.stem(t) for t in tokens]

    return tokens


def tokenize_simple(text: str) -> List[str]:
    """Simple tokenization without stopword removal or stemming.

    Used for word count calculations.

    Args:
        text: Input text.

    Returns:
        List of lowercase alphabetic tokens.
    """
    if pd.isna(text) or not text:
        return []
    return _token_pattern.findall(text.lower())
