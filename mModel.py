import pickle
import os


model_folder = os.path.join(os.getcwd(), "model")


svc_model = pickle.load(open(os.path.join(model_folder, 'clf.pkl'), 'rb'))
tfidf = pickle.load(open(os.path.join(model_folder, 'tfidf.pkl'), 'rb'))
le = pickle.load(open(os.path.join(model_folder, 'encoder.pkl'), 'rb'))

def predict_category(resume_text):
    vectorized_text = tfidf.transform([resume_text]).toarray()
    predicted_category = svc_model.predict(vectorized_text)
    category_name=le.inverse_transform(predicted_category)[0]
    return category_name

