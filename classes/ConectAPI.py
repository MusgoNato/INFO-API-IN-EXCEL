import requests

class ConectApi:
    def __init__(self, url):
        self.url = url

    def returnAllCharacteres(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            content = response.json()
            return content
        else:
            print("Nao foi possivel conectar")
