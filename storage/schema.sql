PRAGMA foreign_keys = ON;

-- =========================
-- ARTIFACTS
-- =========================

CREATE TABLE IF NOT EXISTS artifacts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_hash TEXT NOT NULL UNIQUE,
    source_path TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE TABLE chunks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    artifact_id INTEGER NOT NULL,
    page_number INTEGER NOT NULL,
    chunk_index INTEGER NOT NULL,
    text TEXT NOT NULL,
    FOREIGN KEY(artifact_id) REFERENCES artifacts(id) on DELETE CASCADE,
    UNIQUE(artifact_id, page_number, chunk_index)
);

CREATE TABLE embeddings(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chunk_id INTEGER NOT NULL,
    model_name TEXT NOT NULL,
    vector BLOB NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY(chunk_id) REFERENCES chunks(id) ON DELETE CASCADE,
UNIQUE(chunk_id, model_name)
);