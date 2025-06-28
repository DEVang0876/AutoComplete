import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Load the text corpus
def load_corpus(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        corpus = file.readlines()
    return [line.strip() for line in corpus]

# Train the autocomplete model
def train_autocomplete_model(corpus):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus)
    y = [line.split()[0] for line in corpus]  # Assuming the first word is the label

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = MultinomialNB()
    model.fit(X_train, y_train)

    return model, vectorizer

# Save the trained model and vectorizer
def save_model(model, vectorizer, model_path, vectorizer_path):
    with open(model_path, 'wb') as model_file:
        pickle.dump(model, model_file)
    with open(vectorizer_path, 'wb') as vectorizer_file:
        pickle.dump(vectorizer, vectorizer_file)

if __name__ == "__main__":
    corpus = load_corpus('data/corpus.txt')
    model, vectorizer = train_autocomplete_model(corpus)
    save_model(model, vectorizer, 'model/autocomplete_model.pkl', 'model/autocomplete_vectorizer.pkl')