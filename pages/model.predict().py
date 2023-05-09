import streamlit as st
import pandas as pd
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
    ct_players_alive = st.number_input("ct_players_alive", min_value=0)
with right:
    t_score = st.number_input("t_score", min_value=0)
    t_health = st.number_input("t_health", min_value=0)
    t_armor = st.number_input("t_armor", min_value=0)
    t_money = st.number_input("t_money", min_value=0)
    t_players_alive = st.number_input("t_players_alive", min_value=0)
time_left = st.number_input("time_left", min_value=0)
map = st.selectbox("Карта", data["map"].unique())
button_click = st.button("Predict", )
dataframe_test = pd.DataFrame(columns=data_new.columns)


if button_click:
    st.write(dataframe_test.columns)
    row = [time_left, ct_score, t_score,
           ct_health, t_health, ct_money, t_money,
           ct_players_alive, t_players_alive,

           ]
    maps = ['map_de_cache', 'map_de_dust2', 'map_de_inferno',
            'map_de_mirage', 'map_de_nuke', 'map_de_overpass', 'map_de_train',
            'map_de_vertigo']
    maplist = []
    choosen_map = "map_"+map
    for current_map in maps:
        if current_map == choosen_map:
            maplist.append(1)

        else:
            maplist.append(0)
    row.extend(maplist)
    dataframe_test.loc[len(dataframe_test.index)] = row
    st.dataframe(dataframe_test)
