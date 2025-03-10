**ClassiHire - a smart solution that analyzes resumes, identifies skills, and aligns candidates with the most suitable job roles**<br>

#Overview<br>
ClassiHire is an AI-powered resume classification system that categorizes resumes into different job roles using Natural Language Processing (NLP) and Machine Learning (ML). It leverages TF-IDF vectorization, a Support Vector Classifier (SVC) model, and Label Encoding to predict resume categories with high accuracy.

**Key Features**<br>
✅ Automated Resume Classification – Predicts the job category based on resume content.<br>
✅ Supports Multiple File Formats – Accepts PDF, DOCX, and TXT files.<br>
✅ Pretrained ML Model – Uses TF-IDF and SVC for accurate predictions.<br>
✅ Flask Web Application – Simple and user-friendly web interface.<br>

**Model Working**<br>
1️⃣ Upload a resume (PDF, DOCX, or TXT).<br>
2️⃣ The system extracts and cleans the text from the file.<br>
3️⃣ The pre-trained TF-IDF + SVC model processes the text.<br>
4️⃣ The resume is categorized into the most relevant job role.<br>
5️⃣ The predicted category is displayed on the web app.<br>

**web UI**<br>
🔹 Framework: Built using Flask, a lightweight Python web framework.<br>
🔹 Frontend:<br>
    Uses HTML, CSS, JavaScript for a simple & user-friendly UI.<br>
    Bootstrap ensures a responsive design.<br>
🔹 User Flow:<br>
1️⃣ Upload PDF/DOCX/TXT resume via web UI.<br>
2️⃣ System processes the file and extracts text.<br>
3️⃣ Model predicts the job category based on resume content.<br>
4️⃣ Displays the predicted category on the webpage.<br>

<img src="https://github.com/Neha-Sharma666/Classi-Hire/blob/main/web1.png">

<img src="https://github.com/Neha-Sharma666/Classi-Hire/blob/main/web2.png">

**Setup and installation**
-> Clone the Repository
    git clone https://github.com/Neha-Sharma666/Classi_Hire.git
    cd Classi_Hire
-> Run the Application
    python app.py
    
