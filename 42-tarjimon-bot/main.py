from translate import translate
import telebot

TOKEN = "1637883576:AAH6ZQkXL..." 
tarjimonbot  = telebot.TeleBot(token=TOKEN)

# \start komandasi uchun mas'ul funksiya
@tarjimonbot.message_handler(commands=['start'])
def salom(message):    
    xabar = "Assalom alaykum, tarjimon botiga xush kelbisiz."
    xabar += '\nMatningizni yuboring.'
    tarjimonbot.reply_to(message, xabar)
    

# matnlar uchun mas'ul funksiya
@tarjimonbot.message_handler(func=lambda msg: msg.text is not None)
def tarjima(message):
    msg = message.text
    tarjimonbot.reply_to(message, translate(msg))
    

tarjimonbot.polling()