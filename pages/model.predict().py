import joblib
import numpy as np
import streamlit as st
import pandas as pd
st.set_page_config(layout="centered")
st.title("Получение предсказания")
left, right = st.columns(2)

data = st.session_state["data"]
manufacturer_name = st.selectbox("Карта", data["manufacturer_name"].unique())
model_name = st.text_input("Модель")
transmission = st.selectbox("Трансмиссия", data["transmission"].unique())
odometer_value = st.number_input("Пробег", min_value=0)
year_produced = st.number_input("Год", min_value=2000)
engine_type = st.selectbox("Карта", data["engine_type"].unique())
engine_capacity = st.number_input("Емкость двигателя", min_value=0)
body_type = st.selectbox("body_type", data["body_type"].unique())
has_warranty = st.checkbox('has_warranty')
state = st.selectbox("state", data["state"].unique())
drivetrain = st.selectbox("drivetrain", data["drivetrain"].unique())
number_of_photos = st.number_input("number_of_photos", min_value=0)
feature_0 = st.checkbox('feature_0')
feature_1 = st.checkbox('feature_1')
feature_2 = st.checkbox('feature_2')
feature_3 = st.checkbox('feature_3')
feature_4 = st.checkbox('feature_4')
feature_5 = st.checkbox('feature_5')
feature_6 = st.checkbox('feature_6')
feature_7 = st.checkbox('feature_7')
feature_8 = st.checkbox('feature_8')
feature_9 = st.checkbox('feature_9')
button_click = st.button("Predict", )
model = st.selectbox(
    "Модель", ["Bagging Classifier", "Decision Tree", "Neural Network"])

if button_click:
    row = np.array(
        [[False.astype(np.bool), manufacturer_name, model_name, transmission, odometer_value, year_produced, engine_type, engine_type, engine_capacity, body_type, has_warranty,
          state,  drivetrain, number_of_photos, feature_0, feature_1, feature_2,  feature_3, feature_4, feature_5, feature_6, feature_7, feature_8, feature_9]])
    # dataframe_test = pd.DataFrame(
    #     row, columns=data.drop(["price_usd"], axis=1).columns)
    # pipeline = joblib.load(f"models/ridge.pkl")
    # pred = pipeline.predict(dataframe_test)
    print(row)
