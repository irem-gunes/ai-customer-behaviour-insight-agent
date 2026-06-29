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
- Sentiment analysis
- Pain point detection
- Behavioural insight layer
- Business risk explanation
- Priority scoring
- Recommended actions
- Downloadable insight report
- Streamlit dashboard
- AI-generated executive summary using an LLM
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
git clone https://github.com/<your-username>/ai-customer-behaviour-agent.git
cd ai-customer-behaviour-agent
pip install -r requirements.txt
```

### Run the app
```bash
streamlit run app.py
```
Then open the local URL Streamlit prints (usually http://localhost:8501) and upload a CSV.
A demo file is included at `data/sample_reviews.csv` — your CSV needs `rating` and `review_text` columns.

## Demo
<!-- Add a screenshot or GIF of the dashboard here, e.g.: -->
<!-- ![Dashboard](docs/screenshot.png) -->

## Example Use Case
A customer experience team wants to understand what is driving negative reviews and what issue should be fixed first.

## Why This Project Matters
The project combines data analytics and behavioural science. It does not only identify what customers complain about; it also explains why those issues may affect trust, frustration, perceived control, and repeat behaviour.

## AI Agent Layer
The app includes an AI summary agent that takes the structured pain point table as input and generates an executive summary. The prompt instructs the model to use only the evidence provided by the analysis pipeline and avoid inventing claims.