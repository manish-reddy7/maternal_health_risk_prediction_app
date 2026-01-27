# Maternal Health Risk Prediction App

A demo machine learning web application that predicts maternal health risk levels based on clinical parameters using a trained Random Forest model.

![Maternal Health Risk Analysis Demo](image1)

> **⚠️ Disclaimer:** This is a demonstration project for educational purposes only. It is **NOT** a medical device and must **NOT** be used as a substitute for professional medical advice, diagnosis, or treatment.

---

## Overview

This project demonstrates an end-to-end machine learning workflow:
- Data preprocessing and exploratory data analysis
- Model training with hyperparameter tuning (GridSearchCV)
- Flask API backend for serving predictions
- Modern, responsive web UI for user interaction

---

## Features

### 🤖 Machine Learning Model
- Random Forest classifier trained on the Maternal Health Risk dataset
- Hyperparameter optimization using GridSearchCV
- Predicts risk levels: Low, Mid, or High
- Model persisted as `maternal_health_model.pkl`

### 🌐 Flask API Backend
- **`GET /`** – Serves the web interface
- **`GET /health`** – Health check endpoint
- **`POST /predict`** – Returns risk predictions with confidence scores

### 💻 Web Interface
- Clean, two-panel layout for patient input and risk assessment
- Real-time validation (e.g., systolic BP > diastolic BP)
- Visual confidence indicators with color-coded risk levels
- Backend status monitoring
- Responsive design for desktop and tablet

---

## Project Structure

```
ml_project/
├── app.py                              # Flask API server
├── index.html                          # Frontend UI
├── Maternal Health Risk Data Set.csv   # Training dataset
├── maternal_health_model.pkl           # Trained model
└── ml_project.ipynb                    # Jupyter notebook (EDA + training)
```

---

## How It Works

### 1. Model Training
The Jupyter notebook handles:
- Loading and exploring the dataset
- Data cleaning (removing outliers)
- Feature selection: Age, SystolicBP, DiastolicBP, Blood Glucose, Body Temperature
- Training and tuning a Random Forest classifier
- Saving the model to `maternal_health_model.pkl`

### 2. Prediction API
The Flask backend:
- Loads the pre-trained model on startup
- Accepts patient data via POST request
- Returns risk level prediction and confidence probabilities

**Example Request:**
```json
{
  "age": 30,
  "systolicBP": 120,
  "diastolicBP": 80,
  "bs": 7.0,
  "bodyTemp": 98.6,
  "heartRate": 80
}
```

**Example Response:**
```json
{
  "risk_level": "low risk",
  "probabilities": [0.85, 0.10, 0.05]
}
```

### 3. Web Interface
The UI displays:
- Input form with validation
- Color-coded risk assessment (green/yellow/red)
- Animated confidence bar
- Error handling for backend connectivity issues

---

## Getting Started

### Prerequisites
- Python 3.9+
- Virtual environment (recommended)

### Installation

1. **Install dependencies:**
```bash
pip install flask flask-cors scikit-learn pandas numpy
```

2. **Run the Flask server:**
```bash
python app.py
```

3. **Open your browser:**
Navigate to `http://127.0.0.1:5000/`

You should see the interface shown in the screenshot above. Enter patient information and click "Analyze Risk Level" to get predictions.

---

## API Reference

### Health Check
```
GET /health
```
**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

### Predict Risk Level
```
POST /predict
```
**Request Body:**
```json
{
  "age": 30,
  "systolicBP": 120,
  "diastolicBP": 80,
  "bs": 7.0,
  "bodyTemp": 98.6,
  "heartRate": 80
}
```

**Response:**
```json
{
  "risk_level": "mid risk",
  "probabilities": [0.15, 0.70, 0.15]
}
```

*Note: `heartRate` is currently optional and not used by the model, but kept for future extensions.*

---

## Future Enhancements

- 🔐 Add authentication and request logging
- 🐳 Containerize with Docker
- ☁️ Deploy to cloud platforms (Azure, AWS, Heroku)
- 📊 Include additional features in the model
- 📱 Improve mobile responsiveness

---

## License

This project is for educational and demonstration purposes only.

**Medical Disclaimer:** This tool provides model-based estimates only. It is not a medical device and must not be used as a substitute for professional medical advice, diagnosis, or treatment.