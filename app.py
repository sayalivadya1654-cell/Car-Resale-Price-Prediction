import streamlit as st
import pandas as pd
import joblib


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Car Resale Price Prediction",
    page_icon="🚗",
    layout="wide"
)


# --------------------------------------------------
# Load Model
# --------------------------------------------------

model = joblib.load("car_price_model.pkl")


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🚗 Car Resale Price Prediction")

st.write(
    "Enter the details of a used car to estimate its resale price."
)

st.divider()


# --------------------------------------------------
# Input Section
# --------------------------------------------------

st.subheader("Enter Car Details")

col1, col2 = st.columns(2)


# --------------------------------------------------
# Column 1
# --------------------------------------------------

with col1:

    brand = st.selectbox(
        "Brand",
        [
            "Maruti",
            "Hyundai",
            "Honda",
            "Toyota",
            "Mahindra",
            "Ford",
            "Volkswagen",
            "Tata",
            "Renault",
            "Nissan",
            "Chevrolet",
            "Skoda",
            "Other"
        ]
    )

    location = st.selectbox(
        "Location",
        [
            "Mumbai",
            "Pune",
            "Delhi",
            "Bangalore",
            "Chennai",
            "Hyderabad",
            "Kolkata",
            "Ahmedabad",
            "Jaipur",
            "Other"
        ]
    )

    year = st.number_input(
        "Manufacturing Year",
        min_value=1990,
        max_value=2026,
        value=2018,
        step=1
    )

    kilometers = st.number_input(
        "Kilometers Driven",
        min_value=0,
        value=50000,
        step=1000
    )

    fuel_type = st.selectbox(
        "Fuel Type",
        [
            "Petrol",
            "Diesel",
            "CNG",
            "LPG",
            "Electric"
        ]
    )


# --------------------------------------------------
# Column 2
# --------------------------------------------------

with col2:

    transmission = st.selectbox(
        "Transmission",
        [
            "Manual",
            "Automatic"
        ]
    )

    owner_type = st.selectbox(
        "Owner Type",
        [
            "First",
            "Second",
            "Third",
            "Fourth & Above"
        ]
    )

    mileage = st.number_input(
        "Mileage",
        min_value=1.0,
        value=18.0,
        step=0.1
    )

    engine = st.number_input(
        "Engine (CC)",
        min_value=500.0,
        value=1200.0,
        step=100.0
    )

    power = st.number_input(
        "Power (bhp)",
        min_value=20.0,
        value=80.0,
        step=5.0
    )

    seats = st.number_input(
        "Number of Seats",
        min_value=2.0,
        max_value=10.0,
        value=5.0,
        step=1.0
    )


st.divider()


# --------------------------------------------------
# Prediction
# --------------------------------------------------

if st.button("🔮 Predict Resale Price", use_container_width=True):

    # Calculate car age
    car_age = 2026 - year

    # Create input DataFrame
    input_data = pd.DataFrame({
        "Brand": [brand],
        "Location": [location],
        "Car_Age": [car_age],
        "Kilometers_Driven": [kilometers],
        "Fuel_Type": [fuel_type],
        "Transmission": [transmission],
        "Owner_Type": [owner_type],
        "Mileage": [mileage],
        "Engine": [engine],
        "Power": [power],
        "Seats": [seats]
    })

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display result
    st.subheader("Predicted Resale Price")

    if prediction < 0:
        st.warning(
            "The model produced an unrealistic negative prediction. "
            "This input may be outside the range learned by the model."
        )
    else:
        st.success(
            f"Estimated Resale Price: ₹ {prediction} Lakh"
        )