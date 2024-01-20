from flask import Flask
from pyrogram import Client, Response
from init import api_id, api_hash, bot_token

app = Flask("__telestream__")

@app.route("/")
def telestream__():
    return "OK"
    
@app.route("/content.mp4")
def stream_content_channel(c, m):
    with Client("Bot", api_id, api_hash, bot_token=bot_token, in_memory=True) as bot:
        def gen():
            for i in ran(0, 2000):
                try:
                    msg = bot.get_messages("contentdownload", i)
                    for chunk in bot.stream_media(msg):
                        yield chunk
                except:
                    continue
    return Response(gen(), mimetype="video/mp4")
                 