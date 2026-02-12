import requests

def groups_count(token: str) -> int :
    url = "https://graph.microsoft.com/v1.0/me/memberOf"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    count = 0

    while url:
        response = requests.get(url, headers=headers)
        data = response.json()

        values = data.get("value", [])
        count += len(values)

        url = data.get("@odata.nextLink")

    return count