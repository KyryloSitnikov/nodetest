import telebot
import spacy
from spacy import displacy
from flask import Flask, request
import os

app = Flask(__name__)
bot = telebot.TeleBot('6130614504:AAHYFuTbmbNtflJFiUqwsra_vipxSNjRyLA')

nlp = spacy.load('uk_core_news_lg')

@app.route('/' + bot.token, methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return '', 200

@app.route('/')
def index():
    return 'Hello, world!'

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, 'Welcome to my bot!')

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text
    doc = nlp(text)
    if doc[0].text.lower() in ('привіт', 'привет'):
        bot.reply_to(message, 'І вам здоровенькі були!')
    else:
        bot.reply_to(message, 'I do not understand your message.')

bot.remove_webhook()
bot.set_webhook(url='https://ogneshka.herokuapp.com/' + bot.token)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
