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
    

    def __str__(self):
        # diminuir a quantidade caracteres
        return f"{self.name} - {self.account_id[:5]} - {self.id[:5]} - {self.puu_id[:5]} - {self.summoner_level}"    


