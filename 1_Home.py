import pandas as pd
import streamlit as st
import requests

st.set_page_config(
    page_title='Home',
    layout='wide'
)


#if "data" not in st.session_state:

    #df = pd.read_csv('https://raw.githubusercontent.com/DartagnanFreire/UT_supertrunfo/main/arquivos%20csv/ultimateteam.csv', sep='\t', encoding='utf-8')
    #st.session_state["data"] = df
    

st.markdown("# Ultimate Team Card Game! ⚽️")

st.markdown('''   
            Esse projeto foi desenvolvido para treinar funcionalidades da ferramenta Streamlit, além de melhorar minhas skills em webscrapping,   
            lógica, tratamento de dados e algumas coisas de css.   
            
            Na página Players, você pode conferir todas as cartas presentes no ultimate team, de overall 75 acima, com suas versões, fotos, status e muito mais   
            Ela foi montada a partir de uma tabela, e essa tabela foi gerada a partir de webscrapping, utilizando beautifulsoup 4   
               
            A página Super, eu criei um "jogo" estilo super trunfo, onde duas cartas são selecionadas randomicamente e comparadas para se obter o vencedor.
            Você pode escolher entre 3 "tipos" de comparação: Status Individuais, Status Agregados, e por Ação.

            Status individuais, o nome já diz, e ele seleciona um dos status e compara.
            Status agrupados, como o nome diz, agrupa os status individuais em grandes grupos, e elabora uma média. Perceba que a média NÃO reflete a carta, 
            já que a carta leva em conta fatores desconhecidos por nós, humanos.

            Em ações, eu criei, diretamente do artigo "vozes da minha cabeça", ações possíveis em campo, elaborei quais status individuais poderiam interferir
            nessas ações, e fiz uma média, assim como nos status agrupados. Em breve colocarei em uma página a parte, quais são os critérios que utilizei.
            Mas para exemplo: a ação "Chute a Gol sem domínio - FDA (Fora da área)" eu utilizei Posicionamento, Finalização, Força do Chute, Chute de Longe, Voleio,
            Equilibrio, Reação e Frieza, divididos por 8. Assim, a carta do Halland Team of The Week versão 1, possui 80 de total para essa ação.
            ''')

#df = st.session_state["data"]
df = pd.read_csv('https://raw.githubusercontent.com/DartagnanFreire/UT_supertrunfo/main/arquivos%20csv/ultimateteam.csv', sep='\t', encoding='utf-8')
df
