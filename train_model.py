import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import joblib

# Load the dataset
df = pd.read_csv("synthetic_transactions.csv")

# Select features
features = ["amount", "gas_fee", "transaction_count", "wallet_age"]
X = df[features]

# Train Isolation Forest Model
model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
model.fit(X)

# Save the model
joblib.dump(model, "fraud_detection_model.pkl")
print("✅ Model trained and saved!")
