import streamlit as st
import joblib
import numpy as np

model = joblib.load("fraud_detector.pkl")

st.title("Credit Card Fraud Detection")

amount = st.number_input("Transaction Amount")
features = [amount] + list(np.random.rand(28))  # Dummy V1-V28

if st.button("Check"):
    prediction = model.predict([features])
    st.write("🚨 Fraudulent" if prediction[0] == 1 else "✅ Legitimate")
