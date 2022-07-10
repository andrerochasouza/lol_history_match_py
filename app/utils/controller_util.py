import enum
import requests as res

# Methods to Controllers -------------------------------------------------------------------------------

def get_response_by_token_url(token: str, url: str):
    """
    Retorna um objeto de uma requisição HTTP pelo token de acesso e url.

    :param token: Token de acesso.
    :param url: Url da requisição.
    :return: Objeto de resposta.
    """

    headers = {'X-Riot-Token': token}
    response = res.get(url, headers=headers)
    print('Status code -- ', response.status_code)
    return response.json() if response.status_code == 200 else validate_status_code(response)



def create_url(endpoint_region: enum, endpoint_type: enum, *args):
    """
    Retorna uma url formatada para a requisição.

    :param endpoint_region: Endpoint da região.
    :param endpoint_type: Endpoint do tipo.
    :param args: Argumentos para o endpoint.
    :return: Url formatada.
    """

    url_format = endpoint_region.value + endpoint_type.value
    for arg in args:
        url_format += "/" + arg if url_format[-1] != "/" else arg

    return url_format if url_format[-1] == "/" else url_format + "/"



def validate_status_code(response: res.Response):
    """
    Retorna um erro caso o status code da requisição seja diferente de 200.
    
    :param response: Objeto de resposta.
    :return: Erro.
    """

    if response.status_code == 400: raise Exception("Erro de requisição")
    elif response.status_code == 401: raise Exception("Token de acesso inválido.")
    elif response.status_code == 403: raise Exception("Servidor não foi capaz de processar a requisição pela URL especificada.")
    elif response.status_code == 404: raise Exception("Nome de invocador não encontrado.")
    elif response.status_code == 429: raise Exception("O limite de requisições foi atingido. Tente novamente mais tarde.")
    elif response.status_code == 500: raise Exception("Erro interno do servidor.")
    else: raise Exception("Erro desconhecido.")