BUSINESS_IMPACT = {
    "Delivery delays": 3,
    "Poor communication": 3,
    "Refund issues": 4,
    "Customer support": 4,
    "App or website friction": 3,
    "Tracking issues": 2,
}


def calculate_priority_score(theme, count):
    """
    Calculates a simple priority score based on frequency and estimated business impact.
    """
    impact = BUSINESS_IMPACT.get(theme, 2)
    score = count * impact

    if score >= 9:
        priority = "Critical"
    elif score >= 6:
        priority = "High"
    elif score >= 3:
        priority = "Medium"
    else:
        priority = "Low"

    return score, priority