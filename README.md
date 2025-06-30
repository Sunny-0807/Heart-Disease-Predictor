# ❤️ Heart Disease Prediction App with AI Chatbot

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-orange?logo=streamlit)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

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

- File: `heart_disease_data.csv`
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
Heart-Disease-Predictor/
├── .gitignore                  
├── README.md                   
├── heart_disease.ipynb         
├── heart_disease_data.csv     
├── heart_disease_model.pkl     
├── requirements.txt         
├── Predictor.py              
└── pages/
    └── Chatbot.py             

```
---

## 🚀 How to Run Locally

1. **🧬Clone the repository:**
   ```bash
   https://github.com/Sunny-0807/Heart-Disease-Predictor.git
   cd Heart-Disease-Predictor
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

## 📜 Disclaimer
This project is for **educational/demo purposes only** and is not **intended for real-world diagnosis or medical decisions**.

