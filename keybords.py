from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_main_menu = ReplyKeyboardMarkup(resize_keyboard=True)

btn_help = KeyboardButton('/help')
btn_new_game = KeyboardButton('/new_game')

kb_main_menu.add(btn_help, btn_new_game)