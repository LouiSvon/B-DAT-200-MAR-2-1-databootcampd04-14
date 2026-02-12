import requests

def my_mail(token: str) -> str:
    url = "https://graph.microsoft.com/v1.0/me"

    params = {
        "$select": "mail,userPrincipalName"
    }

    headers = {
        "Authorization": f"Bearer {token}",
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    mail = data.get("mail")
    upn = data.get("userPrincipalName")

    if mail:
        return mail

    return upn