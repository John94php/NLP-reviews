import tkinter as tk
from tkinter import messagebox
from nltk.sentiment import SentimentIntensityAnalyzer
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


def analyze_review():
    review_title = title_entry.get()
    review_text_content = review_text.get("1.0", "end")
    processed_review = preprocess_review(review_text_content)
    sentiment_score = analyze_sentiment(processed_review)
    suggested_rating = suggest_rating(sentiment_score)
    messagebox.showinfo("Analiza", f"Propozycja oceny: {suggested_rating}")
def preprocess_review(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    processed_text = ' '.join(tokens)

    return processed_text


def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)['compound']
    return sentiment_score


def suggest_rating(sentiment_score):
    rating = round((sentiment_score + 1) * 2.5)
    return rating


root = tk.Tk()
root.title("Analizator recenzji")

title_label = tk.Label(root, text="Tytuł recenzji:")
title_label.pack()

title_entry = tk.Entry(root, width=50)
title_entry.pack()

review_label = tk.Label(root, text="Treść recenzji:")
review_label.pack()

review_text = tk.Text(root, height=10, width=50)
review_text.pack()

analyze_button = tk.Button(root, text="Analizuj recenzję", command=analyze_review)
analyze_button.pack()

root.mainloop()
