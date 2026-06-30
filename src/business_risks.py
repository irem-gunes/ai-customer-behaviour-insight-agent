BUSINESS_RISKS = {
    "Cleanliness issues": "High risk of negative reviews because cleanliness is a basic expectation in hospitality.",
    "Poor service": "May reduce guest trust, increase complaint escalation, and harm repeat booking likelihood.",
    "Room quality issues": "May create expectation gaps and reduce perceived value for money.",
    "Noise and sleep problems": "May strongly reduce satisfaction because sleep quality is central to the hotel experience.",
    "Value for money concerns": "May damage perceived fairness and reduce willingness to recommend.",
    "Location problems": "May lead to dissatisfaction when convenience expectations are not managed before arrival.",
    "Booking or check-in problems": "May create a poor first impression and increase frustration early in the guest journey.",
    "Breakfast or food issues": "May reduce overall satisfaction because food is a visible, memorable service touchpoint."
}


def get_business_risk(theme):
    return BUSINESS_RISKS.get(
        theme,
        "May negatively affect customer satisfaction, trust, or retention."
    )
