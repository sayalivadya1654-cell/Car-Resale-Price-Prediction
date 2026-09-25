# 🚗 Car Resale Price Prediction

An end-to-end **Machine Learning project using Linear Regression** to predict the resale price of used cars based on vehicle specifications, age, usage, and other characteristics.

## 🎯 Project Overview

The goal of this project is to build a regression model that estimates the resale price of a used car from historical vehicle data.

The project covers the complete Machine Learning workflow:

**Data Collection → Data Cleaning → EDA → Feature Engineering → Preprocessing → Model Training → Evaluation → Model Deployment**

## ✨ Key Features

* 🚗 Used car resale price prediction
* 🧹 Data cleaning and missing-value handling
* 🔢 Conversion of text-based numerical features
* ⚙️ Feature engineering such as **Car Age** and **Brand**
* 📊 Exploratory Data Analysis
* 📈 Outlier detection using the IQR method
* 🔠 Categorical feature encoding using One-Hot Encoding
* 🤖 Linear Regression model
* 📏 Evaluation using MAE, MSE, RMSE, and R²
* 💾 Model serialization using Joblib
* 🌐 Interactive prediction using Streamlit

## 🛠️ Tech Stack

**Language**
* Python
**Data Analysis**
* Pandas
* NumPy
**Visualization**
* Matplotlib
**Machine Learning**
* Scikit-learn
  * Linear Regression
  * Train-Test Split
  * ColumnTransformer
  * Pipeline
  * OneHotEncoder
**Deployment & Tools**
* Streamlit
* Joblib
* Jupyter Notebook
* VS Code
* Git & GitHub

## 📊 Dataset
The project uses a used-car dataset containing vehicle information such as:

* Car Name
* Location
* Year
* Kilometers Driven
* Fuel Type
* Transmission
* Owner Type
* Mileage
* Engine
* Power
* Seats
* Price

The target variable is:

**Price — Used car resale price**

## 🤖 Machine Learning Model

The primary model used in this project is:

### Linear Regression

Linear Regression is used to learn the relationship between vehicle features and resale price.

The preprocessing and model training are combined using a Scikit-learn **Pipeline**.
## 📏 Model Evaluation

The Linear Regression model is evaluated using:

| Metric       | Purpose                                                           |
| ------------ | ----------------------------------------------------------------- |
| **MAE**      | Measures average absolute prediction error                        |
| **MSE**      | Measures average squared prediction error                         |
| **RMSE**     | Measures the typical magnitude of prediction error                |
| **R² Score** | Measures the proportion of price variation explained by the model |

The exact evaluation results are generated when the notebook is executed.

## 🌐 Streamlit Application

The trained model is integrated into a **Streamlit web application**.

Users can enter vehicle information such as:

* Brand
* Location
* Fuel Type
* Transmission
* Owner Type
* Car Age
* Kilometers Driven
* Mileage
* Engine
* Power
* Seats

The application then generates an estimated resale price.

### Example Output

```text
Estimated Resale Price
₹ XX.XX Lakh
```

## 📁 Project Structure

```text
Car-Resale-Price-Prediction/
│
├── dataset/
│   └── used_cars_dataset.csv
│
├── Car_Resale_Price_Prediction.ipynb
├── app.py
├── car_price_model.pkl
├── requirements.txt
└── README.md
```

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/sayalivadya1654-cell/Car-Resale-Price-Prediction.git
```

### 2. Navigate to the Project

```bash
cd Car-Resale-Price-Prediction
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit App

```bash
streamlit run app.py
```

The application will open in your browser.

