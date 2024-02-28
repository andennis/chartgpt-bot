import telebot
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
    base_url=os.environ.get('OPENAI_URL'),
)

bot = telebot.TeleBot(os.environ.get('BOT_TOKEN'))

chat_histories = {}


def chat_with_ai(message):
    chat_id = message.chat.id
    user_input = message.text

    if chat_id not in chat_histories:
        chat_histories[chat_id] = []

    messages = chat_histories[chat_id]
    messages.append({"role": "user", "content": user_input})
    # messages.append({"role": "system", "content": "answer as a funny clown"})

    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages
    )

    ai_response = chat_completion.choices[0].message.content
    bot.send_message(chat_id, ai_response)

    messages.append({"role": "assistant", "content": ai_response})


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    chat_with_ai(message)


bot.polling()
