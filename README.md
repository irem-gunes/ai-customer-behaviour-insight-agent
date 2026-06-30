# AI Customer & Behaviour Insight Agent

## Overview
This project is an AI-assisted analytics tool that turns customer reviews into business insight. It identifies sentiment, recurring pain points, behavioural drivers, business risks, and recommended actions.

## Problem
Businesses collect large volumes of customer feedback, but the feedback is often unstructured and difficult to turn into decisions.

## Solution
The agent analyses review text, detects common issues, explains why those issues may affect customer behaviour, and produces a prioritised insight report.

## Key Features
- CSV review upload
- Data cleaning
- Fast rule-based sentiment analysis (TextBlob) across all reviews
- Optional LLM sentiment check that handles sarcasm and nuance
- Pain point detection
- Behavioural insight layer
- Business risk explanation
- Priority scoring
- Recommended actions
- Downloadable insight report
- Streamlit dashboard
- AI-generated executive summary using an LLM
- Interactive "Ask the Agent" Q&A on the analysed feedback
- Evidence-grounded recommendation generation

## Tech Stack
- Python
- Pandas
- Streamlit
- TextBlob (sentiment)
- Matplotlib
- Ollama (local LLM — `llama3.2`)

The AI summary runs **entirely locally** through Ollama, so no API keys or cloud services are required.

## Getting Started

### Prerequisites
- Python 3.10+
- [Ollama](https://ollama.com) installed and running, with the model pulled:
  ```bash
  ollama pull llama3.2
  ```

### Installation
```bash
git clone https://github.com/irem-gunes/ai-customer-behaviour-agent.git
cd ai-customer-behaviour-agent
pip install -r requirements.txt
```

### Run the app
```bash
python -m streamlit run app.py
```
Then open the local URL Streamlit prints (usually http://localhost:8501) and upload a CSV.

### Data
A small demo file is included at `data/sample_reviews.csv` (340 hotel reviews, stratified across 1–5 star ratings) so you can try the app immediately. In the app you choose which columns hold the review text and the rating.

The demo is sampled from the public **TripAdvisor hotel review dataset** (~255k reviews). The full dataset is not committed here because of its size — download it separately if you want to run the agent at scale.

## Demo
<!-- Add a screenshot or GIF of the dashboard here, e.g.: -->
<!-- ![Dashboard](docs/screenshot.png) -->

## Example Use Case
A customer experience team wants to understand what is driving negative reviews and what issue should be fixed first.

## Why This Project Matters
The project combines data analytics and behavioural science. It does not only identify what customers complain about; it also explains why those issues may affect trust, frustration, perceived control, and repeat behaviour.

## AI Agent Layer
The app includes an AI summary agent that takes the structured pain point table as input and generates an executive summary. The prompt instructs the model to use only the evidence provided by the analysis pipeline and avoid inventing claims.

## Sentiment: two layers
Sentiment is handled in two deliberate stages:

1. **Rule-based (TextBlob)** runs on *every* review. It is fast and cheap, which is what makes the dashboard responsive on large datasets — but, being keyword-based, it cannot read sarcasm or context (e.g. *"Five stars for the noise that kept me up all night. Wonderful."* scores as positive).
2. **LLM sentiment check (Ollama)** runs on a small, user-selected sample. Because it reads each review in context, it correctly handles sarcasm, double negatives, and mixed sentiment. The app surfaces exactly where the two methods disagree — which is usually the most interesting subset of reviews.

## Limitations
- The LLM sentiment check is intentionally capped to a small sample, because local inference takes a few seconds per review and does not scale to the full ~255k-review dataset. For production scale, a fine-tuned transformer classifier would be the next step.
- Pain-point detection is keyword/theme based, so it captures the themes defined in `src/theme_extraction.py` and may miss issues phrased in unexpected ways.
- The LLM runs locally via Ollama, so output quality depends on the chosen model (`llama3.2` by default).
