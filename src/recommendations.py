RECOMMENDATIONS = {
    "Delivery delays": "Send proactive delivery updates and set clearer delivery expectations at checkout.",
    "Poor communication": "Create automated status updates and improve response-time standards.",
    "Refund issues": "Add a refund tracking page and clearer refund timelines.",
    "Customer support": "Review support scripts, escalation rules, and empathy training.",
    "App or website friction": "Simplify the checkout journey and reduce unnecessary steps.",
    "Tracking issues": "Improve order tracking visibility and send milestone notifications.",
}


def get_recommendation(theme):
    """
    Returns practical business recommendation for a given theme.
    """
    return RECOMMENDATIONS.get(
        theme,
        "Investigate this issue further using more customer feedback and operational data."
    )