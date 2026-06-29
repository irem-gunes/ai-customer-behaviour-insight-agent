import ollama


MODEL_NAME = "llama3.2"


def generate_ai_summary(theme_df):
    """
    Generates an AI-powered executive summary from the pain point table using Ollama locally.
    """

    if theme_df.empty:
        return "No pain points were detected, so an AI summary could not be generated."

    insight_data = theme_df.to_dict(orient="records")

    prompt = f"""
You are a Customer & Behaviour Insight Analyst.

You are analysing customer review data. Use ONLY the evidence provided below.
Do not invent numbers, themes, or claims.

Pain point data:
{insight_data}

Write a concise business-facing executive summary with the following sections:

1. Overall finding
2. Main customer pain points
3. Behavioural interpretation
4. Business risks
5. Recommended priority actions

Style:
- Clear analyst tone
- Practical and commercial
- No hype
- No invented evidence
- Mention that findings are based on the uploaded review data
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


def ask_agent(theme_df, question):
    """
    Allows the user to ask questions about the analysed customer feedback using Ollama locally.
    """

    if theme_df.empty:
        return "No pain point data is available to answer this question."

    insight_data = theme_df.to_dict(orient="records")

    prompt = f"""
You are a Customer & Behaviour Insight Analyst.

Use ONLY the evidence provided below.
Do not invent numbers, themes, or findings.

Pain point data:
{insight_data}

User question:
{question}

Answer clearly and practically.
Focus on customer behaviour, business risk, and recommended actions.
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]
