from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from api import get_video, get_audio, ttlive
from app import join, play, leave
from util import albums, album, add_media, del_media


@Client.on_message(filters.command("join"))
def join_chat_call(c, m):
    chat = m.chat.id
    try:
        m.reply(f"--**Chương trình đã bắt đầu**--", reply_markup=albums())
        join(chat)
    except Exception as e:
        print(e)
        m.reply("Có vấn đề xảy ra! Không thể mở trình phát")
    m.delete()