from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

def get_embeddings(text_chunks):
    return model.encode(text_chunks, show_progress_bar=True)