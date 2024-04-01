import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='Regras Gerais',
    layout='wide'
)

st.markdown('# Regras Gerais')
st.markdown('Geralmente, cada jogada terá 3 fases: ')

st.markdown('**Fase 1**: Jogador com a bola faz ação.')
st.markdown('**Fase 2**: Caso tenha algum adversário, ele realiza ação aqui.')
st.markdown('**Fase 3**: Caso tenha algum jogador para receber a bola, ele realiza ação aqui.')
st.markdown('''Para cada fase é jogado dois dados: Um para teste de aptidão, e outro D100 para verificar se atingiu o valor.
            O teste de aptidão é um d10 onde temos 5 dificuldades:\n
    de 1 a 2 é fácil
    de 3 a 4 é mediano
    de 5 a 6 é dificil
    de 7 a 8 é muito dificil
    de 9 a 0 é impossível''')
st.markdown('''O teste de aptidão varia de acordo com o que o jogador quer fazer e se existem impeditivos.
            ''')