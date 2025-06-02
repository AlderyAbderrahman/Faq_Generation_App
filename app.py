from flask import Flask, render_template, request
import pdfplumber
from utils import generate_faq 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    extracted_text = ""
    faqs = ""
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename.endswith('.pdf'):
            with pdfplumber.open(uploaded_file) as pdf:
                for page in pdf.pages:
                    extracted_text += page.extract_text()

            faqs = generate_faq(extracted_text)

    return render_template('index.html', text=extracted_text, faqs=faqs)

if __name__ == '__main__':
    app.run(debug=True)