from telegram import Bot, Update, Message
import os, random

def send(bot: Bot, message: Message, text: str):
    bot.send_message(chat_id=message.chat_id, text=text, reply_to_message_id=message.message_id)

def sendaudio(bot: Bot, message: Message, voice):
    bot.send_voice(chat_id=message.chat_id, voice=voice, reply_to_message_id=message.message_id)

def sendvideonote(bot: Bot, message: Message, video):
    bot.send_video_note(chat_id=message.chat_id, video_note=video)

def leerLista():
    with open("./files/tblop.txt", 'r') as tblop:
        lista = [linea for linea in tblop]
    return lista

class GolfilloActions(object):
    # porno
    @staticmethod
    def porno(bot: Bot, update: Update):
        lista = leerLista()
        n = random.randint(0, (len(lista) - 2))
        text = "A ver porno a " + lista[n]
        send(bot, update.message, text)

    # /list | /tblop
    @staticmethod
    def tblop(bot: Bot, update: Update):
        lista = leerLista()
        text = "".join(lista)
        send(bot, update.message, text)

    # /oc
    @staticmethod
    def oc(bot: Bot, update: Update):
        voice = open("./files/oc.ogg", 'rb')
        sendaudio(bot, update.message, voice)

    # /ping
    @staticmethod
    def ping(bot: Bot, update: Update):
        text = "Yo tiro"
        send(bot, update.message, text)
    
    # /gracies
    @staticmethod
    def gracies(bot: Bot, update: Update):
        video = open("./files/gracies.mp4", 'rb')
        sendvideonote(bot, update.message, video)