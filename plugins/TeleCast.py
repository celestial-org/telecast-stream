from hydrogram import Client, filters
from app import Cast
import os

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
    
@Client.on_message(filters.command("pause"))
def pause_cast(c, m):
    if not os.getenv(str(m.chat.id)):
        Cast(m.chat.id).pause()
        st = m.reply("Đang tạm dừng", quote=True)
        os.environ[str(m.chat.id)] = str(st.id)
  
@Client.on_message(filters.command("resume"))
def resume_cast(c, m):
    if os.getenv(str(m.chat.id)):
        Cast(m.chat.id).resume()
        mid = int(os.getenv(str(m.chat.id)))
        mid.delete()
