from typing import Dict, List

CHUNK_SIZE = 500
OVERLAP = 50

def chunk_page(page: Dict) -> List[Dict]:
    text = page["text"]
    chunks = []
    start = 0
    idx = 0

    while start < len(text):
        end = start + CHUNK_SIZE
        chunk_text = text[start:end].strip()
        if chunk_text:
            chunks.append({
                "page_number": page["page_number"],
                "chunk_index": idx,
                "text": chunk_text
            })
            idx += 1
        start = end - OVERLAP

    return chunks
