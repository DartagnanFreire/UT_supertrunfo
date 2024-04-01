import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='Jogadores',
    layout='wide'
)

#df = st.session_state["data"]
df = pd.read_csv('https://raw.githubusercontent.com/DartagnanFreire/UT_supertrunfo/main/arquivos%20csv/ultimateteam.csv', sep='\t', encoding='utf-8')

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

velo = (player_stats['Acceleration'] + player_stats['Sprint Speed'])/2
chute = (player_stats['Positioning'] + player_stats['Finishing'] + player_stats['Shot Power'] + player_stats['Long Shot'] + player_stats['Volleys'] + player_stats['Penalties'])/6
passe = (player_stats['Vision'] + player_stats['Crossing'] + player_stats['Free Kick'] + player_stats['Shot Passing'] + player_stats['Long Passing'] + player_stats['Curve'])/6
drible = (player_stats['Agility'] + player_stats['Balance'] + player_stats['Reactions'] + player_stats['Ball Control'] + player_stats['Dribbling'] + player_stats['Composure'])/6
defesa = (player_stats['Interceptions'] + player_stats['Heading'] + player_stats['Def. Awareness'] + player_stats['Standing Tackle'] + player_stats['Sliding'])/5
fisico = (player_stats['Jumping'] + player_stats['Stamina'] + player_stats['Strength'] + player_stats['Aggression'])/4
overall = (velo + chute + passe + drible + defesa + fisico)/6
overallgk = (velo + player_stats['Diving'] + player_stats['Kicking'] + player_stats['Handling'] + player_stats['Positioning'] + (player_stats['Reflexes'] + player_stats['Reactions']))/6

col1, col2, col3 = st.columns(3)

with col1:
    container = st.container()
    container.title(player_stats['Nome Completo'])
    container.image(player_stats['Foto'], width = 270)

with col2:
    with st.container():
        st.empty()
    with st.container():        
        col11, col12 = st.columns([1, 5])
        col11.image(player_stats['País'], width = 80)
        try:
            col12.image(player_stats['Time'], width = 50)
        except Exception as e:
            col12.image('https://game-assets.fut.gg/2024/leagues/2118.png?quality=100&width=80', width = 50)

        st.markdown(f"**Posição**: {player_stats['Posição']}")
        st.markdown(f"**Posições Alternativas**: {player_stats['Posição Alternativa 1']}/{player_stats['Posição Alternativa 2']}/{player_stats['Posição Alternativa 3']}")
        st.markdown(f"**Tipo de carta:** {player_stats['Tipo']}")
        st.title(f"Overall Carta: {player_stats['Overall']}")


with col3:
    with st.container():
        st.empty()

col1, col2, col3, col4, col5, col6 = st.columns(6)

if player_stats['Posição'] == 'GK':
    col1.markdown(f'#### **Velocidade** <span style="color: {def_cor(velo)};">{velo:.0f}</span>', unsafe_allow_html=True)
    col1.markdown(f'**Aceleração** <span style="color: {def_cor(player_stats["Acceleration"])};">{player_stats["Acceleration"]}</span>', unsafe_allow_html=True)
    col1.markdown(f'**Sprint Speed** <span style="color: {def_cor(player_stats["Sprint Speed"])};">{player_stats["Sprint Speed"]}</span>', unsafe_allow_html=True)

    col2.markdown(f'#### **Ponte** <span style="color: {def_cor(player_stats["Diving"])};">{player_stats["Diving"]}</span>', unsafe_allow_html=True)
    col2.markdown(f'**Ponte** <span style="color: {def_cor(player_stats["Diving"])};">{player_stats["Diving"]}</span>', unsafe_allow_html=True)

    col3.markdown(f'#### **Chute** <span style="color: {def_cor(player_stats["Kicking"])};">{player_stats["Kicking"]}</span>', unsafe_allow_html=True)
    col3.markdown(f'**Chute** <span style="color: {def_cor(player_stats["Kicking"])};">{player_stats["Kicking"]}</span>', unsafe_allow_html=True)

    col4.markdown(f'#### **Jogo de mãos** <span style="color: {def_cor(player_stats["Handling"])};">{player_stats["Handling"]}</span>', unsafe_allow_html=True)
    col4.markdown(f'**Jogo de mãos** <span style="color: {def_cor(player_stats["Handling"])};">{player_stats["Handling"]}</span>', unsafe_allow_html=True)

    col5.markdown(f'#### **Posicionamento** <span style="color: {def_cor(player_stats["Positioning GK"])};">{player_stats["Positioning GK"]:.0f}</span>', unsafe_allow_html=True)
    col5.markdown(f'**Posicionamento** <span style="color: {def_cor(player_stats["Positioning GK"])};">{player_stats["Positioning GK"]:.0f}</span>', unsafe_allow_html=True)

    reflex = (player_stats["Reflexes"] + player_stats["Reactions"])/2
    col6.markdown(f'#### **Reflexos** <span style="color: {def_cor(reflex)};">{reflex:.0f}</span>', unsafe_allow_html=True)
    col6.markdown(f'**Reflexos** <span style="color: {def_cor(player_stats["Reflexes"])};">{player_stats["Reflexes"]}</span>', unsafe_allow_html=True)
    col6.markdown(f'**Reação** <span style="color: {def_cor(player_stats["Reactions"])};">{player_stats["Reactions"]}</span>', unsafe_allow_html=True)

else:
    col1.markdown(f'#### **Velocidade** <span style="color: {def_cor(velo)};">{velo:.0f}</span>', unsafe_allow_html=True)
    col1.markdown(f'**Aceleração** <span style="color: {def_cor(player_stats["Acceleration"])};">{player_stats["Acceleration"]}</span>', unsafe_allow_html=True)
    col1.markdown(f'**Sprint Speed** <span style="color: {def_cor(player_stats["Sprint Speed"])};">{player_stats["Sprint Speed"]}</span>', unsafe_allow_html=True)

    col2.markdown(f'#### **Chute** <span style="color: {def_cor(chute)};">{chute:.0f}</span>', unsafe_allow_html=True)
    col2.markdown(f'**Posicionamento** <span style="color: {def_cor(player_stats["Positioning"])};">{player_stats["Positioning"]}</span>', unsafe_allow_html=True)
    col2.markdown(f'**Finalização** <span style="color: {def_cor(player_stats["Finishing"])};">{player_stats["Finishing"]}</span>', unsafe_allow_html=True)
    col2.markdown(f'**Força do Chute** <span style="color: {def_cor(player_stats["Shot Power"])};">{player_stats["Shot Power"]}</span>', unsafe_allow_html=True)
    col2.markdown(f'**Chute de Longe** <span style="color: {def_cor(player_stats["Long Shot"])};">{player_stats["Long Shot"]}</span>', unsafe_allow_html=True)
    col2.markdown(f'**Voleios** <span style="color: {def_cor(player_stats["Volleys"])};">{player_stats["Volleys"]}</span>', unsafe_allow_html=True)
    col2.markdown(f'**Penaltis** <span style="color: {def_cor(player_stats["Penalties"])};">{player_stats["Penalties"]}</span>', unsafe_allow_html=True)

    col3.markdown(f'#### **Passe** <span style="color: {def_cor(passe)};">{passe:.0f}</span>', unsafe_allow_html=True)
    col3.markdown(f'**Visão** <span style="color: {def_cor(player_stats["Vision"])};">{player_stats["Vision"]}</span>', unsafe_allow_html=True)
    col3.markdown(f'**Cruzamento** <span style="color: {def_cor(player_stats["Crossing"])};">{player_stats["Crossing"]}</span>', unsafe_allow_html=True)
    col3.markdown(f'**Faltas** <span style="color: {def_cor(player_stats["Free Kick"])};">{player_stats["Free Kick"]}</span>', unsafe_allow_html=True)
    col3.markdown(f'**Passe Curto** <span style="color: {def_cor(player_stats["Shot Passing"])};">{player_stats["Shot Passing"]}</span>', unsafe_allow_html=True)
    col3.markdown(f'**Passe Longo** <span style="color: {def_cor(player_stats["Long Passing"])};">{player_stats["Long Passing"]}</span>', unsafe_allow_html=True)
    col3.markdown(f'**Curva** <span style="color: {def_cor(player_stats["Curve"])};">{player_stats["Curve"]}</span>', unsafe_allow_html=True)

    col4.markdown(f'#### **Drible** <span style="color: {def_cor(drible)};">{drible:.0f}</span>', unsafe_allow_html=True)
    col4.markdown(f'**Agilidade** <span style="color: {def_cor(player_stats["Agility"])};">{player_stats["Agility"]}</span>', unsafe_allow_html=True)
    col4.markdown(f'**Balanço** <span style="color: {def_cor(player_stats["Balance"])};">{player_stats["Balance"]}</span>', unsafe_allow_html=True)
    col4.markdown(f'**Reação** <span style="color: {def_cor(player_stats["Reactions"])};">{player_stats["Reactions"]}</span>', unsafe_allow_html=True)
    col4.markdown(f'**Controle de Bola** <span style="color: {def_cor(player_stats["Ball Control"])};">{player_stats["Ball Control"]}</span>', unsafe_allow_html=True)
    col4.markdown(f'**Drible** <span style="color: {def_cor(player_stats["Dribbling"])};">{player_stats["Dribbling"]}</span>', unsafe_allow_html=True)
    col4.markdown(f'**Frieza** <span style="color: {def_cor(player_stats["Composure"])};">{player_stats["Composure"]}</span>', unsafe_allow_html=True)

    col5.markdown(f'#### **Defesa** <span style="color: {def_cor(defesa)};">{defesa:.0f}</span>', unsafe_allow_html=True)
    col5.markdown(f'**Interceptação** <span style="color: {def_cor(player_stats["Interceptions"])};">{player_stats["Interceptions"]}</span>', unsafe_allow_html=True)
    col5.markdown(f'**Cabeceio** <span style="color: {def_cor(player_stats["Heading"])};">{player_stats["Heading"]}</span>', unsafe_allow_html=True)
    col5.markdown(f'**Def. Awareness** <span style="color: {def_cor(player_stats["Def. Awareness"])};">{player_stats["Def. Awareness"]}</span>', unsafe_allow_html=True)
    col5.markdown(f'**Bloqueio** <span style="color: {def_cor(player_stats["Standing Tackle"])};">{player_stats["Standing Tackle"]}</span>', unsafe_allow_html=True)
    col5.markdown(f'**Carrinho** <span style="color: {def_cor(player_stats["Sliding"])};">{player_stats["Sliding"]}</span>', unsafe_allow_html=True)

    col6.markdown(f'#### **Físico** <span style="color: {def_cor(fisico)};">{fisico:.0f}</span>', unsafe_allow_html=True)
    col6.markdown(f'**Pulo** <span style="color: {def_cor(player_stats["Jumping"])};">{player_stats["Jumping"]}</span>', unsafe_allow_html=True)
    col6.markdown(f'**Estamina** <span style="color: {def_cor(player_stats["Stamina"])};">{player_stats["Stamina"]}</span>', unsafe_allow_html=True)
    col6.markdown(f'**Força** <span style="color: {def_cor(player_stats["Strength"])};">{player_stats["Strength"]}</span>', unsafe_allow_html=True)
    col6.markdown(f'**Agressão** <span style="color: {def_cor(player_stats["Aggression"])};">{player_stats["Aggression"]}</span>', unsafe_allow_html=True)
