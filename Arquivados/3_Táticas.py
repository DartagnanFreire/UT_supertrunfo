import streamlit as st
import pandas as pd
import random
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

st.set_page_config(
    page_title='Jogadores',
    layout='wide'
)

col1, col2, col3 = st.columns(3)

with col1:
    container = st.container()

with col2:
    container = st.container()
    jogador = st.selectbox(
    'Selecione uma tática.',
    ['3-4-1-2', '3-4-2-1', '3-1-4-2', '3-4-3', '3-5-2', '4-1-2-1-2', '4-1-2-1-2(2)', '4-1-4-1', '4-2-1-3', '4-2-3-1', '4-2-3-1(2)', '4-2-2-2', '4-2-4', '4-3-1-2',
     '4-1-3-2', '4-3-2-1', '4-3-3', '4-3-3(2)', '4-3-3(3)', '4-3-3(4)', '4-3-3(5)', '4-4-1-1', '4-4-1-1(2)', '4-4-2', '4-4-2(2)', '4-5-1', '4-5-1(2)',
     '5-2-1-2', '5-2-2-1', '5-1-2-2', '5-4-1'], index=None,
    placeholder="Escolha uma tática...",)
    st.write(f'Você escolheu a tática: {jogador}')

    if jogador:
        col1.image(f'/Users/dafreire/Desktop/Fifa project/Imagens/{jogador}.png')

    if jogador == None:
        col1.image('/Users/dafreire/Desktop/Fifa project/Imagens/4-4-2.jpg')
    
with col3:
    container = st.container()

