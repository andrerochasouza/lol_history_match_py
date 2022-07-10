from utils.enums import endpoints
from urllib.parse import quote
import utils.controller_util as cu
import enum

def get_summoner_by_name(token_access: str, region: enum, name: str):
    """
    Retorna um objeto Summoner pelo nome do invocador.

    :param token_access: Token de acesso.
    :param region: Região.
    :param name: Nome do invocador.
    :return: Objeto Summoner.
    """

    url_format = cu.create_url(region, endpoints.SUMMONER_BY_NAME, quote(name))
    return cu.get_response_by_token_url(token_access, url_format)



def get_elo_by_id(token_access: str, region: enum, summoner_id: str):
    """
    Retorna um objeto Elo pelo id do invocador.

    :param token_access: Token de acesso.
    :param region: Região.
    :param summoner_id: Id do invocador.
    :return: Objeto Elo.
    """

    url_format = cu.create_url(region, endpoints.ELO_SOMMONER_BY_SUMMONER_ID, summoner_id)
    return cu.get_response_by_token_url(token_access, url_format)



def get_list_champion_by_id(token_access: str, region: enum, summoner_id: str):
    """
    Retorna uma lista de objetos Champion pelo id do invocador.

    :param token_access: Token de acesso.
    :param region: Região.
    :param summoner_id: Id do invocador.
    :return: Objeto Lista de Champion.
    """

    url_format = cu.create_url(region, endpoints.CHAMPIONS_BY_SUMMONER_ID, summoner_id)
    return cu.get_response_by_token_url(token_access, url_format)