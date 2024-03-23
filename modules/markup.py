from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def gen_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    check = KeyboardButton("🔎 Check")
    markup.add(check)
    return markup
