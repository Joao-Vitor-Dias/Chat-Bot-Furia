import requests
from bs4 import BeautifulSoup
import pandas as pd

partidas = []


source = requests.get("https://bo3.gg/pt/lol/teams/furia-esports-lol/matches")

content = source.content

site = BeautifulSoup(content, "html.parser")

ultimas_partidas = site.find_all("div", attrs={"class":"table-row table-row--finished"})

for ultima_partida in ultimas_partidas:
    nomes_times = ultima_partida.find_all("div", attrs={"class" : "team-name"})
    placar = ultima_partida.find("div", attrs={"class": "c-match-score score c-match-score--small"})
    data = ultima_partida.find("span", attrs={"class": "date"})

    partidas.append([nomes_times[0].text,placar.text,nomes_times[1].text, data.text])

lista_ultimas_partidas = pd.DataFrame(partidas,columns=["TIME 1", "PLACAR", "TIME 2", "DATA"])

lista_ultimas_partidas.to_csv("teste_ultiamas.csv", index=False)

