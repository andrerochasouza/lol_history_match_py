from enum import Enum

class endpoints(Enum):
    """
    Endpoints para requisições.
    """

    SUMMONER_BY_NAME = "/lol/summoner/v4/summoners/by-name/"
    ELO_SOMMONER_BY_SUMMONER_ID = "/lol/league/v4/entries/by-summoner/"
    CHAMPIONS_BY_SUMMONER_ID = "/lol/champion-mastery/v4/champion-masteries/by-summoner/"

class region(Enum):
    """
    URLs de regiões para requisições.
    """
    
    HTTP_BR1 = "https://br1.api.riotgames.com"
    HTTP_EUNE = "https://eune.api.riotgames.com"
    HTTP_EUW = "https://euw.api.riotgames.com"
    HTTP_JP1 = "https://jp1.api.riotgames.com"
    HTTP_KR = "https://kr.api.riotgames.com"
    HTTP_LA1 = "https://la1.api.riotgames.com"
    HTTP_LA2 = "https://la2.api.riotgames.com"
    HTTP_NA = "https://na.api.riotgames.com"
    HTTP_OCE = "https://oce.api.riotgames.com"
    HTTP_TR1 = "https://tr1.api.riotgames.com"
    HTTP_RU = "https://ru.api.riotgames.com"
    HTTP_PBE = "https://pbe.api.riotgames.com"
    HTTP_GLOBAL = "https://global.api.riotgames.com"