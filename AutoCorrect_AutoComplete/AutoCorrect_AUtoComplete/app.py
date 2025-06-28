from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the models
with open('model/autocorrect_model.pkl', 'rb') as f:
    autocorrect_model = pickle.load(f)

with open('model/autocomplete_model.pkl', 'rb') as f:
    autocomplete_model = pickle.load(f)

@app.route('/autocorrect', methods=['POST'])
def autocorrect():
    text = request.json.get('text', '')
    # Implement autocorrect logic using the loaded model
    corrected_text = autocorrect_model.correct(text)  # Placeholder for actual correction logic
    return jsonify({'corrected_text': corrected_text})

@app.route('/autocomplete', methods=['POST'])
def autocomplete():
    prefix = request.json.get('prefix', '')
    # Implement autocomplete logic using the loaded model
    suggestions = autocomplete_model.suggest(prefix)  # Placeholder for actual suggestion logic
    return jsonify({'suggestions': suggestions})

if __name__ == '__main__':
    app.run(debug=True)