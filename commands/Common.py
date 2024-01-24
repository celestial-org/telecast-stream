from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from api import get_video, get_audio, ttlive
from app import join, play, leave
from more_itertools import chunked
import os, shelve

db = shelve.open("channels.db")

@Client.on_message(filters.command("setting"))
def set_stream_quality(c, m):
    try:
        for att in m.command:
            if att.startswith("audio"):
                os.environ["AUDIO_QUAL"] = att.split("=")[1]
            if att.startswith("video"):
                os.environ["VIDEO_QUAL"] = att.split("=")[1]
            if att.startswith("ffmpeg"):
                os.environ["FFMPEG"] = att.split("=")[1]
    except:
        pass
    aq = os.getenv("AUDIO_QUAL")
    vq = os.getenv("VIDEO_QUAL")
    ffmpeg = on.getenv("FFMPEG")
    m.reply(f"Thông tin cài đặt:\nAudio: `{aq}`\nVideo: `{vq}`\nffmpeg: `{ffmpeg}`")
    
@bot.on_message(filters.command("join"))
def join_chat_call(c, m):
    chat = m.chat.id
    try:
        allkeys = list(db.keys())
        chunked_keys = list(chunked(allkeys, 3))
        playlist = []
        for chunk in chunked_keys:
            row_buttons = [InlineKeyboardButton(pre, callback_data=pre) for pre in chunk]
            playlist.appen
        m.reply(f"Đã bắt đầu phát sóng", reply_markup=InlineKeyboardMarkup(playlist))
        join(chat)
    except Exception as e:
        print(e)
        m.reply("Có vấn đề xảy ra! Không thể mở trình phát")
    m.delete()