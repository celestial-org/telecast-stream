from flask import Flask, Response
from pyrogram import Client
from init import api_id, api_hash, bot_token
import time

app = Flask("__telestream__")

@app.route("/")
def telestream__():
    return "OK"
    
@app.route("/content.mp4")
def stream_content_channel():
    bot = Client("Bot", api_id, api_hash, bot_token=bot_token, in_memory=True)
    try:
        bot.start()
    except:
        pass
    def gen():
        for i in range(1, 2000):
            try:
                msg = bot.get_messages("contentdownload", message_ids=i)
                for chunk in bot.stream_media(msg):
                    yield chunk
            except:
                continue
    return Response(gen(), mimetype="video/mp4")
                 