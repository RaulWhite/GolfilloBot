from PIL import Image, ImageFont, ImageDraw
import datetime

def create_viejotruco(image_name, blank_image, saved_image, ttf, text):
    text = text.upper().strip() # All uppercase
    if text.startswith("DE "): # Strip start already in image
        text = text[3:]
    elif text == "DE":
        text = " "
    if text == "":
        img = Image.open(blank_image)
    else:
        img = Image.open(image_name)
    draw = ImageDraw.Draw(img)
    ### Weekday
    font = ImageFont.truetype(ttf, 38)
    draw.text((740, 555), weekday(), font=font, fill=(0,0,0,255))
    ### Message
    if text != "":
        font = ImageFont.truetype(ttf, 64)
        w = conW = 460 # x start point
        h = 202 # y start point
        linesLimit = 5 # Limit of lines
        words = text.split()
        w += 90 # First line further right
        line = 0
        wrap = False
        for word in words:
            word += " " # Space every word
            # Check if word fits in line
            w, h, line, wrap = needWrap(w, h, img.size[0], line, conW, font, word)
            if wrap: # If word doesn't fit even in new line, wrap it
                for letter in word:
                    w, h, line, wrap = needWrap(w, h, img.size[0], line, conW, font, letter)
                    if line >= linesLimit: break # Number of lines limit
                    draw.text((w, h), letter, font=font, fill=(0,0,0,255))
                    w += int(font.getlength(letter))
                    w -= 7 #Condense letters
                w += int(font.getlength(" ")) # Space at end of word
            else: # Word fits in line
                if line >= linesLimit: break # Number of lines limit
                draw.text((w, h), word, font=font, fill=(0,0,0,255))
                w += int(font.getlength(word)) # New x appending drawn word width
    img.save(saved_image, "JPEG")

def needWrap(w, h, imgW, line, conW, font, text):
    wrap = False
    if (w + int(font.getlength(text))) > imgW: # If it doesn't fit, new line
        w = conW # Start of line
        h += font.getbbox(text)[3] # Calculate font height
        line += 1 # New line at limiter
        wrap = (w + int(font.getlength(text))) > imgW # If word doesn't fit, wrap it
    return w, h, line, wrap

def weekday():
    weekdaysES = ["Lunes", "Martes", "Miércoles", "Jueves",
                "Viernes", "Sábado", "Domingo"]
    return weekdaysES[datetime.datetime.today().weekday()].upper()
