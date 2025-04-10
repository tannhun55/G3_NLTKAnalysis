import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
from src.sentiment_analysis import vader_sentiment_analysis
from src.preprocessing import load_and_clean_data

st.set_page_config(page_title="Sentiment Analysis Dashboard", layout="wide")

st.title("📊 Sentiment Analysis Dashboard (VADER + Preprocessing)")

uploaded_file = st.file_uploader("📤 Upload a CSV file", type="csv")

if uploaded_file:
    st.subheader("📄 Raw Data")
    df = load_and_clean_data(uploaded_file)
    st.dataframe(df.head())

    # User selects which column to analyze
    text_column = st.selectbox("📌 Select the column to analyze", df.columns)

    if text_column:
        st.subheader("🎯 Sentiment Results (VADER Scores)")
        df = vader_sentiment_analysis(df, text_column=text_column)
        st.dataframe(df[[text_column, 'compound', 'positive', 'negative', 'neutral']].head())

        st.subheader("📊 Sentiment Distribution")
        sentiment_counts = (
            df['compound']
            .apply(lambda x: 'positive' if x > 0 else 'negative' if x < 0 else 'neutral')
            .value_counts()
        )
        st.bar_chart(sentiment_counts)

        st.subheader("⬇️ Download Results")
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download CSV", csv, "sentiment_results.csv", "text/csv")
else:
    st.info("Upload a CSV file to begin.")
