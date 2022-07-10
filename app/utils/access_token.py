import pathlib as Path


def get_access_token():
    """
    Retorna o token de acesso.

    Precisa especificar o diretorio do arquivo de token de acesso.

    :return: Token de acesso.
    """

    path = Path.Path(Path.Path.home() / "Desktop" / "py_app" / "access_token_riot.txt").absolute()
    with open(path, 'r') as file:
        return file.read()