# 📦 Import NLTK and pandas for NLP and data handling
import nltk
import pandas as pd

# ⬇️ Download necessary NLTK resources (only downloads once)
nltk.download('stopwords')  # Stopwords like 'the', 'is', 'and'
nltk.download('punkt')      # Tokenizer support for splitting sentences/words

# 🧹 Function to preprocess text before analysis
def preprocess_text(text):
    """
    Preprocess the input text by:
    - Converting to lowercase
    - Removing punctuation
    - Tokenizing into words
    - Removing English stopwords
    - Returning cleaned text
    """
    text = text.lower()  # Convert to lowercase
    text = ''.join([char for char in text if char.isalnum() or char.isspace()])  # Remove punctuation
    tokens = nltk.word_tokenize(text)  # Tokenize text into words
    stopwords = set(nltk.corpus.stopwords.words('english'))  # Get English stopwords
    tokens = [word for word in tokens if word not in stopwords]  # Remove stopwords
    return ' '.join(tokens)  # Return cleaned text as a string

# 📄 Function to load a CSV file and clean basic structure
def load_and_clean_data(file):
    """
    Loads a CSV and drops rows that contain any missing values.
    This keeps the data valid before applying sentiment analysis.
    We wait to preprocess text until after a column is selected by the user.
    """
    df = pd.read_csv(file)  # Load CSV into a DataFrame
    df.dropna(inplace=True)  # Remove any rows with empty values
    return df  # Return the cleaned DataFrame
