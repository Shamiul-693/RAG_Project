import re

def chunk_text(text, max_len=512):
    sentences = re.split(r'(?<=[।!?])\s+', text)
    chunks, current = [], ""
    for sent in sentences:
        if len(current) + len(sent) <= max_len:
            current += sent + " "
        else:
            chunks.append(current.strip())
            current = sent + " "
    if current:
        chunks.append(current.strip())
    return chunks
