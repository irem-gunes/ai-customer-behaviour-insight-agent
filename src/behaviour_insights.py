BEHAVIOURAL_INSIGHTS = {
    "Delivery delays": "Customers may tolerate delays better when expectations are managed. The issue is likely uncertainty, not only speed.",
    "Poor communication": "Lack of updates reduces perceived control and can increase frustration.",
    "Refund issues": "Money-related friction can feel especially painful because customers experience loss aversion.",
    "Customer support": "Negative support interactions can damage perceived fairness, empathy, and trust.",
    "App or website friction": "Complicated digital journeys increase cognitive load and can reduce conversion or satisfaction.",
    "Tracking issues": "Limited order visibility creates uncertainty and makes customers feel less in control.",
}


def get_behavioural_insight(theme):
    """
    Returns behavioural interpretation for a given theme.
    """
    return BEHAVIOURAL_INSIGHTS.get(
        theme,
        "This issue may affect customer trust, ease, or perceived value."
    )