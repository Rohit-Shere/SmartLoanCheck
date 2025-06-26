# SmartLoanCheck
# 📄 LoanLens: ML-Powered Loan Approval Predictor

LoanLens is a professional Streamlit web application that predicts whether a loan application is likely to be approved or not. Powered by a machine learning model trained on real-world credit data, it provides instant predictions with high accuracy and transparency.

---

## 🚀 Live Demo
👉 [Click here to try the app](https://your-username.streamlit.app) *(Replace with your actual link after deployment)*

---

## 🧠 Features
- Interactive form to input applicant details  
- Real-time loan approval prediction  
- Probability score output for better interpretability  
- Professional UI with clean layout  
- Based on Random Forest Classifier with 93% accuracy

---

## 🛠️ Tech Stack
- **Python**  
- **Streamlit** (frontend)  
- **scikit-learn** (modeling)  
- **Pandas** / **NumPy** (data processing)  
- **Joblib** (model persistence)

---

## 📦 Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/loanlens-app.git
cd loanlens-app
```

### 2. Install dependencies
```bash
pip install -r requirements.txt 
```

### 3. Run the app
```bash
streamlit run app.py 
```

---

## 📈 Model Details
- **Model Used:** Random Forest Classifier  
- **Accuracy:** 93%  
- **ROC AUC Score:** 0.93+  
- **Features Used:**
  - `person_age`  
  - `person_income`  
  - `person_emp_length`  
  - `loan_grade`  
  - `loan_amnt`  
  - `loan_int_rate`  
  - `loan_percent_income`  
  - `cb_person_default_on_file`  
  - `cb_person_cred_hist_length`  
  - `person_home_ownership_OTHER`, `OWN`, `RENT` *(one-hot)*  
  - `loan_intent_EDUCATION`, `HOMEIMPROVEMENT`, `MEDICAL`, `PERSONAL`, `VENTURE` *(one-hot)*



---

## 📌 Sample Prediction Flow
1. User inputs age, income, credit history, etc.  
2. App calculates features like DTI and EMI  
3. Scaler transforms numerical inputs  
4. Model predicts approval (1) or rejection (0)  
5. Probability of approval is also displayed

---

## 🙋‍♂️ Author
**Rohit Shere**  
📧 ru@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/rohitshere) | [GitHub](https://github.com/rohitshere)

---

## 📜 License
This project is open-source and free to use under the [MIT License](LICENSE).
