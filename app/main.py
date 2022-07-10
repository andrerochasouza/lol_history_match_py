import controllers.summoner_controller as sc
from utils.enums import region
from utils.access_token import get_access_token


token_access = get_access_token() # Token de acesso -> https://developer.riotgames.com/

response = sc.get_summoner_by_name(token_access, region.HTTP_BR1, '///////')
print(response)
