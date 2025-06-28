from flask import Flask, request, jsonify, send_from_directory
import pickle
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load autocomplete model
with open("model/autocomplete_model.pkl", "rb") as f:
    prefix_dict = pickle.load(f)

# Load pretrained T5 model for autocorrect (no training needed!)
tokenizer = T5Tokenizer.from_pretrained("t5-small")
model = T5ForConditionalGeneration.from_pretrained("t5-small")

app = Flask(__name__, static_folder='static')

@app.route("/autocomplete")
def autocomplete():
    prefix = request.args.get("prefix", "")
    suggestions = sorted(list(prefix_dict.get(prefix.lower(), [])))[:5]
    return jsonify(suggestions)

@app.route("/autocorrect")
def autocorrect():
    word = request.args.get("word", "")
    input_text = f"fix spelling: {word}"
    inputs = tokenizer.encode(input_text, return_tensors="pt")
    outputs = model.generate(inputs, max_length=10)
    correction = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({"correction": correction})

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    app.run(debug=True)
