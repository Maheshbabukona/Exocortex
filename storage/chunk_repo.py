from typing import List
from storage.db import get_connection


def insert_chunks(
    artifact_id: int,
    page_number: int,
    chunks: List[str]
) -> None:
    conn = get_connection()
    cur = conn.cursor()

    for idx, text in enumerate(chunks):
        cur.execute(
            """
            INSERT OR IGNORE INTO chunks
            (artifact_id, page_number, chunk_index, text)
            VALUES (?, ?, ?, ?)
            """,
            (artifact_id, page_number, idx, text)
        )

    conn.commit()


def get_chunks_by_artifact(artifact_id: int) -> list[dict]:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT * FROM chunks
        WHERE artifact_id = ?
        ORDER BY page_number, chunk_index
        """,
        (artifact_id,)
    )

    return [dict(row) for row in cur.fetchall()]
