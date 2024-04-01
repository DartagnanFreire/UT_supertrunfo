import streamlit as st
import pandas as pd
import random

df = st.session_state["data"]

col1, col2, col3 = st.columns(3)

col2.title("Role seus dados aqui!")

  
col4, col5 = st.columns(2)
with col4:
    btn = st.button("d10")
    if btn:
        num = random.randint(0,9)
        st.markdown(f"{num}")

with col5:
    btn1 = st.button("d100")
    if btn1:
        num1 = random.randint(0,100)
        st.markdown(f"{num1}")

st.divider()
col1, col2, col3 = st.columns(3)