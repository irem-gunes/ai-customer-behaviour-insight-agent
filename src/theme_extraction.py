from collections import Counter


THEME_KEYWORDS = {
    "Cleanliness issues": [
        "dirty", "unclean", "stain", "stains", "dust", "dusty",
        "smell", "smelly", "mold", "mould", "bathroom dirty"
    ],
    "Poor service": [
        "rude", "unhelpful", "staff", "reception", "front desk",
        "service", "ignored", "unfriendly"
    ],
    "Room quality issues": [
        "room", "small room", "old room", "dated", "broken",
        "bed", "uncomfortable", "air conditioning", "ac", "heating"
    ],
    "Noise and sleep problems": [
        "noise", "noisy", "loud", "sleep", "could not sleep",
        "thin walls", "traffic"
    ],
    "Value for money concerns": [
        "expensive", "overpriced", "not worth", "price", "cost",
        "value", "money"
    ],
    "Location problems": [
        "location", "far", "distance", "hard to find", "transport",
        "parking"
    ],
    "Booking or check-in problems": [
        "booking", "check in", "check-in", "reservation",
        "waiting", "queue", "late check in"
    ],
    "Breakfast or food issues": [
        "breakfast", "food", "restaurant", "buffet", "coffee",
        "cold food"
    ]
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


def get_example_reviews(df, theme, max_examples=3):
    """
    Returns example reviews where a theme was detected.
    """
    matching_reviews = df[df["themes"].apply(lambda themes: theme in themes)]

    return matching_reviews["review_text"].head(max_examples).tolist()
