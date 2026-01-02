import os
import hashlib
import logging 
from typing import Iterator, Dict

logger = logging.getLogger(__name__)


def compute_file_hash(path: str, chunk_size: int=8192) ->str:
    """
    compute a deterministic sha256 hash for as file.

    """
    sha256 = hashlib.sha256()
    with open(path,"rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            sha256.update(chunk)
    return sha256.hexdigest()

def scan_pdf_folder(folder_path: str) -> Iterator[Dict]:
    """
    Scan a folder recursively and yield metadata for each pdf found.

    output format is storage agnostic and deterministic.
    """
    if not os.path.isdir(folder_path):
        raise ValueError(f"Not a directory: {folder_path}")
    
    for root, _, files in os.walk(folder_path):
        for filename in sorted(files):
            if not filename.lower().endswith("pdf"):
                continue

            full_path = os.path.join(root,filename)

            try:
                file_hash = compute_file_hash(full_path)
            except Exception as e:
                logger.error(f"Failed to hash file {full_path}: e")

            yield {
                "path": full_path,
                "filename": filename,
                "hash": file_hash
            }


