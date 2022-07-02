from utils.enums import endpoints
from urllib.parse import quote
import requests as res


def get_summoner_by_name(token_access, region, name):
    url_format = __create_url(region, endpoints.SUMMONER_BY_NAME, quote(name))
    return __get_response_by_token_url(token_access, url_format)


def get_elo_by_id(token_access, region, summoner_id):
    url_format = __create_url(region, endpoints.ELO_SOMMONER_BY_SUMMONER_ID, summoner_id)
    return __get_response_by_token_url(token_access, url_format)

def get_list_champion_by_id(token_access, region, summoner_id):
    url_format = __create_url(region, endpoints.CHAMPIONS_BY_SUMMONER_ID, summoner_id)
    return __get_response_by_token_url(token_access, url_format)


def __validate_status_code(response):
    if response.status_code == 400: return "Erro de requisição"
    elif response.status_code == 401: return "Token de acesso inválido."
    elif response.status_code == 403: return "Servidor não foi capaz de processar a requisição pela URL especificada."
    elif response.status_code == 404: return "Nome de invocador não encontrado."
    elif response.status_code == 429: return "O limite de requisições foi atingido. Tente novamente mais tarde."
    elif response.status_code == 500: return "Erro interno do servidor."
    else: return "Erro desconhecido."


def __create_url(endpoint_region, endpoint_type, params_1 = None, params_2 = None, params_3 = None):
    url_format = endpoint_region.value + endpoint_type.value
    if params_1 == None and params_2 == None and params_3 == None:  return url_format
    elif params_1 != None and params_2 == None and params_3 == None: return url_format.format(params_1)
    elif params_1 != None and params_2 != None and params_3 == None: return url_format.format(params_1, params_2)
    elif params_1 != None and params_2 != None and params_3 != None: return url_format.format(params_1, params_2, params_3)
    else: return "Erro ao criar url!"


def __get_response_by_token_url(token, url):
    headers = {'X-Riot-Token': token}
    response = res.get(url, headers=headers)
    print('Status code -- ', response.status_code)
    return response.json() if response.status_code == 200 else __validate_status_code(response)