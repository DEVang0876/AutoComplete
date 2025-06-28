import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

def load_corpus(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text.split()

words = [w.lower() for w in load_corpus("data/corpus.txt") if w.isalpha()]


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






# import pickle
# from nltk.corpus import brown
# from collections import defaultdict

# # Load corpus
# words = [w.lower() for w in brown.words() if w.isalpha()]
# prefix_dict = defaultdict(set)

# for word in words:
#     for i in range(1, len(word)+1):
#         prefix_dict[word[:i]].add(word)

# with open("model/autocomplete_model.pkl", "wb") as f:
#     pickle.dump(prefix_dict, f)

# print("Autocomplete model trained and saved.")