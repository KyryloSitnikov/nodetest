import telebot
from datetime import datetime
from flask import Flask, request

app = Flask(__name__)
bot = telebot.TeleBot('6130614504:AAHYFuTbmbNtflJFiUqwsra_vipxSNjRyLA')

responses = {
    '1': 'My name is Bot',
    '2': datetime.now().strftime("%H:%M:%S"),
    '3': 'I am doing well, thanks for asking!'
}

@app.route('/', methods=['POST'])
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
    question = message.text
    if question in responses:
        bot.reply_to(message, responses[question])

bot.remove_webhook()
bot.set_webhook(url='https://ogneshka.herokuapp.com/' + bot.token)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))


"""
import telebot
from datetime import datetime

bot = telebot.TeleBot('6130614504:AAHYFuTbmbNtflJFiUqwsra_vipxSNjRyLA')

responses = {
    '1': 'My name is Bot',
    '2': datetime.now().strftime("%H:%M:%S"),
    '3': 'I am doing well, thanks for asking!'
}

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, 'Welcome to my bot!')

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    question = message.text
    if question in responses:
        bot.reply_to(message, responses[question])
print('hhh')
bot.polling()
"""