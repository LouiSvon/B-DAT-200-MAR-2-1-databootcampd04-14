import requests

def my_mail(token: str) -> str:
    url = "https://graph.microsoft.com/v1.0/me"

    headers = {
        "Authorization": f"Bearer {token}",
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    return data.get("mail")