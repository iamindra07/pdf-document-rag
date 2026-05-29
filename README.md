# 📄 PDF Document RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot built using **FastAPI**, **Gemini API**, **Sentence Transformers**, and **ChromaDB**.

This project allows users to upload PDF documents and ask questions based on the document content. The chatbot retrieves the most relevant chunks using semantic search and generates grounded answers using Gemini.

---

# 🚀 Features

* Upload PDF documents
* Extract text from PDFs
* Semantic search using embeddings
* Vector database with ChromaDB
* Retrieval-Augmented Generation (RAG)
* Gemini AI integration
* FastAPI backend
* Swagger API documentation
* Context-aware AI responses

---

# 🛠️ Tech Stack

* Python
* FastAPI
* Gemini API
* Sentence Transformers
* ChromaDB
* PyPDF2
* Uvicorn

---

# 📂 Project Structure

```bash
pdf-document-rag/
│
├── main.py
├── requirements.txt
├── .env
├── uploads/
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/your-username/pdf-document-rag.git
cd pdf-document-rag
```

---

## 2. Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Create `.env` file

```env
GEMINI_API_KEY=your_api_key_here
```

---

# ▶️ Run the Project

```bash
uvicorn main:app --reload
```

Server runs on:

```bash
http://127.0.0.1:8000
```

Swagger Docs:

```bash
http://127.0.0.1:8000/docs
```

---

# 📤 Upload PDF

Use the `/upload` endpoint to upload a PDF document.

The server:

* extracts text from the PDF
* converts text into embeddings
* stores embeddings inside ChromaDB

---

# 💬 Ask Questions

Use the `/chat` endpoint.

Example:

```json
{
  "question": "What is RAG?"
}
```

The system:

1. Converts the question into embeddings
2. Finds relevant document chunks
3. Sends context + question to Gemini
4. Generates an AI response grounded in the uploaded document

---

# 🧠 How RAG Works

```text
PDF → Text Extraction → Embeddings → ChromaDB
                                      ↓
User Question → Embedding → Similarity Search
                                      ↓
Relevant Context + Question → Gemini
                                      ↓
Generated Answer
```

---

# 📸 Example Response

```json
{
  "Question": "What is RAG?",
  "Context": [
    "RAG stands for Retrieval-Augmented Generation."
  ],
  "Answer": "Based on the context provided, RAG stands for Retrieval-Augmented Generation."
}
```

---

# 📌 Future Improvements

* Multi-file support
* Chat memory
* Streaming responses
* LangGraph agent workflow
* Conversation history
* Better chunking strategy
* Hybrid search (BM25 + dense retrieval)

---

# 📖 What I Learned

* FastAPI backend development
* Vector databases
* Embeddings and semantic search
* Retrieval-Augmented Generation (RAG)
* PDF text processing
* Gemini API integration
* Building AI-powered APIs

---

# 👨‍💻 Author

Indranil Majumder

If you liked this project, consider giving it a ⭐ on GitHub.
