from pyrogram import Client
from pytgcalls import PyTgCalls, idle
from pytgcalls.types import MediaStream
import os, sys

chat = sys.argv[1]
url = sys.argv[2]
session_string = sys.argv[3]


client = Client("telex", session_string=session_string)
app = PyTgCalls(client)

app.start()
app.join_group_call(chat, MediaStream(url,))
os.system("echo Đã kết nối")
idle()
