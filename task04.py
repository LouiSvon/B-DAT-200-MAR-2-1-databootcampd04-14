import requests

def my_teams(token: str) -> list:
    url = "https://graph.microsoft.com/v1.0/me/joinedTeams"

    headers = {
        "Authorization": f"Bearer {token}",
    }

    result = [] #Liste finale avec IDs des teams

    while url:
        response = requests.get(url, headers=headers)
        data = response.json()

        for team in data.get("value", []): #value contient les teams de la page
            team_id = team.get("id")
            if team_id is not None:
                result.append(team_id)

        url = data.get("@odata.nextLink")

    return result