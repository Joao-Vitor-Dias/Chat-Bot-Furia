import requests
import pandas as pd
import json
import os

arquivo = "base_stats_jogador.json"

url = "https://api.bo3.gg/api/v1/lol/stats/matches/85444/players_stats"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    all_data = []
    numero_partida = 0


    for match_stats in data:
        dia = match_stats['begin_at']
        numero_partida = match_stats['game_number']
        vitoria_codigo = match_stats['winner_team_id']
        if (vitoria_codigo == 17448):
            resultado = "FURIA VENCEU"
        else:
            resultado = "FURIA PERDEU"    

        for player in match_stats['lol_game_players']:
            time = player.get('team_id')
            if(time == 	17448):
                time = "FURIA"
                rota = player.get('role')
                
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

                time = player.get('team_id')                        
                kills = player.get('kills') 
                mortes = player.get('deaths')
                assistencias = player.get('assists') 
                campeao = player['lol_champion']['name']

                all_data.append({"DATA":dia,
                                "PARTIDA": numero_partida,
                                "RESULTADO DA PARTIDA": resultado,
                                "TIME":time,
                                "NOME JOGADOR": nome_jogador ,
                                "ROTA":rota,
                                "CAMPEAO":campeao,
                                "KILLS":kills,
                                "MORTES":mortes,
                                "ASSISTENCIAS":assistencias
                                })

    df_stats_jogadores = pd.DataFrame(all_data)

if not os.path.exists(arquivo):
    # Se o arquivo não existir, cria com o DataFrame diretamente
    df_stats_jogadores.to_json(arquivo, orient="records", indent=4, force_ascii=False, index=False)
else:
    with open("base_stats_jogador.json", "r+", encoding="utf-8") as f:
        dados = json.load(f)
        dados.extend(df_stats_jogadores.to_dict(orient="records"))
        f.seek(0)
        json.dump(dados, f, indent=4, ensure_ascii=False)
