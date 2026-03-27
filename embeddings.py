from sentence_transformers import SentenceTransformer
import numpy as np

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(text: str):
    text = text[:3000]  # safety limit
    embedding = model.encode(text)
    return np.array(embedding, dtype="float32")