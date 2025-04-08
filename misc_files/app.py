import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from pyngrok import ngrok

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
else:
    st.write("Press the 'Tokenize' button to see the result.")

# Set up ngrok
ngrok.set_auth_token("2vELlOuyvl6OzhW3UT1FfJIFVTH_6jCw9eKx7LYJTDU8ReHzS")  # Replace with your actual token
public_url = ngrok.connect(port=8501)
print(f"Streamlit app is live at: {public_url}")