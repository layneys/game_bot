import requests
import auth_data as auth
import random
import re

clean = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')


async def get_game():
    id = random.randint(0, 10000)
    game = requests.get(
        f"https://api.rawg.io/api/games/{id}?key={auth.RAWG_TOKEN}").json()
    while ('description' not in game) or ('background_image' not in game) or ('name' not in game) or (
            game['background_image'] is None) \
            or (game['name'] is None) or (game['description'] is None) or (len(game['description']) < 500)\
            or (len(game['developers']) == 0):
        id = random.randint(0, 10000)
        game = requests.get(
            f"https://api.rawg.io/api/games/{id}?key={auth.RAWG_TOKEN}").json()
    description = re.sub(clean, " ", game['description'])
    description = description[0:950] + f"<a href =\"https://rawg.io/games/{game['slug']}\">...</a>"
    print(id)
    rez = {
        "name": re.sub(clean, " ", game['name']),
        "description": description,
        "main_image": game['background_image'],
        "rating": game['metacritic'],
        "released": game['released'],
        "developer": game['developers'][0]['name'],
    }

    return rez
