from pyrogram import Client, filters, idle
from pytgcalls import PyTgCalls
from pytgcalls.types import MediaStream, AudioParameters, VideoParameters, AudioQuality, VideoQuality
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os, sys
from init import api_id, api_hash, bot_token, session
from custom import on_channel
from api import get_video, get_audio, ttlive
from more_itertools import chunked
import shelve
import time
import json

db = shelve.open("channels.db")
app = PyTgCalls(Client("telecast", session_string=session))
bot = Client("Bot", api_id, api_hash, bot_token=bot_token, in_memory=True)
app.start()

aq = 10000,1
vq = 1920,1080,60
ffmpeg_param = ""

def stream(media):
    return MediaStream(
        media,
        audio_parameters=AudioParameters(*aq), 
        video_parameters=VideoParameters(*vq), 
        additional_ffmpeg_parameters=ffmpeg_param)

@bot.on_message(filters.command("setting"))
def set_stream_quality(c, m):
    global ffmpeg_param, aq, vq
    try:
        for att in m.command:
            if att.startswith("audio"):
                att = att.split("=")[1]
                aq = tuple(map(int, att.split(',')))
            if att.startswith("video"):
                att = att.split("=")[1]
                vq = tuple(map(int, att.split(',')))
            if att.startswith("ffmpeg"):
                ffmpeg_param = att.split("=")[1]
    except:
        pass
    m.reply(f"Cài đặt:\nAudio: `{aq}`\nVideo: `{vq}`\nffmpeg: `{ffmpeg_param}`")

@bot.on_message(filters.command("join"))
def join_chat_call(c, m):
    chat = m.chat.id
    try:
        url = m.command[1]
    except:
        url = "https://youtu.be/5zsBVm4qK_A?si=YeNGaxega00-NmEu"
    if len(m.command) > 2:
        url = m.command[2]
    if not url:
        m.reply("Không tìm thấy nội dung", quote=True)
        return
    if any(pre in url for pre in ["youtube", "youtu.be", "soundcloud", "bilibili", "tiktok", "zing"]):
        if url == "music":
            media = get_audio(url)
        else:
            try:
                if "tiktok" in url:
                    media = ttlive(url)
                else:
                    raise
            except:
                media = get_video(url)
    else:
        media = url
    if url == "content":
        media = "http://127.0.0.1:8080/content.mp4"
    try:
        m.reply(f"Đã bắt đầu phát sóng. [Liên kết]({url})")
        app.join_group_call(chat, stream(media))
    except:
        m.reply("Có vấn đề xảy ra! Không thể mở trình phát")
    m.delete()
        
@bot.on_message(filters.command("broadcast") & filters.create(on_channel))
def join_content_channel(c, m):
    chat = "contentdownload"
    try:
        url = m.command[1]
    except:
        url = "https://youtu.be/5zsBVm4qK_A?si=YeNGaxega00-NmEu"
    if len(m.command) > 2:
        url = m.command[2]
    if not url:
        return
    if any(pre in url for pre in ["youtube", "youtu.be", "soundcloud", "bilibili", "tiktok", "zing"]):
        if url == "music":
            media = get_audio(url)
        else:
            try:
                if "tiktok" in url:
                    media = ttlive(url)
                else:
                    raise
            except:
                media = get_video(url)
    else:
        media = url
    if url == "content":
        media = "http://127.0.0.1:8080/content.mp4"
    try:
        m.reply(f"Đã bắt đầu phát sóng ở @contentdownload. [Liên kết]({url})")
        app.join_group_call(chat, stream(media))
    except:
        m.reply("Có vấn đề xảy ra! Không thể mở trình phát")
    m.delete()
        
@bot.on_message(filters.command("endcast") & filters.create(on_channel))
def leave_content_channel(c, m):
    app.leave_group_call("contentdownload",)
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
    chat = m.chat.id
    if len(m.command) > 2 and m.command[1] == "channel":
        v = m.command[2]
        chat = "contentdownload"
    app.change_volume_call(chat, v,)
    m.reply(f"Đã thay đổi mức âm lượng thành {v}")
    m.delete()

@bot.on_message(filters.command("play"))
def play_requested_media(c, m):
    chat = m.chat.id
    try:
        url = m.command[1]
    except:
        m.reply("Thiếu tham số", quote = True)
        return 
    try:
        app.get_call(chat)
    except:
        m.reply("Không có phiên phát sóng nào mở cả", quote=True)
        return
    if len(m.command) > 2:
        url = m.command[2]
    if not url:
        m.reply("Không tìm thấy nội dung", quote=True)
        return
    if not url.startswith("http"):
        url = db[url]
    if any(pre in url for pre in ["youtube", "youtu.be", "soundcloud", "bilibili", "tiktok", "zing"]):
        if m.command[1] == "music":
            media = get_audio(url)
        else:
            try:
                if "tiktok" in url:
                    media = ttlive(url)
                else:
                    raise
            except:
                media = get_video(url)
    else:
        media = url
    #m.reply(f"**[{m.from_user.first_name}](tg://user?id={m.from_user.id})** đã gửi yêu cầu phát sóng [liên kết]({url})")
    m.delete()
    app.change_stream(chat, stream(media))
    
@bot.on_message(filters.command("cast")& filters.create(on_channel))
def request_channel_cast(c, m):
    chat = "contentdownload"
    try:
        url = m.command[1]
    except:
        m.reply("Thiếu tham số", quote = True)
        return 
    try:
        app.get_call(chat)
    except:
        m.reply("Không có phiên phát sóng nào mở ở @contentdownload", quote=True)
        return
    if len(m.command) > 2:
        url = m.command[2]
    if not url:
        m.reply("Không tìm thấy nội dung", quote=True)
        return
    if any(pre in url for pre in ["youtube", "youtu.be", "soundcloud", "bilibili", "tiktok", "zing"]):
        if m.command[1] == "music":
            media = get_audio(url)
        else:
            try:
                if "tiktok" in url:
                    media = ttlive(url)
                else:
                    raise
            except:
                media = get_video(url)
    else:
        media = url
    if m.command[1] == "content":
        media = "http://127.0.0.1:8080/content.mp4"
    m.reply(f"[Liên kết]({url}) đã bắt đầu phát sóng")
    m.delete()
    app.change_stream(chat, stream(media))
    
@bot.on_message(filters.command("addplay"))
def add_channel(c, m):
    if len(m.command) > 2:
        pre = m.command[1]
        link = m.command[2]
        db[pre] = link
        m.reply(f"Đã thêm __{pre}__", quote=True)
    else:
        m.reply("Thiếu tham số cần thiết", quote=True)
            
@bot.on_message(filters.command("playlist"))
def channels_list(c, m):
    try:
        allpre = list(db.keys())
        chunked_keys = list(chunked(allpre, 6))
        playlist = []
        for chunk in chunked_keys:
            row_buttons = [InlineKeyboardButton(pre, callback_data=pre) for pre in chunk]
            playlist.append(row_buttons)
        m.reply(f"__--**Playlist**--__", quote=True, reply_markup=InlineKeyboardMarkup(playlist))
    except:
        m.reply("Tài nguyên không có sẵn", quote=True)
    
@bot.on_callback_query()
def switch_play(c, cq):
    print(cq)
    pre = cq.data
    link = db[pre]
    cq.answer(f"Bắt đầu phát kênh {pre}")
    chat = cq.message.chat.id
    app.change_stream(chat, stream(media))
    
bot.start()
idle()