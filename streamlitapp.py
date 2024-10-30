
import streamlit as st
import pandas as pd
import pickle

# Load the cleaned data and model
data = pd.read_csv('C:\\Users\\HP\\Desktop\\capstone.3\\overalldata.csv')
with open('C:\\Users\\HP\\Desktop\\capstone.3\\GradientBoost_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Title for the app
st.title("Car Price Prediction")

# Input fields for filtering
fuel_type = st.selectbox("Fuel Type", data['Fuel_Type'].unique())
kilometers_driven = st.slider("Kilometers Driven", min_value=int(data['Kilometers_Driven'].min()), max_value=int(data['Kilometers_Driven'].max()), step=1000)
transmission_type = st.selectbox("Transmission Type", data['Transmission_Type'].unique())
no_of_owners = st.selectbox("Number of Owners", sorted(data['No_of_Owners'].unique()))
manufactured_by = st.selectbox("Manufactured By", data['Manufactured_By'].unique())
car_model = st.selectbox("Car Model", data['Car_Model'].unique())
car_produced_year = st.selectbox("Car Produced Year", sorted(data['Car_Produced_Year'].unique(), reverse=True))
registration_year = st.selectbox("Registration Year", sorted(data['Registration_Year'].unique(), reverse=True))
no_of_seats = st.selectbox("Number of Seats", sorted(data['No_of_Seats'].unique()))
engine_cc = st.slider("Engine CC", min_value=int(data['Engine_CC'].min()), max_value=int(data['Engine_CC'].max()), step=10)
mileage = st.slider("Mileage (kmpl)", min_value=float(data['Mileage(kmpl)'].min()), max_value=float(data['Mileage(kmpl)'].max()), step=0.1)
location = st.selectbox("Location", data['Location'].unique())

# Predict button
if st.button("Predict Price"):
    # Collect the input values into a DataFrame for the model
    input_data = pd.DataFrame({
        'Fuel_Type': [fuel_type],
        'Kilometers_Driven': [kilometers_driven],
        'Transmission_Type': [transmission_type],
        'No_of_Owners': [no_of_owners],
        'Manufactured_By': [manufactured_by],
        'Car_Model': [car_model],
        'Car_Produced_Year': [car_produced_year],
        'Registration_Year': [registration_year],
        'No_of_Seats': [no_of_seats],
        'Engine_CC': [engine_cc],
        'Mileage(kmpl)': [mileage],
        'Location': [location]
    })

    # Perform encoding/preprocessing if necessary
    # Assuming the preprocessing file you provided contains the steps, integrate that here
    #One-hot encode categorical variables
    input_data = pd.get_dummies(input_data, drop_first=False)

    # Align input data with the model’s feature order
    model_features = model.feature_names_in_
    input_data = input_data.reindex(columns=model_features, fill_value=0)

    # Predict the car price
      
    predicted_price = model.predict(input_data)[0]


# Convert the price to lakhs and round to one decimal place
    predicted_price_in_lakhs = round(predicted_price / 100000, 1)

  
# Display the result
    st.write(f"### Predicted Car Price: {predicted_price_in_lakhs} lakhs")