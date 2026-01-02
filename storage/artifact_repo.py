from datetime import datetime
from typing import Optional
from storage.db import get_connection


def insert_artifact(file_hash: str, source_path: str) -> int:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT OR IGNORE INTO artifacts (file_hash, source_path, created_at)
        VALUES (?, ?, ?)
        """,
        (file_hash, source_path, datetime.utcnow().isoformat() + "Z")
    )

    conn.commit()

    cur.execute(
        "SELECT id FROM artifacts WHERE file_hash = ?",
        (file_hash,)
    )
    row = cur.fetchone()
    return row["id"]


def get_artifact_by_hash(file_hash: str) -> Optional[dict]:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM artifacts WHERE file_hash = ?",
        (file_hash,)
    )
    row = cur.fetchone()
    return dict(row) if row else None
