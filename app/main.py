from app.summoner_lol import Summoner


def get_access_token():
    with open('token_and_env/access_token_riot', 'r') as f:
        access_token = f.read()
    return access_token

token_access = get_access_token() # Token de acesso -> https://developer.riotgames.com/

sommoner = Summoner("dede cereja") # Cria um objeto Summoner com o nickname existente

