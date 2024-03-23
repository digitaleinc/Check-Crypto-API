from modules.markup import gen_markup
from processing import process_usdt_trc20
from functions import logger

from config import bot


@bot.message_handler(commands=['start'], func=lambda message: message.chat.type == 'private')
def start(message):
    logger(message)
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    if user_name is None:
        user_name = ""
    bot.send_message(user_id, f"🌟 <b>Hello {user_name}!</b>\n"
                              f"\n"
                              f"📌 This bot is designed to quickly verify transactions on the USDT TRC20 network.\n"
                              f"\n"
                              f"🚀 With the help of this bot, you can quickly get the necessary "
                              f"information of the transaction hash.\n"
                              f"\n"
                              f"🍹 <b>Enjoy using it!</b>"
                              f"\n"
                              f"<i>Bot was created by A.K.</i>\n"
                              f"<b>GitHub ► https://github.com/digitaleinc</b>",
                     parse_mode='HTML',
                     reply_markup=gen_markup())


@bot.message_handler(commands=['check'])
def checking(message):
    logger(message)
    bot.send_message(message.chat.id, "🔗 Send me hash of USDT TRC20 Transaction:",
                     reply_to_message_id=message.message_id)
    bot.register_next_step_handler(message, process_usdt_trc20)


@bot.message_handler(content_types=['text'], func=lambda message: message.chat.type == 'private')
def text_handler(message):
    logger(message)
    user_id = message.from_user.id
    if message.text == "🔎 Check":
        bot.send_message(user_id, "🔗 Send me hash of USDT TRC20 Transaction:")
        bot.register_next_step_handler(message, process_usdt_trc20)
