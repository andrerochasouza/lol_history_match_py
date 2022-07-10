from model.champion_mastery import Champion_Mastery
from model.elo import Elo

class Summoner:

    account_id: str
    profile_icon_id: float
    name: str
    id: str
    puu_id: str
    summoner_level: float
    elo: Elo
    champion_mastery: Champion_Mastery
    

    def __init__(self):
        self.account_id = ""
        self.profile_icon_id = 0
        self.name = ""
        self.id = ""
        self.puu_id = ""
        self.summoner_level = 0
        self.elo = Elo()
        self.champion_mastery = Champion_Mastery()
    

    def __str__(self):
        return f"{self.name} - {self.account_id[:5]} - {self.id[:5]} - {self.puu_id[:5]} - {self.summoner_level}"    