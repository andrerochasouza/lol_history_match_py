import controllers.summoner_controller as sc
from model.summoner import Summoner 
from utils.enum_region import region
from utils.access_token import get_access_token as get_token


token_access = get_token() # Token de acesso -> https://developer.riotgames.com/

summoner = Summoner()

response = sc.get_summoner_by_name(token_access, region.HTTP_BR1, '////////')
print(response)