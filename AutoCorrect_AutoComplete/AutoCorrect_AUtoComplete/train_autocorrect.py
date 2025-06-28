from transformers import T5ForConditionalGeneration, T5Tokenizer
import pickle
import os

# Load pre-trained model and tokenizer
tokenizer = T5Tokenizer.from_pretrained("t5-small")
model = T5ForConditionalGeneration.from_pretrained("t5-small")

# Save both into a pickle file
os.makedirs("model", exist_ok=True)
with open("model/train_autocorrect.pkl", "wb") as f:
    pickle.dump((tokenizer, model), f)

print("✅ T5 autocorrect model saved as train_autocorrect.pkl")
