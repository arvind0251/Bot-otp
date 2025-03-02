import telebot
import requests
from database.db import db_connect
from config import BOT_TOKEN, FIVESIM_API_KEY

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['buy_number'])
def buy_number(message):
    user_id = message.chat.id
    conn = db_connect()
    cursor = conn.cursor()

    cursor.execute("SELECT balance FROM users WHERE telegram_id=?", (user_id,))
    user = cursor.fetchone()

    if user and user[0] >= 10:  
        response = requests.get(
            "https://5sim.net/v1/user/buy/activation",
            headers={"Authorization": f"Bearer {FIVESIM_API_KEY}"},
            params={"country": "russia", "operator": "any", "product": "telegram"}
        )

        data = response.json()
        if "phone" in data:
            phone_number = data["phone"]
            order_id = data["id"]

            cursor.execute("UPDATE users SET balance = balance - 10 WHERE telegram_id=?", (user_id,))
            conn.commit()

            bot.send_message(user_id, f"✅ Number Purchased: {phone_number}\nOrder ID: {order_id}\nUse /get_otp {order_id} to check OTP.")
        else:
            bot.send_message(user_id, "❌ Failed to buy number! Try again.")
    else:
        bot.send_message(user_id, "❌ Insufficient Balance! Use /add_funds to recharge.")
