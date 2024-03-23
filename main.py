from config import bot


def start_bot():
    print("Bot was successfully started")
    bot.infinity_polling(timeout=10, long_polling_timeout=5)


if __name__ == '__main__':
    start_bot()
