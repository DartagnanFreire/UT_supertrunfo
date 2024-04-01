import streamlit as st
import pandas as pd
import random

st.set_page_config(
    page_title='Super Trunfo',
    layout='wide'
)

df = st.session_state["data"]
df_gk = df[df['Posição'].str.contains('GK')]
df_gk = df_gk.reset_index(drop=True)
df = df.loc[df['Posição'] != 'GK']
df = df.reset_index(drop=True)
numeros = random.sample(range(len(df)), 2)
num1 = numeros[0]
num2 = numeros[1]

acceleration = df['Acceleration'][num1]
sprint_speed = df['Sprint Speed'][num1]
positioning = df['Positioning'][num1]
finishing = df['Finishing'][num1]
shot_power = df['Shot Power'][num1]
long_shots = df['Long Shot'][num1]
volleys = df['Volleys'][num1]
penalties = df['Penalties'][num1]
vision = df['Vision'][num1]
crossing = df['Crossing'][num1]
fk_accuracy = df['Free Kick'][num1]
short_passing = df['Shot Passing'][num1]
long_passing = df['Long Passing'][num1]
curve = df['Curve'][num1]
agility = df['Agility'][num1]
balance = df['Balance'][num1]
reactions = df['Reactions'][num1]
ball_control = df['Ball Control'][num1]
dribbling = df['Dribbling'][num1]
composure = df['Composure'][num1]
interceptions = df['Interceptions'][num1]
heading_accuracy = df['Heading'][num1]
defensive_awareness = df['Def. Awareness'][num1]
standing_tackle = df['Standing Tackle'][num1]
sliding_tackle = df['Sliding'][num1]
jumping = df['Jumping'][num1]
stamina = df['Stamina'][num1]
strength = df['Strength'][num1]
aggression = df['Aggression'][num1]

acceleration2 = df['Acceleration'][num2]
sprint_speed2 = df['Sprint Speed'][num2]
positioning2 = df['Positioning'][num2]
finishing2 = df['Finishing'][num2]
shot_power2 = df['Shot Power'][num2]
long_shots2 = df['Long Shot'][num2]
volleys2 = df['Volleys'][num2]
penalties2 = df['Penalties'][num2]
vision2 = df['Vision'][num2]
crossing2 = df['Crossing'][num2]
fk_accuracy2 = df['Free Kick'][num2]
short_passing2 = df['Shot Passing'][num2]
long_passing2 = df['Long Passing'][num2]
curve2 = df['Curve'][num2]
agility2 = df['Agility'][num2]
balance2 = df['Balance'][num2]
reactions2 = df['Reactions'][num2]
ball_control2 = df['Ball Control'][num2]
dribbling2 = df['Dribbling'][num2]
composure2 = df['Composure'][num2]
interceptions2 = df['Interceptions'][num2]
heading_accuracy2 = df['Heading'][num2]
defensive_awareness2 = df['Def. Awareness'][num2]
standing_tackle2 = df['Standing Tackle'][num2]
sliding_tackle2 = df['Sliding'][num2]
jumping2 = df['Jumping'][num2]
stamina2 = df['Stamina'][num2]
strength2 = df['Strength'][num2]
aggression2 = df['Aggression'][num2]

gk = random.sample(range(len(df_gk)), 1)
gk = gk[0]

# Verifica a condição da variável
def def_cor(defi):
    if defi <= 49:
        cor = '#ec1b1e'
    elif defi >= 50 and defi <= 69:
        cor = '#ff8c00'
    elif defi >=70 and defi <= 79:
        cor = '#3fd442'
    elif defi == 99:
        cor = '#00B4FF'
    else:
        cor = '#29982b' 
    return cor

jogador = st.selectbox(
    'Selecione um formato:',
    ['Status Individuais', 'Status Agrupados', 'Por ação'], index=None,
    placeholder="Escolha um jogador...",)
st.write(f'Você escolheu o {jogador}')
st.button("Gerar", type="primary")
col1, col2 = st.columns(2)

col1.markdown('# Jogador 1')
col2.markdown('# Jogador 2')

if jogador == 'Status Individuais':
    status = ['aceleracao', 'sprint', 'posicionamento', 'finalizacao', 'forca chute', 'chute longe', 'voleio', 'penalti', 'visao', 'cruzamento', 'falta', 'passe curto',
          'passe longo', 'curva', 'agilidade', 'balanco', 'reacao', 'controle', 'drible', 'frieza', 'interceptacao', 'cabeceio', 'def', 'bloqueio', 'carrinho',
           'pulo', 'estamina', 'forca', 'agressao']
    status_ok = random.choice(status)
    with col1:
        col3, col4 = st.columns(2)
        if status_ok == 'aceleracao':
            col4.markdown(f'#### **Aceleração** <span style="color: {def_cor(df["Acceleration"][num1])};">{df["Acceleration"][num1]}</span>', unsafe_allow_html=True)
        if status_ok == 'sprint':
            col4.markdown(f'#### **Sprint Speed** <span style="color: {def_cor(df["Sprint Speed"][num1])};">{df["Sprint Speed"][num1]}</span>', unsafe_allow_html=True) 
        if status_ok == 'posicionamento':
            col4.markdown(f'#### **Posicionamento** <span style="color: {def_cor(df["Positioning"][num1])};">{df["Positioning"][num1]}</span>', unsafe_allow_html=True)
        if status_ok == 'finalizacao':
            col4.markdown(f'#### **Finalização** <span style="color: {def_cor(df["Finishing"][num1])};">{df["Finishing"][num1]}</span>', unsafe_allow_html=True)
        if status_ok == 'forca chute':
            col4.markdown(f'#### **Força do Chute** <span style="color: {def_cor(df["Shot Power"][num1])};">{df["Shot Power"][num1]}</span>', unsafe_allow_html=True)
        if status_ok == 'chute longe':
            col4.markdown(f'#### **Chute de Longe** <span style="color: {def_cor(df["Long Shot"][num1])};">{df["Long Shot"][num1]}</span>', unsafe_allow_html=True)
        if status_ok == 'voleio':
            col4.markdown(f'#### **Voleios** <span style="color: {def_cor(df["Volleys"][num1])};">{df["Volleys"][num1]}</span>', unsafe_allow_html=True)
        if status_ok == 'penalti':
            col4.markdown(f'#### **Penaltis** <span style="color: {def_cor(df["Penalties"][num1])};">{df["Penalties"][num1]}</span>', unsafe_allow_html=True)
        if status_ok == 'visao':
            col4.markdown(f'#### **Visão** <span style="color: {def_cor(df["Vision"][num1])};">{df["Vision"][num1]}</span>', unsafe_allow_html=True)
        if status_ok == 'cruzamento':
            col4.markdown(f'#### **Cruzamento** <span style="color: {def_cor(df["Crossing"][num1])};">{df["Crossing"][num1]}</span>', unsafe_allow_html=True)
        if status_ok == 'falta':
            col4.markdown(f'#### **Faltas** <span style="color: {def_cor(df["Free Kick"][num1])};">{df["Free Kick"][num1]}</span>', unsafe_allow_html=True)
        if status_ok == 'passe curto':
            col4.markdown(f'**Passe Curto** <span style="color: {def_cor(df["Shot Passing"][num1])};">{df["Shot Passing"][num1]}</span>', unsafe_allow_html=True)
        if status_ok == 'passe longo':
            col4.markdown(f'#### **Passe Longo** <span style="color: {def_cor(df["Long Passing"][num1])};">{df["Long Passing"][num1]}</span>', unsafe_allow_html=True)
        if status_ok == 'curva':
            col4.markdown(f'#### **Curva** <span style="color: {def_cor(df["Curve"][num1])};">{df["Curve"][num1]}</span>', unsafe_allow_html=True)
        if status_ok == 'agilidade':
            col4.markdown(f'#### **Agilidade** <span style="color: {def_cor(df["Agility"][num1])};">{df["Agility"][num1]}</span>', unsafe_allow_html=True)
        if status_ok == 'balanco':
            col4.markdown(f'#### **Balanço** <span style="color: {def_cor(df["Balance"][num1])};">{df["Balance"][num1]}</span>', unsafe_allow_html=True)
        if status_ok == 'reacao':
            col4.markdown(f'#### **Reação** <span style="color: {def_cor(df["Reactions"][num1])};">{df["Reactions"][num1]}</span>', unsafe_allow_html=True)
        if status_ok == 'controle':
            col4.markdown(f'#### **Controle de Bola** <span style="color: {def_cor(df["Ball Control"][num1])};">{df["Ball Control"][num1]}</span>', unsafe_allow_html=True)
        if status_ok == 'drible':
            col4.markdown(f'#### **Drible** <span style="color: {def_cor(df["Dribbling"][num1])};">{df["Dribbling"][num1]}</span>', unsafe_allow_html=True)
        if status_ok == 'frieza':
            col4.markdown(f'#### **Frieza** <span style="color: {def_cor(df["Composure"][num1])};">{df["Composure"][num1]}</span>', unsafe_allow_html=True)
        if status_ok == 'interceptacao':
            col4.markdown(f'#### **Interceptação** <span style="color: {def_cor(df["Interceptions"][num1])};">{df["Interceptions"][num1]}</span>', unsafe_allow_html=True)
        if status_ok == 'cabeceio':
            col4.markdown(f'#### **Cabeceio** <span style="color: {def_cor(df["Heading"][num1])};">{df["Heading"][num1]}</span>', unsafe_allow_html=True)
        if status_ok == 'def':
            col4.markdown(f'#### **Def. Awareness** <span style="color: {def_cor(df["Def. Awareness"][num1])};">{df["Def. Awareness"][num1]}</span>', unsafe_allow_html=True)
        if status_ok == 'bloqueio':
            col4.markdown(f'#### **Bloqueio** <span style="color: {def_cor(df["Standing Tackle"][num1])};">{df["Standing Tackle"][num1]}</span>', unsafe_allow_html=True)
        if status_ok == 'carrinho':
            col4.markdown(f'#### **Carrinho** <span style="color: {def_cor(df["Sliding"][num1])};">{df["Sliding"][num1]}</span>', unsafe_allow_html=True)
        if status_ok == 'pulo':
            col4.markdown(f'#### **Pulo** <span style="color: {def_cor(df["Jumping"][num1])};">{df["Jumping"][num1]}</span>', unsafe_allow_html=True)
        if status_ok == 'estamina':
            col4.markdown(f'#### **Estamina** <span style="color: {def_cor(df["Stamina"][num1])};">{df["Stamina"][num1]}</span>', unsafe_allow_html=True)
        if status_ok == 'forca':
            col4.markdown(f'#### **Força** <span style="color: {def_cor(df["Strength"][num1])};">{df["Strength"][num1]}</span>', unsafe_allow_html=True)
        if status_ok == 'agressao':
            col4.markdown(f'#### **Agressão** <span style="color: {def_cor(df["Aggression"][num1])};">{df["Aggression"][num1]}</span>', unsafe_allow_html=True)
        col3.subheader(df['Nome Completo'][num1])
        col3.image(df['Foto'][num1], width = 270)

    with col2:
        col5, col6 = st.columns(2)
        if status_ok == 'aceleracao':
            col6.markdown(f'#### **Aceleração** <span style="color: {def_cor(df["Acceleration"][num2])};">{df["Acceleration"][num2]}</span>', unsafe_allow_html=True)
        if status_ok == 'sprint':
            col6.markdown(f'#### **Sprint Speed** <span style="color: {def_cor(df["Sprint Speed"][num2])};">{df["Sprint Speed"][num2]}</span>', unsafe_allow_html=True) 
        if status_ok == 'posicionamento':
            col6.markdown(f'#### **Posicionamento** <span style="color: {def_cor(df["Positioning"][num2])};">{df["Positioning"][num2]}</span>', unsafe_allow_html=True)
        if status_ok == 'finalizacao':
            col6.markdown(f'#### **Finalização** <span style="color: {def_cor(df["Finishing"][num2])};">{df["Finishing"][num2]}</span>', unsafe_allow_html=True)
        if status_ok == 'forca chute':
            col6.markdown(f'#### **Força do Chute** <span style="color: {def_cor(df["Shot Power"][num2])};">{df["Shot Power"][num2]}</span>', unsafe_allow_html=True)
        if status_ok == 'chute longe':
            col6.markdown(f'#### **Chute de Longe** <span style="color: {def_cor(df["Long Shot"][num2])};">{df["Long Shot"][num2]}</span>', unsafe_allow_html=True)
        if status_ok == 'voleio':
            col6.markdown(f'#### **Voleios** <span style="color: {def_cor(df["Volleys"][num2])};">{df["Volleys"][num2]}</span>', unsafe_allow_html=True)
        if status_ok == 'penalti':
            col6.markdown(f'#### **Penaltis** <span style="color: {def_cor(df["Penalties"][num2])};">{df["Penalties"][num2]}</span>', unsafe_allow_html=True)
        if status_ok == 'visao':
            col6.markdown(f'#### **Visão** <span style="color: {def_cor(df["Vision"][num2])};">{df["Vision"][num2]}</span>', unsafe_allow_html=True)
        if status_ok == 'cruzamento':
            col6.markdown(f'#### **Cruzamento** <span style="color: {def_cor(df["Crossing"][num2])};">{df["Crossing"][num2]}</span>', unsafe_allow_html=True)
        if status_ok == 'falta':
            col6.markdown(f'#### **Faltas** <span style="color: {def_cor(df["Free Kick"][num2])};">{df["Free Kick"][num2]}</span>', unsafe_allow_html=True)
        if status_ok == 'passe curto':
            col6.markdown(f'#### **Passe Curto** <span style="color: {def_cor(df["Shot Passing"][num2])};">{df["Shot Passing"][num2]}</span>', unsafe_allow_html=True)
        if status_ok == 'passe longo':
            col6.markdown(f'#### **Passe Longo** <span style="color: {def_cor(df["Long Passing"][num2])};">{df["Long Passing"][num2]}</span>', unsafe_allow_html=True)
        if status_ok == 'curva':
            col6.markdown(f'#### **Curva** <span style="color: {def_cor(df["Curve"][num2])};">{df["Curve"][num2]}</span>', unsafe_allow_html=True)
        if status_ok == 'agilidade':
            col6.markdown(f'#### **Agilidade** <span style="color: {def_cor(df["Agility"][num2])};">{df["Agility"][num2]}</span>', unsafe_allow_html=True)
        if status_ok == 'balanco':
            col6.markdown(f'#### **Balanço** <span style="color: {def_cor(df["Balance"][num2])};">{df["Balance"][num2]}</span>', unsafe_allow_html=True)
        if status_ok == 'reacao':
            col6.markdown(f'#### **Reação** <span style="color: {def_cor(df["Reactions"][num2])};">{df["Reactions"][num2]}</span>', unsafe_allow_html=True)
        if status_ok == 'controle':
            col6.markdown(f'#### **Controle de Bola** <span style="color: {def_cor(df["Ball Control"][num2])};">{df["Ball Control"][num2]}</span>', unsafe_allow_html=True)
        if status_ok == 'drible':
            col6.markdown(f'#### **Drible** <span style="color: {def_cor(df["Dribbling"][num2])};">{df["Dribbling"][num2]}</span>', unsafe_allow_html=True)
        if status_ok == 'frieza':
            col6.markdown(f'#### **Frieza** <span style="color: {def_cor(df["Composure"][num2])};">{df["Composure"][num2]}</span>', unsafe_allow_html=True)
        if status_ok == 'interceptacao':
            col6.markdown(f'#### **Interceptação** <span style="color: {def_cor(df["Interceptions"][num2])};">{df["Interceptions"][num2]}</span>', unsafe_allow_html=True)
        if status_ok == 'cabeceio':
            col6.markdown(f'#### **Cabeceio** <span style="color: {def_cor(df["Heading"][num2])};">{df["Heading"][num2]}</span>', unsafe_allow_html=True)
        if status_ok == 'def':
            col6.markdown(f'#### **Def. Awareness** <span style="color: {def_cor(df["Def. Awareness"][num2])};">{df["Def. Awareness"][num2]}</span>', unsafe_allow_html=True)
        if status_ok == 'bloqueio':
            col6.markdown(f'#### **Bloqueio** <span style="color: {def_cor(df["Standing Tackle"][num2])};">{df["Standing Tackle"][num2]}</span>', unsafe_allow_html=True)
        if status_ok == 'carrinho':
            col6.markdown(f'#### **Carrinho** <span style="color: {def_cor(df["Sliding"][num2])};">{df["Sliding"][num2]}</span>', unsafe_allow_html=True)
        if status_ok == 'pulo':
            col6.markdown(f'#### **Pulo** <span style="color: {def_cor(df["Jumping"][num2])};">{df["Jumping"][num2]}</span>', unsafe_allow_html=True)
        if status_ok == 'estamina':
            col6.markdown(f'#### **Estamina** <span style="color: {def_cor(df["Stamina"][num2])};">{df["Stamina"][num2]}</span>', unsafe_allow_html=True)
        if status_ok == 'forca':
            col6.markdown(f'#### **Força** <span style="color: {def_cor(df["Strength"][num2])};">{df["Strength"][num2]}</span>', unsafe_allow_html=True)
        if status_ok == 'agressao':
            col6.markdown(f'#### **Agressão** <span style="color: {def_cor(df["Aggression"][num2])};">{df["Aggression"][num2]}</span>', unsafe_allow_html=True)
        col5.subheader(df['Nome Completo'][num2])
        col5.image(df['Foto'][num2], width = 270)


if jogador == 'Status Agrupados':
    agrupado = ['velo', 'chute', 'passe', 'drible', 'defesa', 'fisico']
    agg_ok = random.choice(agrupado)
    with col1:
        col3, col4 = st.columns(2)
        velo = ((df['Acceleration'][num1]) + (df['Sprint Speed'][num1]))/2
        chute = (df['Positioning'][num1] + df['Finishing'][num1] + df['Shot Power'][num1] + df['Long Shot'][num1] + df['Volleys'][num1] + df['Penalties'][num1])/6
        passe = (df['Vision'][num1] + df['Crossing'][num1] + df['Free Kick'][num1] + df['Shot Passing'][num1] + df['Long Passing'][num1] + df['Curve'][num1])/6
        drible = (df['Agility'][num1] + df['Balance'][num1] + df['Reactions'][num1] + df['Ball Control'][num1] + df['Dribbling'][num1] + df['Composure'][num1])/6
        defesa = (df['Interceptions'][num1] + df['Heading'][num1] + df['Def. Awareness'][num1] + df['Standing Tackle'][num1] + df['Sliding'][num1])/5
        fisico = (df['Jumping'][num1] + df['Stamina'][num1] + df['Strength'][num1] + df['Aggression'][num1])/4
        overall = (velo + chute + passe + drible + defesa + fisico)/6
        if agg_ok == 'velo':
            col4.markdown(f'#### **Velocidade** <span style="color: {def_cor(velo)};">{velo:.0f}</span>', unsafe_allow_html=True)
        if agg_ok == 'chute':
            col4.markdown(f'#### **Chute** <span style="color: {def_cor(chute)};">{chute:.0f}</span>', unsafe_allow_html=True)
        if agg_ok == 'passe':
            col4.markdown(f'#### **Passe** <span style="color: {def_cor(passe)};">{passe:.0f}</span>', unsafe_allow_html=True)
        if agg_ok == 'drible':
            col4.markdown(f'#### **Drible** <span style="color: {def_cor(drible)};">{drible:.0f}</span>', unsafe_allow_html=True)
        if agg_ok == 'defesa':
            col4.markdown(f'#### **Defesa** <span style="color: {def_cor(defesa)};">{defesa:.0f}</span>', unsafe_allow_html=True)
        if agg_ok == 'fisico':
            col4.markdown(f'#### **Físico** <span style="color: {def_cor(fisico)};">{fisico:.0f}</span>', unsafe_allow_html=True)
        col3.subheader(df['Nome Completo'][num1])
        col3.image(df['Foto'][num1], width = 270)
    
    with col2:
        col5, col6 = st.columns(2)
        velo = ((df['Acceleration'][num2]) + (df['Sprint Speed'][num2]))/2
        chute = (df['Positioning'][num2] + df['Finishing'][num2] + df['Shot Power'][num2] + df['Long Shot'][num2] + df['Volleys'][num2] + df['Penalties'][num2])/6
        passe = (df['Vision'][num2] + df['Crossing'][num2] + df['Free Kick'][num2] + df['Shot Passing'][num2] + df['Long Passing'][num2] + df['Curve'][num2])/6
        drible = (df['Agility'][num2] + df['Balance'][num2] + df['Reactions'][num2] + df['Ball Control'][num2] + df['Dribbling'][num2] + df['Composure'][num2])/6
        defesa = (df['Interceptions'][num2] + df['Heading'][num2] + df['Def. Awareness'][num2] + df['Standing Tackle'][num2] + df['Sliding'][num2])/5
        fisico = (df['Jumping'][num2] + df['Stamina'][num2] + df['Strength'][num2] + df['Aggression'][num2])/4
        overall = (velo + chute + passe + drible + defesa + fisico)/6
        if agg_ok == 'velo':
            col6.markdown(f'#### **Velocidade** <span style="color: {def_cor(velo)};">{velo:.0f}</span>', unsafe_allow_html=True)
        if agg_ok == 'chute':
            col6.markdown(f'#### **Chute** <span style="color: {def_cor(chute)};">{chute:.0f}</span>', unsafe_allow_html=True)
        if agg_ok == 'passe':
            col6.markdown(f'#### **Passe** <span style="color: {def_cor(passe)};">{passe:.0f}</span>', unsafe_allow_html=True)
        if agg_ok == 'drible':
            col6.markdown(f'#### **Drible** <span style="color: {def_cor(drible)};">{drible:.0f}</span>', unsafe_allow_html=True)
        if agg_ok == 'defesa':
            col6.markdown(f'#### **Defesa** <span style="color: {def_cor(defesa)};">{defesa:.0f}</span>', unsafe_allow_html=True)
        if agg_ok == 'fisico':
            col6.markdown(f'#### **Físico** <span style="color: {def_cor(fisico)};">{fisico:.0f}</span>', unsafe_allow_html=True)
        col5.subheader(df['Nome Completo'][num2])
        col5.image(df['Foto'][num2], width = 270)
        
if jogador == 'Por ação':
    acao = ['Chute a gol sem domínio', 'Chute a gol sem domínio - FDA', 'Cabeceio ATK', 'Cabeceio DEF', 'Correr atrás', 'Falta de perto', 'Falta de longe', 
         'Penalty', 'Interceptação Rasteira', 'Interceptação alta', 'Carrinho', 'Disputa de bola', 'Drible', 'Colocar á frente', 'Passe curto', 'Passe longo', 'Cruzamento',
         'Receber a bola', 'Chutar a gol', 'Chutar a gol - FDA', 'Defesa Goleiro']
    acao_ok = random.choice(acao)
    col1.write(f'Foi escolhida a ação: {acao_ok}')
    col2.write(f'<p style="color:white;">Foi escolhida a ação: {acao_ok}</p>', unsafe_allow_html=True)
    with col1:
        col3, col4 = st.columns(2)
        col3.subheader(df['Nome Completo'][num1])
        col3.image(df['Foto'][num1], width = 270)
        if acao_ok == 'Chute a gol sem domínio':
            valortotal = (positioning+finishing+shot_power+volleys+balance+reactions+composure)/7
            col4.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)
        
        if acao_ok == 'Chute a gol sem domínio - FDA':
            valortotal = (positioning+finishing+shot_power+volleys+long_shots+balance+reactions+composure)/8
            col4.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Cabeceio ATK':
            valortotal = (positioning+jumping+aggression+heading_accuracy+reactions+composure+balance)/7
            col4.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Cabeceio DEF':
            valortotal = (positioning+jumping+aggression+heading_accuracy+reactions+composure+balance+interceptions+defensive_awareness)/9
            col4.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Correr atrás':
            valortotal = (acceleration+sprint_speed+agility+stamina+interceptions+defensive_awareness+standing_tackle+reactions+composure)/9
            col4.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Falta de perto':
            valortotal = (finishing+shot_power+vision+fk_accuracy+curve+composure)/6
            col4.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Falta de longe':
            valortotal = (finishing+shot_power+vision+fk_accuracy+curve+composure+long_shots)/7
            col4.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Penalty':
            valortotal = (finishing+shot_power+penalties+curve+composure)/5
            col4.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Interceptação Rasteira':
            valortotal = (positioning+reactions+composure+interceptions+ball_control+vision+agility+balance)/8
            col4.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Interceptação alta':
            valortotal = (positioning+reactions+composure+interceptions+ball_control+vision+agility+jumping+balance)/9
            col4.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Carrinho':
            valortotal = (strength+aggression+reactions+composure+interceptions+defensive_awareness+sliding_tackle)/7
            col4.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Disputa de bola':
            valortotal = (strength+aggression+standing_tackle+defensive_awareness+composure+reactions+balance+acceleration)/8
            col4.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Drible':
            valortotal = (acceleration+vision+agility+balance+reactions+ball_control+dribbling+composure+aggression)/9
            col4.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Colocar á frente':
            valortotal = (acceleration+sprint_speed+positioning+vision+ball_control+composure+stamina)/7
            col4.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Passe curto':
            valortotal = (vision+curve+short_passing+reactions+composure)/5
            col4.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Passe longo':
            valortotal = (vision+curve+long_passing+reactions+composure+shot_power)/6
            col4.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Cruzamento':
            valortotal = (vision+curve+crossing+reactions+composure+shot_power)/6
            col4.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Receber a bola':
            valortotal = (positioning+balance+reactions+ball_control+composure)/5
            col4.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Chutar a gol':
            valortotal = (positioning+finishing+shot_power+balance+ball_control+composure+reactions)/7
            col4.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Chutar a gol - FDA':
            valortotal = (positioning+finishing+shot_power+balance+ball_control+composure+reactions+long_shots)/8
            col4.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)
    
    with col2:
        col5, col6 = st.columns(2)
        col5.subheader(df['Nome Completo'][num2])
        col5.image(df['Foto'][num2], width = 270)
        if acao_ok == 'Chute a gol sem domínio':
            valortotal = (positioning2+finishing2+shot_power2+volleys2+balance2+reactions2+composure2)/7
            col6.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)
        
        if acao_ok == 'Chute a gol sem domínio - FDA':
            valortotal = (positioning2+finishing2+shot_power2+volleys2+long_shots2+balance2+reactions2+composure2)/8
            col6.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Cabeceio ATK':
            valortotal = (positioning2+jumping2+aggression2+heading_accuracy2+reactions2+composure2+balance2)/7
            col6.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Cabeceio DEF':
            valortotal = (positioning2+jumping2+aggression2+heading_accuracy2+reactions2+composure2+balance2+interceptions2+defensive_awareness2)/9
            col6.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Correr atrás':
            valortotal = (acceleration2+sprint_speed2+agility2+stamina2+interceptions2+defensive_awareness2+standing_tackle2+reactions2+composure2)/9
            col6.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Falta de perto':
            valortotal = (finishing2+shot_power2+vision2+fk_accuracy2+curve2+composure2)/6
            col6.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Falta de longe':
            valortotal = (finishing2+shot_power2+vision2+fk_accuracy2+curve2+composure2+long_shots2)/7
            col6.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Penalty':
            valortotal = (finishing2+shot_power2+penalties2+curve2+composure2)/5
            col6.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Interceptação Rasteira':
            valortotal = (positioning2+reactions2+composure2+interceptions2+ball_control2+vision2+agility2+balance2)/8
            col6.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Interceptação alta':
            valortotal = (positioning2+reactions2+composure2+interceptions2+ball_control2+vision2+agility2+jumping2+balance2)/9
            col6.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Carrinho':
            valortotal = (strength2+aggression2+reactions2+composure2+interceptions2+defensive_awareness2+sliding_tackle2)/7
            col6.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Disputa de bola':
            valortotal = (strength2+aggression2+standing_tackle2+defensive_awareness2+composure2+reactions2+balance2+acceleration2)/8
            col6.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Drible':
            valortotal = (acceleration2+vision2+agility2+balance2+reactions2+ball_control2+dribbling2+composure2+aggression2)/9
            col6.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Colocar á frente':
            valortotal = (acceleration2+sprint_speed2+positioning2+vision2+ball_control2+composure2+stamina2)/7
            col6.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Passe curto':
            valortotal = (vision2+curve2+short_passing2+reactions2+composure2)/5
            col6.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Passe longo':
            valortotal = (vision2+curve2+long_passing2+reactions2+composure2+shot_power2)/6
            col6.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Cruzamento':
            valortotal = (vision2+curve2+crossing2+reactions2+composure2+shot_power2)/6
            col6.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Receber a bola':
            valortotal = (positioning2+balance2+reactions2+ball_control2+composure2)/5
            col6.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Chutar a gol':
            valortotal = (positioning2+finishing2+shot_power2+balance2+ball_control2+composure2+reactions2)/7
            col6.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)

        if acao_ok == 'Chutar a gol - FDA':
            valortotal = (positioning2+finishing2+shot_power2+balance2+ball_control2+composure2+reactions2+long_shots2)/8
            col6.markdown(f'#### **Valor total:** <span style="color: {def_cor(valortotal)};">{valortotal:.0f}</span>', unsafe_allow_html=True)
