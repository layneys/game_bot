from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import keyboards as nav
from auth_data import TOKEN
import random
from rawg_requests import Game

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

genre = ''

game_obj = Game()


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Choose genre", reply_markup=nav.genreMenu)


@dp.callback_query_handler(text="btnStart")
async def start_callback(query: types.CallbackQuery):
    await bot.delete_message(chat_id=query.from_user.id, message_id=query.message.message_id)
    await bot.send_message(text="Choose genre", reply_markup=nav.genreMenu, chat_id=query.from_user.id)


@dp.callback_query_handler(text='btnRandom')
async def rand_num(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_message(call.from_user.id, "Случайное число {}".format(random.randint(0, 1000)),
                           reply_markup=nav.rNumMenu)


@dp.callback_query_handler(text='btnNext')
async def new_game(call: types.CallbackQuery):
    # print(game_obj.genre)
    # print(game_obj.game['id'])
    await game_obj.get_game(f'{game_obj.genre}')
    full_info = await game_obj.get_full_info()
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_photo(photo=types.InputFile.from_url(f"{game_obj.game['background_image']}"),
                         chat_id=call.from_user.id,
                         caption=full_info, reply_markup=nav.gameMenu, parse_mode=types.ParseMode.HTML) \


@dp.callback_query_handler(text='btnBack')
async def go_back(call: types.CallbackQuery):
    full_info = await game_obj.get_full_info()
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_photo(photo=types.InputFile.from_url(f"{game_obj.game['background_image']}"),
                         chat_id=call.from_user.id,
                         caption=full_info, reply_markup=nav.gameMenu, parse_mode=types.ParseMode.HTML) \

@dp.callback_query_handler(text='btnTrailer')
async def trailer(call: types.CallbackQuery):
    trailer = await game_obj.get_trailer()
    if trailer == 0:
        await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        await bot.send_message(text="No trailer found", reply_markup=nav.trailerMenu, chat_id=call.from_user.id)
    else:
        await bot.send_message(call.from_user.id, text=f"{trailer[0]['data']['480']}",
                             reply_markup=nav.trailerMenu)


@dp.callback_query_handler(text='btnScrns')
async def trailer(call: types.CallbackQuery):
    global length
    length = 0
    screenshots = await game_obj.get_screenshots()
    if screenshots:
        group = types.MediaGroup()
        for scr in screenshots[::5]:
            group.attach_photo(photo=types.InputFile.from_url(f"{scr['image']}"))
            length += 1
        await bot.send_media_group(media=group, chat_id=call.from_user.id)
        await bot.send_message(text="Back to game?", reply_markup=nav.screenshotsMenu, chat_id=call.from_user.id)
        await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    else:
        await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        await bot.send_message("No screenshots found", reply_markup=nav.trailerMenu)


@dp.callback_query_handler(text='btnScrnBack')
async def back_scr(call: types.CallbackQuery):
    full_info = await game_obj.get_full_info()
    # await bot.delete_message(call.from_user.id, call.message.message_id-2)
    for i in range(length + 1):
        await bot.delete_message(call.from_user.id, call.message.message_id - i)
    await bot.send_photo(photo=types.InputFile.from_url(f"{game_obj.game['background_image']}"),
                         chat_id=call.from_user.id,
                         caption=full_info, reply_markup=nav.gameMenu, parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(text="btnAction")
async def action_game(call: types.CallbackQuery):
    genre = call.data[3::].lower()
    await game_obj.get_game(f'{genre}')
    full_info = await game_obj.get_full_info()
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_photo(photo=types.InputFile.from_url(f"{game_obj.game['background_image']}"),
                         chat_id=call.from_user.id,
                         caption=full_info, reply_markup=nav.gameMenu, parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(text="btnAdventure")
async def adventure_game(call: types.CallbackQuery):
    genre = call.data[3::].lower()
    await game_obj.get_game(f'{genre}')
    full_info = await game_obj.get_full_info()
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_photo(photo=types.InputFile.from_url(f"{game_obj.game['background_image']}"),
                         chat_id=call.from_user.id,
                         caption=full_info, reply_markup=nav.gameMenu, parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(text="btnArcade")
async def arcade_game(call: types.CallbackQuery):
    genre = call.data[3::].lower()
    await game_obj.get_game(f'{genre}')
    full_info = await game_obj.get_full_info()
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_photo(photo=types.InputFile.from_url(f"{game_obj.game['background_image']}"),
                         chat_id=call.from_user.id,
                         caption=full_info, reply_markup=nav.gameMenu, parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(text="btnFighting")
async def fighting_game(call: types.CallbackQuery):
    genre = call.data[3::].lower()
    await game_obj.get_game(f'{genre}')
    full_info = await game_obj.get_full_info()
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_photo(photo=types.InputFile.from_url(f"{game_obj.game['background_image']}"),
                         chat_id=call.from_user.id,
                         caption=full_info, reply_markup=nav.gameMenu, parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(text="btnIndie")
async def indie_game(call: types.CallbackQuery):
    genre = call.data[3::].lower()
    await game_obj.get_game(f'{genre}')
    full_info = await game_obj.get_full_info()
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_photo(photo=types.InputFile.from_url(f"{game_obj.game['background_image']}"),
                         chat_id=call.from_user.id,
                         caption=full_info, reply_markup=nav.gameMenu, parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(text="btnRacing")
async def racing_game(call: types.CallbackQuery):
    genre = call.data[3::].lower()
    await game_obj.get_game(f'{genre}')
    full_info = await game_obj.get_full_info()
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_photo(photo=types.InputFile.from_url(f"{game_obj.game['background_image']}"),
                         chat_id=call.from_user.id,
                         caption=full_info, reply_markup=nav.gameMenu, parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(text="btnRPG")
async def rpg_game(call: types.CallbackQuery):
    genre = call.data[3::].lower()
    await game_obj.get_game(f'role-playing-games-rpg')
    full_info = await game_obj.get_full_info()
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_photo(photo=types.InputFile.from_url(f"{game_obj.game['background_image']}"),
                         chat_id=call.from_user.id,
                         caption=full_info, reply_markup=nav.gameMenu, parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(text="btnShooter")
async def shooter_game(call: types.CallbackQuery):
    genre = call.data[3::].lower()
    await game_obj.get_game(f'{genre}')
    full_info = await game_obj.get_full_info()
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_photo(photo=types.InputFile.from_url(f"{game_obj.game['background_image']}"),
                         chat_id=call.from_user.id,
                         caption=full_info, reply_markup=nav.gameMenu, parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(text="btnSports")
async def sports_game(call: types.CallbackQuery):
    genre = call.data[3::].lower()
    await game_obj.get_game(f'{genre}')
    full_info = await game_obj.get_full_info()
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_photo(photo=types.InputFile.from_url(f"{game_obj.game['background_image']}"),
                         chat_id=call.from_user.id,
                         caption=full_info, reply_markup=nav.gameMenu, parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(text="btnStrategy")
async def strategy_game(call: types.CallbackQuery):
    genre = call.data[3::].lower()
    await game_obj.get_game(f'{genre}')
    full_info = await game_obj.get_full_info()
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_photo(photo=types.InputFile.from_url(f"{game_obj.game['background_image']}"),
                         chat_id=call.from_user.id,
                         caption=full_info, reply_markup=nav.gameMenu, parse_mode=types.ParseMode.HTML)


if __name__ == '__main__':
    executor.start_polling(dp)
