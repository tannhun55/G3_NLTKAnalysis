import nltk
import pandas as pd

# Download necessary NLTK data
nltk.download('stopwords')
nltk.download('punkt')

def preprocess_text(text):
    """
    Preprocess the input text by lowercasing, removing punctuation,
    tokenizing, and removing stopwords.
    """
    text = text.lower()
    text = ''.join([char for char in text if char.isalnum() or char.isspace()])
    tokens = nltk.word_tokenize(text)
    stopwords = set(nltk.corpus.stopwords.words('english'))
    tokens = [word for word in tokens if word not in stopwords]
    return ' '.join(tokens)

def load_and_clean_data(file):
    """
    Load a CSV file, drop rows with any missing values.
    Preprocessing is now done after the user selects a column.
    """
    df = pd.read_csv(file)
    df.dropna(inplace=True)
    return df
