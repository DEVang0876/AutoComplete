# from flask import Flask, request, jsonify
# import pickle

# app = Flask(__name__)

# # Load the models
# with open('model/autocorrect_model.pkl', 'rb') as f:
#     autocorrect_model = pickle.load(f)

# with open('model/autocomplete_model.pkl', 'rb') as f:
#     autocomplete_model = pickle.load(f)

# @app.route('/autocorrect', methods=['POST'])
# def autocorrect():
#     text = request.json.get('text', '')
#     # Implement autocorrect logic using the loaded model
#     corrected_text = autocorrect_model.correct(text)  # Placeholder for actual correction logic
#     return jsonify({'corrected_text': corrected_text})

# @app.route('/autocomplete', methods=['POST'])
# def autocomplete():
#     prefix = request.json.get('prefix', '')
#     # Implement autocomplete logic using the loaded model
#     suggestions = autocomplete_model.suggest(prefix)  # Placeholder for actual suggestion logic
#     return jsonify({'suggestions': suggestions})

# if __name__ == '__main__':
#     app.run(debug=True)








from flask import Flask, request, jsonify, send_from_directory
import pickle
import os

# Load models
with open("model/autocorrect_model.pkl", "rb") as f:
    vec, auto_model = pickle.load(f)

with open("model/autocomplete_model.pkl", "rb") as f:
    prefix_dict = pickle.load(f)

app = Flask(__name__, static_folder='static')

@app.route("/autocorrect")
def autocorrect():
    word = request.args.get("word", "")
    X = vec.transform([word])
    prediction = auto_model.predict(X)[0]
    return jsonify({"correction": prediction})

@app.route("/autocomplete")
def autocomplete():
    prefix = request.args.get("prefix", "")
    suggestions = sorted(list(prefix_dict.get(prefix.lower(), [])))[:5]
    return jsonify(suggestions)

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    app.run(debug=True)
