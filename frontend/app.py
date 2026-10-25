
import streamlit as st
import pandas as pd
import requests

# Base URL of the Flask backend
BACKEND_URL = "http://backend:7860"

# define the title of the app.
st.title("SuperKart Forecasting App") 

#Collect user input - Input fields for product and store data
Product_Weight = st.number_input(
    "Product Weight", min_value=0.0, value=12.66
)

Product_Sugar_Content = st.selectbox(
    "Product Sugar Content",
    ["Low Sugar", "Regular", "No Sugar"]
)

Product_Allocated_Area = st.number_input(
    "Product Allocated Area",
    min_value=0.0,
    max_value=1.0,
    value=0.05
)

Product_MRP = st.number_input(
    "Product MRP",
    min_value=0.0,
    value=150.0
)

Store_Size = st.selectbox(
    "Store Size",
    ["Small", "Medium", "High"]
)

Store_Location_City_Type = st.selectbox(
    "Store Location City Type",
    ["Tier 1", "Tier 2", "Tier 3"]
)

Store_Type = st.selectbox(
    "Store Type",
    [
        "Departmental Store",
        "Supermarket Type1",
        "Supermarket Type2",
        "Food Mart"
    ]
)

Product_Id_char = st.selectbox(
    "Product ID Category",
    ["FD", "DR", "NC"]
)

Store_Age_Years = st.number_input(
    "Store Age (Years)",
    min_value=0,
    value=10,
    step=1
)

Product_Type_Category = st.selectbox(
    "Product Type Category",
    ["Perishables", "Non Perishables"]
)

# Convert user input into a DataFrame
product_data = pd.DataFrame([{
    "Product_Weight": Product_Weight,
    "Product_Sugar_Content": Product_Sugar_Content,
    "Product_Allocated_Area": Product_Allocated_Area,
    "Product_MRP": Product_MRP,
    "Store_Size": Store_Size,
    "Store_Location_City_Type": Store_Location_City_Type,
    "Store_Type": Store_Type,
    "Product_Id_char": Product_Id_char,
    "Store_Age_Years": Store_Age_Years,
    "Product_Type_Category": Product_Type_Category
}])

if st.button("Predict", type='primary'):
    response = requests.post(f"{BACKEND_URL}/v1/rental", json=product_data.to_dict(orient='records')[0])  # Send data to Flask API
    if response.status_code == 200:
        result = response.json()
        predicted_sales = result["Sales"]
        st.write(f"Predicted Product Store Sales Total: ₹{predicted_sales:.2f}")
    else:
        st.error("Error in API request")
