import re

_WHITESPACE_RE = re.compile(r"[ \t]+") # finds space or tab space
_NEWLINE_RE =  re.compile(r"\n{3,}") # finds consecutive three or more lines

def normalize_text(text: str) -> str:
    """
    Deterministically normalize extracted text

    rules:
    normalize whitespace
    collapse excessive newelines
    """

    if not text:
        return ""
    text = _WHITESPACE_RE.sub(" ",text)
    text = _NEWLINE_RE.sub("\n\n", text)
    return text.strip()

