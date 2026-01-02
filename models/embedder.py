from typing import List
import numpy as np
from sentence_transformers import SentenceTransformer

from models.model_config import EMBEDDING_MODEL_NAME

_model = None


def _get_model() -> SentenceTransformer:
    global _model
    if _model is None:
        _model = SentenceTransformer(EMBEDDING_MODEL_NAME)
    return _model


def embed_texts(texts: List[str]) -> np.ndarray:
    """
    Deterministically embed texts.
    Output shape: (N, D), normalized.
    """
    model = _get_model()
    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=False,
    )
    return embeddings
