from telegram import Update
from telegram.ext import CallbackContext
import os, random
from specialActions import create_viejotruco

async def send(update: Update, text: str, **kwargs):
    await update.message.reply_text(text=text, reply_to_message_id=update.message.message_id, **kwargs)

async def sendaudio(update: Update, voice):
    #bot.send_voice(chat_id=message.chat_id, voice=voice, reply_to_message_id=message.message_id
    await update.message.reply_voice(voice=voice, reply_to_message_id=update.message.message_id)

async def sendphoto(update: Update, image):
    # bot.send_photo(chat_id=message.chat_id, photo=image, reply_to_message_id=message.message_id)
    await update.message.reply_photo(photo=image, reply_to_message_id=update.message.message_id)

async def sendvideonote(update: Update, video):
    # bot.send_video_note(chat_id=message.chat_id, video_note=video)
    await update.message.reply_video_note(video_note=video, reply_to_message_id=update.message.message_id)

def leerLista():
    with open("./files/tblop.txt", "r") as tblop:
        lista = [linea for linea in tblop]
    return lista

class GolfilloActions(object):
    # porno
    @staticmethod
    async def porno(update: Update, context: CallbackContext):
        lista = leerLista()
        n = random.randint(0, (len(lista) - 2))
        text = "A ver porno a " + lista[n]
        await send(update, text)

    # /list | /tblop
    @staticmethod
    async def tblop(update: Update, context: CallbackContext):
        lista = leerLista()
        text = "".join(lista)
        await send(update, text)

    # /oc
    @staticmethod
    async def oc(update: Update, context: CallbackContext):
        voice = open("./files/oc.ogg", "rb")
        await sendaudio(update, voice)

    # /ping
    @staticmethod
    async def ping(update: Update, context: CallbackContext):
        text = "Yo tiro"
        await send(update, text)
    
    # /gracies
    @staticmethod
    async def gracies(update: Update, context: CallbackContext):
        notes = ["gracies", "gracies2"]
        video = open("./files/" + random.choice(notes) + ".mp4", "rb")
        await sendvideonote(update, video)

    # /f
    @staticmethod
    async def f(update: Update, context: CallbackContext):
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
        await send(update, text, parse_mode='Markdown')

    # /papopepo
    @staticmethod
    async def papopepo(update: Update, context: CallbackContext):
        voice = open("./files/papopepo.ogg", "rb")
        await sendaudio(update, voice)

    # /pr
    @staticmethod
    async def pr(update: Update, context: CallbackContext):
        photo = open("./files/pr.jpg", "rb")
        await sendphoto(update, photo)

    # /flauta
    @staticmethod
    async def flauta(update: Update, context: CallbackContext):
        voice = open('./files/flauta.ogg', 'rb')
        await sendaudio(update, voice)

    # /hola
    @staticmethod
    async def hola(update: Update, context: CallbackContext):
        video = open("./files/hola.mp4", "rb")
        await sendvideonote(update, video)

    # /scatman
    @staticmethod
    async def scatman(update: Update, context: CallbackContext):
        voice = open('./files/sc.opus', 'rb')
        await sendaudio(update, voice)

    # /viejotruco
    @staticmethod
    async def viejotruco(update: Update, context: CallbackContext):
        text = update.message.text
        if len(text.split()) > 1:
            text = text.split(" ", 1)[1]
        else:
            text = ""
        create_viejotruco("./files/truco_original.png", "./files/truco_caer.png",
                            "./files/truco_generated.jpg", "./files/Cantarell-BoldOblique.ttf",
                            text)
        photo = open("./files/truco_generated.jpg", "rb")
        await sendphoto(update, photo)
        os.remove("./files/truco_generated.jpg")

    # /lajungla
    @staticmethod
    async def lajungla(update: Update, context: CallbackContext):
        voice = open('./files/viernesdelajungla.ogg', 'rb')
        await sendaudio(update, voice)
