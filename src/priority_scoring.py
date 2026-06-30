BUSINESS_IMPACT = {
    "Cleanliness issues": 5,
    "Poor service": 4,
    "Room quality issues": 4,
    "Noise and sleep problems": 5,
    "Value for money concerns": 4,
    "Location problems": 3,
    "Booking or check-in problems": 4,
    "Breakfast or food issues": 3,
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
