from hydrogram import Client, filters
from app import Cast

@Client.on_message(filters.command("join"))
def join_chat_call(c, m):
    chat = m.chat.id
    status = Cast(chat).join()
    if status:
        m.reply("--**Chương trình đã bắt đầu**--")
        m.delete()
    else:
        m.reply("Không thể bắt đầu phát sóng", quote=True)
        
@Client.on_message(filters.command("quit"))
def leave_chat_call(c, m):
    Cast(m.chat.id).end()
    m.reply("--**Chương trình đã kết thúc**--")
    m.delete()