import telebot
from gtts import gTTS
import io

TOKEN = 'TOKEN'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    try:
        tts = gTTS(text=message.text, lang='en')
        voice_io = io.BytesIO()
        tts.write_to_fp(voice_io)
        voice_io.name = 'voice.ogg'
        voice_io.seek(0)

        bot.send_voice(chat_id=message.chat.id, voice=voice_io)
    except Exception as e:
        bot.reply_to(message, 'An error occurred: ' + str(e))


if __name__ == '__main__':
    bot.polling(none_stop=True)
