# 🚗 CarDekho - Used Car Price Prediction App

An end-to-end machine learning project that predicts the price of used cars based on user-input features. This project transforms unstructured vehicle data into an interactive **Streamlit web app** using powerful regression models and data preprocessing pipelines.

---

## 🔍 Problem Statement

Accurately predicting the price of a used car can be complex due to factors like mileage, engine condition, city, brand perception, etc.

> **Objective:**  
> Build a machine learning model to predict used car prices and deploy it as a real-time, user-friendly dashboard.

---
## ⚙️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python** | Core scripting |
| **Pandas & NumPy** | Data cleaning, feature engineering |
| **Scikit-learn** | ML modeling, evaluation, hyperparameter tuning |
| **Streamlit** | Web application dashboard |
| **Pickle** | Model serialization |
| **Matplotlib & Seaborn** | Visual analysis and EDA |

---

## 🧠 Machine Learning Models

The following regression models were trained, evaluated, and tuned using **GridSearchCV**:

- ✅ Decision Tree Regressor *(final model used)*
- ✅ Random Forest Regressor
- ✅ Gradient Boosting Regressor
- ✅ AdaBoost Regressor

**Evaluation Metrics Used:**
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## 🛠 Preprocessing Highlights

- Converted ₹ values like `6.5 Lakh`, `1.2 Crore` ➝ numeric
- Cleaned strings like `45,000 kms`, `1197 cc`, `18.5 kmpl` ➝ float/int
- One-hot encoded all nominal features: `Fuel_Type`, `Transmission_Type`, `Body_Type`, etc.
- Handled missing data with mean/median imputation

---

## 💻 Streamlit App Features

> 👉 Run the app with:  
> `streamlit run app.py`

**🧩 Pages:**
- **Home**: Project description, business context, problem & conclusion
- **Predictor**: Sidebar filters for input (e.g., fuel type, kms, engine cc, etc.), model outputs price in **lakhs**
