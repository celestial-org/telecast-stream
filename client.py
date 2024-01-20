from pyrogram import Client, filters, idle
from pytgcalls import PyTgCalls
from pytgcalls.types import MediaStream
import os, sys
from init import api_id, api_hash, bot_token, session
from custom import on_channel
from api import get_video, get_audio

app = PyTgCalls(Client("telecast", session_string=session))
bot = Client("Bot", api_id, api_hash, bot_token=bot_token, in_memory=True)
app.start()

def _filter(_, __, m):
    return m.from_user.id == 5665225938 if m.from_user else (m.sender_chat.id == -1001559828576)
    
@bot.on_message(filters.command("join") & filters.create(on_channel))
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
    if any(pre in media for pre in ["youtube", "youtu.be"]):
        media = get_yt(media)
    m.reply(f"Đã chuyển kênh", quote=True)
    app.change_stream(chat, MediaStream(media,))
    
bot.start()
idle()