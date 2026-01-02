import numpy as np
from typing import List, Dict

from models.embedder import embed_texts
from models.model_config import EMBEDDING_DTYPE
from storage.embedding_repo import get_embeddings_for_model
from models.model_config import EMBEDDING_MODEL_NAME


def _bytes_to_vector(blob: bytes) -> np.ndarray:
    return np.frombuffer(blob, dtype=EMBEDDING_DTYPE)


def semantic_search(query: str, top_k: int = 5) -> List[Dict]:
    """
    Returns ranked chunk_ids with similarity scores.
    """
    query_vec = embed_texts([query])[0]

    rows = get_embeddings_for_model(EMBEDDING_MODEL_NAME)

    scored = []
    for row in rows:
        vec = _bytes_to_vector(row["vector"])
        score = float(np.dot(query_vec, vec))  # cosine (normalized)
        scored.append({
            "chunk_id": row["chunk_id"],
            "score": score,
        })

    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored[:top_k]
