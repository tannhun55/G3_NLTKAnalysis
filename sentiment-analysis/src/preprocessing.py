import nltk

#downloading stopwords and punkt
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

def preprocess_text(text):
    """
    Preprocess the input text by lowercasing, removing punctuation, tokenizing, and removing stopwords.
    """

    # Lowercase the text
    text = text.lower()
    
    # Remove punctuation
    text = ''.join([char for char in text if char.isalnum() or char.isspace()])
    
    # Tokenize the text
    tokens = nltk.word_tokenize(text)
    
    # Remove stopwords
    stopwords = set(nltk.corpus.stopwords.words('english'))
    tokens = [word for word in tokens if word not in stopwords]
    
    return ' '.join(tokens)