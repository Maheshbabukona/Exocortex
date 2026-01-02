import json
import os
from typing import Set

MANIFEST_PATH = "manifest.json"

def _load() -> Set[str]:
    if not os.path.exists(MANIFEST_PATH):
        return set()
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        return set(json.load(f))

def _save(hashes: Set[str]):
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(sorted(list(hashes)), f, indent=2)

def is_already_ingested(file_hash: str) -> bool:
    return file_hash in _load()

def record_ingestion(file_hash: str):
    hashes = _load()
    hashes.add(file_hash)
    _save(hashes)
