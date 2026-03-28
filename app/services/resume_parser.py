from multiprocessing import Value
import fitz
import docx
import io

def extract_text_from_pdf(file_bytes : bytes) -> str:
    pdf = fitz.open(stream= file_bytes, filetype= "pdf")
    text = ""

    for page in pdf:
        text += page.get_text()

    return text

def extract_text_from_docx(file_bytes: bytes) -> str:
    doc = docx.Document(io.BytesIO(file_bytes))

    text = ""

    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"

    return text

def extract_text(file_bytes : bytes, file_name: str) -> str:
    if file_name.endswith("pdf"):
        return extract_text_from_pdf(file_bytes)
    elif file_name.endswith("docx"):
        return extract_text_from_docx(file_bytes)
    else:
        raise ValueError("Unsupported file type. only Pdf and Docx are allowed.")

