import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from src.ai_summary_agent import generate_ai_summary
from src.data_cleaning import prepare_reviews
from src.sentiment_analysis import add_sentiment
from src.theme_extraction import add_themes, summarise_themes, get_example_reviews
from src.behaviour_insights import get_behavioural_insight
from src.recommendations import get_recommendation
from src.priority_scoring import calculate_priority_score
from src.business_risks import get_business_risk


st.set_page_config(
    page_title="AI Customer & Behaviour Insight Agent",
    layout="wide"
    )

st.title("AI Customer & Behaviour Insight Agent")

st.write(
    """
    This tool analyses customer review data to identify recurring pain points, 
    behavioural drivers, business risks, and recommended actions.

    It is designed as a decision-support tool for customer experience, product, 
    operations, and marketing teams.
    """
    )

st.sidebar.title("About this Agent")

st.sidebar.write(
    """
    This agent helps turn unstructured customer feedback into business insight.

    It analyses:
    - Sentiment
    - Pain points
    - Behavioural drivers
    - Business risks
    - Recommended actions
    """
    )

st.sidebar.write("Built with Python, Pandas, NLP and Streamlit.")
st.write(
    "Upload customer reviews and the agent will identify sentiment, recurring pain points, "
    "behavioural drivers, and recommended business actions."
    )

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Raw Data Preview")
    st.dataframe(df.head())

    try:
        df = prepare_reviews(df)
        df = add_sentiment(df)
        df = add_themes(df)

        st.subheader("Dataset Overview")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Total Reviews", len(df))

        with col2:
            st.metric("Average Rating", round(df["rating"].mean(), 2))

        with col3:
            negative_pct = round(
                (df["sentiment_label"].eq("Negative").mean()) * 100,
                1
            )
            st.metric("Negative Reviews", f"{negative_pct}%")

        st.subheader("Sentiment Distribution")
        sentiment_counts = df["sentiment_label"].value_counts()
        st.bar_chart(sentiment_counts)

        st.subheader("Rating Distribution")
        rating_counts = df["rating"].value_counts().sort_index()
        st.bar_chart(rating_counts)

        st.subheader("Detected Pain Points")

        theme_counts = summarise_themes(df)
        negative_df = df[
            (df["sentiment_label"] == "Negative") | (df["rating"] <= 2)]

        negative_theme_counts = summarise_themes(negative_df)

        if negative_theme_counts:
            theme_summary = []

            for theme, count in negative_theme_counts.most_common():
                priority_score, priority = calculate_priority_score(theme, count)
                    
                examples = get_example_reviews(negative_df, theme)

                theme_summary.append({
                    "Pain Point": theme,
                    "Mentions in Negative Reviews": count,
                    "Priority Score": priority_score,
                    "Priority": priority,
                    "Example Review": examples[0] if examples else "",
                    "Behavioural Insight": get_behavioural_insight(theme),
                    "Business Risk": get_business_risk(theme),
                    "Recommendation": get_recommendation(theme)
                    })

            theme_df = pd.DataFrame(theme_summary)

            st.dataframe(theme_df)

            st.subheader("AI-Generated Executive Summary")

            if st.button("Generate AI Summary"):
                with st.spinner("Generating AI-powered customer insight summary..."):
                    ai_summary = generate_ai_summary(theme_df)
                    st.write(ai_summary)

            csv = theme_df.to_csv(index=False).encode("utf-8")
            
            st.download_button(
                label="Download Insight Report as CSV",
                data=csv,
                file_name="customer_behaviour_insight_report.csv",
                mime="text/csv"
                )
            
            st.subheader("Top Pain Points")
            pain_point_chart = theme_df.set_index("Pain Point")["Mentions in Negative Reviews"]
            st.bar_chart(pain_point_chart)
            

            st.subheader("Executive Summary")

            top_theme = negative_theme_counts.most_common(1)[0][0]
            top_count = negative_theme_counts.most_common(1)[0][1]

            st.write(
                f"The highest-priority customer pain point is **{top_theme}**, "
                f"with **{top_count} mention(s)** among negative or low-rated reviews. "
                f"The pattern suggests that this issue may be contributing to dissatisfaction by affecting "
                f"customer trust, perceived control, or ease of experience."
                )
            
            st.write(
                f"From a behavioural perspective, this matters because: "
                f"{get_behavioural_insight(top_theme)}"
                )
            
            st.write(
                f"Recommended action: {get_recommendation(top_theme)}"
                )

        else:
            st.info("No major themes detected. Try using a larger dataset.")

        st.subheader("Processed Data")
        st.dataframe(df)

    except Exception as e:
        st.error(f"Error: {e}")

else:
    st.info("Upload a CSV file to begin.")
