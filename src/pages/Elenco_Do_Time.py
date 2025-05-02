import streamlit as st

st.set_page_config(
    page_title="Elenco da FURIA",
    page_icon="https://api.draft5.gg/teams/330/logo",
 )

st.title("ELENCO DO TIME")


# Menu de seleção
opcao = st.radio("Escolha uma esporte", ["LTA SUL", "CS:GO"])

time_lol = [
    {"nome": "Guigo", "rota": "TOP", "imagem_url": "https://am-a.akamaihd.net/image?resize=375:&f=http%3A%2F%2Fstatic.lolesports.com%2Fplayers%2F1737719411230_image67.png"},  
    {"nome": "Tatu", "rota": "JUNGLE", "imagem_url": "https://am-a.akamaihd.net/image?resize=375:&f=http%3A%2F%2Fstatic.lolesports.com%2Fplayers%2F1737720151865_image69.png"},
    {"nome": "Tutsz", "rota": "MID", "imagem_url": "https://am-a.akamaihd.net/image?resize=375:&f=http%3A%2F%2Fstatic.lolesports.com%2Fplayers%2F1737720319734_image610.png"},
    {"nome": "Ayu", "rota": "ADC", "imagem_url": "https://am-a.akamaihd.net/image?resize=375:&f=http%3A%2F%2Fstatic.lolesports.com%2Fplayers%2F1737718665203_image65.png"},
    {"nome": "Jojo", "rota": "SUP", "imagem_url": "https://am-a.akamaihd.net/image?resize=375:&f=http%3A%2F%2Fstatic.lolesports.com%2Fplayers%2F1737719808158_image68.png"},
    ]

time_cs = [
    {"nome": "Fallen","imagem_url": "https://profilerr.net/static/content/thumbs/300x320/c/55/wntvkz-2bfc3455d0b32854a3b0f446ca9f555c.png"},  
    {"nome": "Chelo", "imagem_url": "https://profilerr.net/static/content/thumbs/300x320/e/cd/unwz7w-a415cf230c089376816be57459c3fcde.png"},
    {"nome": "Yuurih", "imagem_url": "https://profilerr.net/static/content/thumbs/300x320/5/60/uahjnx-e54da6dd34064e9fb1b1b465dff83605.png"},
    {"nome": "Skullz", "imagem_url": "https://profilerr.net/static/content/thumbs/300x320/e/58/u4x3h6-ff1f9da73136f54ba8bbb1c2664a558e.png"},
    {"nome": "Kscerato", "imagem_url": "https://profilerr.net/static/content/thumbs/300x320/c/a0/3q6pkn-c56a5c764944aa2c4eb95b3bde795a0c.png"},
    ]

# Conteúdo dinâmico
if opcao == "LTA SUL": 
    for membro in time_lol:
        st.subheader(membro["nome"])
        st.image(membro["imagem_url"], caption=membro["rota"], width=200)  # Ajuste o tamanho da imagem
        st.write("---")  # Separador

elif opcao == "CS:GO":
     for membro in time_cs:
        st.subheader(membro["nome"])
        st.image(membro["imagem_url"], width=150)  # Ajuste o tamanho da imagem
        st.write("---") 

with st.sidebar:
    
    st.subheader(" Acesse a nossa loja oficial: ")
    "[Furia.gg](https://www.furia.gg/)"

    st.subheader(" Siga a gente em nossas redes para não perder nada: ")
    "[Instagram.com](https://www.instagram.com/furiagg/)"
    "[Twitter.com](https://x.com/FURIA)"