import pandas as pd
import streamlit as st
from PIL import Image

st.set_page_config(page_title='Информация о датасете',
                   page_icon=':bar_chart:', layout='wide')

st.title("Информация о датасете")
st.sidebar.title("")
c1, c2, c3 = st.columns(3)
with c1:
    st.info("""
    Описание
    - Датасет посвящен игре Counter-Strike: Global Offensive. 
    - В нем содержится информация о раундах для каждой из команд.
    - Предназначен для бинарной классификации.
    - Целевой признак - поставлена ли бомба либо нет для каждого раунда.""")
with c2:

    st.info("""
Признаки
- time_left - оставшееся время
- ct_score, t_score - счет
- ct_health, t_health - количество здоровья
- ct_armor, t_armor - количество армора
- ct_money	t_money - общее количество денег
- ct_players_alive, t_players_alive - количество живых
- map - название игровой карты
- bomb_planted - стоит ли бомба (да, нет)
""")
with c3:
    st.info("""
   Особенности предобработки данных:
- Один категориальный признак - (one-hot encoding)
- Дизбаланс классов - (under-sampling | over-sampling)
- Разброс числовых данных (standart scaling)

    """)

data = pd.read_csv("data/csgo_task.csv")
data.dropna(inplace=True)
st.session_state["data"] = data
