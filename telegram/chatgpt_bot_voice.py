import telebot
from gtts import gTTS
import io
from openai import OpenAI

client = OpenAI(
    api_key="KEY",
    base_url="https://api.proxyapi.ru/openai/v1",
)

TOKEN = "TOKEN"
bot = telebot.TeleBot(TOKEN)

chat_histories = {}


def chat_with_ai(message):
    chat_id = message.chat.id
    user_input = message.text

    if chat_id not in chat_histories:
        chat_histories[chat_id] = []

    messages = chat_histories[chat_id]
    messages.append({"role": "user", "content": user_input})

    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages
    )

    ai_response = chat_completion.choices[0].message.content

    tts = gTTS(text=ai_response, lang='ru')
    voice_io = io.BytesIO()
    tts.write_to_fp(voice_io)
    voice_io.name = 'voice.ogg'
    voice_io.seek(0)

    bot.send_voice(chat_id, voice=voice_io)

    messages.append({"role": "assistant", "content": ai_response})


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    chat_with_ai(message)


bot.polling()
