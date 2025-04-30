import streamlit as st
import pandas as pd
import pickle

# Set page config FIRST
st.set_page_config(page_title=" 🚗 Cardeko", layout="wide")


# Custom CSS for light red background and styling
st.markdown("""
    <style>
        .stApp {
            background-color: #fff0f0;
        }
        .css-18e3th9 {
            background-color: #fff0f0 !important;
        }
        .css-1d391kg {
            background-color: #fff0f0 !important;
        }
        .stSidebar {
            background-color: #ffe6e6;
        }
        .stButton>button {
            color: white;
            background-color: #e63946;
        }
        h1, h2, h3 {
            color: #b80000;
        }
    </style>
""", unsafe_allow_html=True)


# Load cleaned data and model
data = pd.read_csv('C:\\Users\\HP\\Desktop\\capstone.3\\preprocessed_car_data.csv')
with open('C:\\Users\\HP\\Desktop\\capstone.3\\decision_tree_car_price.pkl', 'rb') as file:
    model = pickle.load(file)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Price Predictor"])

# -------------------- Page 1: HOME --------------------
if page == "Home":
    st.title("🚗 Car Dheko - Used Car Price Prediction")
    
    st.header("About CarDekho")
    st.markdown("""
    [**CarDekho**](https://www.cardekho.com) is a leading Indian online platform for buying and selling used and new cars. 
    It provides detailed car reviews, comparisons, price guides, and financing options, 
    empowering customers with everything they need to make informed decisions.
    """)

    st.header("📘 Project Overview")
    st.markdown("""
    This project focuses on building a **used car price prediction model** using machine learning.
    We worked with unstructured datasets from 6 cities (Delhi, Chennai, Bangalore, Kolkata, Jaipur,hyderabad) 
    and transformed them into a single structured dataset.

    Using features like **Fuel Type, Transmission, Engine Size, Mileage, City, Year**, etc., 
    the project aims to accurately predict the selling price of used cars using models like 
    Decision Trees, Random Forests, and Gradient Boosting.

    The model is deployed as an interactive **Streamlit application** to provide instant price estimates.
    """)

    st.header("🎯 Objective & Problem Statement")
    st.markdown("""
    Imagine you are a data scientist at **Car Dheko**.  
    Your goal is to:
    
    - Streamline the used car price evaluation process  
    - Enhance customer and sales rep experience with a **user-friendly price prediction tool**
    
    🔍 **Problem Statement:**  
    > Build an accurate, interactive ML-powered tool that predicts the price of a used car based on input features, integrated into a real-time Streamlit interface.
    """)

    st.header("✅ Conclusion")
    st.markdown("""
    This end-to-end project demonstrates the full ML lifecycle — from **data ingestion and cleaning** to **model training and deployment**.

    ✅ We built a robust **Decision Tree-based price predictor**  
    ✅ We deployed the model with a **clean, intuitive Streamlit app**  
    ✅ The tool enables real-time, data-driven car price recommendations

    This solution is a step toward **automating price discovery in the used car market**, 
    aligning with the digital mission of CarDekho.
    """)

    st.markdown("🔗 [View Project Report](https://github.com/Suriya11072001/cardekho.git)")



# -------------------- Page 2: PRICE PREDICTOR --------------------
elif page == "Price Predictor":
    st.title("🎯 Predict Your Car's Price")

    # Sidebar input fields
    st.sidebar.header("🔍 Input Car Details")

    fuel_type = st.sidebar.selectbox("Fuel Type", data['Fuel_Type'].dropna().unique())
    kilometers_driven = st.sidebar.slider("Kilometers Driven", 
                                          int(data['Kilometers_Driven'].min()), 
                                          int(data['Kilometers_Driven'].max()), 
                                          step=1000)
    transmission_type = st.sidebar.selectbox("Transmission Type", data['Transmission_Type'].dropna().unique())
    no_of_owners = st.sidebar.selectbox("Number of Owners", sorted(data['No_of_Owners'].dropna().unique()))
    manufactured_by = st.sidebar.selectbox("Manufactured By", data['Manufactured_By'].dropna().unique())
    car_model = st.sidebar.selectbox("Car Model", data['Car_Model'].dropna().unique())
    car_produced_year = st.sidebar.selectbox("Car Produced Year", sorted(data['Car_Produced_Year'].dropna().unique(), reverse=True))
    registration_year = st.sidebar.selectbox("Registration Year", sorted(data['Registration_Year'].dropna().unique(), reverse=True))
    no_of_seats = st.sidebar.selectbox("Number of Seats", sorted(data['No_of_Seats'].dropna().unique()))
    engine_cc = st.sidebar.slider("Engine CC", 
                                  int(data['Engine_CC'].min()), 
                                  int(data['Engine_CC'].max()), 
                                  step=10)
    mileage = st.sidebar.slider("Mileage (kmpl)", 
                                float(data['Mileage_kmpl'].min()), 
                                float(data['Mileage_kmpl'].max()), 
                                step=0.1)
    city = st.sidebar.selectbox("City", data['City'].dropna().unique())

    if st.sidebar.button("Predict Price"):
        input_data = pd.DataFrame({
            'Fuel_Type': [fuel_type],
            'Kilometers_Driven': [kilometers_driven],
            'Transmission_Type': [transmission_type],
            'No_of_Owners': [no_of_owners],
            'Manufactured_By': [manufactured_by],
            'Car_Model': [car_model],  # Not used in model, but good for display
            'Car_Produced_Year': [car_produced_year],
            'Registration_Year': [registration_year],
            'No_of_Seats': [no_of_seats],
            'Engine_CC': [engine_cc],
            'Mileage_kmpl': [mileage],
            'City': [city]
        })

        # One-hot encode input
        input_encoded = pd.get_dummies(input_data, drop_first=False)

        # Align with model input features
        model_features = model.feature_names_in_
        input_encoded = input_encoded.reindex(columns=model_features, fill_value=0)

        # Predict
        predicted_price = model.predict(input_encoded)[0]
        predicted_lakhs = round(predicted_price / 100000, 2)

        st.success(f"💰 Predicted Car Price: ₹{predicted_lakhs} Lakhs")
