RECOMMENDATIONS = {
    "Cleanliness issues": "Prioritise room inspection standards, bathroom checks, and visible housekeeping quality controls.",
    "Poor service": "Review front-desk service standards, escalation rules, and staff empathy training.",
    "Room quality issues": "Audit recurring room defects and prioritise maintenance fixes for comfort-related problems.",
    "Noise and sleep problems": "Identify rooms affected by noise, improve guest warnings, and offer proactive room changes where possible.",
    "Value for money concerns": "Improve expectation-setting in listings and review whether pricing matches the delivered experience.",
    "Location problems": "Make transport, parking, and distance information clearer before booking.",
    "Booking or check-in problems": "Simplify check-in communication and reduce uncertainty around reservation status and waiting times.",
    "Breakfast or food issues": "Review breakfast quality, freshness, and service consistency."
}


def get_recommendation(theme):
    """
    Returns practical business recommendation for a given theme.
    """
    return RECOMMENDATIONS.get(
        theme,
        "Investigate this issue further using more customer feedback and operational data."
    )
