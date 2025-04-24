import pickle
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(base_dir, "../models/model.pkl")
vectorizer_path = os.path.join(base_dir, "../models/vectorizer.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(vectorizer_path, "rb") as f:
    vectorizer = pickle.load(f)

def predict_spam(message: str) -> str:
    features = vectorizer.transform([message])
    prediction = model.predict(features)[0]
    return prediction
