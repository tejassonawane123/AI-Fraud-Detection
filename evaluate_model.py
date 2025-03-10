from sklearn.metrics import precision_score, recall_score, f1_score
import pandas as pd
import joblib

# Load dataset and model
df = pd.read_csv("synthetic_transactions.csv")
model = joblib.load("fraud_detection_model.pkl")

# Select features
X = df[["amount", "gas_fee", "transaction_count", "wallet_age"]]
y_true = df["is_fraud"]

# Get predictions
y_pred = model.predict(X)
y_pred = [1 if p == -1 else 0 for p in y_pred]

# Calculate metrics
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

print(f"🔹 Precision: {precision:.2f}")
print(f"🔹 Recall: {recall:.2f}")
print(f"🔹 F1-Score: {f1:.2f}")
