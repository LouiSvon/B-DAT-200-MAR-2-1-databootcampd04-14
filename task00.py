import requests

def test_connection(token: str) -> int: #fonction et je veux une str
    url = "https://graph.microsoft.com/v1.0/me" 

    headers = {
        "Authorization": f"Bearer {token}", #bearer == authentifaction pour pas avoir d'erreur
    }

    response = requests.get(url, headers=headers) #j'envoi une requete http pour attendre une réponse

    return response.status_code