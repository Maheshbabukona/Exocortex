import logging
from typing import Callable, Dict, List

from ingest.scanner import scan_pdf_folder
from ingest.pdf_reader import extract_text_by_page
from ingest.normalizer import normalize_text

logger = logging.getLogger(__name__)

def run_ingestion_pipeline(
        folder_path:str,
        is_already_ingested: Callable[[str],bool],
        emit: Callable[[Dict],None],
):
    """
    orchestrate ingestion:
    """
    for file_meta in scan_pdf_folder(folder_path):
        file_hash = file_meta["hash"]

        if is_already_ingested(file_hash):
            logger.info(f"Skipping unchanged file: {file_meta['path']}")
            continue
        
        logger.info(f"Ingesting File: {file_meta['path']}")

        pages = extract_text_by_page(file_meta['path'])

        normalized_pages: List[Dict] =[]

        for page in pages:
            normalized_pages.append({
                "page_number": page["page_number"],
                "text": normalize_text(page["text"]),
            })
        payload ={
            "source_path": file_meta["path"],
            "file_hash": file_hash,
            "pages": normalized_pages,
        }

        emit(payload)
    
