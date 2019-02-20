import logging
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
updater = Updater(token='777912703:AAFrmem2Wo2L2ae-bUNCWz6hHf0vFae6C5g')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hey, you wanna play ")
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()
