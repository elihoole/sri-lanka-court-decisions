"""
LDA Topic Modeling for Sri Lanka Court Decisions.
Ported from 2_lda_analysis.ipynb.
"""

from typing import Any, Dict, List

import pandas as pd

from gensim import corpora, models

from utils import load_stopwords, preprocess_text


def find_topics_for_corpus(docs_set: List[List[str]], lda_model: models.LdaModel, dictionary: corpora.Dictionary) -> pd.DataFrame:
    """Calculate topic distribution for a corpus."""
    topics_for_corpus = dict()
    for doc in docs_set:
        doc_bow = dictionary.doc2bow(doc)
        topics_for_doc = lda_model.get_document_topics(doc_bow)
        for topic, prob in topics_for_doc:
            topics_for_corpus[topic] = topics_for_corpus.get(topic, 0) + prob

    topics_df = pd.DataFrame.from_dict(topics_for_corpus, orient="index")
    topics_df = topics_df.reset_index()
    topics_df = topics_df.rename(columns={"index": "topic", 0: "probability"})
    topics_df["probability"] = topics_df["probability"] / len(docs_set)
    return topics_df


def run_lda_analysis(df: pd.DataFrame, num_topics: int = 20, random_state: int = 0) -> Dict[str, Any]:
    """Run LDA topic modeling analysis.

    Args:
        df: DataFrame with 'text' and 'court' columns
        num_topics: Number of LDA topics
        random_state: Random seed for reproducibility

    Returns:
        dict with LDA model, dictionary, and topic analysis results
    """
    print("\nRunning LDA Analysis...")
    print("=" * 50)

    # Load stopwords
    stop_tokens = load_stopwords()
    print(f"Loaded {len(stop_tokens)} stopwords")

    # Prepare data
    df_lda = df[['text', 'court']].copy()
    df_lda['corpus_name'] = df_lda['court'].str.lower()

    # Preprocess texts
    print("Preprocessing texts...")
    df_lda['tokens'] = df_lda['text'].apply(lambda x: preprocess_text(x, stop_tokens))

    # Remove empty documents
    df_lda = df_lda[df_lda['tokens'].astype(bool)]
    print(f"Documents after preprocessing: {len(df_lda)}")

    # Create corpus
    doc_set = df_lda["tokens"].values.tolist()
    dictionary = corpora.Dictionary(doc_set)

    # Filter extremes
    dictionary.filter_extremes(no_below=20, no_above=0.5)
    print(f"Dictionary size after filtering: {len(dictionary)}")

    # Create bag of words corpus
    corpus = [dictionary.doc2bow(text) for text in doc_set]

    # Train LDA model
    print(f"Training LDA model with {num_topics} topics...")
    lda_model = models.ldamodel.LdaModel(
        corpus,
        num_topics=num_topics,
        passes=1,
        id2word=dictionary,
        random_state=random_state,
    )

    # Analyze topics by court
    sc_docs = df_lda[df_lda["corpus_name"] == "sc"]["tokens"].values.tolist()
    ca_docs = df_lda[df_lda["corpus_name"] == "ca"]["tokens"].values.tolist()

    print(f"\nSC documents: {len(sc_docs)}")
    print(f"CA documents: {len(ca_docs)}")

    sc_topics = find_topics_for_corpus(sc_docs, lda_model, dictionary)
    ca_topics = find_topics_for_corpus(ca_docs, lda_model, dictionary)

    # Find top topics
    merged = pd.merge(sc_topics, ca_topics, on="topic", how="inner")
    merged["prob_sum"] = merged["probability_x"] + merged["probability_y"]
    merged = merged.sort_values(by="prob_sum", ascending=False)

    top_3_topics = merged["topic"].iloc[:3].values.tolist()

    # Print results
    print("\n" + "=" * 50)
    print("TOP 3 TOPICS (SC and CA combined)")
    print("=" * 50)

    for topic_id in top_3_topics:
        words_with_probs = lda_model.show_topic(topic_id, topn=40)
        words = [word for word, prob in words_with_probs]
        print(f"\nTopic {topic_id}:")
        print(f"  Top 20 words: {', '.join(words[:20])}")

    # Topics unique to each court
    sc_top10 = sc_topics.sort_values(by="probability", ascending=False)["topic"].iloc[:10].tolist()
    ca_top10 = ca_topics.sort_values(by="probability", ascending=False)["topic"].iloc[:10].tolist()

    sc_unique = [t for t in sc_top10 if t not in ca_top10]
    ca_unique = [t for t in ca_top10 if t not in sc_top10]

    print("\n" + "=" * 50)
    print("TOPICS UNIQUE TO SC (not in CA top 10)")
    print("=" * 50)
    for topic_id in sc_unique:
        words = [w for w, p in lda_model.show_topic(topic_id, topn=20)]
        print(f"\nTopic {topic_id}: {', '.join(words)}")

    print("\n" + "=" * 50)
    print("TOPICS UNIQUE TO CA (not in SC top 10)")
    print("=" * 50)
    for topic_id in ca_unique:
        words = [w for w, p in lda_model.show_topic(topic_id, topn=20)]
        print(f"\nTopic {topic_id}: {', '.join(words)}")

    return {
        'model': lda_model,
        'dictionary': dictionary,
        'top_3_topics': top_3_topics,
        'sc_topics': sc_topics,
        'ca_topics': ca_topics,
        'sc_unique_topics': sc_unique,
        'ca_unique_topics': ca_unique,
    }


def print_topic_table(lda_result: Dict[str, Any], num_words: int = 40) -> None:
    """Print topic table in format suitable for paper (Table 4)."""
    lda_model = lda_result['model']
    top_topics = lda_result['top_3_topics']

    print("\n" + "=" * 70)
    print("TABLE 4: Top-3 LDA Topics with Top-40 Terms")
    print("=" * 70)

    topic_names = {
        0: "Land/Property",
        1: "Writs/Service",
        2: "Criminal"
    }

    for i, topic_id in enumerate(top_topics):
        words_with_probs = lda_model.show_topic(topic_id, topn=num_words)
        words = [word for word, prob in words_with_probs]

        print(f"\nTopic {i+1} ({topic_names.get(i, 'Unknown')}) - LDA Topic {topic_id}:")
        print("-" * 70)
        # Print in rows of 10
        for j in range(0, len(words), 10):
            print("  " + ", ".join(words[j:j+10]))


if __name__ == "__main__":
    from data_loader import load_court_decisions

    df = load_court_decisions()
    results = run_lda_analysis(df, num_topics=20, random_state=0)
    print_topic_table(results)
