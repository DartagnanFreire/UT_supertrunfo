import streamlit as st
import pandas as pd
import random
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

st.set_page_config(
    page_title='Ações',
    layout='wide'
)

df = st.session_state["data"]

posi = df["Posição"].value_counts().index
club = st.sidebar.selectbox("Posição", posi)

df_players = df[(df["Posição"] == club)]
players = df_players["Nome Completo"].value_counts().index
player = st.sidebar.selectbox("Jogador", players)

df_tipo = df[(df["Nome Completo"] == player)]
tipos = df_tipo["Tipo"].value_counts().index
tipo = st.sidebar.selectbox("Tipo Carta", tipos)

# Filter the DataFrame based on the selected player and card type
df_selected = df_tipo[(df_tipo["Nome Completo"] == player) & (df_tipo["Tipo"] == tipo)]

# Use the player's photo as an additional unique identifier
photos = df_selected["Versão"]
photo = st.sidebar.selectbox("Versão", photos)

# Get the player stats based on the selected player, card type, and photo
player_stats = df_selected[df_selected["Versão"] == photo].iloc[0]

acceleration = player_stats['Acceleration']
sprint_speed = player_stats['Sprint Speed']
positioning = player_stats['Positioning']
finishing = player_stats['Finishing']
shot_power = player_stats['Shot Power']
long_shots = player_stats['Long Shot']
volleys = player_stats['Volleys']
penalties = player_stats['Penalties']
vision = player_stats['Vision']
crossing = player_stats['Crossing']
fk_accuracy = player_stats['Free Kick']
short_passing = player_stats['Shot Passing']
long_passing = player_stats['Long Passing']
curve = player_stats['Curve']
agility = player_stats['Agility']
balance = player_stats['Balance']
reactions = player_stats['Reactions']
ball_control = player_stats['Ball Control']
dribbling = player_stats['Dribbling']
composure = player_stats['Composure']
interceptions = player_stats['Interceptions']
heading_accuracy = player_stats['Heading']
defensive_awareness = player_stats['Def. Awareness']
standing_tackle = player_stats['Standing Tackle']
sliding_tackle = player_stats['Sliding']
jumping = player_stats['Jumping']
stamina = player_stats['Stamina']
strength = player_stats['Strength']
aggression = player_stats['Aggression']
gk_diving = player_stats['Diving']
gk_kicking = player_stats['Kicking']
gk_handling = player_stats['Handling']
gk_reflexes = player_stats['Reflexes']
gk_positioning = int(player_stats['Positioning GK'])

# Verifica a condição da variável
def def_cor(defi):
    if defi <= 49:
        cor = '#ec1b1e'
    elif defi >= 50 and defi <= 69:
        cor = '#ff8c00'
    elif defi >=70 and defi <= 79:
        cor = '#3fd442'
    elif defi >=80 and defi <=98:
        cor = '#29982b' 
    elif defi == 99:
        cor = '#00B4FF'
    return cor

col1, col2, col3 = st.columns([8,5,9])

with col1:
    container = st.container()
    acao = st.selectbox(
        'Selecione uma ação.',
        ['Chute a gol sem domínio', 'Chute a gol sem domínio - FDA', 'Cabeceio ATK', 'Cabeceio DEF', 'Correr atrás', 'Falta de perto', 'Falta de longe', 
         'Penalty', 'Interceptação Rasteira', 'Interceptação alta', 'Carrinho', 'Disputa de bola', 'Drible', 'Colocar á frente', 'Passe curto', 'Passe longo', 'Cruzamento',
         'Receber a bola', 'Chutar a gol', 'Chutar a gol - FDA', 'Defesa Goleiro'], index=None,
        placeholder="Escolha uma ação...",)
    st.write(f'Você escolheu a ação: {acao}')

    inter = st.selectbox(
        'Selecione quantidade de jogadores no caminho:',
        ['Nenhum jogador', 'Um jogador', 'Dois jogadores', 'Três jogadores', 'Quatro jogadores'], index=None,
        placeholder="Escolha uma opção...",)
    st.write(f'Você escolheu a ação: {inter}')
    
    if acao == None:
        valortotal = 0

    if acao == 'Chute a gol sem domínio':
        col2.markdown(f'#### {acao}')
        col2.markdown(f'**Posicionamento** <span style="color: {def_cor(positioning)};">{positioning}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Finalização** <span style="color: {def_cor(finishing)};">{finishing}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Força do Chute** <span style="color: {def_cor(shot_power)};">{shot_power}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Voleio** <span style="color: {def_cor(volleys)};">{volleys}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Equilibrio** <span style="color: {def_cor(balance)};">{balance}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Reações** <span style="color: {def_cor(reactions)};">{reactions}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Frieza** <span style="color: {def_cor(composure)};">{composure}</span>', unsafe_allow_html=True)
        valortotal = (positioning+finishing+shot_power+volleys+balance+reactions+composure)/7
        col2.markdown(f'#### **Valor total:** {valortotal:.0f}')

    if acao == 'Chute a gol sem domínio - FDA':
        col2.markdown(f'#### {acao}')
        col2.markdown(f'**Posicionamento** <span style="color: {def_cor(positioning)};">{positioning}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Finalização** <span style="color: {def_cor(finishing)};">{finishing}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Força do Chute** <span style="color: {def_cor(shot_power)};">{shot_power}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Voleio** <span style="color: {def_cor(volleys)};">{volleys}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Chute de longe** <span style="color: {def_cor(long_shots)};">{long_shots}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Equilibrio** <span style="color: {def_cor(balance)};">{balance}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Reações** <span style="color: {def_cor(reactions)};">{reactions}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Frieza** <span style="color: {def_cor(composure)};">{composure}</span>', unsafe_allow_html=True)
        valortotal = (positioning+finishing+shot_power+volleys+long_shots+balance+reactions+composure)/8
        col2.markdown(f'#### **Valor total:** {valortotal:.0f}')

    if acao == 'Cabeceio ATK':
        col2.markdown(f'#### {acao}')
        col2.markdown(f'**Posicionamento** <span style="color: {def_cor(positioning)};">{positioning}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Impulsão** <span style="color: {def_cor(jumping)};">{jumping}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Combatividade** <span style="color: {def_cor(aggression)};">{aggression}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Cabeceio** <span style="color: {def_cor(heading_accuracy)};">{heading_accuracy}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Reação** <span style="color: {def_cor(reactions)};">{reactions}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Frieza** <span style="color: {def_cor(composure)};">{composure}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Equilibrio** <span style="color: {def_cor(balance)};">{balance}</span>', unsafe_allow_html=True)
        valortotal = (positioning+jumping+aggression+heading_accuracy+reactions+composure+balance)/7
        col2.markdown(f'#### **Valor total:** {valortotal:.0f}')

    if acao == 'Cabeceio DEF':
        col2.markdown(f'#### {acao}')
        col2.markdown(f'**Posicionamento** <span style="color: {def_cor(positioning)};">{positioning}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Impulsão** <span style="color: {def_cor(jumping)};">{jumping}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Combatividade** <span style="color: {def_cor(aggression)};">{aggression}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Cabeceio** <span style="color: {def_cor(heading_accuracy)};">{heading_accuracy}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Reação** <span style="color: {def_cor(reactions)};">{reactions}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Frieza** <span style="color: {def_cor(composure)};">{composure}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Equilibrio** <span style="color: {def_cor(balance)};">{balance}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Interceptação** <span style="color: {def_cor(interceptions)};">{interceptions}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Def. Awareness** <span style="color: {def_cor(defensive_awareness)};">{defensive_awareness}</span>', unsafe_allow_html=True) 
        valortotal = (positioning+jumping+aggression+heading_accuracy+reactions+composure+balance+interceptions+defensive_awareness)/9
        col2.markdown(f'#### **Valor total:** {valortotal:.0f}')

    if acao == 'Correr atrás':
        col2.markdown(f'#### {acao}')
        col2.markdown(f'**Aceleração** <span style="color: {def_cor(acceleration)};">{acceleration}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Sprint** <span style="color: {def_cor(sprint_speed)};">{sprint_speed}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Agilidade** <span style="color: {def_cor(agility)};">{agility}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Estamina** <span style="color: {def_cor(stamina)};">{stamina}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Interceptação** <span style="color: {def_cor(interceptions)};">{interceptions}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Def. Awareness** <span style="color: {def_cor(defensive_awareness)};">{defensive_awareness}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Dividida em pé** <span style="color: {def_cor(standing_tackle)};">{standing_tackle}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Reações** <span style="color: {def_cor(reactions)};">{reactions}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Frieza** <span style="color: {def_cor(composure)};">{composure}</span>', unsafe_allow_html=True)
        valortotal = (acceleration+sprint_speed+agility+stamina+interceptions+defensive_awareness+standing_tackle+reactions+composure)/9
        col2.markdown(f'#### **Valor total:** {valortotal:.0f}')

    if acao == 'Falta de perto':
        col2.markdown(f'#### {acao}')
        col2.markdown(f'**Finalização** <span style="color: {def_cor(finishing)};">{finishing}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Força do Chute** <span style="color: {def_cor(shot_power)};">{shot_power}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Visão** <span style="color: {def_cor(vision)};">{vision}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Falta** <span style="color: {def_cor(fk_accuracy)};">{fk_accuracy}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Curva** <span style="color: {def_cor(curve)};">{curve}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Frieza** <span style="color: {def_cor(composure)};">{composure}</span>', unsafe_allow_html=True)
        valortotal = (finishing+shot_power+vision+fk_accuracy+curve+composure)/6
        col2.markdown(f'#### **Valor total:** {valortotal:.0f}')

    if acao == 'Falta de longe':
        col2.markdown(f'#### {acao}')
        col2.markdown(f'**Finalização** <span style="color: {def_cor(finishing)};">{finishing}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Força do Chute** <span style="color: {def_cor(shot_power)};">{shot_power}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Visão** <span style="color: {def_cor(vision)};">{vision}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Falta** <span style="color: {def_cor(fk_accuracy)};">{fk_accuracy}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Curva** <span style="color: {def_cor(curve)};">{curve}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Frieza** <span style="color: {def_cor(composure)};">{composure}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Chute de Longe** <span style="color: {def_cor(long_shots)};">{long_shots}</span>', unsafe_allow_html=True)
        valortotal = (finishing+shot_power+vision+fk_accuracy+curve+composure+long_shots)/7
        col2.markdown(f'#### **Valor total:** {valortotal:.0f}')

    if acao == 'Penalty':
        col2.markdown(f'#### {acao}')
        col2.markdown(f'**Finalização** <span style="color: {def_cor(finishing)};">{finishing}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Força do chute** <span style="color: {def_cor(shot_power)};">{shot_power}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Penalty** <span style="color: {def_cor(penalties)};">{penalties}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Curva** <span style="color: {def_cor(curve)};">{curve}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Frieza** <span style="color: {def_cor(composure)};">{composure}</span>', unsafe_allow_html=True)
        valortotal = (finishing+shot_power+penalties+curve+composure)/5
        col2.markdown(f'#### **Valor total:** {valortotal:.0f}')

    if acao == 'Interceptação Rasteira':
        col2.markdown(f'#### {acao}')
        col2.markdown(f'**Posicionamento** <span style="color: {def_cor(positioning)};">{positioning}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Reação** <span style="color: {def_cor(reactions)};">{reactions}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Frieza** <span style="color: {def_cor(composure)};">{composure}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Interceptação** <span style="color: {def_cor(interceptions)};">{interceptions}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Controle de Bola** <span style="color: {def_cor(ball_control)};">{ball_control}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Visão** <span style="color: {def_cor(vision)};">{vision}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Agilidade** <span style="color: {def_cor(agility)};">{agility}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Equilibrio** <span style="color: {def_cor(balance)};">{balance}</span>', unsafe_allow_html=True)
        valortotal = (positioning+reactions+composure+interceptions+ball_control+vision+agility+balance)/8
        col2.markdown(f'#### **Valor total:** {valortotal:.0f}')

    if acao == 'Interceptação alta':
        col2.markdown(f'#### {acao}')
        col2.markdown(f'**Posicionamento** <span style="color: {def_cor(positioning)};">{positioning}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Reação** <span style="color: {def_cor(reactions)};">{reactions}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Frieza** <span style="color: {def_cor(composure)};">{composure}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Interceptação** <span style="color: {def_cor(interceptions)};">{interceptions}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Controle de Bola** <span style="color: {def_cor(ball_control)};">{ball_control}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Visão** <span style="color: {def_cor(vision)};">{vision}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Agilidade** <span style="color: {def_cor(agility)};">{agility}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Impulsão** <span style="color: {def_cor(jumping)};">{jumping}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Equilibrio** <span style="color: {def_cor(balance)};">{balance}</span>', unsafe_allow_html=True)
        valortotal = (positioning+reactions+composure+interceptions+ball_control+vision+agility+jumping+balance)/9
        col2.markdown(f'#### **Valor total:** {valortotal:.0f}')

    if acao == 'Carrinho':
        col2.markdown(f'#### {acao}')
        col2.markdown(f'**Força** <span style="color: {def_cor(strength)};">{strength}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Combatividade** <span style="color: {def_cor(aggression)};">{aggression}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Reação** <span style="color: {def_cor(reactions)};">{reactions}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Frieza** <span style="color: {def_cor(composure)};">{composure}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Interceptação** <span style="color: {def_cor(interceptions)};">{interceptions}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Def. Awareness** <span style="color: {def_cor(defensive_awareness)};">{defensive_awareness}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Carrinho** <span style="color: {def_cor(sliding_tackle)};">{sliding_tackle}</span>', unsafe_allow_html=True)
        valortotal = (strength+aggression+reactions+composure+interceptions+defensive_awareness+sliding_tackle)/7
        col2.markdown(f'#### **Valor total:** {valortotal:.0f}')

    if acao == 'Disputa de bola':
        col2.markdown(f'#### {acao}')
        col2.markdown(f'**Força** <span style="color: {def_cor(strength)};">{strength}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Combatividade** <span style="color: {def_cor(aggression)};">{aggression}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Dividida em Pé** <span style="color: {def_cor(standing_tackle)};">{standing_tackle}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Def. Awareness** <span style="color: {def_cor(defensive_awareness)};">{defensive_awareness}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Frieza** <span style="color: {def_cor(composure)};">{composure}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Reações** <span style="color: {def_cor(reactions)};">{reactions}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Equilibrio** <span style="color: {def_cor(balance)};">{balance}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Aceleração** <span style="color: {def_cor(acceleration)};">{acceleration}</span>', unsafe_allow_html=True)
        valortotal = (strength+aggression+standing_tackle+defensive_awareness+composure+reactions+balance+acceleration)/8
        col2.markdown(f'#### **Valor total:** {valortotal:.0f}')

    if acao == 'Drible':
        col2.markdown(f'#### {acao}')
        col2.markdown(f'**Aceleração** <span style="color: {def_cor(acceleration)};">{acceleration}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Visão** <span style="color: {def_cor(vision)};">{vision}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Agilidade** <span style="color: {def_cor(agility)};">{agility}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Equilibrio** <span style="color: {def_cor(balance)};">{balance}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Reações** <span style="color: {def_cor(reactions)};">{reactions}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Controle de Bola** <span style="color: {def_cor(ball_control)};">{ball_control}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Drible** <span style="color: {def_cor(dribbling)};">{dribbling}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Frieza** <span style="color: {def_cor(composure)};">{composure}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Combatividade** <span style="color: {def_cor(aggression)};">{aggression}</span>', unsafe_allow_html=True)
        valortotal = (acceleration+vision+agility+balance+reactions+ball_control+dribbling+composure+aggression)/9
        col2.markdown(f'#### **Valor total:** {valortotal:.0f}')

    if acao == 'Colocar á frente':
        col2.markdown(f'#### {acao}')
        col2.markdown(f'**Aceleração** <span style="color: {def_cor(acceleration)};">{acceleration}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Sprint** <span style="color: {def_cor(sprint_speed)};">{sprint_speed}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Posicionamento** <span style="color: {def_cor(positioning)};">{positioning}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Visão** <span style="color: {def_cor(vision)};">{vision}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Controle de Bola** <span style="color: {def_cor(ball_control)};">{ball_control}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Frieza** <span style="color: {def_cor(composure)};">{composure}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Estamina** <span style="color: {def_cor(stamina)};">{stamina}</span>', unsafe_allow_html=True)
        valortotal = (acceleration+sprint_speed+positioning+vision+ball_control+composure+stamina)/7
        col2.markdown(f'#### **Valor total:** {valortotal:.0f}')

    if acao == 'Passe curto':
        col2.markdown(f'#### {acao}')
        col2.markdown(f'**Visão** <span style="color: {def_cor(vision)};">{vision}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Curva** <span style="color: {def_cor(curve)};">{curve}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Passe Curto** <span style="color: {def_cor(short_passing)};">{short_passing}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Reação** <span style="color: {def_cor(reactions)};">{reactions}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Frieza** <span style="color: {def_cor(composure)};">{composure}</span>', unsafe_allow_html=True)
        valortotal = (vision+curve+short_passing+reactions+composure)/5
        col2.markdown(f'#### **Valor total:** {valortotal:.0f}')

    if acao == 'Passe longo':
        col2.markdown(f'#### {acao}')
        col2.markdown(f'**Visão** <span style="color: {def_cor(vision)};">{vision}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Curva** <span style="color: {def_cor(curve)};">{curve}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Passe Longo** <span style="color: {def_cor(long_passing)};">{long_passing}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Reação** <span style="color: {def_cor(reactions)};">{reactions}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Frieza** <span style="color: {def_cor(composure)};">{composure}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Força do Passe** <span style="color: {def_cor(shot_power)};">{shot_power}</span>', unsafe_allow_html=True)
        valortotal = (vision+curve+long_passing+reactions+composure+shot_power)/6
        col2.markdown(f'#### **Valor total:** {valortotal:.0f}')

    if acao == 'Cruzamento':
        col2.markdown(f'#### {acao}')
        col2.markdown(f'**Visão** <span style="color: {def_cor(vision)};">{vision}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Curva** <span style="color: {def_cor(curve)};">{curve}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Cruzamento** <span style="color: {def_cor(crossing)};">{crossing}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Reação** <span style="color: {def_cor(reactions)};">{reactions}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Frieza** <span style="color: {def_cor(composure)};">{composure}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Força do Passe** <span style="color: {def_cor(shot_power)};">{shot_power}</span>', unsafe_allow_html=True)
        valortotal = (vision+curve+crossing+reactions+composure+shot_power)/6
        col2.markdown(f'#### **Valor total:** {valortotal:.0f}')

    if acao == 'Receber a bola':
        col2.markdown(f'#### {acao}')
        col2.markdown(f'**Posicionamento** <span style="color: {def_cor(positioning)};">{positioning}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Equilibrio** <span style="color: {def_cor(balance)};">{balance}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Reação** <span style="color: {def_cor(reactions)};">{reactions}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Controle de Bola** <span style="color: {def_cor(ball_control)};">{ball_control}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Frieza** <span style="color: {def_cor(composure)};">{composure}</span>', unsafe_allow_html=True)
        valortotal = (positioning+balance+reactions+ball_control+composure)/5
        col2.markdown(f'#### **Valor total:** {valortotal:.0f}')

    if acao == 'Chutar a gol':
        col2.markdown(f'#### {acao}')
        col2.markdown(f'**Posicionamento** <span style="color: {def_cor(positioning)};">{positioning}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Finalização** <span style="color: {def_cor(finishing)};">{finishing}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Força do Chute** <span style="color: {def_cor(shot_power)};">{shot_power}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Equilibrio** <span style="color: {def_cor(balance)};">{balance}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Controle de Bola** <span style="color: {def_cor(ball_control)};">{ball_control}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Frieza** <span style="color: {def_cor(composure)};">{composure}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Reação** <span style="color: {def_cor(reactions)};">{reactions}</span>', unsafe_allow_html=True)
        valortotal = (positioning+finishing+shot_power+balance+ball_control+composure+reactions)/7
        col2.markdown(f'#### **Valor total:** {valortotal:.0f}')


    if acao == 'Chutar a gol - FDA':
        col2.markdown(f'#### {acao}')
        col2.markdown(f'**Posicionamento** <span style="color: {def_cor(positioning)};">{positioning}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Finalização** <span style="color: {def_cor(finishing)};">{finishing}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Força do Chute** <span style="color: {def_cor(shot_power)};">{shot_power}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Equilibrio** <span style="color: {def_cor(balance)};">{balance}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Controle de Bola** <span style="color: {def_cor(ball_control)};">{ball_control}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Frieza** <span style="color: {def_cor(composure)};">{composure}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Reação** <span style="color: {def_cor(reactions)};">{reactions}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Chute de Longe** <span style="color: {def_cor(long_shots)};">{long_shots}</span>', unsafe_allow_html=True)
        valortotal = (positioning+finishing+shot_power+balance+ball_control+composure+reactions+long_shots)/8
        col2.markdown(f'#### **Valor total:** {valortotal:.0f}')

    if acao == 'Defesa Goleiro':
        col2.markdown(f'#### {acao}')
        col2.markdown(f'**Ponte** <span style="color: {def_cor(gk_diving)};">{gk_diving}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Posicionamento** <span style="color: {def_cor(gk_positioning)};">{gk_positioning}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Reflexos** <span style="color: {def_cor(gk_reflexes)};">{gk_reflexes}</span>', unsafe_allow_html=True)
        col2.markdown(f'**Reação** <span style="color: {def_cor(reactions)};">{reactions}</span>', unsafe_allow_html=True)
        valortotal = (gk_diving+gk_positioning+gk_reflexes+reactions)/4
        col2.markdown(f'#### **Valor total:** {valortotal:.0f}')
        

    if inter == 'Nenhum jogador':

        if valortotal > 0 and valortotal <= 20:
            col1.write('Será um teste impossível, tire 9 ou 0')

        if valortotal > 21 and valortotal <= 40:
            col1.write('Será um teste Muito Difícil, tire 7 ou 8')

        if valortotal > 41 and valortotal <= 60:
            col1.write('Será um teste Difícil, tire 5 ou 6')

        if valortotal > 61 and valortotal <= 80:
            col1.write('Será um teste Mediano, tire 3 ou 4')

        if valortotal > 81 and valortotal <= 100:
            col1.write('Será um teste Fácil, tire 1 ou 2')

    if inter == 'Um jogador':

        if valortotal > 0 and valortotal <= 20:
            col1.write(f'Será um teste impossível, tire 0')
        
        if valortotal > 21 and valortotal <= 40:
            col1.write(f'Será um teste Muito Difícil, tire 8 ou 9')
    
        if valortotal > 41 and valortotal <= 60:
            col1.write(f'Será um teste Difícil, tire 6 ou 7')
    
        if valortotal > 61 and valortotal <= 80:
            col1.write(f'Será um teste Mediano, tire 4 ou 5')
    
        if valortotal > 81 and valortotal <= 100:
            col1.write(f'Será um teste Fácil, tire 2 ou 3')

    if inter == 'Dois jogadores':

        if valortotal > 0 and valortotal <= 20:
            col1.write(f'Será um teste impossível, tire 11 ou 12')
            col1.write(f'Jogue 2 dados d10 e tire em um deles 9 ou 0')
        
        if valortotal > 21 and valortotal <= 40:
            col1.write(f'Será um teste Muito Difícil, tire 9 ou 0')
    
        if valortotal > 41 and valortotal <= 60:
            col1.write(f'Será um teste Difícil, tire 7 ou 8')
    
        if valortotal > 61 and valortotal <= 80:
            col1.write(f'Será um teste Mediano, tire 5 ou 6')
    
        if valortotal > 81 and valortotal <= 100:
            col1.write(f'Será um teste Fácil, tire 3 ou 4')

    if inter == 'Três jogadores':

        if valortotal > 0 and valortotal <= 20:
            col1.write(f'Será um teste impossível, tire 12 ou  13')
            col1.write(f'Jogue 2 dados d10 e tire 9 ou 0 no primeiro e 2 ou mais no segundo')
        
        if valortotal > 21 and valortotal <= 40:
            col1.write(f'Será um teste Muito Difícil, tire 10 ou 11')
            col1.write(f'Jogue 2 dados d10 e tire em um deles 9 ou 0')
    
        if valortotal > 41 and valortotal <= 60:
            col1.write(f'Será um teste Difícil, tire 8 ou 9')
    
        if valortotal > 61 and valortotal <= 80:
            col1.write(f'Será um teste Mediano, tire 6 ou 7')
    
        if valortotal > 81 and valortotal <= 100:
            col1.write(f'Será um teste Fácil, tire 4 ou 5')

    if inter == 'Quatro jogadores':

        if valortotal > 0 and valortotal <= 20:
            col1.write(f'Será um teste impossível, tire 13 ou 14')
            col1.write(f'Jogue 2 dados d10 e tire 9 ou 0 no primeiro e 4 ou mais no segundo')
        
        if valortotal > 21 and valortotal <= 40:
            col1.write(f'Será um teste Muito Difícil, 11 ou 12')
            col1.write(f'Jogue 2 dados d10 e tire 9 ou 0 no primeiro e 2 ou mais no segundo')
    
        if valortotal > 41 and valortotal <= 60:
            col1.write(f'Será um teste Difícil, tire 9 ou 0')
            col1.write(f'Jogue 2 dados d10 e tire em um deles 9 ou 0')
    
        if valortotal > 61 and valortotal <= 80:
            col1.write(f'Será um teste Mediano, tire 7 ou 8')
            col1.write(f'Jogue 2 dados d10')
    
        if valortotal > 81 and valortotal <= 100:
            col1.write(f'Será um teste Fácil, tire 5 ou 6')

    col3.image(player_stats['Foto'], width = 300)

    col4, col5, col6 =  st.columns([1,5,1])

    btn = col4.button("d10")
    if btn:
        num = random.randint(0,9)
        col5.markdown(f"Seu d10 tirou: {num}")

    btn1 = col4.button("d100")
    if btn1:
        num1 = random.randint(0,100)
        col5.markdown(f"Seu d100 tirou: {num1}")

with col2:
    container = st.container()
    
with col3:
    container = st.container()

col7, col8 = st.columns(2)
if acao == 'Defesa Goleiro':
    gol = col7.selectbox(
        'Selecione a posição do goleiro',
        ['Esquerda', 'Meio Esquerda', 'Meio Direita', 'Direita'], index=None,
        placeholder="Escolha uma opção...",)
    col7.write(f'Você escolheu a ação: {gol}')
    if gol == 'Esquerda':
        col8.image('/Users/dafreire/Desktop/Fifa project/Imagens/esquerda.png')
    if gol == 'Direita':
        col8.image('/Users/dafreire/Desktop/Fifa project/Imagens/direita.png')
    if gol == 'Meio Esquerda':
        col8.image('/Users/dafreire/Desktop/Fifa project/Imagens/meia equerda.png')
    if gol == 'Meio Direita':
        col8.image('/Users/dafreire/Desktop/Fifa project/Imagens/meia direita.png')
