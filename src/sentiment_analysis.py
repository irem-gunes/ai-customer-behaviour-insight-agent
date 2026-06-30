from functools import lru_cache

import ollama
from textblob import TextBlob


LLM_MODEL = "llama3.2"

_VALID_LABELS = ("Positive", "Negative", "Neutral")


def get_sentiment_score(text):
    """
    Returns sentiment polarity from -1 to +1.
    -1 = very negative
    0 = neutral
    +1 = very positive
    """
    return TextBlob(text).sentiment.polarity


def classify_sentiment(score):
    """
    Converts sentiment score into a label.
    """
    if score > 0.1:
        return "Positive"
    elif score < -0.1:
        return "Negative"
    else:
        return "Neutral"


def add_sentiment(df):
    """
    Adds sentiment score and sentiment label to the dataset.
    """
    df = df.copy()
    df["sentiment_score"] = df["clean_review"].apply(get_sentiment_score)
    df["sentiment_label"] = df["sentiment_score"].apply(classify_sentiment)

    return df


@lru_cache(maxsize=4096)
def get_llm_sentiment(text):
    """
    Classifies a review's sentiment using the local Ollama LLM.

    Unlike the rule-based TextBlob score, the LLM reads the sentence in
    context, so it can handle sarcasm, irony, and mixed sentiment.
    Returns one of: "Positive", "Negative", "Neutral".

    Results are cached so repeated identical reviews are not re-queried.
    """
    text = (text or "").strip()
    if not text:
        return "Neutral"

    prompt = (
        "Classify the sentiment of this customer review as exactly one word: "
        "Positive, Negative, or Neutral.\n"
        "Judge the reviewer's actual opinion, accounting for sarcasm, irony, "
        "and mixed sentiment - not just individual positive or negative words.\n\n"
        f'Review: "{text}"\n\n'
        "Answer with only one word."
    )

    response = ollama.chat(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 0},
    )

    answer = response["message"]["content"].strip().lower()

    # Robustly map the reply back to a valid label, even if the model adds words.
    for label in _VALID_LABELS:
        if label.lower() in answer:
            return label

    return "Neutral"