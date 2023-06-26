import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.set_page_config(layout="wide")
data = st.session_state["data"]

if 'indexone' not in st.session_state:
    st.session_state.indexone = 0
if 'indextwo' not in st.session_state:
    st.session_state.indextwo = 0

if 'featuresone' not in st.session_state:
    st.session_state.featuresone = tuple(
        data.drop(["manufacturer_name"], axis=1).columns)

if 'featurestwo' not in st.session_state:
    st.session_state.featurestwo = tuple(data.columns)
st.title("Визуализация данных")
tab1, tab2, tab3 = st.tabs(
    ["Гистограмма", "Ящик с усами", "Тепловая карта"])


with tab1:

    col1, col2 = st.columns(2)
    st.selectbox("Выберите признак", options=st.session_state.featuresone,
                 index=st.session_state.indexone, key='featureone')
    st.session_state.indexone = st.session_state.featureone.index(
        st.session_state.featureone)
    x = data[st.session_state.featureone]
    st.info("На графике мы можем увидеть количественную характеристику значений каждого отдельно взятого признака относительно целевого.")
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.histplot(data, x=st.session_state.featureone, multiple="stack")
    plt.xlabel(st.session_state.featureone)
    plt.ylabel("Количество")
    st.pyplot(fig)


with tab2:

    col1, col2 = st.columns(2)

    with col1:

        st.selectbox("Выберите признак", options=st.session_state.featurestwo,
                     index=st.session_state.indextwo, key='featuretwo')
        st.session_state.indextwo = st.session_state.featurestwo.index(
            st.session_state.featuretwo)
        x = data[st.session_state.featuretwo]
        st.info(
            "Ящик с усами позволяет найти числовые характеристики случайных величин.")

    with col2:

        fig, ax = plt.subplots(figsize=(10, 9))
        sns.boxplot(
            data=data, x=data[st.session_state.featuretwo])
        plt.xlabel(st.session_state.featuretwo)
        st.pyplot(fig)
with tab3:
    col1, col2 = st.columns(2)
    with col1:
        st.info("Тепловая карта позволяет увидеть кореляцию между признаками. Мы можем увидеть, что признаки с одинаковой семантикой противоположных сторон коррелируют между собой.")
    with col2:
        correlation_matrix = data.corr()
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, ax=ax)
        plt.xticks(rotation=45)
        plt.yticks(rotation=45)
        st.pyplot(fig)
