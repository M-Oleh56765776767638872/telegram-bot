import os
import telebot

# Получаем токен из переменной окружения
TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я бот-обработчик заявок.\nОтправь мне свою заявку.")

# Обработка входящих сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.send_message(message.chat.id, f"Спасибо! Ваша заявка получена: {message.text}")

# Запуск бота
bot.polling()
