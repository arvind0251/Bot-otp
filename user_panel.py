import telebot
from database.db import db_connect
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['my_balance'])
def my_balance(message):
    user_id = message.chat.id
    conn = db_connect()
    cursor = conn.cursor()

    # Get user balance
    cursor.execute("SELECT balance FROM users WHERE telegram_id=?", (user_id,))
    user = cursor.fetchone()

    if user:
        balance = user[0]
        bot.send_message(user_id, f"💰 Your Current Balance: ₹{balance}")
    else:
        bot.send_message(user_id, "❌ You are not registered. Use /start to register.")

conn.close()
