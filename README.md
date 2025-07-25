
# Bengali PDF-based RAG QA System

This project implements a simple Bengali Retrieval-Augmented Generation (RAG) pipeline using OCR, vector search (FAISS), and a local LLM (Ollama with Mistral) to answer questions from scanned Bangla PDFs.

---

## ✅ Setup Guide

1. Clone the repository:

```bash
git clone https://github.com/Shamiul-693/RAG_Project.git
cd rag_project
```

2. Create and activate virtual environment:

```bash
python -m venv venv
venv\Scripts\activate.bat
```

3. Install requirements:

```bash
pip install -r requirements.txt
```

4. Install Poppler (required for pdf2image):

- Download from: [https://github.com/oschwartz10612/poppler-windows/releases/](https://github.com/oschwartz10612/poppler-windows/releases/)
- Extract to a folder, e.g. `C:\poppler`
- Add `C:\poppler\Library\bin` to your system PATH

5. Install Tesseract OCR:

- Download from: [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)
- Add to PATH: `C:\Program Files\Tesseract-OCR\`
- Ensure `ben.traineddata` exists in `C:\Program Files\Tesseract-OCR\tessdata`

6. Install and run Ollama with mistral model:

```bash
ollama run mistral
```

---

## 🧰 Tools, Libraries, Packages Used

- Python 3.10+
- pytesseract (OCR)
- pdf2image
- sentence-transformers
- faiss-cpu
- ollama
- tqdm, re, nltk, numpy

---

## 💡 Sample Queries and Output

- Query (Bangla): `অনুপমের ভাষায় সুপুরুষ কাকে বলা হয়েছে?`
- Output (Bangla): `ুম্ভনাথ `

---

## 📡 API Documentation 

If exposed via FastAPI:

```python
@app.post("/ask")
def ask_question(file: UploadFile, query: str):
    # Process PDF and run RAG
    return {"answer": "..." }
```

---

## 📊 Evaluation Matrix (optional)

| Metric           | Description                                    |
| ---------------- | ---------------------------------------------- |
| Top-k Accuracy   | If correct chunk is among top k retrieved      |
| BLEU/ROUGE Score | Comparing generated answer vs reference answer |
| Manual Check     | Human judgment for answer relevance            |

---

## 🤔 Questions & Answers

1. 🔍 What method/library did you use to extract the text and why?

   - Used pytesseract + pdf2image since the PDF is scanned.
   - Challenge: OCR quality may vary with noise or poor layout.

2. ✂️ What chunking strategy did you choose?

   - Sentence or paragraph-based chunks (\~400 chars).
   - Works well for semantic search and maintains context.

3. 🧠 What embedding model did you use and why?

   - `paraphrase-multilingual-MiniLM-L12-v2`
   - Lightweight, supports Bengali, good semantic matching.

4. 📌 How are you comparing the query with chunks?

   - Used FAISS with cosine similarity.
   - Fast vector retrieval and scalable.

5. 🔎 How do you ensure meaningful comparison?

   - Consistent preprocessing, same embedder for query + chunks.
   - Handles vague queries by increasing top-k or fallback keyword search.

6. ✅ Are results relevant?

   - Mostly yes.
   - Improvements: better chunking, OCR cleanup, embedding tuning.

---

## 📂 Folder Structure

```
rag_project/
├── app/
│   ├── pdf_loader.py
│   ├── cleaner.py
│   ├── chunker.py
│   ├── embedder.py
│   ├── vector_store.py
│   ├── retriever.py
│   └── generator.py
├── data/
│   └── HSC26-Bangla1st-Paper.pdf
├── main.py
├── requirements.txt
└── README.md
```

---


