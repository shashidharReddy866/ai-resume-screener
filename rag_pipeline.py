import faiss
import numpy as np
from embeddings import get_embedding

dimension = 384
index = faiss.IndexFlatL2(dimension)

resume_store = []

def chunk_text(text, chunk_size=500):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def store_resume(resume_text, resume_id):
    chunks = chunk_text(resume_text)

    for chunk in chunks:
        emb = np.array([get_embedding(chunk)]).astype("float32")
        index.add(emb)

        resume_store.append({
            "resume_id": resume_id,
            "text": chunk
        })

def retrieve_chunks(query, k=5):
    query_emb = np.array([get_embedding(query)]).astype("float32")
    distances, indices = index.search(query_emb, k)

    results = []
    for idx in indices[0]:
        if idx < len(resume_store):
            results.append(resume_store[idx])

    return results