from datetime import datetime
from storage.db import get_connection


def insert_embedding(
    chunk_id: int,
    model_name: str,
    vector: bytes
) -> None:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT OR IGNORE INTO embeddings
        (chunk_id, model_name, vector, created_at)
        VALUES (?, ?, ?, ?)
        """,
        (chunk_id, model_name, vector, datetime.utcnow().isoformat() + "Z")
    )

    conn.commit()


def get_embeddings_for_model(model_name: str) -> list[dict]:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT * FROM embeddings
        WHERE model_name = ?
        """,
        (model_name,)
    )

    return [dict(row) for row in cur.fetchall()]
