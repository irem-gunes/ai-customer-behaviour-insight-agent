BEHAVIOURAL_INSIGHTS = {
    "Cleanliness issues": "Cleanliness strongly affects trust because customers use visible hygiene cues to judge safety, care, and overall quality.",
    "Poor service": "Negative staff interactions can reduce perceived fairness, empathy, and psychological safety during the stay.",
    "Room quality issues": "Room problems create expectation gaps because the customer compares the actual stay against the promised experience.",
    "Noise and sleep problems": "Sleep disruption has a high emotional impact because it affects comfort, recovery, and the core purpose of a hotel stay.",
    "Value for money concerns": "Price dissatisfaction is often linked to perceived unfairness when the experience does not match the amount paid.",
    "Location problems": "Location friction increases effort and can make the stay feel less convenient than expected.",
    "Booking or check-in problems": "Waiting and unclear processes reduce perceived control at the start of the customer journey.",
    "Breakfast or food issues": "Food and breakfast issues can disproportionately affect satisfaction because they are repeated daily touchpoints during a stay.",
}


def get_behavioural_insight(theme):
    """
    Returns behavioural interpretation for a given theme.
    """
    return BEHAVIOURAL_INSIGHTS.get(
        theme,
        "This issue may affect customer trust, ease, or perceived value."
    )
