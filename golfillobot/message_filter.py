from telegram.ext import BaseFilter

#porno
class porno(BaseFilter):
    def filter(self, message):
        text = message.text.lower()
        return 'porno' in text