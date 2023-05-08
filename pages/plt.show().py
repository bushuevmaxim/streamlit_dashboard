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


if 'maps' not in st.session_state:
    st.session_state.maps = data["map"].unique()


current_maps = st.multiselect("",
                              st.session_state.maps, [], help="Выберете карту")


hist, pie = st.columns(2)


# maps = dict((i, mapa) for i, mapa in enumerate(data["map"].unique()) if mapa in )
# maps = dict((mapa, data) for mapa in )
maps = data.groupby(["map"])["map"].count()
# maps_del = maps.drop(current_maps, axis=0)
# print()
# x = maps.to_frame() - maps_del.to_frame()
# print(x)
# y = data.groupby(["map", "bomb_planted"]).count()

# plot
# fig, ax = plt.subplots()

# ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
# # x = data[current_maps]

# fig, ax = plt.subplots(figsize=(5, 5))
# ax.bar(maps, width=1, edgecolor="white", linewidth=0.7, height=1)
# st.pyplot(fig)


fig, ax = plt.subplots(figsize=(10, 5))
ax.pie(maps, radius=3, center=(4, 4), labels=maps.keys(),
       wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)
plt.legend()
st.pyplot(fig)
