# # FILE: train_autocorrect.py
# import os
# import pickle
# from transformers import T5ForConditionalGeneration, T5Tokenizer

# # Load T5 model & tokenizer
# tokenizer = T5Tokenizer.from_pretrained("t5-small")
# model = T5ForConditionalGeneration.from_pretrained("t5-small")

# # Create model directory if not exists
# os.makedirs("model", exist_ok=True)

# # Save model + tokenizer to a pickle
# with open("model/train_autocorrect.pkl", "wb") as f:
#     pickle.dump((tokenizer, model), f)

# print("✅ T5 model and tokenizer saved as train_autocorrect.pkl")
