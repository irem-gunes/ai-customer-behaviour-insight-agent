from collections import Counter


THEME_KEYWORDS = {
    "Delivery delays": ["late", "delay", "delayed", "waiting", "long delivery"],
    "Poor communication": ["no update", "communication", "nobody replied", "no apology"],
    "Refund issues": ["refund", "money back", "charged", "charged twice"],
    "Customer support": ["support", "customer service", "rude", "unhelpful"],
    "App or website friction": ["app", "website", "checkout", "confusing", "too many steps"],
    "Tracking issues": ["tracking", "order status", "status"],
}


def detect_themes(text):
    """
    Detects themes based on keyword matching.
    """
    detected = []

    for theme, keywords in THEME_KEYWORDS.items():
        for keyword in keywords:
            if keyword in text:
                detected.append(theme)
                break

    return detected


def add_themes(df):
    """
    Adds detected themes to each review.
    """
    df = df.copy()
    df["themes"] = df["clean_review"].apply(detect_themes)

    return df


def summarise_themes(df):
    """
    Counts how often each theme appears.
    """
    all_themes = []

    for themes in df["themes"]:
        all_themes.extend(themes)

    theme_counts = Counter(all_themes)

    return theme_counts


def get_example_reviews(df, theme, max_examples=2):
    """
    Returns example reviews where a theme was detected.
    """
    matching_reviews = df[df["themes"].apply(lambda themes: theme in themes)]

    return matching_reviews["review_text"].head(max_examples).tolist()
