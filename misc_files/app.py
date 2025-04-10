# 🔧 Add the project root to the Python path so we can import from 'src' folder
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 📦 Import required libraries
import streamlit as st  # For building the web app UI
import pandas as pd     # For handling data
from src.sentiment_analysis import vader_sentiment_analysis  # VADER logic
from src.preprocessing import load_and_clean_data            # Data cleaning

# 🖥️ Streamlit app configuration
st.set_page_config(page_title="Sentiment Analysis Dashboard", layout="wide")

# 🧾 App title
st.title("📊 Sentiment Analysis Dashboard (VADER + Preprocessing)")

# 📤 File uploader to allow users to upload CSV files
uploaded_file = st.file_uploader("📤 Upload a CSV file", type="csv")

# ✅ Once a file is uploaded
if uploaded_file:
    # 🔍 Show raw data before sentiment analysis
    st.subheader("📄 Raw Data")
    df = load_and_clean_data(uploaded_file)  # Clean/load CSV
    st.dataframe(df.head())  # Show first few rows

    # 🧠 Let user choose which column to analyze (text column)
    text_column = st.selectbox("📌 Select the column to analyze", df.columns)

    # 🎯 Run VADER sentiment analysis on selected column
    if text_column:
        st.subheader("🎯 Sentiment Results (VADER Scores)")
        df = vader_sentiment_analysis(df, text_column=text_column)
        # Display the selected text and sentiment scores
        st.dataframe(df[[text_column, 'compound', 'positive', 'negative', 'neutral']].head())

        # 📊 Bar chart showing the count of each sentiment category
        st.subheader("📊 Sentiment Distribution")
        sentiment_counts = (
            df['compound']
            .apply(lambda x: 'positive' if x > 0 else 'negative' if x < 0 else 'neutral')
            .value_counts()
        )
        st.bar_chart(sentiment_counts)

        # 📥 Let user download the resulting DataFrame as a CSV file
        st.subheader("⬇️ Download Results")
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download CSV", csv, "sentiment_results.csv", "text/csv")
else:
    # ℹ️ Show message before a file is uploaded
    st.info("Upload a CSV file to begin.")
