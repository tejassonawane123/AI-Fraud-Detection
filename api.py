from fastapi import FastAPI
import joblib
import numpy as np

# Load trained model
model = joblib.load("fraud_detection_model.pkl")

# Initialize API
app = FastAPI()

@app.get("/status")
def get_status():
    return {"status": "Model is trained and ready!"}

@app.post("/detect_fraud")
def detect_fraud(transaction: dict):
    features = np.array([[transaction["amount"], transaction["gas_fee"], transaction["transaction_count"], transaction["wallet_age"]]])
    prediction = model.predict(features)[0]
    fraud_probability = 1 if prediction == -1 else 0
    return {"fraud_probability": fraud_probability}
