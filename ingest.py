"""
Contains methods for ingesting file
"""
import magic

from PyPDF2 import PdfReader

def determine_filetype(path):
    """
    Uses python magic library to figure out which handler to use
    """
    type_map = {
        "PDF": read_pdf,
    }

    ftype = magic.from_file(path)
    for this in type_map.keys():
        if this in ftype:
            return type_map[this](path)
    return False

def read_pdf(path):
    """
    Attempts to pull text out of PDF
    """
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

