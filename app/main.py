from controllers.summoner_lol import Summoner
from utils.enum_region import region
import pathlib as Path


def get_access_token():
    path = Path.Path(Path.Path.home() / "Desktop" / "Python - repositorios" / "token_and_env" / "access_token_riot.txt")
    with open(path, 'r') as file:
        return file.read()


token_access = get_access_token() # Token de acesso -> https://developer.riotgames.com/

summoner = Summoner()
response = summoner.get_response_summoner_by_name(token_access, region.HTTP_BR1, "///////")
print(response)
