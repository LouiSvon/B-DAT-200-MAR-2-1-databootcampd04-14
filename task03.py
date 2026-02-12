import requests

def groups_dict(token: str) -> dict:
    url = "https://graph.microsoft.com/v1.0/me/memberOf"

    headers = {
        "Authorization": f"Bearer {token}",
    }

    result = {}

    while url:  # pagination
        response = requests.get(url, headers=headers)
        data = response.json() # Conversion JSON > dict Python

        for group in data.get("value", []):  # value == liste des groupes
            group_id = group.get("id")
            display_name = group.get("displayName")

            if group_id is not None and display_name is not None:  
                result[group_id] = display_name # Ajout dico

        url = data.get("@odata.nextLink")  

    return result