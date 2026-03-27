# 🤖 AI Resume Screener

An AI-powered system that evaluates resumes against job descriptions using semantic embeddings, FAISS vector search, and a RAG pipeline.

---

## 🚀 Demo Output

![Output](output.png)

---

## 🧠 Overview

This project simulates an intelligent resume screening system that:

- Extracts resume content
- Converts text into embeddings
- Stores vectors using FAISS
- Retrieves relevant sections
- Scores resumes based on semantic similarity

---

## ⚙️ Tech Stack

- Python  
- Sentence Transformers (all-MiniLM-L6-v2)  
- FAISS (Vector Database)  
- Gradio (UI)  

---

## 🔍 How It Works

1. Upload job description + resumes  
2. Extract text from PDF/DOCX  
3. Chunk resume into segments  
4. Convert chunks into embeddings  
5. Store embeddings in FAISS  
6. Retrieve relevant chunks  
7. Compute similarity score  

---

## 📊 Features

- Resume parsing (PDF/DOCX)
- Semantic similarity scoring
- Multi-resume comparison
- Clean UI with Gradio
- Real-time evaluation

---

## 📈 Example Output

Resume: Shashidhar_Reddy.pdf  
Score: 67%  
Status: Good Fit  

---

## 💡 Future Improvements

- Add skill gap detection  
- Add LLM-based reasoning  
- Add dashboard visualization  
- Deploy on cloud  

---

## 👨‍💻 Author

Shashidhar Reddy
