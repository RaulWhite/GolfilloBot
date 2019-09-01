# **Golfillo Bot**

<small>Golfillo stands for little golfo, a.k.a. someone with special necesities (if you know what I mean...)</small>

Golfillo Bot is a Telegram Bot in Python that helps you on those ocassions of extreme need of... ehem... you know what I mean...

![The meme](https://i.imgur.com/V9IoYcym.png)

## **Description**

This is a basic Telegram bot written in Python3, and dockerized for easy deployment.

## **Why?**

For having fun on Telegram groups. I'm publishing the code to github mainly for code references for someone that is trying to do someting similar.

## **Bot Actions**

This bot, in particular, can help you in different ways. The messages the bot sends are written in spanish (sorry about that), but feel free to edit them as you wish. In addition, it does other stuff that is more SFW.

|Trigger|Action|
|--|--|
|`/list`<br>`/tblop`|Gives you a list of pages, which can help you on those situations (prints `files/tblop.txt`)|
|`porno`|When someone writes `porno` (_porn_ in english), it helps you with that situation<br>(it answers with random line of `files/tblop.txt` with the message "A ver porno a `<line>`", that means _"To watch porn, go to `<line>`"_)|
|`/ping`|Shows that it is working (answers "Yo tiro", that means _"I'm working"_)|
|`/oc`|It demonstrates the agreement with the situation (send a voice note with the file `files/oc.ogg`)|
|`/gracies`|It thanks you very kindly in Mallorca's language (sends a video note with the file `files/gracies.mp4` or `files/gracies2.mp4` randomly selected)|
|`/f`|Pays respects in a very original way (prints a big `F` chosen randomly from an array of texts)|
|`/papopepo`|It sings along one of the spiciest memes between my friends and I (send a voice note with the file `files/papopepo.ogg`)|

**NOTE:** The files are not available in this repo by request of the owner and/or for avoiding any trouble.

## **Usage**

You have 2 options for running this bot: **Python3** or **Docker**

### **Python3**

You need Python3 and pip.

Install the pip requirements with

```bash
pip install -r requirements.txt
```

Then, create a `.env` file with the Telegram API key in the variable `TEL_BOT_TOKEN`. The format is as follows:

```bash
TEL_BOT_TOKEN=<API Key>
```

You can also ditch the file and put the key on a system variable with the same name, but it will be volatile. The file it's only for permanent storage porpuses.

The `files` directory must by in the same path as the `golfillobot` folder, or in the directory you are positioned in the terminal at the time of running the bot.

Finally, start the bot with

```bash
python3 golfillobot/main.py
```

### **Docker** 🐋 (recommended method <3)

An easy alternative. You can also build and use a docker image with the inclued `Dockerfile`. Simply build the image with

```bash
docker image build . -t <IMAGE NAME>
```

where image name is whatever you want. Then run it with

```bash
docker run -d \
-e TEL_BOT_TOKEN=<API KEY> \
-v <FILES PATH>:/app/files \
<IMAGE NAME>
```

**AND YOU'RE DONE!**
