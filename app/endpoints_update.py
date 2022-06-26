import requests as res
from bs4 import BeautifulSoup as bs
from pathlib import Path
import time
import json


def get_list_api():
    url = 'https://developer.riotgames.com/apis'
    response = res.get(url)
    soup = bs(response.text, 'html.parser')
    div_api = soup.find_all('div', {'class': 'api_detail inner_content'})
    list_api_dev = []
    for i in div_api:
        list_api_dev.append(i['api-name'])
    return list_api_dev


def get_endpoints_to_api(name_dev_api):
    url = 'https://developer.riotgames.com/api-details/' + name_dev_api
    response = res.get(url)
    soup = bs(response.text, 'html.parser')
    span_url = soup.find_all('span', {'class': r'\"path\"'})
    list_endpoints = []
    for i in span_url:
        list_endpoints.append(i.text.strip().replace(r'\n', '').replace(' ', ''))
    return list_endpoints


def create_or_update_json_endpoints():
    list_api = get_list_api()
    for i in list_api:
        list_endpoints = get_endpoints_to_api(i)
        if len(list_endpoints) > 0:
            fpath = Path('endpoints').absolute()
            with open(fpath / (i + '.json'), 'w') as f:
                json.dump(list_endpoints, f)
        time.sleep(1)
        
create_or_update_json_endpoints()