import telebot

TOKEN = '<TOKEN>'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Hi! I'm a Telegram-бот. How can I help you?")


@bot.message_handler(commands=['help'])
def handle_help(message):
    response = """
    Menu: 
    /start - Hi message
    /help - help
    /reverse - reverse text
    /caps - transform text to caps
    """
    bot.send_message(message.chat.id, response)


@bot.message_handler(commands=['reverse'])
def handle_reverse(message):
    text_to_flip = message.text[len('/reverse '):]
    flipped_text = text_to_flip[::-1]
    bot.send_message(message.chat.id, flipped_text)


@bot.message_handler(commands=['caps'])
def handle_caps(message):
    text_to_caps = message.text[len('/caps '):]
    caps_text = text_to_caps.upper()
    bot.send_message(message.chat.id, caps_text)


bot.polling(non_stop=True)
