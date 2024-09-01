from flask import Flask, request, render_template, send_file
from pdf2docx import Converter
from docx import Document
from io import BytesIO
import os

app = Flask(__name__)

# PDF to Word Conversion
@app.route('/convert_pdf_to_word', methods=['POST'])
def convert_pdf_to_word():
    pdf_file = request.files['pdf_file']
    pdf_path = os.path.join("uploads", pdf_file.filename)
    pdf_file.save(pdf_path)

    docx_file = pdf_path.replace('.pdf', '.docx')
    cv = Converter(pdf_path)
    cv.convert(docx_file)
    cv.close()

    return send_file(docx_file, as_attachment=True)

# Word to PDF Conversion
@app.route('/convert_word_to_pdf', methods=['POST'])
def convert_word_to_pdf():
    word_file = request.files['word_file']
    word_path = os.path.join("uploads", word_file.filename)
    word_file.save(word_path)

    pdf_file = word_path.replace('.docx', '.pdf')
    document = Document(word_path)
    pdf_buffer = BytesIO()
    document.save(pdf_buffer)
    pdf_buffer.seek(0)

    return send_file(pdf_buffer, as_attachment=True, download_name=pdf_file)

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    os.makedirs("uploads", exist_ok=True)
    app.run(debug=True)
