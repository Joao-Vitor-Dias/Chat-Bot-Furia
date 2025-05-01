import requests
import pandas as pd

url = "https://api.bo3.gg/api/v1/lol/stats/matches/85448/players_stats"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    all_data = []
    numero_partida = 0


    for match_stats in data:
        dia = match_stats['begin_at']
        numero_partida = match_stats['game_number']

        for player in match_stats['lol_game_players']:
            rota = player.get('role')
            time = player.get('team_id')
            if(time == 	17448):
                time = "FURIA"
                match rota:
                    case "top":
                        nome_jogador = "Guigo"
                    case "jun":
                        nome_jogador = "Tatu"
                    case "mid":
                        nome_jogador = "Tutz"
                    case "adc":
                        nome_jogador = "Ayu"
                    case "sup":
                        nome_jogador = "Jojo"           
            else:
                nome_jogador = "Outro time"
                time = "OUTRO TIME"
            kills = player.get('kills') 
            mortes = player.get('deaths')
            assistencias = player.get('assists') 
            campeao = player['lol_champion']['name']

            all_data.append({"DATA":dia,
                             "PARTIDA": numero_partida,
                             "TIME":time,
                             "NOME JOGADOR": nome_jogador ,
                             "ROTA":rota,
                             "CAMPEAO":campeao,
                             "KILLS":kills,
                             "MORTES":mortes,
                             "ASSISTENCIAS":assistencias
                             })

    df_stats_jogadores = pd.DataFrame(all_data)

df_stats_jogadores.to_csv("teste_estats_jogador.csv", index=False, mode="a")
