# 🧠 Sentiment Analysis Dashboard (Streamlit + VADER + NLTK)

This project is a sentiment analysis tool built using **Streamlit**, **VADER**, and **NLTK**. It allows users to upload a CSV file containing text reviews, preprocesses the text, runs VADER sentiment analysis, and displays the results with charts and a downloadable file.

---

## 📁 Project Structure

```
G3_NLTKANALYSIS/
├── misc_files/
│   └── app.py                   # Main Streamlit UI
├── src/
│   ├── preprocessing.py         # Text cleaner
│   ├── sentiment_analysis.py    # VADER sentiment analyzer
│   └── data/
│       └── sample_reviews.csv   # Optional test file
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run This Locally

### 1. Clone or Download the Repository

```bash
git clone <repo-url>
cd G3_NLTKANALYSIS
```

### 2. (Optional) Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate    # On Windows
source venv/bin/activate # On macOS/Linux
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit App

```bash
cd misc_files
python -m streamlit run app.py
```

---

## 📥 Upload Format

Upload a `.csv` file with **one column named `review`**:

```
review
I love this product!
Worst purchase ever.
It's okay, not great.
```

You can use the provided [sample_reviews.csv](src/data/sample_reviews.csv) to test the app.

---

## 🧠 Features

✅ CSV Upload  
✅ Preprocessing (lowercase, remove punctuation, stopwords)  
✅ VADER Sentiment Analysis  
✅ Sentiment score columns (compound, pos, neg, neu)  
✅ Sentiment chart  
✅ Download analyzed data as CSV  

---

## 👥 Authors

- Tanjil bin Hasan
- [Your Teammates Here]

---

## 📌 To-Do / Future Features

- [ ] Word Cloud by sentiment  
- [ ] Pie Chart visualization  
- [ ] Topic Modeling (LDA)  
- [ ] Naïve Bayes classifier module  
