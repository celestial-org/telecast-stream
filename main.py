from flask import Flask, Response
from pyrogram import Client
from init import api_id, api_hash, bot_token
import time

app = Flask("__telestream__")
bot = Client("Bot", api_id, api_hash, bot_token=bot_token, in_memory=True)
bot.start()

@app.route("/")
def telestream__():
    return "OK"
    
@app.route("/content.mp4")
def stream_content_channel(c, m):
    def gen():
        for i in ran(0, 2000):
            try:
                msg = bot.get_messages("contentdownload", i)
                for chunk in bot.stream_media(msg):
                    yield chunk
            except:
                pass
            time.sleep(2)
    return Response(gen(), mimetype="video/mp4")
                 