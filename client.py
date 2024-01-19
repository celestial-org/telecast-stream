from pyrogram import Client, filters, idle
from pytgcalls import PyTgCalls
from pytgcalls.types import MediaStream
import os, sys

api_id = os.getenv("ID")
api_hash = os.getenv("HASH")
bot_token = os.getenv("BOT")
session_string = os.getenv("SS")
client = Client("telecast", session_string=session_string)
app = PyTgCalls(client)
bot = Client("Bot", api_id, api_hash, bot_token=bot_token)
app.start()
@bot.on_message(filters.command("join") & filters.user(5665225938))
def join_chat_call(c, m):
    chat = m.chat.id
    media = m.command[1]
    m.reply("Đã bắt đầu phát")
    app.join_group_call(chat, MediaStream(media,))
