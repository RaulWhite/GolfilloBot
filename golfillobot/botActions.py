from telegram import Bot, Update, Message
import os, random
from specialActions import create_viejotruco

def send(bot: Bot, message: Message, text: str, **kwargs):
    bot.send_message(chat_id=message.chat_id, text=text, reply_to_message_id=message.message_id, **kwargs)

def sendaudio(bot: Bot, message: Message, voice):
    bot.send_voice(chat_id=message.chat_id, voice=voice, reply_to_message_id=message.message_id)

def sendphoto(bot: Bot, message: Message, image):
    bot.send_photo(chat_id=message.chat_id, photo=image, reply_to_message_id=message.message_id)

def sendvideonote(bot: Bot, message: Message, video):
    bot.send_video_note(chat_id=message.chat_id, video_note=video)

def leerLista():
    with open("./files/tblop.txt", "r") as tblop:
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
        voice = open("./files/oc.ogg", "rb")
        sendaudio(bot, update.message, voice)

    # /ping
    @staticmethod
    def ping(bot: Bot, update: Update):
        text = "Yo tiro"
        send(bot, update.message, text)
    
    # /gracies
    @staticmethod
    def gracies(bot: Bot, update: Update):
        notes = ["gracies", "gracies2"]
        video = open("./files/" + random.choice(notes) + ".mp4", "rb")
        sendvideonote(bot, update.message, video)

    # /f
    @staticmethod
    def f(bot: Bot, update: Update):
        fs = [
        '''```
FFFFFFFFFFFFFFFFFFFFFF
F::::::::::::::::::::F
F::::::::::::::::::::F
FF::::::FFFFFFFFF::::F
  F:::::F       FFFFFF
  F:::::F             
  F::::::FFFFFFFFFF   
  F:::::::::::::::F   
  F:::::::::::::::F   
  F::::::FFFFFFFFFF   
  F:::::F             
  F:::::F             
FF:::::::FF           
F::::::::FF           
F::::::::FF           
FFFFFFFFFFF           
```''',
        '''```
FFFFFFFFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFFFFFFFF
  FFFFFFF       FFFFFF
  FFFFFFF             
  FFFFFFFFFFFFFFFFF   
  FFFFFFFFFFFFFFFFF   
  FFFFFFFFFFFFFFFFF    
  FFFFFFFFFFFFFFFFF   
  FFFFFFF             
  FFFFFFF             
FFFFFFFFFFF           
FFFFFFFFFFF           
FFFFFFFFFFF           
FFFFFFFFFFF           
```''']
        text = random.choice(fs)
        send(bot, update.message, text, parse_mode='Markdown')

    # /papopepo
    @staticmethod
    def papopepo(bot: Bot, update: Update):
        voice = open("./files/papopepo.ogg", "rb")
        sendaudio(bot, update.message, voice)

    # /pr
    @staticmethod
    def pr(bot: Bot, update: Update):
        photo = open("./files/pr.jpg", "rb")
        sendphoto(bot, update.message, photo)

    # /flauta
    @staticmethod
    def flauta(bot: Bot, update: Update):
        voice = open('./files/flauta.ogg', 'rb')
        sendaudio(bot, update.message, voice)

    # /hola
    @staticmethod
    def hola(bot: Bot, update: Update):
        video = open("./files/hola.mp4", "rb")
        sendvideonote(bot, update.message, video)

    # /scatman
    @staticmethod
    def scatman(bot: Bot, update: Update):
        voice = open('./files/sc.opus', 'rb')
        sendaudio(bot, update.message, voice)

    # /viejotruco
    @staticmethod
    def viejotruco(bot: Bot, update: Update):
        text = update.message.text
        if len(text.split()) > 1:
            text = text.split(" ", 1)[1]
        else:
            text = ""
        create_viejotruco("./files/truco_original.png", "./files/truco_caer.png",
                          "./files/truco_generated.jpg", "./files/Cantarell-BoldOblique.ttf",
                           text)
        photo = open("./files/truco_generated.jpg", "rb")
        sendphoto(bot, update.message, photo)
        os.remove("./files/truco_generated.jpg")

    # /lajungla
    @staticmethod
    def lajungla(bot: Bot, update: Update):
        voice = open('./files/viernesdelajungla.ogg', 'rb')
        sendaudio(bot, update.message, voice)

