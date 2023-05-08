import telebot
import spacy
from flask import Flask, request
import os

app = Flask(__name__)
bot = telebot.TeleBot('6130614504:AAHYFuTbmbNtflJFiUqwsra_vipxSNjRyLA')

# Load the uk_core_web_md model
nlp = spacy.load('uk_core_web_md')

# Set the greeting message for the bot
greeting_message = 'І вам здоровенькі були.'

# Add your allowed user IDs here
allowed_users = [
    # Kyrylo Sitnikov
    152274647, 
    # Oleksandr Bondarenko
    445706100
]

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
    if message.from_user.id not in allowed_users:
        bot.reply_to(message, 'Перепрошую, ми з вами не знайомі. Мій батько не дозволяє мені спілкуватися з незнайомими людьми. Бувайте.')
        return

    # Use spaCy to check for a greeting message
    doc = nlp(message.text.lower())
    if 'привіт' in [token.text for token in doc] or 'привет' in [token.text for token in doc]:
        bot.reply_to(message, greeting_message)
        return

    # Handle other messages
    bot.reply_to(message, 'Я вас не розумію, перепрошую, задайте інше питання')

bot.remove_webhook()
bot.set_webhook(url='https://ogneshka.herokuapp.com/' + bot.token)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))