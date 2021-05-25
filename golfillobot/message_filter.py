from telegram.ext import BaseFilter
from telegram.ext.filters import MessageFilter

#porno
class porno(MessageFilter):
    def filter(self, message):
        if message.text is not None:
            text = message.text.lower()
            return 'porno' in text
        else:
            return False