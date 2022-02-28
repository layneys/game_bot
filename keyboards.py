from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Genre Menu
genreMenu = InlineKeyboardMarkup(row_width=2)

btnAction = InlineKeyboardButton(text='Action', callback_data='btnAction')
btnIndie = InlineKeyboardButton(text='Indie', callback_data='btnIndie')
btnAdventure = InlineKeyboardButton(text='Adventure', callback_data='btnAdventure')
btnRPG = InlineKeyboardButton(text='RPG', callback_data='btnRPG')
btnStrategy = InlineKeyboardButton(text='Strategy', callback_data='btnStrategy')
btnShooter = InlineKeyboardButton(text='Shooter', callback_data='btnShooter')
btnArcade = InlineKeyboardButton(text='Arcade', callback_data='btnArcade')
btnRacing = InlineKeyboardButton(text='Racing', callback_data='btnRacing')
btnSports = InlineKeyboardButton(text='Sports', callback_data='btnSports')
btnFighting = InlineKeyboardButton(text='Fighting', callback_data='btnFighting')
btnFamily = InlineKeyboardButton(text='Family', callback_data='btnFamily')
btnCart = InlineKeyboardButton(text='Cart', callback_data='btnCart')


genreMenu.insert(btnAction)
genreMenu.insert(btnAdventure)
genreMenu.insert(btnArcade)
genreMenu.insert(btnFighting)
genreMenu.insert(btnIndie)
genreMenu.insert(btnRacing)
genreMenu.insert(btnRPG)
genreMenu.insert(btnShooter)
genreMenu.insert(btnSports)
genreMenu.insert(btnStrategy)


# Single Game Menu
gameMenu = InlineKeyboardMarkup(row_width=2)
btnScreenshots = InlineKeyboardButton(text='Screenshots', callback_data='btnScrns')
btnTrailer = InlineKeyboardButton(text='Watch trailer', callback_data='btnTrailer')
btnNext = InlineKeyboardButton(text='Find other', callback_data='btnNext')
btnDLC = InlineKeyboardButton(text='btnDLC', callback_data='btnDLC')
btnSeries = InlineKeyboardButton(text='btnSeries', callback_data='btnSeries')
btnToGenre = InlineKeyboardButton(text='To genres', callback_data='btnStart')
gameMenu.insert(btnToGenre)
gameMenu.insert(btnNext)
gameMenu.insert(btnScreenshots)
gameMenu.insert(btnTrailer)
# Trailer menu
trailerMenu = InlineKeyboardMarkup(row_width=1)
btnBack = InlineKeyboardButton(text="Back", callback_data="btnBack")
trailerMenu.insert(btnBack)
# Screenshots menu
screenshotsMenu = InlineKeyboardMarkup(row_width=1)
btnScrBack = InlineKeyboardButton(text="Back", callback_data="btnScrnBack")
screenshotsMenu.insert(btnScrBack)



# Random number menu
rNumMenu = InlineKeyboardMarkup(row_width=2)
btnRandom = InlineKeyboardButton(text="RandNum", callback_data='btnRandom')
genreMenu.insert(btnRandom)
rNumMenu.insert(btnRandom)
rNumMenu.insert(btnToGenre)