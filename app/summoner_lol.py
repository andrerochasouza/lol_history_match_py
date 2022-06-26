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
    
    def historic_rank(self, token_access):
        pass

    def get_summoner_by_name(self, token_access):
        pass

    def get_endpoint_by_json():
        pass

    def __str__(self):
        return f"Nome: {self.name} - Level: {self.summoner_level} - Id: {self.id[:5]}... - puuId: {self.puu_id[:5]}..."

    

