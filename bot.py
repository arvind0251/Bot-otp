import telebot
from config import BOT_TOKEN
from handlers import start_handler, buy_number_handler, otp_handler

bot = telebot.TeleBot(BOT_TOKEN)

if __name__ == "__main__":
    print("Bot is running...")
    bot.polling(none_stop=True)
