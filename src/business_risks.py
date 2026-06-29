BUSINESS_RISKS = {
    "Delivery delays": "May reduce repeat purchases and increase complaints if expectations are not managed.",
    "Poor communication": "May reduce customer trust and increase support follow-ups.",
    "Refund issues": "May create strong dissatisfaction because money-related friction feels high-stakes.",
    "Customer support": "May damage brand trust and increase churn risk.",
    "App or website friction": "May reduce conversion and increase drop-off during checkout.",
    "Tracking issues": "May increase uncertainty and avoidable contact with support teams.",
}


def get_business_risk(theme):
    return BUSINESS_RISKS.get(
        theme,
        "May negatively affect customer satisfaction, trust, or retention."
    )
