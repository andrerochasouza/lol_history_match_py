from utils.enum_endpoints import endpoints
from utils.enum_region import region
from urllib.parse import quote 
import json
import requests as res

class Summoner:
    account_id = ""
    profile_icon_id = 0
    name = ""
    id = ""
    puu_id = ""
    summoner_level = 0.0

    def __init__(self):
        self.name
        self.account_id
        self.profile_icon_id
        self.id
        self.puu_id
        self.summoner_level
    

    # Get a summoner by summoner name
    def get_response_summoner_by_name(self, token_access, region, name):
        url_format = self.__create_url(region, endpoints.SUMMONER_BY_NAME, quote(name))
        headers = {'X-Riot-Token': token_access}
        response = res.get(url_format, headers=headers)
        return response.json() if self.__validate_status_code(response) == True else self.__validate_status_code(response)

    # Get a summoner's elo ranking
    def get_elo_ranking_summoner(self, token_access, region):
        if self.id == "": return "Não foi possível obter o id do invocador."
        url_format = self.__create_url(region, endpoints.ELO_SOMMONER_BY_SUMMONER_ID, self.id)
        headers = {'X-Riot-Token': token_access}
        response = res.get(url_format, headers=headers)
        return response.json() if self.__validate_status_code(response) == True else self.__validate_status_code(response)

    # Set summoner's account id
    def set_values_account_summoner(self, response):
        self.account_id = response["accountId"]
        self.profile_icon_id = response["profileIconId"]
        self.name = response["name"]
        self.id = response["id"]
        self.puu_id = response["puuid"]
        self.summoner_level = response["summonerLevel"]

    def __str__(self):
        return f"Nome: {self.name} - Level: {self.summoner_level} - Id: {self.id[:7]}... - puuId: {self.puu_id[:7]}..."

    def __validate_status_code(self, response):
        print(response)
        if response.status_code == 200: return True
        elif response.status_code == 429: return "O limite de requisições foi atingido. Tente novamente mais tarde."
        elif response.status_code == 401: return "Token de acesso inválido."
        elif response.status_code == 404: return "Nome de invocador não encontrado."
        elif response.status_code == 500: return "Erro interno do servidor."
        else: return "Erro desconhecido."

    def __create_url(self, endpoint_region, endpoint_type, params_1 = None, params_2 = None, params_3 = None):
        url_format = endpoint_region.value + endpoint_type.value
        if params_1 == None and params_2 == None and params_3 == None:  return url_format
        elif params_1 != None and params_2 == None and params_3 == None: return url_format.format(params_1)
        elif params_1 != None and params_2 != None and params_3 == None: return url_format.format(params_1, params_2)
        elif params_1 != None and params_2 != None and params_3 != None: return url_format.format(params_1, params_2, params_3)
        else: return "Erro ao criar url!"