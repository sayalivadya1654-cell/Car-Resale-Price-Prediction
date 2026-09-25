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
# CUSTOM CSS - UI DESIGN ONLY
# --------------------------------------------------

st.markdown("""
<style>

    /* ==========================================
       MAIN PAGE
       ========================================== */

    .stApp {
        background-color: #ffffff;
        color: #000000;
    }

    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }


    /* ==========================================
       ALL NORMAL TEXT
       ========================================== */

    p {
        color: #000000 !important;
    }

    label {
        color: #000000 !important;
        font-weight: 600 !important;
    }


    /* ==========================================
       MAIN TITLE
       ========================================== */

    h1 {
        color: #123b70 !important;
        font-size: 42px !important;
        font-weight: 800 !important;
        letter-spacing: -1px;
    }


    /* ==========================================
       SUB HEADINGS
       ========================================== */

    h2 {
        color: #164e86 !important;
        font-size: 30px !important;
        font-weight: 750 !important;
    }

    h3 {
        color: #1b5e9e !important;
        font-size: 24px !important;
        font-weight: 700 !important;
    }


    /* ==========================================
       INPUT LABELS
       ========================================== */

    .stSelectbox label,
    .stNumberInput label {
        color: #000000 !important;
        font-size: 15px !important;
        font-weight: 650 !important;
    }


    /* ==========================================
       SELECT BOX
       ========================================== */

    .stSelectbox > div > div {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 1px solid #bfc9d6 !important;
        border-radius: 8px !important;
    }


    /* ==========================================
       NUMBER INPUT
       ========================================== */

    .stNumberInput input {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 1px solid #bfc9d6 !important;
        border-radius: 8px !important;
    }


    /* ==========================================
       INPUT FOCUS
       ========================================== */

    .stSelectbox > div > div:focus-within,
    .stNumberInput input:focus {
        border: 2px solid #2674c9 !important;
        box-shadow: 0 0 0 2px rgba(38, 116, 201, 0.12);
    }


    /* ==========================================
       PREDICT BUTTON
       ========================================== */

    .stButton > button {

        width: 100%;

        height: 58px;

        background: linear-gradient(
            135deg,
            #0d47a1,
            #1976d2
        );

        color: #ffffff !important;

        border: none;

        border-radius: 12px;

        font-size: 19px !important;

        font-weight: 750 !important;

        letter-spacing: 0.3px;

        box-shadow:
            0 6px 18px rgba(13, 71, 161, 0.25);

        transition: all 0.25s ease;
    }


    /* BUTTON HOVER */

    .stButton > button:hover {

        background: linear-gradient(
            135deg,
            #083b8c,
            #0d65b5
        );

        color: #ffffff !important;

        transform: translateY(-2px);

        box-shadow:
            0 10px 25px rgba(13, 71, 161, 0.35);
    }


    /* BUTTON CLICK */

    .stButton > button:active {

        transform: translateY(0px);

        box-shadow:
            0 4px 10px rgba(13, 71, 161, 0.25);
    }


    /* ==========================================
       SUCCESS / PREDICTION RESULT
       ========================================== */

    div[data-testid="stAlert"] {

        background-color: #ecfff5 !important;

        border: 2px solid #21a366 !important;

        border-radius: 14px !important;

        padding: 22px !important;

        box-shadow:
            0 7px 22px rgba(33, 163, 102, 0.15);
    }


    div[data-testid="stAlert"] p {

        color: #087443 !important;

        font-size: 24px !important;

        font-weight: 800 !important;

        line-height: 1.4 !important;
    }


    /* ==========================================
       WARNING
       ========================================== */

    div[data-testid="stAlert"][kind="warning"] {

        background-color: #fff8e6 !important;

        border-color: #f0a500 !important;
    }


    /* ==========================================
       DIVIDER
       ========================================== */

    hr {
        border: none !important;

        height: 1px !important;

        background-color: #dfe5ec !important;

        margin-top: 25px !important;

        margin-bottom: 25px !important;
    }


    /* ==========================================
       PAGE CONTAINER
       ========================================== */

    [data-testid="stAppViewContainer"] {
        background-color: #ffffff;
    }


    /* ==========================================
       INPUT HOVER
       ========================================== */

    .stSelectbox > div > div:hover,
    .stNumberInput input:hover {

        border-color: #1976d2 !important;

        box-shadow:
            0 2px 8px rgba(25, 118, 210, 0.08);
    }


</style>
""", unsafe_allow_html=True)


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
            f"Estimated Resale Price: ₹ {prediction:.2f} Lakh"
        )