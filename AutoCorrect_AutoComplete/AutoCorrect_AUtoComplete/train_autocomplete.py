# ----------------------------
# FILE: train_autocomplete.py
# ----------------------------
import pickle
from nltk.corpus import brown
from collections import defaultdict
import nltk
import os

# Ensure the corpus is available
nltk.download('brown')

# Load words from NLTK Brown corpus
words = [w.lower() for w in brown.words() if w.isalpha()]

# Create prefix dictionary for autocomplete
prefix_dict = defaultdict(set)
for word in words:
    for i in range(1, len(word) + 1):
        prefix_dict[word[:i]].add(word)

# Create model directory if it doesn't exist
os.makedirs("model", exist_ok=True)

# Save the autocomplete model
with open("model/autocomplete_model.pkl", "wb") as f:
    pickle.dump(prefix_dict, f)

print("✅ Autocomplete model trained and saved.")
