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

@bot.on_message(filters.command("join") & filters.create(on_channel))
def join_chat_call(c, m):
    chat = m.chat.id
    media = m.command[1]
    if len(m.command) > 2:
        types = m.command[1]
        url = m.command[2]
    if not media:
        m.reply("Không tìm thấy nội dung", quote=True)
        return
    if any(pre in url for pre in ["youtube", "youtu.be", "soundcloud", "bilibili", "tiktok", "zing"]):
        if types == "music":
            media = get_audio(url)
        else:
            media = get_video(url)
    if m.command[1] == "content":
        media = "http://127.0.0.1:8080/content.mp4"
    try:
        m.reply("Đã bắt đầu phát sóng")
        app.join_group_call(chat, MediaStream(media,))
    except:
        m.reply("Có vấn đề xảy ra! Không thể mở trình phát")
    m.delete()
        
@bot.on_message(filters.command("broadcast") & filters.create(on_channel))
def join_content_channel(c, m):
    chat = "contentdownload"
    media = m.command[1]
    if len(m.command) > 2:
        types = m.command[1]
        url = m.command[2]
    if not media:
        return
    if any(pre in url for pre in ["youtube", "youtu.be", "soundcloud", "bilibili", "tiktok", "zing"]):
        if types == "music":
            media = get_audio(url)
        else:
            media = get_video(url)
    if m.command[1] == "content":
        media = "http://127.0.0.1:8080/content.mp4"
    try:
        m.reply("Đã bắt đầu phát sóng ở @contentdownload")
        app.join_group_call(chat, MediaStream(media,))
    except:
        m.reply("Có vấn đề xảy ra! Không thể mở trình phát")
    m.delete()
        
@bot.on_message(filters.command("endcast") & filters.create(on_channel))
def leave_content_channel(c, m):
    app.leave_group_call(m.chat.id,)
    m.reply("Đã ngừng phát sóng ở @contentdownload")
    m.delete()    
        
@bot.on_message(filters.command("leave") & filters.create(on_channel))
def leave_video_chat(c, m):
    app.leave_group_call(m.chat.id,)
    m.reply("Đã ngừng phát sóng")
    m.delete()
    
@bot.on_message(filters.command("volume") & filters.create(on_channel))
def change_volume(c, m):
    v = m.command[1]
    app.change_volume_call(m.chat.id, v,)
    m.reply(f"Đã thay đổi mức âm lượng thành {v}")
    m.delete()

@bot.on_message(filters.command("play"))
def play_requested_media(c, m):
    chat = m.chat.id
    media = m.command[1]
    try:
        app.get_call(chat)
    except:
        m.reply("Không có phiên phát sóng nào mở cả", quote=True)
        return
    if len(m.command) > 2:
        types = m.command[1]
        url = m.command[2]
    if not media:
        m.reply("Không tìm thấy nội dung", quote=True)
        return
    if any(pre in url for pre in ["youtube", "youtu.be", "soundcloud", "bilibili", "tiktok", "zing"]):
        if types == "music":
            media = get_audio(url)
        else:
            media = get_video(url)
    if m.command[1] == "content":
        media = "http://127.0.0.1:8080/content.mp4"
    else:
        media = url
    m.reply(f"**[{m.from_user.first_name}](tg://user?id={m.from_user.id})** đã gửi yêu cầu phát sóng [liên kết]({url})")
    m.delete()
    app.change_stream(chat, MediaStream(media,))
    
bot.start()
idle()