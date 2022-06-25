import requests as res
import json
import sys
import os

url_api = "https://br1.api.riotgames.com" # url da api
token_access = "////////////////////" # Token de acesso -> https://developer.riotgames.com/


account_v4 = {
    "summoner_name" : "/lol/summoner/v4/summoners/by-name/",
    "encry_account_id" : "/lol/summoner/v4/summoners/by-account/",
    "encry_summoner_id" : "/lol/summoner/v4/summoners/",
    "me" : "/lol/summoner/v4/summoners/me",
}

def get_account_data(url, token, params = None):

    url = (url_api + url + params) if params else (url_api + url)
    headers = {
        "X-Riot-Token": token
    }
    response = res.get(url, headers=headers)
    print(url)
    print(response.status_code)
    print(response.text)
    return response.json()

get_account_data(account_v4['summoner_name'], token_access, params = "dede cereja")
