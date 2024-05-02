"""
This module initializes a Flask application and loads a trained model for predictions.
It also sets up Firebase for data storage and retrieval.
"""

from flask import Flask, render_template, request, jsonify
from joblib import load
from firebase_admin import db
import firebase_admin
from firebase_admin import credentials

app = Flask(__name__)

# Load the trained model from the saved file
MODEL_FILE_PATH = 'svm_model.pkl'
loaded_model = load(MODEL_FILE_PATH)

# Initialize Firebase
cred_obj = credentials.Certificate('crops-prediction-57b7c-firebase-adminsdk-9g39z-4f541dd1e0.json')
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': 'https://crops-prediction-57b7c-default-rtdb.firebaseio.com/'
})

# Get a reference to the database service
ref = db.reference('/preds')

# Dictionary mapping label encoded numbers to label text
label_encoded_to_text = {
    0: 'apple', 1: 'banana', 2: 'blackgram', 3: 'chickpea', 4: 'coconut',
    5: 'coffee', 6: 'cotton', 7: 'grapes', 8: 'jute', 9: 'kidneybeans',
    10: 'lentil', 11: 'maize', 12: 'mango', 13: 'mothbeans', 14: 'mungbean',
    15: 'muskmelon', 16: 'orange', 17: 'papaya', 18: 'pigeonpeas',
    19: 'pomegranate', 20: 'rice', 21: 'watermelon'
}
@app.route('/')
def home():
    """
    Renders the 'index.html' template.

    Returns:
        The rendered template.
    """
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_crop():
    """
    Predicts the crop based on the input data.

    Returns:
        A JSON response containing the predicted crop.
    """
    # Receive input data from the user
    data = request.get_json()

    # Extract required features from input data
    features = ['N', 'P', 'K', 'humidity', 'rainfall']
    input_features = [data[feature] for feature in features]

    # Make predictions using the loaded model
    predictions = loaded_model.predict([input_features])

    # Use the predicted label encoded number to retrieve the corresponding label text
    predicted_label_text = label_encoded_to_text[predictions[0]]

    # Push the input data and prediction to Firebase
    ref.set({
        'input_data': data,
        'prediction': predicted_label_text
    })

    # Return the predicted crop as JSON response
    return jsonify({'predicted_crop': predicted_label_text})


if __name__ == '__main__':
    app.run(debug=True, port=5002)