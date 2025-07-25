from app.pdf_loader import extract_text_from_pdf
from app.cleaner import clean_text
from app.chunker import chunk_text
from app.embedder import get_embeddings
from app.vector_store import VectorStore
from app.retriever import retrieve_top_chunks
from app.generator import generate_answer

PDF_PATH = "data/HSC26-Bangla1st-Paper.pdf"

if __name__ == "__main__":
    print("✅ শুরু হচ্ছে...")

    print("📄 PDF লোড হচ্ছে...")
    text = extract_text_from_pdf(PDF_PATH)

    print("🧹 টেক্সট ক্লিন হচ্ছে...")
    text = clean_text(text)

    print("✂️ চাঙ্কে ভাগ হচ্ছে...")
    chunks = chunk_text(text)
    print(f"🔹 মোট চাঙ্ক: {len(chunks)}")

    print("🔎 এমবেডিং তৈরি হচ্ছে...")
    embeddings = get_embeddings(chunks)

    print("💾 ভেক্টর স্টোরে যোগ করা হচ্ছে...")
    vstore = VectorStore(dim=len(embeddings[0]))
    vstore.add(embeddings, chunks)

    print("🤖 প্রশ্নের উত্তর তৈরি হচ্ছে...")
    query = "অনুপমের ভাষায় সুপুরুষ কাকে বলা হয়েছে?"
    top_chunks = retrieve_top_chunks(query, vstore, k=10)

    print("🔍 রিলেভেন্ট চাঙ্কগুলো:")
    for i, chunk in enumerate(top_chunks, 1):
        print(f"Chunk {i}: {chunk[:200]}...\n")

    context = " ".join(top_chunks)
    answer = generate_answer(context, query)

    print("📌 প্রশ্ন:", query)
    print("✅ উত্তর:", answer)
