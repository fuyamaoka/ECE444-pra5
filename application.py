from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

application = Flask(__name__)

# Index route to confirm the app is running
@application.route("/")
def index():
    return "Your Flask App Works! V1.0"

# Load model and vectorizer
def load_model():
    with open('basic_classifier.pkl', 'rb') as fid:
        model = pickle.load(fid)
    with open('count_vectorizer.pkl', 'rb') as vd:
        vectorizer = pickle.load(vd)
    return model, vectorizer

model, vectorizer = load_model()

# /predict endpoint to make predictions
@application.route("/predict", methods=['POST'])
def predict():
    data = request.get_json()  # Get the JSON from the request
    text = data.get('text', '')  # Extract the text field

    # Transform the input text and make a prediction
    transformed_text = vectorizer.transform([text])
    prediction = model.predict(transformed_text)[0]

    # Convert the prediction to a human-readable label
    result = 'FAKE' if prediction == 1 else 'REAL'

    # Return the prediction as a JSON response
    return jsonify({'prediction': result})

if __name__ == "__main__":
    application.run(port=5000, debug=True)
