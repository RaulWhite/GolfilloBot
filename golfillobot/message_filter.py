from telegram.ext import BaseFilter

#porno
class porno(BaseFilter):
    def filter(self, message):
        if message.text is not None:
            text = message.text.lower()
            return 'porno' in text
        else:
            return False