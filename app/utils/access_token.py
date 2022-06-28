import pathlib as Path


def get_access_token():
    path = Path.Path(Path.Path.home() / "Desktop" / "Python - repositorios" / "token_and_env" / "access_token_riot.txt")
    with open(path, 'r') as file:
        return file.read()