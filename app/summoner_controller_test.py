import controllers.summoner_controller as sc
from utils.enums import region
from utils.access_token import get_access_token


token_access = get_access_token()
region_type = region.HTTP_BR1

name = '////////////'
summoner_id = '/////////'

def test_request_get_summoner_by_name():
    response = sc.get_summoner_by_name(token_access, region_type, name)
    assert response['name'] == name
    
def test_request_get_elo_by_id():
    response = sc.get_elo_by_id(token_access, region_type, summoner_id)
    assert response[0]['summonerId'] == summoner_id
