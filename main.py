import streamlit as st
from PIL import Image

st.set_page_config(page_title='Информация о датасете', page_icon=':bar_chart:', layout='wide')

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
1. time_left - оставшееся время
1. ct_score, t_score - счет
1. ct_health, t_health - количество здоровья
1. ct_armor, t_armor - количество армора
1. ct_money	t_money - общее количество денег
1. ct_players_alive, t_players_alive - количество живых
1. map - название игровой карты
1. bomb_planted - стоит ли бомба (да, нет)
""")
with c3:
    st.info("", icon="🧠")

    # time_left	ct_score	t_score	map	bomb_planted	ct_health	t_health	ct_armor	t_armor	ct_money	t_money	ct_helmets	t_helmets	ct_defuse_kits	ct_players_alive