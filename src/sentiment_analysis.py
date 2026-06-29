from textblob import TextBlob


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