from hydrogram import Client, filters
from app import Caller

@Client.on_message(filters.command("join"))
def join_chat_call(c, m):
    chat = m.chat.id
    status = Caller(chat).join()
    if status:
        m.reply("--**Chương trình đã bắt đầu**--")
        m.delete()
    else:
        m.reply("Không thể bắt đầu phát sóng", quote=True)