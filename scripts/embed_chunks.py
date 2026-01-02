from storage.chunk_repo import get_chunks_by_artifact
from storage.embedding_repo import insert_embedding
from models.embedder import embed_texts
from models.model_config import EMBEDDING_MODEL_NAME

artifact_id = 1

chunks = get_chunks_by_artifact(artifact_id)
texts = [c["text"] for c in chunks]

vectors = embed_texts(texts)

for c, v in zip(chunks, vectors):
    insert_embedding(
        chunk_id=c["id"],
        model_name=EMBEDDING_MODEL_NAME,
        vector=v.astype("float32").tobytes()
    )

print("embeddings inserted:", len(chunks))
