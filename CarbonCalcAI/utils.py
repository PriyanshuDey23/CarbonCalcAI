from docx import Document
import io

# Function to create a Word document
def create_docx(content):
    doc = Document()
    doc.add_paragraph(content)
    byte_stream = io.BytesIO()
    doc.save(byte_stream)
    byte_stream.seek(0)
    return byte_stream