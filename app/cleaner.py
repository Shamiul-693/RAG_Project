import re

def clean_text(text):
    text = re.sub(r"\n+", "\n", text)  # Remove excessive newlines
    text = re.sub(r"[\u200c\u200d]", "", text)  # Remove Zero-width chars
    text = re.sub(r"[^ঀ-৿\s\.,!?\-\(\)\"]", "", text)  # Keep Bangla + punctuation
    text = re.sub(r"\s+", " ", text)
    return text.strip()