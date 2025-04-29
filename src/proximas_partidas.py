import requests
from bs4 import BeautifulSoup
import pandas as pd

partidas = []


source = requests.get("https://bo3.gg/pt/lol/teams/furia-esports-lol/matches")

content = source.content

site = BeautifulSoup(content, "html.parser")

proximas_partidas = site.find_all("div", attrs={"class":"table-row table-row--upcoming"})

for proxima_partida in proximas_partidas:
    nomes_time = proxima_partida.find_all("div", attrs ={"class" : "team-name"})
    data_jogo = proxima_partida.find("span", attrs = {"class" : "date"})
    partidas.append([nomes_time[0].text, nomes_time[1].text ,data_jogo.text])

lista_proximas_partidas = pd.DataFrame(partidas, columns= ["TIME DA FURIA", "TIME ADVERSARIO","DATA"])  

lista_proximas_partidas.to_csv("teste_proximas.csv", index=False)

print(lista_proximas_partidas)