from datetime import datetime
import pandas as pd

hoje = datetime.now().strftime("%d/%m/%Y")

df_proximas = pd.read_csv("teste_proximas.csv")
df_ultimas = pd.read_csv("teste_ultimas.csv")
df_player_stats = pd.read_csv("teste_estats_jogador.csv")

history_inicial = [
    {
        "role": "user",
        "parts": [f"Hoje é dia {hoje}. Use essa informação para responder perguntas relacionadas a datas."]
    },
    {
        "role": "user",
        "parts": [f"Usar o arquivo {df_proximas} para responder perguntas a respeito de próximas partidas da FURIA na LTA Sul ou CBLOL, e retorne a que tem a data mais próxima do dia de hoje."]
    },
    {
        "role": "user",
        "parts": [f"Usar o arquivo {df_ultimas} para responder perguntas a respeito de últimas partidas da FURIA na LTA Sul ou CBLOL, e retorne a que tem a data mais próxima do dia de hoje."]
    },
    {
        "role": "user",
        "parts": [f"""Usar o arquivo {df_player_stats} para responder perguntas a respeito das estatisticas individuais ou a perguntas de como foi a partida como kills,mortes,assistencias,campeao,etc de cada jogador da FURIA seja por rota ou nome na LTA Sul ou CBLOL,
                   use tambem o {df_ultimas}, compare as datas dos dois arquivos para responder com precisao a partida caso facam perguntas como exemplo: Qual foi a estatistica de um certo jogador na
                   ultima partida. Use o {df_player_stats} para ver se foi uma partida com mais de 1 partida e retorne falando a respeito de ter sido ou uma melhor de tres , ou uma melhor de cinco
                   e caso for perguntado tambem a respeito de estatisticas individuais dos jogadores retorne as estatitisca das partidas que tiveram no dia. 
                   Sempre antes de responder, se a FURIA ter vencido, diga algo engracado tipo: Esse jogo foi um amasso!!!, Esse jogo foi um passeio!!!,etc. E some as estatisca da partida do time
                   da FURIA em abates e  mortes e compare com o time inimigo.
                   Se voce for perguntado a respeito de como foi a partida retorne de uma forma mais descontraida sobre os resultados e uma forma diver Seu tom deve ser empolgado, amigável e sempre leal
                   à identidade combativa e intensa da FURIA sempre. E use o {df_player_stats} pegue o numeros de kills e mortes de uma partida de cada vez.
                  """""]
    }
]
