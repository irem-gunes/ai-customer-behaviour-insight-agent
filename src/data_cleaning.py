import pandas as pd
import re


def clean_text(text):
    """
    Cleans review text by lowercasing and removing extra spaces/symbols.
    """
    if pd.isna(text):
        return ""

    text = str(text).lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()

    return text


def prepare_reviews(df):
    """
    Checks required columns and creates a cleaned review text column.
    """
    required_columns = ["review_text", "rating"]

    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    df = df.copy()
    
    df["review_text"] = df["review_text"].fillna("")
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
    df = df.dropna(subset=["rating"])

    df["clean_review"] = df["review_text"].apply(clean_text)

    return df
