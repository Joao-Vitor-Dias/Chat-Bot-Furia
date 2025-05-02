import requests
import pandas as pd
import json
import os

arquivo = "src\\dados\\base_stats_jogador_cs.json"

url = "https://api.bo3.gg/api/v1/matches/furia-vs-the-mongolz-09-04-2025/players_stats"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    all_data = []
    numero_partida = 0


    for match_stats in data:
        time = match_stats['clan_name']
        if (time == "FURIA"):
            kills = match_stats['kills']
            mortes = match_stats['death']
            assistencias = match_stats['assists']
            time_inimigo = match_stats['enemy_clan_name']
            nome_jogador = match_stats['steam_profile']['nickname']
            

            all_data.append({
                            "PARTIDA": numero_partida,
                            "TIME":time,
                            "NOME JOGADOR": nome_jogador,
                            "KILLS":kills,
                            "MORTES":mortes,
                            "ASSISTENCIAS":assistencias,
                            "TIME INIMIGO":time_inimigo
                            })

    df_stats_jogadores = pd.DataFrame(all_data)

if not os.path.exists(arquivo):
    # Se o arquivo não existir, cria com o DataFrame diretamente
    df_stats_jogadores.to_json(arquivo, orient="records", indent=4, force_ascii=False, index=False)
else:
    with open("src\\dados\\base_stats_jogador_cs.json", "r+", encoding="utf-8") as f:
        dados = json.load(f)
        dados.extend(df_stats_jogadores.to_dict(orient="records"))
        f.seek(0)
        json.dump(dados, f, indent=4, ensure_ascii=False)
