import joblib
import numpy as np
import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
st.title("Получение предсказания")
left, right = st.columns(2)

data = st.session_state["data"]
data_new = pd.read_csv("data/csgo_task_m.csv")
data_new.drop(["Unnamed: 0", "bomb_planted"], axis=1, inplace=True)
with left:
    ct_score = st.number_input("ct_score", min_value=0)
    ct_health = st.number_input("ct_health", min_value=0)
    ct_armor = st.number_input("ct_armor", min_value=0)
    ct_money = st.number_input("ct_money", min_value=0)
    ct_helmets = st.number_input("ct_helmets", min_value=0)
    ct_players_alive = st.number_input("ct_players_alive", min_value=0)
    time_left = st.number_input("time_left", min_value=0)
with right:
    t_score = st.number_input("t_score", min_value=0)
    t_health = st.number_input("t_health", min_value=0)
    t_armor = st.number_input("t_armor", min_value=0)
    t_money = st.number_input("t_money", min_value=0)
    t_helmets = st.number_input("t_helmets", min_value=0)
    t_players_alive = st.number_input("t_players_alive", min_value=0)
    ct_defuse_kits = st.number_input("ct_defuse_kits", min_value=0)


map = st.selectbox("Карта", data["map"].unique())
button_click = st.button("Predict", )
model = st.selectbox(
    "Модель", ["Bagging Classifier", "Decision Tree", "Neural Network"])

if button_click:
    row = np.array([[time_left, ct_score, t_score, map, ct_health, t_health, ct_armor, t_armor, ct_money, t_money,

                    ct_helmets,	t_helmets,
                    ct_defuse_kits,
                    ct_players_alive, t_players_alive]])
    dataframe_test = pd.DataFrame(
        row, columns=data.drop(["bomb_planted"], axis=1).columns)
    pipeline = joblib.load(f"models/{model}.joblib")
    pred = np.around(pipeline.predict(dataframe_test))
    if (pred == 1):
        st.write("Бомба поставлена")
    else:
        st.write("Бомба не поставлена")
