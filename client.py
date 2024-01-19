from pyrogram import Client, filters, idle
from pytgcalls import PyTgCalls
from pytgcalls.types import MediaStream
import os, sys
from deta import Deta 
import yt_dlp

deta = Deta(os.getenv("DETA"))
db = deta.Base("telegram-sessions")
api_id = db.get("API_ID")["value"]
api_hash = db.get("API_HASH")["value"]
bot_token = db.get("TD_TOKEN")["value"]
session_string = os.getenv("SS")
db.put(data=session_string, key="ContentCast")
client = Client("telecast", session_string=session_string)
app = PyTgCalls(client)
bot = Client("Bot", api_id, api_hash, bot_token=bot_token, in_memory=True)
app.start()

@bot.on_message(filters.command("join") & filters.user([5665225938,-1001559828576]))
def join_chat_call(c, m):
    chat = m.chat.id
    media = m.command[1]
    try:
        m.reply("Đã bắt đầu phát")
        app.join_group_call(chat, MediaStream(media,))
    except:
        m.reply("Không thể phát trực tiếp")
        
@bot.on_message(filters.command("quit") & filters.user([5665225938,-1001559828576]))
def leave_video_chat(c, m):
    app.leave_group_call(m.chat.id,)
    m.reply("Đã ngừng phát")

@bot.on_message(filters.command("play"))
def play_requested_media(c, m):
    chat = m.chat.id
    media = m.command[1]
    if any(pre in media for pre in ["youtube", "youtu.be"]):
        media = get_yt(media)
    if not media:
        m.reply("Không tìm thấy nội dung", quote=True)
        return
    m.reply(f"Đã chuyển kênh", quote=True)
    app.change_stream(chat, MediaStream(media,))
    
def get_yt(video_url):
  ydl_opts = {'format': 'best'}
  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(video_url, download=False)
    return info_dict["url"]
    
    
    
bot.start()
idle()