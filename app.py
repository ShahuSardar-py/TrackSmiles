import streamlit as st
import matplotlib as plt

st.set_page_config(
    page_title="TrackSmiles",
    page_icon='💛')

st.title("TrackSmiles")
st.subheader('mood tracking made simple and effective')
st.divider()

mood = st.slider("How are you feeling today?", 1, 10, 5)
