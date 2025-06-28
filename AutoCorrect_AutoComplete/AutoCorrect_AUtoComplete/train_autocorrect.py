import random
import pickle
from nltk.corpus import words
from nltk.metrics.distance import edit_distance
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Load correct words
word_list = list(set(words.words()))

# Generate synthetic errors
def make_typos(word):
    typos = []
    if len(word) > 3:
        for _ in range(2):
            i = random.randint(0, len(word)-1)
            typo = word[:i] + random.choice('abcdefghijklmnopqrstuvwxyz') + word[i+1:]
            typos.append((typo, word))
    return typos

dataset = []
for w in word_list[:5000]:  # limit for speed
    dataset.extend(make_typos(w))

X = [x[0] for x in dataset]
y = [x[1] for x in dataset]

vec = CountVectorizer(analyzer='char', ngram_range=(2, 3))
X_vec = vec.fit_transform(X)

model = LogisticRegression(max_iter=200)
model.fit(X_vec, y)

with open("model/autocorrect_model.pkl", "wb") as f:
    pickle.dump((vec, model), f)

print("Autocorrect model trained and saved.")

