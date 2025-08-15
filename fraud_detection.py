import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.title("Fraud Detection Prediction App")

st.markdown("Please enter the trasaction details and use predict button")

st.divider()

# Load trained pipeline from this folder
try:
    _model_path = Path(__file__).resolve().parent / "fraud_Detection_pipeline.pkl"
    model = joblib.load(str(_model_path))
except Exception as e:
    model = None
    st.error(f"Failed to load model: {e}")

transaction_type = st.selectbox("Trasaction Type", ("PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"))
Amount = st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("old Balance (sender)", min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input("old Balance (Receiver)", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("new Balance (Receiver)", min_value=0.0, value=0.0)

if st.button("predict"):
    input_data = pd.DataFrame([{
        "type" : transaction_type,
        "Amount" : Amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig":newbalanceOrig,
        "oldbalanceDest":oldbalanceDest,
        "newbalanceDest":newbalanceDest,
    }])

    # Some pipelines expect lowercase 'amount'
    if "Amount" in input_data.columns and "amount" not in input_data.columns:
        input_data["amount"] = input_data["Amount"]


    if model is None:
        st.stop()
    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction: '{int(prediction)}'")
    if prediction == 1:
        st.error("this Trasaction might be fraud")
    else:
        st.success("this transaction is not fraud it is all right")
