import requests as res

class Summoner:
    account_id = ""
    profile_icon_id = 0
    name = ""
    id = ""
    puu_id = ""
    summoner_level = 0.0

    def __init__(self, name, token):

        summoner = Summoner.get_summoner_by_name(name, token)

        if type(summoner) == dict:
            self.account_id = summoner["accountId"]
            self.profile_icon_id = summoner["profileIconId"]
            self.name = summoner["name"]
            self.id = summoner["id"]
            self.puu_id = summoner["puuid"]
            self.summoner_level = summoner["summonerLevel"]
        else:
            self.name = name
            self.id = ""
            self.puu_id = ""
            self.summoner_level = 0.0
            self.account_id = ""
            self.profile_icon_id = 0
    
    
    def get_summoner_by_name(name, token):
        url = "https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
        headers = {
            "X-Riot-Token": token
        }
        response = res.get(url + name, headers=headers)

        if response.status_code == 200:
            print("Envocador encontrado!")
            return response.json()
        elif response.status_code == 429:
            print("Excedido o limite de requisições")
            return None
        else:
            print("Envocador não encontrado, Status code: ", response.status_code)
            return None

    
    def __str__(self):
        return f"Nome: {self.name} - Level: {self.summoner_level} - Id: {self.id[:5]}... - puuId: {self.puu_id[:5]}..."