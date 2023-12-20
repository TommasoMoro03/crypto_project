import telebot
import openai
from openai import OpenAI

bot = telebot.TeleBot ('MY_TELEGRAM_API_KEY')

client = OpenAI(
    api_key="MY_OPENAI_API_KEY",
)

@bot.message_handler(commands=['start'])
def main(message):
     msg = bot.send_message(message.chat.id, "Chiedi qualcosa")
     bot.register_next_step_handler(msg, chatgpt)

@bot.message_handler(content_types=['text'])
def chatgpt(message):
    # Generate a response
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": message.text}],
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.7,
    )

    response = completion.choices[0].message.content
    bot.send_message(message.chat.id, response)

bot.polling(none_stop=True)
