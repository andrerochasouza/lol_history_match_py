from utils.enum_endpoints import endpoints
from utils.enum_region import region
import urllib.parse as urlparse
import requests as res

class Summoner:
    account_id = ""
    profile_icon_id = 0
    name = ""
    id = ""
    puu_id = ""
    summoner_level = 0.0

    def __init__(self, name):
        self.name = name
        self.account_id
        self.profile_icon_id
        self.id
        self.puu_id
        self.summoner_level
    

    # Get a summoner by summoner name
    def get_summoner_by_name(self, token_access, region):
        url_format = self.__create_url(region, endpoints.SUMMONER_BY_NAME, self.name)
        headers = {'X-Riot-Token': token_access}
        response = res.get(url_format, headers=headers)
        if self.__validate_status_code(response) == True:
            return response.json()
        else:
            return self.__validate_status_code(response)

    # Get a summoner's elo ranking
    def get_elo_ranking_summoner(self, token_access, region):
        url_format = self.__create_url(region, endpoints.ELO_SOMMONER_BY_SUMMONER_ID, self.id)
        headers = {'X-Riot-Token': token_access}
        response = res.get(url_format, headers=headers)
        if self.__validate_status_code(response) == True:
            return response.json()
        else:
            return self.__validate_status_code(response)


    def __str__(self):
        return f"Nome: {self.name} - Level: {self.summoner_level} - Id: {self.id[:5]}... - puuId: {self.puu_id[:5]}..."

    def __validate_status_code(self, response):
        if response.status_code == 200: return True
        elif response.status_code == 429: return "O limite de requisições foi atingido. Tente novamente mais tarde."
        elif response.status_code == 401: return "Token de acesso inválido."
        elif response.status_code == 404: return "Nome de invocador não encontrado."
        elif response.status_code == 500: return "Erro interno do servidor."
        else: return "Erro desconhecido."

    def __create_url(self, endpoint_region, endpoint_type, params_1 = None, params_2 = None, params_3 = None):
        if params_1 == None and params_2 == None and params_3 == None:
            url_format = urlparse.urljoin(endpoint_region.value, endpoint_type.value)
            return url_format
        elif params_1 != None and params_2 == None and params_3 == None:
            url_format = urlparse.urljoin(endpoint_region.value, endpoint_type.value.format(params_1))
            return url_format
        elif params_1 != None and params_2 != None and params_3 == None:
            url_format = urlparse.urljoin(endpoint_region.value, endpoint_type.value.format(params_1, params_2))
            return url_format
        elif params_1 != None and params_2 != None and params_3 != None:
            url_format = urlparse.urljoin(endpoint_region.value, endpoint_type.value.format(params_1, params_2, params_3))
            return url_format
        else:
            return "Erro ao criar url!"

    

