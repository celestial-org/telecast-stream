from pyrogram import Client, filters
from util import albums, album, get_media
from app import play
import json

@Client.on_callback_query()
def on_callback_query_handle(c, q):
    data = q.data
    m = q.message
    if data == "albums-button":
        m.edit("Danh sách bộ sưu tập", reply_markup=albums())
    elif data.startswith("album:"):
        data = data.replace("album:", "")
        m.edit(data, reply_markup=album(data))
    else:
        try:
            chat = m.chat.id
            q.answer(f"Bắt đầu phát {media}")
            play(chat, data)
        except:
            q.answer("Có vấn đề xảy ra")