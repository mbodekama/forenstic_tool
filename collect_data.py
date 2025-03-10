import requests

#Ameliorer ce script de collecte dinfo via github
"""
1 - SOus forme de fonction 
2- CLI en ligne de commande 
3 - Je veux qun dossier soit creer pour stocker l'avatar et le fichier contenant
    la liste des repo de chaque follower
4- le nom de l'utilisateur github a scanner ne dois pas être figé

-----------
module sys
module pathlib
-----------
"""
r = requests.get('https://api.github.com/users/lesage20')
response = r.json()

follower_req = requests.get(response['followers_url'])
follower_req = follower_req.json()

for follower in follower_req:
    avatar_req = requests.get(follower['avatar_url'])
    avatar_name = follower['login'] + '.jpg'
    with open(avatar_name, 'wb') as f:
        f.write(avatar_req.content)


avatar_req = requests.get(response['avatar_url'])
with open('mbodekama.jpg', 'wb') as f:
    f.write(avatar_req.content)


#LIst des repo de lutilisateur
list_repo_req = requests.get(response['repos_url'])
list_repo_req = list_repo_req.json()

for repo in list_repo_req:
    line = (f"Nom repository : {repo['name']}\n Description : {repo['description']}\n  url : {repo['url']}\n")
    with open('list_repo.txt', 'a') as f:
        f.write(line)


