import requests
import auth_data as auth
import random
import re

clean = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')


async def get_game(genre: str):
    ids = []
    game_page = requests.get(
        f'https://api.rawg.io/api/games?key={auth.RAWG_TOKEN}&genres={genre}&page={random.randint(0, 100)}').json()
    for game in game_page['results']:
        ids.append(game['id'])
    i = 0
    game = {}
    while ('description' not in game) or ('background_image' not in game) or ('name' not in game) or (
            game['background_image'] is None) \
            or (game['name'] is None) or (game['description'] is None) or (len(game['description']) < 500) \
            or (game['metacritic'] is None) or (len(game['developers']) == 0) or (game['platforms'] is None):
        i += 1
        if i > len(ids):
            new_page = requests.get(game_page['next']).json()
            for game in new_page['results']:
                ids.append(game['id'])
        game = requests.get(
            f"https://api.rawg.io/api/games/{ids[i]}?key={auth.RAWG_TOKEN}").json()
    description = re.sub(clean, " ", game['description'])
    description = description[0:450] + f"<a href =\"https://rawg.io/games/{game['slug']}\">...</a>"
    print(ids[i])
    platforms = ""
    for plt in game['platforms']:
        platforms += ", " + f"{plt['platform']['name']}"
    full_info = f"[{game['name']}]\n" + "About:" + description + "\n" \
                + f"Metacritic:[{game['metacritic']}]" +"\n" \
                + f"Main developer: [{game['developers'][0]['name']}]" + "\n"\
                + f"Platforms: [{platforms[1::]}]"
    rez = {
        "name": re.sub(clean, " ", game['name']),
        "description": full_info,
        "main_image": game['background_image'],
        "rating": game['metacritic'],
        "released": game['released'],
        "developer": game['developers'][0]['name'],
    }

    return rez