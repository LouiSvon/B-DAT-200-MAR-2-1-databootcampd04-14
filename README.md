# Data Bootcamp D04 - Microsoft Graph API

## Description

Ce depot contient des exercices Python utilisant l'API Microsoft Graph pour recuperer des informations liees a un utilisateur, ses groupes, ses equipes et les canaux Teams.

## Objectif

L'objectif est de pratiquer les appels HTTP authentifies avec un token Bearer, la lecture de reponses JSON et la gestion de la pagination renvoyee par Microsoft Graph.

## Stack / technologies

- Python
- `requests`
- Microsoft Graph API

## Fonctionnalites principales

- Test de connexion a l'endpoint `/me`.
- Recuperation de l'adresse mail ou du `userPrincipalName`.
- Comptage des groupes de l'utilisateur.
- Transformation des groupes en dictionnaire `id -> displayName`.
- Recuperation des equipes rejointes.
- Recuperation des canaux d'une equipe.

## Structure

```text
.
├── task00.py
├── task01.py
├── task02.py
├── task03.py
├── task04.py
├── task05.py
└── task06.py
```

## Lancement

Installer `requests` si necessaire :

```bash
pip install requests
```

Importer les fonctions depuis Python avec un token Microsoft Graph valide :

```python
from task00 import test_connection

status = test_connection("TOKEN_MICROSOFT_GRAPH")
print(status)
```

## Remarques

`task06.py` est vide dans l'etat actuel du depot. Les exercices necessitent un token Microsoft Graph valide pour produire des resultats.
