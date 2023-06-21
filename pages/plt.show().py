import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = st.session_state["data"]
if 'index' not in st.session_state:
    st.session_state.index = 0

if 'features' not in st.session_state:
    st.session_state.features = tuple(data.columns)
st.title("Визуализация данных")


st.selectbox("Выберете признак", options=st.session_state.features,
             index=st.session_state.index, key='feature')
st.session_state.index = st.session_state.features.index(
    st.session_state.feature)

x = data[st.session_state.feature]
y = data["bomb_planted"]


fig, ax = plt.subplots(figsize=(10, 10))
sns.histplot(data, x=st.session_state.feature,
             hue='bomb_planted', multiple="stack")
plt.title(f"Hist")
plt.xlabel(st.session_state.feature)
plt.ylabel("Count")
st.pyplot(fig)
fig, ax = plt.subplots(figsize=(10, 9))
sns.boxplot(
    data=data, x=data[st.session_state.feature])
plt.title(f'Box Plot')
plt.xlabel(st.session_state.feature)
st.pyplot(fig)
correlation_matrix = data.corr()
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, ax=ax)
plt.title('Heatmap - Корреляция данных')
plt.xticks(rotation=45)
plt.yticks(rotation=45)
st.pyplot(fig)
maps = data.groupby(["map"])["map"].count()
fig, ax = plt.subplots(figsize=(10, 8))
ax.pie(maps, labels=maps.keys())
plt.title(f"Pie")
st.pyplot(fig)
