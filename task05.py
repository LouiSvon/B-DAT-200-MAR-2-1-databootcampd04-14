import requests

def team_channels(token: str, team_id: str) -> list:
    url = f"https://graph.microsoft.com/v1.0/teams/{team_id}/channels"

    headers = {
        "Authorization": f"Bearer {token}",
    }

    result = []

    while url:
        response = requests.get(url, headers=headers)
        data = response.json()

        for channel in data.get("value", []):
            channel_id = channel.get("id")
            if channel_id is not None:
                result.append(channel_id)

        url = data.get("@odata.nextLink")

    return result