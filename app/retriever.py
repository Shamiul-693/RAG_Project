from app.embedder import model

def retrieve_top_chunks(query, vector_store, k=3):
    query_vec = model.encode([query])[0]
    return vector_store.search(query_vec, k)
