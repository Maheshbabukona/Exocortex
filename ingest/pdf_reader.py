import logging
from typing import List, Dict

import fitz #pymupdf - pdf manipulation, extraction

logger = logging.getLogger(__name__)

def extract_text_by_page(pdf_path: str) -> List[Dict]:
    """  
    Extracts text from pdf page by page 
    
    returns:
     page number, text
    """
    pages =[]
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        logger.error(f"Failed to open PDF{pdf_path}: {e}")
        return pages
    
    for page_index in range(len(doc)):
        try: 
            page = doc.load_page(page_index)
            text = page.get_text("text")
        except Exception as e:
            logger.warning(
                f"Failed to extract page{page_index+1} from {pdf_path}: {e}"
            )
            text = ""

        pages.append({
            "page_number": page_index+1,
            "text": text or " "
        })
    
    doc.close()
    return pages

