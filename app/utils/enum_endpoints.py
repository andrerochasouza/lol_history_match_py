from enum import Enum

class endpoints(Enum):

    SUMMONER_BY_NAME = "/lol/summoner/v4/summoners/by-name/{}"
    ELO_SOMMONER_BY_SUMMONER_ID = "/lol/league/v4/entries/by-summoner/{}"

    # Get all champion mastery entries sorted by number of champion points descending
    CHAMPIONS_MASTERYS_SOMMONER_BY_SOMMONER_ID = "/lol/champion-mastery/v4/scores/by-summoner/{}"
    
    # Returns champion rotations, including free-to-play and low-level free-to-play rotations (REST)
    ROTATION_CHAMPIONS = "/lol/platform/v3/champion-rotations"

    # Get a champion mastery by player ID and champion ID
    CHAMPION_MASTERY_SUMMONER_BY_SUMMONER_ID_AND_CHAMPION_ID = "/lol/champion-mastery/v4/champion-masteries/by-summoner/{}/by-champion/{}"