import streamlit as st
import pandas as pd
import random
import time

st.set_page_config(
    page_title='Jogadores',
    layout='wide'
)

df = st.session_state["data"]
df_gk = df[df['Posição'].str.contains('GK')]
df_gk = df_gk.reset_index(drop=True)
df_gk = df_gk.drop(['Unnamed: 0','URLs', 'Nome', 'País', 'Time', 'Posição Alternativa 1', 'Posição Alternativa 2', 'Posição Alternativa 3'], axis=1)

col1, col2, col3 = st.columns(3)

col2.title("Escolha seus jogadores")

if 'num1' not in st.session_state:
    st.session_state['num1'] = random.randint(0,len(df_gk)-1)

if 'num2' not in st.session_state:
    st.session_state['num2'] = random.randint(0,len(df_gk)-1)

if 'num3' not in st.session_state:
    st.session_state['num3'] = random.randint(0,len(df_gk)-1)

if 'num4' not in st.session_state:
    st.session_state['num4'] = random.randint(0,len(df_gk)-1)

if 'num5' not in st.session_state:
    st.session_state['num5'] = random.randint(0,len(df_gk)-1)


num1 = st.session_state['num1']
num2 = st.session_state['num2']
num3 = st.session_state['num3']
num4 = st.session_state['num4']
num5 = st.session_state['num5']
linhagk1 = df_gk.iloc[[num1]]
linhagk2 = df_gk.iloc[[num2]]
linhagk3 = df_gk.iloc[[num3]]
linhagk4 = df_gk.iloc[[num4]]
linhagk5 = df_gk.iloc[[num5]]
jogador1 = linhagk1.iloc[0]['Nome Completo']
jogador2 = linhagk2.iloc[0]['Nome Completo']
jogador3 = linhagk3.iloc[0]['Nome Completo']
jogador4 = linhagk4.iloc[0]['Nome Completo']
jogador5 = linhagk5.iloc[0]['Nome Completo']
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

l, m, r = st.columns([1,10,1])

l.button('Gerar', on_click=click_button)
reset = m.button('Resetar')

if reset:
    st.session_state.pop('num1')
    st.session_state.pop('num2')
    st.session_state.pop('num3')
    st.session_state.pop('num4')
    st.session_state.pop('num5')

gk1, gk2, gk3, gk4, gk5= st.columns([1,1,1,1,1])

if st.session_state.clicked:

    gk1.image(f"{str(df_gk.loc[num1, 'Foto'])}", width = 270)

    gk2.image(f"{str(df_gk.loc[num2, 'Foto'])}", width = 270)
       
    gk3.image(f"{str(df_gk.loc[num3, 'Foto'])}", width = 270)

    gk4.image(f"{str(df_gk.loc[num4, 'Foto'])}", width = 270)

    gk5.image(f"{str(df_gk.loc[num5, 'Foto'])}", width = 270)
    
jogador = st.selectbox(
    'Selecione um jogador.',
    [f'{jogador1}', f'{jogador2}', f'{jogador3}', f'{jogador4}', f'{jogador5}'], index=None,
    placeholder="Escolha um jogador...",)
st.write(f'Você escolheu o {jogador}')

if jogador == jogador1:
    linhagk1
    df_time = pd.DataFrame(columns=df_gk.columns)
    df_time = linhagk1
if jogador == jogador2:
    linhagk2
    df_time = pd.DataFrame(columns=df_gk.columns)
if jogador == jogador3:
    linhagk3
    df_time = pd.DataFrame(columns=df_gk.columns)
    df_time = linhagk3
if jogador == jogador4:
    linhagk4
    df_time = pd.DataFrame(columns=df_gk.columns)
    df_time = linhagk4
if jogador == jogador5:
    linhagk5
    df_time = pd.DataFrame(columns=df_gk.columns)
    df_time = linhagk5


