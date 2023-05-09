import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data_mod = pd.read_csv("data/csgotask_m.csv")
data = pd.read_csv("data/csgo_task.csv")
data.dropna(inplace=True)

if 'index' not in st.session_state:
    st.session_state.index = 0

if 'features' not in st.session_state:
    st.session_state.features = tuple(data.columns)
st.title("Визуализация данных")

st.selectbox("Выберете признак для сравнения с целевым", options=st.session_state.features,
             index=st.session_state.index, key='feature')
st.session_state.index = st.session_state.features.index(
    st.session_state.feature)

plot, scatter = st.columns(2)
x = data[st.session_state.feature]
y = data["bomb_planted"]
with plot:
    plt.plot(data["ct_score"], data["t_score"])
    fig, ax = plt.subplots(figsize=(5, 5),)

    ax.plot(x, y)
    plt.xlabel(st.session_state.feature)
    plt.ylabel("bomb_planted")
    st.pyplot(fig)
with scatter:
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.scatter(x, y)
    plt.xlabel(st.session_state.feature)
    plt.ylabel("bomb_planted")
    st.pyplot(fig)

triplot, stem = st.columns(2)

with triplot:

    fig, ax = plt.subplots()
    plt.xlabel(st.session_state.feature)
    plt.ylabel("bomb_planted")
    ax.triplot(x, y,)
    st.pyplot(fig)
with stem:

    fig, ax = plt.subplots()
    plt.xlabel(st.session_state.feature)
    plt.ylabel("bomb_planted")
    ax.stem(x, y)
    st.pyplot(fig)
# maps = data.groupby(["map"])["map"].count()

# fig, ax = plt.subplots(figsize=(10, 5))
# ax.pie(maps, radius=3, center=(4, 4), labels=maps.keys(),
#        wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)
# plt.legend()
# st.pyplot(fig)
