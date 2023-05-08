import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data_mod = pd.read_csv("data/csgotask_m.csv")
data = pd.read_csv("data/csgo_task.csv")
data.dropna(inplace=True)
print(data.columns)
if 'index' not in st.session_state:
    st.session_state.index = 0

if 'features' not in st.session_state:
    st.session_state.features = tuple(data.columns)
st.title("Зависимость признаков от целевого признака")

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

hist, pie = st.columns(2)
x = 0.5 + np.arange(8)
y = np.random.uniform(2, 7, len(x))
fig, ax = plt.subplots(figsize=(5, 5))
ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
st.pyplot(fig)

maps = dict((i, j) for i, j in enumerate(data["map"].unique()))
fig, ax = plt.subplots(figsize=(10, 5))
ax.pie(maps.keys(), radius=3, center=(4, 4), labels=maps.values(),
       wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)
plt.legend()
st.pyplot(fig)
