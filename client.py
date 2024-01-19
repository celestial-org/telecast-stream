from pyrogram import Client
from pytgcalls import PyTgCalls, idle
from pytgcalls.types import MediaStream
import os, sys

chat = sys.argv[1]
url = sys.argv[2]
session_string = sys.argv[3]
as_chat = sys.argv[4]


client = Client("telestream", session_string=session_string)
app = PyTgCalls(client)
app.start()
if as_chat:
    peer = client.resolve_peer(as_chat)
    app.join_group_call(chat, MediaStream(url,), as_chat=peer)
else:
    app.join_group_call(chat, MediaStream(url,))
os.system("echo Đã kết nối")
idle()
