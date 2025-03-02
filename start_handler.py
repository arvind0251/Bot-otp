import telebot
from database.db import db_connect
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    conn = db_connect()
    cursor = conn.cursor()

    cursor.execute("SELECT balance FROM users WHERE telegram_id=?", (user_id,))
    user = cursor.fetchone()

    if not user:
        cursor.execute("INSERT INTO users (telegram_id, balance) VALUES (?, ?)", (user_id, 0.0))
        conn.commit()

    bot.send_message(user_id, "Welcome! Use /buy_number to get a virtual number.")
