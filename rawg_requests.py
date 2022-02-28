import requests
import auth_data as auth
import random
import re
import aiohttp, asyncio

clean = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')

# async def get_game(genre: str):
#     ids = []
#     game_page = requests.get(
#         f'https://api.rawg.io/api/games?key={auth.RAWG_TOKEN}&genres={genre}&page_size=25&page={random.randint(0, 50)}').json()
#     for game in game_page['results']:
#         ids.append(game['id'])
#     i = 0
#     game = {}
#     while ('description' not in game) or ('background_image' not in game) or ('name' not in game) or (
#             game['background_image'] is None) \
#             or (game['name'] is None) or (game['description'] is None) or (len(game['description']) < 500) \
#             or (game['metacritic'] is None) or (len(game['developers']) == 0) or (game['platforms'] is None):
#         i += 1
#         if i >= len(ids):
#             new_page = requests.get(game_page['next']).json()
#             for game in new_page['results']:
#                 ids.append(game['id'])
#         game = requests.get(
#             f"https://api.rawg.io/api/games/{ids[i]}?key={auth.RAWG_TOKEN}").json()
#     description = re.sub(clean, " ", game['description'])
#     description =  description[0:450] + f"<a href =\"https://rawg.io/games/{game['slug']}\">...</a>"
#     print(ids[i])
#     platforms = ""
#     for plt in game['platforms']:
#         platforms += ", " + f"{plt['platform']['name']}"
#     full_info = f"[{game['name']}]\n" + "About:" + description + "\n" \
#                 + f"Metacritic:[{game['metacritic']}]" +"\n" \
#                 + f"Main developer: [{game['developers'][0]['name']}]" + "\n"\
#                 + f"Platforms: [{platforms[1::]}]"
#     rez = {
#         "name": re.sub(clean, " ", game['name']),
#         "id":id,
#         "description": full_info,
#         "main_image": game['background_image'],
#         "rating": game['metacritic'],
#         "released": game['released'],
#         "developer": game['developers'][0]['name'],
#     }
#
#     return rez

session = aiohttp.ClientSession()


class Game():
    game_id = 0
    game = {}
    genre = ""

    def __init__(self):
        pass

    async def get_game(self, genre):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f'https://api.rawg.io/api/games?key=f66a61e487e54610ae729bb987415b2f&ordering=-metacritic&page_size=40&genres={genre}&page={random.randint(1, 10)}') as game_page:
                game_page = await game_page.json()
                results = game_page['results']
                game_id = results[random.randint(0, 39)]['id']
                async with session.get(
                        f'https://api.rawg.io/api/games/{game_id}?key=f66a61e487e54610ae729bb987415b2f') as game_req:
                    game = await game_req.json()
                    self.game = game
                    self.game_id = id
                    self.genre = genre


    async def get_full_info(self):
        game = self.game
        description = re.sub(clean, " ", game['description'])
        platforms = ""
        for plt in game['platforms']:
            platforms += ", " + f"{plt['platform']['name']}"
        description = description[0:450] + f"<a href =\"https://rawg.io/games/{game['slug']}\">...</a>"
        full_info = f"[{game['name']}]\n" + "About:" + description + "\n" \
                    + f"Metacritic:[{game['metacritic']}]" + "\n" \
                    + f"Main developer: [{game['developers'][0]['name']}]" + "\n" \
                    + f"Platforms: [{platforms[1::]}]"
        return full_info



    async def get_trailer(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f'https://api.rawg.io/api/games/{3328}/movies?key=f66a61e487e54610ae729bb987415b2f') as movies_page_req:
                movies_page = await movies_page_req.json()
                if 'count' not in movies_page or movies_page['count'] == 0:
                    return 0
                else:
                    return movies_page['count']

#
# async def get_screenshots(id:int):
#     game_screenshots = requests.get(f'https://api.rawg.io/api/games/{id}/screenshots?key={auth.RAWG_TOKEN}').json()
#     screenshots = []
#     for screen in game_screenshots['results']:
#         screenshots.append(screen['image'])
#     return screenshots
#
#
# async def get_trailer(id:int):
#     game_trailers = requests.get(f'https://api.rawg.io/api/games/{id}/movies?key={auth.RAWG_TOKEN}').json()
#     trailer_info = {}
#     try:
#         trailer_info['trailer_found'] = game_trailers['results'][0]['data']['480']
#     except:
#         trailer_info['trailer_not_found'] = "No trailer found"
#     return trailer_info
