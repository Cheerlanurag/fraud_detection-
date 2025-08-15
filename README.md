## Fraud Detection Project

This project implements a machine learning-based fraud detection system. The core goal is to accurately classify whether a given transaction exhibits signs of fraud based on key financial inputs and transaction details.

### Features

- *Data Processing*: Takes user inputs such as transaction amount, old and new balances for sender and receiver, and transaction type.
- *Model Training & Pipeline*: The heart of the system is a trained ML model saved as a pipeline (fraud_Detection_pipeline.pkl), which leverages standard preprocessing and classification techniques for fraud analysis.
- *Streamlit Web App*: A user-friendly Streamlit interface allows users to enter transaction details and immediately receive a prediction about fraud risk.
- *End-to-End Workflow*: Includes all steps from data ingestion and processing, to prediction and UI deployment for hands-on experimentation.
- *Easy Extension*: Modular code enables new features, dataset swaps, or further ML enhancements.

### Usage

1. *Clone the repo and install requirements.*
2. *Run the app:*  
   
   streamlit run fraud_detection.py
   
3. *Input transaction fields in the web interface.*
4. *Get instant feedback* on whether a transaction is likely to be fraudulent.

### Technologies

- Python (pandas, scikit-learn, joblib)
- Streamlit

### Why This Project

Detecting fraudulent transactions in real time is crucial for financial institutions and e-commerce platforms. This project delivers a practical demonstration of using machine learning for fraud prevention, complete with live prediction and an interactive UI.
