# 📦 Import NLTK's VADER sentiment analyzer
from nltk.sentiment import SentimentIntensityAnalyzer

# 🔁 Import the text preprocessing function from our preprocessing module
from src.preprocessing import preprocess_text

# 🧠 Main function to run sentiment analysis
def vader_sentiment_analysis(df, text_column):
    """
    Apply VADER sentiment analysis on the specified text column.
    Preprocesses the text using our custom function before scoring.
    
    Returns the DataFrame with added sentiment score columns:
    - compound
    - positive
    - negative
    - neutral
    """

    # 🧰 Initialize the VADER sentiment analyzer
    sia = SentimentIntensityAnalyzer()

    # 🧹 Preprocess the selected text column (clean text before scoring)
    df[text_column] = df[text_column].astype(str).apply(preprocess_text)

    # 🎯 Apply VADER and extract sentiment scores
    df['compound'] = df[text_column].apply(lambda x: sia.polarity_scores(x)['compound'])  # Overall score
    df['positive'] = df[text_column].apply(lambda x: sia.polarity_scores(x)['pos'])       # Positive score
    df['negative'] = df[text_column].apply(lambda x: sia.polarity_scores(x)['neg'])       # Negative score
    df['neutral'] = df[text_column].apply(lambda x: sia.polarity_scores(x)['neu'])        # Neutral score

    # ✅ Return DataFrame with new sentiment columns
    return df
