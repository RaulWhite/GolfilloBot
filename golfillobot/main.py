from telegram.ext import Application, CommandHandler, MessageHandler
from tokens import get_token
from message_filter import *
from botActions import GolfilloActions as Gactions
import logging

logging.basicConfig(format='\n%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

application = Application.builder().token(get_token()).build()

application.add_handler(CommandHandler("tblop", Gactions.tblop))
application.add_handler(CommandHandler("list", Gactions.tblop))
application.add_handler(CommandHandler("oc", Gactions.oc))
application.add_handler(CommandHandler("ping", Gactions.ping))
application.add_handler(CommandHandler("gracies", Gactions.gracies))
application.add_handler(CommandHandler("f", Gactions.f))
application.add_handler(CommandHandler("papopepo", Gactions.papopepo))
application.add_handler(CommandHandler("pr", Gactions.pr))
application.add_handler(CommandHandler("flauta", Gactions.flauta))
application.add_handler(CommandHandler("hola", Gactions.hola))
application.add_handler(CommandHandler('scatman', Gactions.scatman))
application.add_handler(CommandHandler('viejotruco', Gactions.viejotruco))
application.add_handler(CommandHandler('lajungla', Gactions.lajungla))

application.add_handler(MessageHandler(porno(), Gactions.porno))

if __name__ == '__main__':
    application.run_polling()
