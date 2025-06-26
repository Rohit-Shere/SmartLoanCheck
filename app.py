# app.py

import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model and scaler
model = joblib.load("loan_approval_RF_model.pkl")
# scaler = joblib.load("featured_loan_approval_model.pkl")  # if used

st.set_page_config(page_title="Loan Approval Predictor", layout="centered")
st.title("🏦 Loan Approval Prediction App")
st.markdown("Enter applicant details to predict loan approval status.")

# --- INPUT FORM ---
with st.form("input_form"):
    person_age = st.number_input("Age", min_value=18, max_value=100, value=30)
    person_income = st.number_input("Monthly Income (INR)", min_value=1000, value=25000)
    person_emp_lenght=st.number_input("")
    loan_amnt = st.number_input("Loan Amount Requested", min_value=1000, value=100000)
    loan_int_rate = st.slider("Interest Rate (%)", min_value=5.0, max_value=40.0, value=15.0, step=0.5)
    loan_percent_income= st.number_input("Loan Amount as % of Income", min_value=0.0, max_value=1.0,value=0.5,step=0.01)
    person_emp_length=st.number_input("No of Months of Employmen",min_value=0,max_value=300,value=4,step=1)
    
    loan_grade = st.selectbox("Loan Grade", ['A', 'B', 'C', 'D', 'E', 'F', 'G'])
    loan_grade = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7}[loan_grade]

    person_home_ownership = st.selectbox("Home Ownership", ['RENT', 'OWN', 'MORTGAGE', 'OTHER'])
    loan_intent = st.selectbox("Loan Purpose", ['PERSONAL', 'EDUCATION', 'MEDICAL', 'VENTURE', 'HOMEIMPROVEMENT', 'DEBTCONSOLIDATION'])

    cb_person_cred_hist_length=st.number_input("No of years of Credit history?")
    cb_default = st.radio("Previous Default History?", ['Y', 'N'])
    cb_default = 1 if cb_default == 'Y' else 0

    submit_btn = st.form_submit_button("Predict Approval")

# --- FEATURE ENGINEERING ---
if submit_btn:
   

    input_df = pd.DataFrame({
        'person_age': [person_age],
        'person_income': [person_income],
        'person_emp_length':[person_emp_length],
        'loan_grade': [loan_grade],
        'loan_amnt': [loan_amnt],
        'loan_int_rate': [loan_int_rate],
        'loan_percent_income':[loan_percent_income],
        'cb_person_default_on_file': [cb_default],
        'cb_person_cred_hist_length':[cb_person_cred_hist_length],
      

        # one-hot placeholders
        
        'person_home_ownership_OTHER':[0],
        'person_home_ownership_OWN': [0],
        'person_home_ownership_RENT': [0],
        'loan_intent_EDUCATION': [0],
        'loan_intent_HOMEIMPROVEMENT': [0],
        'loan_intent_MEDICAL': [0],
        'loan_intent_PERSONAL': [0],
        'loan_intent_VENTURE': [0],
        
    })

    # Set one-hot encodings
    if (f"person_home_ownership_{person_home_ownership}" in input_df.columns):
        if f"person_home_ownership_{person_home_ownership}" in input_df.columns:
            input_df[f"person_home_ownership_{person_home_ownership}"] = 1
        
        
    if(f'loan_intent_{loan_intent}' in input_df.columns):
        if f"loan_intent_{loan_intent}" in  input_df.columns:
            input_df[f"loan_intent_{loan_intent}"] = 1

    # Scale numerical cols if needed
    # cols_to_scale = ['dti', 'emi', 'balance_income', 'loan_grade_dti']
    # input_df[cols_to_scale] = scaler.transform(input_df[cols_to_scale])

    # Prediction
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    st.success("✅ Loan Approved!" if prediction == 1 else "❌ Loan Rejected.")
    st.info(f"📊 Approval Probability: {probability:.2%}")
