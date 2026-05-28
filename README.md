# 📄🤖 RAG PDF Question Answering System

AI-powered **Retrieval-Augmented Generation (RAG)** application that allows users to upload PDF documents and ask questions in natural language.

The system extracts PDF text, generates embeddings, retrieves relevant context using **ChromaDB**, and produces answers using **Groq LLaMA 3.1**.

💡 Upload PDF → Ask Question → Get AI Answer

---

## 🚀 Features

- 📄 Upload PDF documents
- 🔍 Extract and process document text
- 🧠 Semantic search using embeddings
- ⚡ Fast answer generation using Groq
- 📚 Vector storage with ChromaDB
- 🎨 Simple Flask + Bootstrap UI
- 🔐 Secure API management using `.env`

---

## 🧠 Tech Stack

**Frontend:** HTML, CSS, Bootstrap  
**Backend:** Flask, Python  
**AI:** LangChain, ChromaDB, Sentence Transformers, Groq LLaMA 3.1  
**Utilities:** PyPDF2, python-dotenv  

---

## 🏗️ Workflow

```text
PDF Upload
   ↓
Text Extraction
   ↓
Chunking
   ↓
Embeddings
   ↓
ChromaDB
   ↓
Similarity Search
   ↓
Groq LLaMA
   ↓
Answer
```

---

## 📊 Metrics

| Metric | Value |
|--------|-------|
| Chunk Size | 1000 |
| Chunk Overlap | 200 |
| Embedding Model | all-MiniLM-L6-v2 |
| Vector Store | ChromaDB |
| LLM | LLaMA 3.1 8B |
| Avg Response | ~1–3 sec |

---

## ⚙️ Installation

```bash
git clone https://github.com/Yash-Ghyar/RAG-PDF-AI-System.git
cd RAG-PDF-AI-System
pip install -r requirements.txt
```

Create `.env`

```env
GROQ_API_KEY=your_api_key
```

Run:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 📌 Future Improvements

- Multi-PDF support
- Chat history
- Cloud deployment
- Better retrieval

---

## 👨‍💻 Author

**Yash Ghyar**  
BTech – Artificial Intelligence & Data Science

