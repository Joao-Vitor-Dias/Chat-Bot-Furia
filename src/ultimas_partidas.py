import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta


partidas = []

source = requests.get("https://bo3.gg/pt/lol/teams/furia-esports-lol/matches")

content = source.content

site = BeautifulSoup(content, "html.parser")

meses_ua = {
    "січ": "01",
    "лют": "02",
    "бер": "03",
    "кві": "04",
    "тра": "05",
    "чер": "06",
    "лип": "07",
    "сер": "08",
    "вер": "09",
    "жов": "10",
    "лис": "11",
    "гру": "12"
}

def converter_data_ua(data_str):
    try:
        # Separar hora e o resto
        hora_minuto = data_str[:5]
        mes_dia = data_str[5:].strip().split()

        if len(mes_dia) != 2:
            return data_str  # formato inesperado

        mes_abrev = mes_dia[0]
        dia = mes_dia[1]
        mes = meses_ua.get(mes_abrev.lower(), "01")

        ano_atual = datetime.now().year
        dt = datetime.strptime(f"{dia}/{mes}/{ano_atual} {hora_minuto}", "%d/%m/%Y %H:%M")

        # Ajuste do fuso horário UTC+3 → UTC−3
        dt_corrigido = dt - timedelta(hours=3)

        return dt_corrigido.strftime("%d/%m/%Y %H:%M")

    except Exception as e:
        return data_str

ultimas_partidas = site.find_all("div", attrs={"class":"table-row table-row--finished"})

for ultima_partida in ultimas_partidas:
    nomes_times = ultima_partida.find_all("div", attrs={"class" : "team-name"})
    placar = ultima_partida.find("div", attrs={"class": "c-match-score score c-match-score--small"})
    data = ultima_partida.find("span", attrs={"class": "date"})
    torneio = ultima_partida.find("p", attrs={"class": "tournament-name"})

    data_formatada = converter_data_ua(data.text)

    partidas.append([nomes_times[0].text,placar.text,nomes_times[1].text, data_formatada,torneio.text])

lista_ultimas_partidas = pd.DataFrame(partidas,columns=["TIME 1", "PLACAR", "TIME 2", "DATA","TORNEIO"])


# O codigo abaixo vai criar um arquivo CSV com as informacoes extraidas do site sobre as ultimas partidas
#lista_ultimas_partidas.to_csv("teste_ultiamas.csv", index=False) 

# O codigo abaixo vai exibir no terminal as informacoes das ultimas partidas
print(lista_ultimas_partidas)