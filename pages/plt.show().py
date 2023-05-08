import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('_mpl-gallery')

data = pd.read_csv("data/csgo_task.csv")
plt.plot(data["ct_score"], data["t_score"])
fig, ax = plt.subplots(figsize=(5, 5),)
ax.plot(data["ct_score"], data["t_score"])
plt.xlabel("ct_score")
plt.ylabel("t_score")
st.pyplot(fig)

np.random.seed(3)
x = data["ct_score"]
y = data["t_score"]
fig, ax = plt.subplots()

ax.scatter(x, y, vmin=0, vmax=100)

plt.xlabel("ct_score")
plt.ylabel("t_score")

st.pyplot(fig)

x = 0.5 + np.arange(8)
y = np.random.uniform(2, 7, len(x))

fig, ax = plt.subplots()

ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

st.pyplot(fig)

x = data["map"].unique()
colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))

# plot
fig, ax = plt.subplots()
ax.pie(x, colors=colors, radius=3, center=(4, 4),labels=x,
       wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)
st.pyplot(fig)