def vader_sentiment_analysis(df, text_column):
    from nltk.sentiment import SentimentIntensityAnalyzer
    import pandas as pd

    sia = SentimentIntensityAnalyzer()

    df['compound'] = df[text_column].apply(lambda x: sia.polarity_scores(x)['compound'])
    df['positive'] = df[text_column].apply(lambda x: sia.polarity_scores(x)['pos'])
    df['negative'] = df[text_column].apply(lambda x: sia.polarity_scores(x)['neg'])
    df['neutral'] = df[text_column].apply(lambda x: sia.polarity_scores(x)['neu'])

    return df
