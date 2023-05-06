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