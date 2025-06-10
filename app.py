from flask import Flask, request, render_template, jsonify
from model import autocorrect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    text = request.json["text"]
    corrected = autocorrect(text)
    # autocomplete_words = ...
    return jsonify({"correction": corrected})

if __name__ == "__main__":
    app.run(debug=True)
