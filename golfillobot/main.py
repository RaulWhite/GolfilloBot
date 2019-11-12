from telegram.ext import Updater, CommandHandler, MessageHandler, BaseFilter
from tokens import get_token
from message_filter import *
from botActions import GolfilloActions as Gactions
import logging

logging.basicConfig(format='\n%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater(get_token())
dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(porno(), Gactions.porno))
dispatcher.add_handler(CommandHandler("tblop", Gactions.tblop))
dispatcher.add_handler(CommandHandler("list", Gactions.tblop))
dispatcher.add_handler(CommandHandler("oc", Gactions.oc))
dispatcher.add_handler(CommandHandler("ping", Gactions.ping))
dispatcher.add_handler(CommandHandler("gracies", Gactions.gracies))
dispatcher.add_handler(CommandHandler("f", Gactions.f))
dispatcher.add_handler(CommandHandler("papopepo", Gactions.papopepo))
dispatcher.add_handler(CommandHandler("pr", Gactions.pr))

if __name__ == '__main__':
    updater.start_polling()
    updater.idle()