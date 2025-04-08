# Sentiment Analysis Project

This project implements a sentiment analysis pipeline using VADER sentiment analysis, along with optional topic modeling and Naïve Bayes classification. The main components of the project are organized into separate modules for clarity and maintainability.

## Project Structure

```
sentiment-analysis
├── src
├── data
│   └── data_reviews.csv
│   ├── main.py
│   ├── preprocess.py
│   ├── sentiment_analysis.py
│   ├── topic_modeling.py -- Need to add this 
│   └── naive_bayes.py -- Need to add this too 
├── requirements.txt -- lists dependencies you need. Update as required. 
└── README.md
We then can add any additional NLTK we think would work with our project. 
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd sentiment-analysis-project
   ```

2. **Install the required packages**:
   Create a virtual environment (optional but recommended): -- Do not do this yet - we need to figure out what virtual envirnment
   we are using. Right now I am using Terminal to display output data. 
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

   Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the sentiment analysis pipeline, execute the `main.py` script:

```
python src/main.py
```
I don't use terminal to run projects, just the added button feature in VS code. 

### Optional Features - to be determiend

- **Topic Modeling**: The project includes a module for topic modeling. You can call the `analyze_topics` function from `topic_modeling.py` to identify topics in the text data.
  
- **Naïve Bayes Classification**: The `train_evaluate_naive_bayes` function in `naive_bayes.py` can be used to train and evaluate a Naïve Bayes classifier on the text data.

## Dependencies

The project requires the following Python packages:

- pandas
- nltk
- vaderSentiment

Make sure to install these packages using the `requirements.txt` file provided.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.