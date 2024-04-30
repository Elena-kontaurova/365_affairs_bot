
import telebot
from telebot import types

bot = telebot.TeleBot('7163086368:AAFq4mlOlUu7dL7QoFT0E8EAOnjF9HiBTeE')

@bot.message_handler(commands=['start']) 
def handle_start(message): 
    # Создание клавиатуры 
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True) 
    button1 = types.KeyboardButton('Что мне поделать?') 
    button1.height = 1  # Устанавливаем высоту кнопки
    keyboard.add(button1) 

    # Отправка сообщения с клавиатурой 
    bot.reply_to(message, 'Приветик', reply_markup=keyboard)

@bot.message_handler(func=lambda message: True) 
def handle_message(message): 
    if message.text == 'Что мне поделать?': 
        # Действия при нажатии на кнопку 1 
        bot.reply_to(message, 'Тут будет идея') 
    else: 
        # Действия при получении другого сообщения 
        bot.reply_to(message, 'Извини, я тебя не понимаю')



bot.polling(none_stop=True)