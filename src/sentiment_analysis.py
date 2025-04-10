from nltk.sentiment import SentimentIntensityAnalyzer
from src.preprocessing import preprocess_text  # reuse your cleaner

def vader_sentiment_analysis(df, text_column):
    """
    Apply VADER sentiment analysis on the specified text column.
    Preprocesses text before scoring.
    """
    sia = SentimentIntensityAnalyzer()

    # Apply preprocessing
    df[text_column] = df[text_column].astype(str).apply(preprocess_text)

    # Apply VADER sentiment scoring
    df['compound'] = df[text_column].apply(lambda x: sia.polarity_scores(x)['compound'])
    df['positive'] = df[text_column].apply(lambda x: sia.polarity_scores(x)['pos'])
    df['negative'] = df[text_column].apply(lambda x: sia.polarity_scores(x)['neg'])
    df['neutral'] = df[text_column].apply(lambda x: sia.polarity_scores(x)['neu'])

    return df
