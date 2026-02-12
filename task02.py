import requests 

def groups_count(token: str) -> int: #prend un token et retourne un entier 
    url = "https://graph.microsoft.com/v1.0/me/memberOf"

    headers = {
        "Authorization": f"Bearer {token}",
    }

    count = 0  #compteur total de groupes

    while url:

        response = requests.get(url, headers=headers) #envoi de la requête HTTP GET vers l’API

        data = response.json() #conversion de la réponse JSON en dictionnaire Python

        values = data.get("value", [])  
        # "value" contient la liste des groupes sur la page actuelle
        # Si "value" n’existe pas, on met une liste vide pour éviter une erreur

        count += len(values) #ajoute au compteur le nombre de groupes trouvés

        url = data.get("@odata.nextLink")  
        #Si l’API indique qu’il existe une page suivante,
        # @odata.nextLink contient nouvelle URL
        #Sinon valeur devient None → la boucle s’arrête

    return count