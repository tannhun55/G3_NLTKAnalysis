import streamlit as st
# Importing necessary libraries
import nltk
from nltk.tokenize import word_tokenize

# Download necessary NLTK data (if needed)
nltk.download('punkt')

# Streamlit Interface
st.title("Simple NLTK Tokenizer")

# Instructions
st.write("This is a simple example using NLTK's word tokenizer.")

# Input Textbox
text_input = st.text_area("Enter some text to tokenize:")

# Button to process the text
if st.button("Tokenize"):
    if text_input:
        tokens = word_tokenize(text_input)
        st.write("Tokens:", tokens)
    else:
        st.write("Please enter some text to tokenize.")