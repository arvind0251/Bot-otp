import telebot
import requests
from config import BOT_TOKEN, FIVESIM_API_KEY

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['get_otp'])
def get_otp(message):
    user_id = message.chat.id
    args = message.text.split()

    if len(args) < 2:
        bot.send_message(user_id, "❌ Invalid Format! Use: /get_otp order_id")
        return

    order_id = args[1]

    response = requests.get(
        f"https://5sim.net/v1/user/check/{order_id}",
        headers={"Authorization": f"Bearer {FIVESIM_API_KEY}"}
    )

    data = response.json()
    if "sms" in data and data["sms"]:
        otp = data["sms"][0]["code"]
        bot.send_message(user_id, f"✅ Your OTP: {otp}")
    else:
        bot.send_message(user_id, "⏳ No OTP received yet! Try again after 1 min.")
