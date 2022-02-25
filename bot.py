from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import keyboards as nav
from auth_data import TOKEN
import random
from rawg_requests import get_game


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

genre = ''

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Choose genre", reply_markup=nav.genreMenu)


@dp.callback_query_handler(text="btnStart")
async def start_callback(query: types.CallbackQuery):
    await bot.delete_message(chat_id=query.from_user.id, message_id=query.message.message_id)
    await bot.send_message(text="Choose genre", reply_markup=nav.genreMenu, chat_id=query.from_user.id)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("This bot helps you to find new games to play."
                        " Just type /search and choose genre. Enjoy ;)")


@dp.callback_query_handler(text='btnRandom')
async def rand_num(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_message(call.from_user.id, "Случайное число {}".format(random.randint(0, 1000)),
                           reply_markup=nav.rNumMenu)


@dp.callback_query_handler(text="btnAction")
async def action_game(call: types.CallbackQuery):
    global genre
    genre = call.data[3::].lower()
    game_info = await get_game(genre)
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_photo(photo=types.InputFile.from_url(f"{game_info['main_image']}"), chat_id=call.from_user.id,
                         caption=game_info['description'], reply_markup=nav.gameMenu, parse_mode=types.ParseMode.HTML)\



@dp.callback_query_handler(text="btnAdventure")
async def adventure_game(call: types.CallbackQuery):
    global genre
    genre = call.data[3::].lower()
    game_info = await get_game(genre)
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_photo(photo=types.InputFile.from_url(f"{game_info['main_image']}"), chat_id=call.from_user.id,
                         caption=game_info['description'], reply_markup=nav.gameMenu, parse_mode=types.ParseMode.HTML)\


@dp.callback_query_handler(text="btnArcade")
async def arcade_game(call: types.CallbackQuery):
    global genre
    genre = call.data[3::].lower()
    game_info = await get_game(genre)
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_photo(photo=types.InputFile.from_url(f"{game_info['main_image']}"), chat_id=call.from_user.id,
                         caption=game_info['description'], reply_markup=nav.gameMenu, parse_mode=types.ParseMode.HTML)\


@dp.callback_query_handler(text="btnCart")
async def cart_game(call: types.CallbackQuery):
    global genre
    genre = call.data[3::].lower()
    game_info = await get_game(genre)
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_photo(photo=types.InputFile.from_url(f"{game_info['main_image']}"), chat_id=call.from_user.id,
                         caption=game_info['description'], reply_markup=nav.gameMenu, parse_mode=types.ParseMode.HTML)\


@dp.callback_query_handler(text="btnEducational")
async def educational_game(call: types.CallbackQuery):
    global genre
    genre = call.data[3::].lower()
    game_info = await get_game(genre)
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_photo(photo=types.InputFile.from_url(f"{game_info['main_image']}"), chat_id=call.from_user.id,
                         caption=game_info['description'], reply_markup=nav.gameMenu, parse_mode=types.ParseMode.HTML)\


@dp.callback_query_handler(text="btnFamily")
async def family_game(call: types.CallbackQuery):
    global genre
    genre = call.data[3::].lower()
    game_info = await get_game(genre)
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_photo(photo=types.InputFile.from_url(f"{game_info['main_image']}"), chat_id=call.from_user.id,
                         caption=game_info['description'], reply_markup=nav.gameMenu, parse_mode=types.ParseMode.HTML)\


@dp.callback_query_handler(text="btnFighting")
async def fighting_game(call: types.CallbackQuery):
    global genre
    genre = call.data[3::].lower()
    game_info = await get_game(genre)
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_photo(photo=types.InputFile.from_url(f"{game_info['main_image']}"), chat_id=call.from_user.id,
                         caption=game_info['description'], reply_markup=nav.gameMenu, parse_mode=types.ParseMode.HTML)\


@dp.callback_query_handler(text="btnIndie")
async def indie_game(call: types.CallbackQuery):
    global genre
    genre = call.data[3::].lower()
    game_info = await get_game(genre)
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_photo(photo=types.InputFile.from_url(f"{game_info['main_image']}"), chat_id=call.from_user.id,
                         caption=game_info['description'], reply_markup=nav.gameMenu, parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(text="btnRacing")
async def racing_game(call: types.CallbackQuery):
    global genre
    genre = call.data[3::].lower()
    game_info = await get_game(genre)
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_photo(photo=types.InputFile.from_url(f"{game_info['main_image']}"), chat_id=call.from_user.id,
                         caption=game_info['description'], reply_markup=nav.gameMenu, parse_mode=types.ParseMode.HTML)\


@dp.callback_query_handler(text="btnRPG")
async def rpg_game(call: types.CallbackQuery):
    global genre
    genre = call.data[3::].lower()
    game_info = await get_game(genre)
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_photo(photo=types.InputFile.from_url(f"{game_info['main_image']}"), chat_id=call.from_user.id,
                         caption=game_info['description'], reply_markup=nav.gameMenu, parse_mode=types.ParseMode.HTML)\


@dp.callback_query_handler(text="btnShooter")
async def shooter_game(call: types.CallbackQuery):
    global genre
    genre = call.data[3::].lower()
    game_info = await get_game(genre)
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_photo(photo=types.InputFile.from_url(f"{game_info['main_image']}"), chat_id=call.from_user.id,
                         caption=game_info['description'], reply_markup=nav.gameMenu, parse_mode=types.ParseMode.HTML)\


@dp.callback_query_handler(text="btnSimulation")
async def simulation_game(call: types.CallbackQuery):
    global genre
    genre = call.data[3::].lower()
    game_info = await get_game(genre)
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_photo(photo=types.InputFile.from_url(f"{game_info['main_image']}"), chat_id=call.from_user.id,
                         caption=game_info['description'], reply_markup=nav.gameMenu, parse_mode=types.ParseMode.HTML)\


@dp.callback_query_handler(text="btnSports")
async def sports_game(call: types.CallbackQuery):
    global genre
    genre = call.data[3::].lower()
    game_info = await get_game(genre)
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_photo(photo=types.InputFile.from_url(f"{game_info['main_image']}"), chat_id=call.from_user.id,
                         caption=game_info['description'], reply_markup=nav.gameMenu, parse_mode=types.ParseMode.HTML)\


@dp.callback_query_handler(text="btnStrategy")
async def strategy_game(call: types.CallbackQuery):
    global genre
    genre = call.data[3::].lower()
    game_info = await get_game(genre)
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_photo(photo=types.InputFile.from_url(f"{game_info['main_image']}"), chat_id=call.from_user.id,
                         caption=game_info['description'], reply_markup=nav.gameMenu, parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(text='btnNext')
async def new_game(call: types.CallbackQuery):
    print(genre)
    game_info = await get_game(genre)

    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_photo(photo=types.InputFile.from_url(f"{game_info['main_image']}"), chat_id=call.from_user.id,
                         caption=game_info['description'], reply_markup=nav.gameMenu, parse_mode=types.ParseMode.HTML)


if __name__ == '__main__':
    executor.start_polling(dp)
