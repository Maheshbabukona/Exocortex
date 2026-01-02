from typing import List
import numpy as np
from sentence_transformers import SentenceTransformer

class Embedder:
    """
    Load embeddings model, generate embeddings for the text, return vectors only
    """

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        
        self.model = SentenceTransformer(model_name)
        self.model.eval() # eval mode 

    def embed_texts(self, texts: List[str]) -> np.ndarray:
        """
        Generate embeddings for list of texts. 
        args: 
        texts :  list of chunk texts

        returns: np.ndarray of shape(N,D)
        """
        embeddings = self.model.encode(
            texts, 
            convert_to_numpy=True,
            normalize_embeddings = True
        )
        return embeddings

    def embed_query(self, query: str) -> np.ndarray:
        """
        Generate embeddings for a single query
        """
        embedding = self.model.encode(
            query,
            convert_to_numpy=True,
            normalize_embeddings= True
        )
        return embedding