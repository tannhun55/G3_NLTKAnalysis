# This is the main script for running sentiment analysis and topic modeling on a dataset of reviews.

# Importing necessary libraries
import pandas as pd
import nltk

# Make sure the VADER lexicon is downloaded 
nltk.download('vader_lexicon') 

#adding addiitonal required NLTK Resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punk_tab')

# Importing necessary modules
from sentiment_analysis import vader_sentiment_analysis
from preprocessing import preprocess_text 

def main(): 
    # Loading data - I had issues using a relative path, so I used an absolute path.
    # You need to update the absolute path with your own path to the CSV file.
    data_path = r'C:\Users\Tanjil\OneDrive\Desktop\Study\Winter 2025\UI_UX Design_BinduGoel\G3_NLTKAnalysis\sentiment-analysis\src\data\sample_reviews.csv'
    df = pd.read_csv(data_path)

    # Clean column names in case there are hidden characters or spaces
    df.columns = df.columns.str.strip().str.replace('\ufeff', '')

    # Debug: Print the first few rows of the data
    print("Data loaded from CSV:")
    print(df.head())
    print("Columns in the DataFrame:", df.columns.tolist())

    # Preprocess the text data
    df['reviewText'] = df['reviewText'].apply(preprocess_text)

    # Debug: Print the data after preprocessing
    print("Data after preprocessing:")
    print(df['reviewText'].head())

    # Perform sentiment analysis using VADER
    print("Performing sentiment analysis...")
    df_with_sentiment = vader_sentiment_analysis(df, text_column="reviewText")

    # Debug: Print the results of the sentiment analysis
    print("VADER Sentiment Analysis Results:")
    print(df_with_sentiment[['reviewText', 'compound', 'positive', 'negative', 'neutral']].head())

if __name__ == "__main__":
    main()