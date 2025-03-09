from flask import Flask, request, render_template

import os
import gdown

#model_files from google drive
MODEL_FILES = {
    "clf.pkl": "https://drive.google.com/uc?id=1N8T0qori6lcQAmumwMyFJKzmSym7wT27",  
    "tfidf.pkl": "https://drive.google.com/uc?id=12WiZ8F4cGpKKberQzyiF1rLqvz2_w5eO",  
    "encoder.pkl": "https://drive.google.com/uc?id=1fKn1LO-B-qV42WrfA6RaEf0YXAkuzhuD"  
}


os.makedirs("model", exist_ok=True)

for filename, url in MODEL_FILES.items():
    file_path = os.path.join("model", filename)
    if not os.path.exists(file_path):
        print(f"Downloading {filename}...")
        gdown.download(url, file_path, quiet=False)
        print(f"Saved {filename} to {file_path}")

print("All model files are ready!")

import pickle
import docx
import PyPDF2
import re
from utils import handle_file_upload
from utils import cleanResume
from mModel import predict_category

app = Flask(__name__, static_folder="static")

# Load the trained model and preprocessing tools
svc_model = pickle.load(open('model/clf.pkl', 'rb'))
tfidf = pickle.load(open('model/tfidf.pkl', 'rb'))
le = pickle.load(open('model/encoder.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return render_template('index.html', error="No file uploaded")

    uploaded_file = request.files['file']
    if uploaded_file.filename == '':
        return render_template('index.html', error="No selected file")

    # Process the file
    resume_text = handle_file_upload(uploaded_file)
    if resume_text == "Unsupported file type":
        return render_template('index.html', error="Unsupported file type")

    # Clean text and predict category
    cleaned_text = cleanResume(resume_text)
    category = predict_category(cleaned_text)

    return render_template('index.html', prediction=f"The predicted category is: {category}")

if __name__ == '__main__':
    app.run(debug=True)
