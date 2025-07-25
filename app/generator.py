# app/generator.py (Improved for Ollama)
import requests

def generate_answer(context, question):
    prompt = f"""
    তুমি একজন বাংলা সাহিত্য বিশারদ। শুধুমাত্র নিচের প্রসঙ্গ (context) ব্যবহার করে প্রশ্নের উত্তর দাও। অনুমান করো না।

    প্রসঙ্গ:
    {context}

    প্রশ্ন:
    {question}

    উত্তর:
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code == 200:
        return response.json().get("response", "উত্তর খুঁজে পাওয়া যায়নি।").strip()
    else:
        return "উত্তর তৈরি করতে সমস্যা হয়েছে।"