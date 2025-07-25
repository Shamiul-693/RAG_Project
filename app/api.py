from flask import Flask, request, jsonify
from app.retriever import retrieve_top_chunks
from app.generator import generate_answer

app = Flask(__name__)
vector_store = None  # Load from main later

@app.route("/query", methods=["POST"])
def query():
    data = request.get_json()
    question = data.get("query")
    chunks = retrieve_top_chunks(question, vector_store)
    context = " ".join(chunks)
    answer = generate_answer(context, question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)