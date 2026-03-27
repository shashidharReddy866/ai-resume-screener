import numpy as np
from embeddings import get_embedding

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def score_resume(jd_text, resume_chunks):
    jd_emb = get_embedding(jd_text)

    scores = []

    for chunk in resume_chunks:
        chunk_emb = get_embedding(chunk["text"])
        sim = cosine_similarity(jd_emb, chunk_emb)
        scores.append(sim)

    if not scores:
        return {"score": 0, "status": "No Match"}

    final_score = int(np.mean(scores) * 100)

    return {
        "score": final_score,
        "status": "Good Fit" if final_score > 60 else "Needs Improvement"
    }