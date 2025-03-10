# AI Fraud Detection System  
🚀 Detect fraudulent blockchain transactions using machine learning  

## 📌 Project Overview  
This project builds an AI-based fraud detection system for blockchain transactions. It generates a synthetic dataset, trains an anomaly detection model, and provides a REST API for fraud detection.  

- **Dataset:** 5,000 synthetic transactions  
- **Model:** Isolation Forest for anomaly detection  
- **API:** FastAPI-based REST service  
- **Evaluation:** Precision, Recall, F1-score  

---

## 📌 Installation & Setup  

### 1️⃣ Clone the Repository  
```cmd
git clone https://github.com/tejassonawane123/AI-Fraud-Detection.git
cd AI-Fraud-Detection
2️⃣ Create Virtual Environment 
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Generate Synthetic Dataset
python generate_dataset.py
✅ Output: synthetic_transactions.csv
5️⃣ Train the Fraud Detection Model
python train_model.py
✅ Output: fraud_detection_model.pkl
6️⃣ Run the API Server
python api.py
✅ Server URL: http://127.0.0.1:8000/

📌 API Endpoints
Method	Endpoint	Description
GET	/status	Check API health
POST	/detect_fraud	Detect fraud in a transaction

📌 Model Evaluation
Run the evaluation script to compute Precision, Recall, and F1-score:
python evaluate_model.py
📌 Dependencies
pandas
scikit-learn
fastapi
uvicorn
Install all with:
pip install -r requirements.txt
📌 Folder Structure
AI-Fraud-Detection/
│── api.py                # REST API for fraud detection  
│── train_model.py        # Model training script  
│── generate_dataset.py   # Creates synthetic dataset  
│── evaluate_model.py     # Model evaluation  
│── fraud_detection_model.pkl  # Trained model  
│── synthetic_transactions.csv  # Generated dataset  
│── requirements.txt      # Dependencies  
│── README.md             # Project documentation 
