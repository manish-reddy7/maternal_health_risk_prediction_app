from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS  # Add this import
import pickle
import pandas as pd
import numpy as np
import warnings

# Filter out the specific version warnings
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load your trained model
try:
    with open('maternal_health_model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/predict', methods=['POST', 'OPTIONS'])
def predict():
    if request.method == 'OPTIONS':
        # Handle preflight request
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        return response
    
    try:
        # Get data from request
        data = request.get_json()
        
        # Prepare features for prediction
        features = np.array([
            data['age'],
            data['systolicBP'],
            data['diastolicBP'],
            data['bs'],
            data['bodyTemp']
        ]).reshape(1, -1)
    
        # Make prediction
        if model is None:
            return jsonify({'error': 'Model not loaded properly'})
        
        prediction = model.predict(features)
        
        # Try to get probabilities if available
        try:
            probabilities = model.predict_proba(features)
            prob_list = probabilities[0].tolist()
        except:
            # If predict_proba is not available, use dummy probabilities
            prob_list = [0.33, 0.33, 0.34]  # Equal distribution for three classes
        
        # Return results
        response = jsonify({
            'risk_level': prediction[0],
            'probabilities': prob_list
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
        
    except Exception as e:
        error_response = jsonify({'error': str(e)})
        error_response.headers.add('Access-Control-Allow-Origin', '*')
        return error_response

@app.route('/health', methods=['GET'])
def health_check():
    response = jsonify({'status': 'healthy', 'model_loaded': model is not None})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5000)