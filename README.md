# ❤️ Heart Disease Prediction App with AI Chatbot

A simple and interactive web application that predicts the risk of heart disease based on user input using a trained Random Forest Classifier.

Built using [Streamlit](https://streamlit.io/) and [scikit-learn](https://scikit-learn.org/), this project includes full data analysis, model training, and a user-friendly prediction app.

---

## 📘 Project Overview

- 🔍 **EDA + Model Building** in Jupyter Notebook
- 🧠 **Machine Learning Pipeline**: preprocessing + Random Forest
- 🌐 **Streamlit Web App**: interactive prediction form
- 📂 **Dataset Included**: for full reproducibility
- 🧠 **Predict** the likelihood of heart disease using ML models
- 🤖 **Chat** with a health assistant powered by Groq + llama
---

## 📊 Dataset

- File: `heart_disease.csv`
- Columns:
  - `age`, `sex`, `chest pain type`, `resting bp s`, `cholesterol`,  
    `fasting blood sugar`, `resting ecg`, `max heart rate`,  
    `exercise angina`, `oldpeak`, `ST slope`, `target`

---

## 📘 Notebook: `heart_disease.ipynb`

This notebook covers the complete ML workflow:

- Exploratory Data Analysis (EDA)
- Outlier detection and Winsorizing
- Preprocessing with pipelines
- Model training (Logistic Regression & Random Forest)
- Hyperparameter tuning using GridSearchCV
- Feature importance visualization

---
## 📁 Project Structure
```bash
heart-disease-app/
├── 🎯Predictor.py
├── heart_disease_model.pkl
├── heart_disease.csv
├── heart_disease.ipynb
├── requirements.txt
├── README.md
└── pages/
    └──  🤖Chatbot.py
```
---

## 📦 How to Run Locally

1. **🧬Clone the repository:**
   ```bash
   git clone https://github.com/your-username/heart-disease-app.git
   cd heart-disease-app
   ```
2. **📦 Install the requirements:**
    ```bash
    pip install -r requirements.txt
    ```
3. **🔐 Add your Groq API key:**

   Create a .env file in the root directory:
    ```bash
    GROQ_API_KEY=your_groq_api_key_here
    ```
4. **▶️ Launch the app:**
    ```bash
    streamlit run 🎯Predictor.py
    ```
Use the sidebar to switch between:
- Predictor
- Chatbot

---


