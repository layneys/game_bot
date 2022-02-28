import requests
import auth_data as auth
import random
import re
import aiohttp, asyncio

clean = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')

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
                    f'https://api.rawg.io/api/games/{self.game["id"]}/movies?key=f66a61e487e54610ae729bb987415b2f') as movies_page_req:
                movies_page = await movies_page_req.json()
                if 'count' not in movies_page or movies_page['count'] == 0:
                    return 0
                else:
                    return movies_page['results']

    async def get_screenshots(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f'https://api.rawg.io/api/games/{self.game["id"]}/screenshots?key=f66a61e487e54610ae729bb987415b2f') as schreenshots_page_req:
                screenshots_page = await schreenshots_page_req.json()
                return screenshots_page['results']
