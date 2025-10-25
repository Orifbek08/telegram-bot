import telebot
import re

TOKEN = "8290141066:AAHNkJru74i9gXfEzUoOG69JCpLt0SsCBBM"
GROUP_ID = -1002237546410

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def check_message(message):
    if message.chat.id == GROUP_ID:
        text = message.text.lower()
        if re.search(r"savdo\s*bor", text):
            bot.reply_to(message, "man bor")

print("🤖 Bot ishga tushdi...")
bot.polling(none_stop=True)