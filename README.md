# 🔤 AutoCorrect + AutoComplete Web App

This is a web application that combines:
- ✅ **Autocomplete** using your own trained prefix model
- ✅ **Autocorrect** using a pretrained BERT model from [NeuSpell](https://github.com/neuspell/neuspell)

No training required for autocorrect — it's plug-and-play!

---

## 🚀 Features

- 🔍 Instant **Autocomplete** from prefix dictionary
- ✨ Real-time **Spelling Correction** using pretrained BERT
- 💻 Clean frontend with responsive UI
- ⚙️ Flask-powered backend API

---

## 🧠 Tech Stack

| Feature       | Technology               |
|---------------|--------------------------|
| Autocomplete  | Custom `.pkl` model      |
| Autocorrect   | NeuSpell pretrained BERT |
| Backend       | Python Flask             |
| Frontend      | HTML + CSS + JavaScript  |

---

## 📁 Folder Structure

```
AutoCorrectProject/
├── app.py                      # Flask backend
├── model/
│   └── autocomplete_model.pkl  # Your autocomplete model
├── static/
│   └── index.html              # Frontend UI
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

1. **Clone or copy** the project files.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

> Note: NeuSpell will auto-download its pretrained model (~400MB) on first run.

---

## ▶️ Run the App

```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000)

---

## 💬 Example Query

Typing:
```
I havv a dreem
```

Returns:
- **Correction** → `I have a dream`
- **Autocomplete** → `["have", "hate", "havey"]` (based on prefix `hav`)

---

## ✏️ Customize

- You can swap `BertChecker()` in `app.py` with other pretrained NeuSpell models:
  ```python
  from neuspell import RobertaChecker
  checker = RobertaChecker()
  checker.from_pretrained()
  ```

---

## 🙌 Credits

- [NeuSpell](https://github.com/neuspell/neuspell) – Pretrained spelling correction
- Your own autocomplete training

---

## 📫 Contact

For questions or suggestions, feel free to message or fork this project.
