from pypdf import PdfReader


def load_pdf_text(pdf_file):
    """
    Extract text from uploaded PDF.
    """

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted

    return text