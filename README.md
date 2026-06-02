# RAG PDF Question Answering System

### Retrieval-Augmented Generation (RAG) Application using LangChain, ChromaDB, and LLaMA 3.1

---

## Overview

A Retrieval-Augmented Generation (RAG) application that enables users to upload PDF documents and ask questions in natural language.

The system extracts text from uploaded PDFs, generates vector embeddings, retrieves relevant context using semantic search, and produces accurate answers using Groq-powered LLaMA 3.1.

This project demonstrates practical implementation of Large Language Models (LLMs), vector databases, document retrieval, and Generative AI workflows.

---

## Features

* PDF Document Upload
* Automatic Text Extraction
* Intelligent Text Chunking
* Semantic Search using Vector Embeddings
* Context Retrieval with ChromaDB
* Question Answering using LLaMA 3.1
* Fast Response Generation through Groq
* Secure API Key Management using Environment Variables
* Simple and Responsive Flask Web Interface

---

## System Workflow

```text
PDF Upload
    │
    ▼
Text Extraction
    │
    ▼
Document Chunking
    │
    ▼
Embedding Generation
    │
    ▼
ChromaDB Vector Store
    │
    ▼
Similarity Search
    │
    ▼
Relevant Context Retrieval
    │
    ▼
LLaMA 3.1
    │
    ▼
Generated Answer
```

---

## Technology Stack

### Backend

* Python
* Flask

### Generative AI

* LangChain
* Groq API
* LLaMA 3.1

### Vector Database

* ChromaDB

### Embeddings

* Sentence Transformers
* all-MiniLM-L6-v2

### Frontend

* HTML5
* CSS3
* Bootstrap

### Utilities

* PyPDF2
* python-dotenv

---

## Architecture Components

### Document Processing

* PDF Text Extraction
* Text Chunking
* Context Preparation

### Retrieval Layer

* Embedding Generation
* Vector Storage
* Similarity Search

### Generation Layer

* Context Injection
* Prompt Construction
* LLM-Based Answer Generation

---

## System Configuration

| Component             | Value            |
| --------------------- | ---------------- |
| Chunk Size            | 1000             |
| Chunk Overlap         | 200              |
| Embedding Model       | all-MiniLM-L6-v2 |
| Vector Database       | ChromaDB         |
| LLM                   | LLaMA 3.1 8B     |
| Average Response Time | 1–3 Seconds      |

---

## Project Structure

```text
RAG-PDF-AI-System/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
│
├── uploads/
├── templates/
├── static/
│
└── chroma_db/
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Yash-Ghyar/RAG-PDF-AI-System.git
```

### Navigate to Project Directory

```bash
cd RAG-PDF-AI-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key
```

### Run Application

```bash
python app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

---

## Project Highlights

* Retrieval-Augmented Generation (RAG) Pipeline
* Vector Database Integration using ChromaDB
* Semantic Search Implementation
* Large Language Model Integration
* End-to-End Document Question Answering
* Production-Oriented Flask Architecture
* Resume-Ready Generative AI Project

---

## Future Enhancements

* Multi-PDF Support
* Conversational Chat History
* Source Citation Support
* Cloud Deployment
* Advanced Retrieval Strategies
* User Authentication System

---

## Author

**Yash Ghyar**

B.Tech – Artificial Intelligence & Data Science

Vishwakarma Institute of Information Technology (VIIT), Pune

---

## Connect With Me

**GitHub**

https://github.com/Yash-Ghyar

**LinkedIn**

https://linkedin.com/in/yash-ghyar-94b58825b
