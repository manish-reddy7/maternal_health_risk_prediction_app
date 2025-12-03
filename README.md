# Maternal Health Risk Prediction App

This project is a small end‑to‑end machine learning application that predicts maternal health risk levels based on clinical parameters. It combines a trained Random Forest model, a Flask API backend, and a modern, responsive HTML/JavaScript frontend for interactive risk assessment.



> **Important:** This application is for educational and demonstration purposes only. It is **not** a medical device and must **not** be used as a substitute for professional medical advice, diagnosis, or treatment.

---

## Features

- **Machine‑learning model**
  - Random Forest classifier trained on the *Maternal Health Risk Data Set*.
  - Hyperparameter tuning using `GridSearchCV`.
  - Model persisted as `maternal_health_model.pkl` and loaded by the API.

- **Flask API backend** (`app.py`)
  - `GET /` – serves the web UI (`index.html`).
  - `GET /health` – simple health‑check endpoint (`{"status": "healthy", "model_loaded": true}`).
  - `POST /predict` – accepts patient data in JSON and returns predicted risk level and class probabilities.

- **Modern web UI** (`index.html`)
  - Clean two‑panel layout: *Patient Information* (inputs) and *Risk Assessment* (results).
  - Inline validation (e.g., prevents Diastolic BP greater than Systolic BP).
  - Shows backend/model health status, risk level badge, and confidence bar.
  - Responsive design for desktop and tablet.

---

## Project Structure

```text
ml_project/
├─ app.py                     # Flask API server
├─ index.html                 # Frontend UI (served at /)
├─ Maternal Health Risk Data Set.csv  # Original dataset used for training
├─ maternal_health_model.pkl  # Trained Random Forest model (GridSearchCV)
└─ ml_project .ipynb    # Jupyter notebook with EDA and model training
```

---

## How It Works

1. **Training (not required to run the app)**
   - The notebook `ml_project - Copy.ipynb`:
     - Loads `Maternal Health Risk Data Set.csv`.
     - Performs exploratory data analysis (EDA).
     - Removes clearly invalid heart‑rate outliers and drops the `HeartRate` feature.
     - Trains and tunes a Random Forest classifier using the following predictors:
       - `Age`
       - `SystolicBP`
       - `DiastolicBP`
       - `BS` (blood glucose)
       - `BodyTemp`
     - Saves the tuned model to `maternal_health_model.pkl`.

2. **Serving predictions**
   - `app.py` loads `maternal_health_model.pkl` on startup.
   - When the frontend submits the form, it issues a `POST /predict` with JSON:

     ```json
     {
       "age": 30,
       "systolicBP": 120,
       "diastolicBP": 80,
       "bs": 7.0,
       "bodyTemp": 98.6,
       "heartRate": 80   // optional, currently ignored by the model
     }
     ```

   - The backend converts these values into a feature vector `[age, systolicBP, diastolicBP, bs, bodyTemp]`, calls the model, and returns:

     ```json
     {
       "risk_level": "low risk",   // model prediction
       "probabilities": [0.85, 0.10, 0.05]
     }
     ```

3. **Displaying results**
   - The UI updates the *Risk Assessment* panel:
     - Colors the card based on `risk_level` (low / mid / high).
     - Animates a confidence bar using the highest probability.
     - Shows messages if the backend is unavailable or an error occurs.

---

## Running the App Locally

### Prerequisites

- Python 3.9+ installed on your machine.
- Recommended: create and activate a virtual environment.
- Install required Python packages (for example):

```bash
pip install flask flask-cors scikit-learn pandas numpy
```

> You **do not** need to retrain the model to run the app; `maternal_health_model.pkl` is already included.

### Start the Flask server

From the project directory (`ml_project`):

```bash
python app.py
```

You should see output similar to:

```text
Model loaded successfully
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

### Open the UI

- Navigate in your browser to: <http://127.0.0.1:5000/>
- The home page will show the **Maternal Health Risk Analysis** interface (screenshot above).
- Fill in the patient information and click **Analyze Risk Level** to see the prediction.

---

## API Reference

### `GET /health`

Health‑check endpoint used by the UI.

**Response (example):**

```json
{
  "status": "healthy",
  "model_loaded": true
}
```

### `POST /predict`

Accepts patient data and returns model predictions.

**Request body:**

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

> `heartRate` is currently optional and ignored by the model, but kept for future extensions and UI completeness.

**Response (example):**

```json
{
  "risk_level": "mid risk",
  "probabilities": [0.15, 0.70, 0.15]
}
```

---

## Extending the Project

Some ideas if you want to take this further:

- **Retrain with additional features**
  - Update the notebook to include `HeartRate` or other engineered features.
  - Save a new model and adjust `app.py` and the UI to match the new feature set.

- **Add authentication and logging**
  - Protect the API and log anonymized prediction requests for auditing.

- **Containerize the app**
  - Add a `Dockerfile` and `docker-compose.yml` so the app can be run with a single `docker compose up`.

- **Deploy to the cloud**
  - Host the Flask app on a platform‑as‑a‑service (for example Azure App Service, Heroku, etc.) and serve the static UI from the same backend.

---

## Disclaimer

This repository is intended **only** for learning and experimentation with basic machine‑learning deployment patterns (model training, persistence, and web serving). It must **not** be used for clinical decision making or in any safety‑critical environment.
