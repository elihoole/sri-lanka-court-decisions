#!/usr/bin/env python3
"""
Main script for Sri Lanka Court Decisions Analysis.

This script reproduces the analysis from the paper:
- Loads dataset from HuggingFace
- Generates plots
- Runs LDA topic modeling
- Performs chi-square and mutual information analysis

Usage:
    python main.py [--plots] [--lda] [--text] [--all]
"""

import argparse
import sys


def main() -> None:
    parser = argparse.ArgumentParser(
        description='Sri Lanka Court Decisions Analysis'
    )
    parser.add_argument('--plots', action='store_true',
                        help='Generate all plots')
    parser.add_argument('--lda', action='store_true',
                        help='Run LDA topic modeling')
    parser.add_argument('--text', action='store_true',
                        help='Run chi-square and mutual information analysis')
    parser.add_argument('--all', action='store_true',
                        help='Run all analyses')

    args = parser.parse_args()

    # If no arguments, show help and run all
    if not any([args.plots, args.lda, args.text, args.all]):
        print("No specific analysis selected. Running all analyses.\n")
        args.all = True

    # Load data
    from data_loader import load_court_decisions
    print("=" * 60)
    print("SRI LANKA COURT DECISIONS ANALYSIS")
    print("=" * 60)
    df = load_court_decisions()

    # Run selected analyses
    if args.plots or args.all:
        print("\n")
        from plots import generate_all_plots
        generate_all_plots(df)

    if args.lda or args.all:
        print("\n")
        from lda_analysis import run_lda_analysis, print_topic_table
        results = run_lda_analysis(df, num_topics=20, random_state=0)
        print_topic_table(results)

    if args.text or args.all:
        print("\n")
        from text_analysis import run_text_analysis
        results = run_text_analysis(df)
        results['mutual_info'].to_csv('mutual_info.csv', index=False)
        results['chi_square'].to_csv('chi_square.csv', index=False)
        print("\nResults saved to mutual_info.csv and chi_square.csv")

    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
