from pyrogram import Client, filters
from app import Cast
import os, time

def on_channel(_, __, m):
    return m.from_user.id == 5665225938 if m.from_user else (m.sender_chat.id == -1001559828576)

@Client.on_message(filters.command("join"))
def join_chat_call(c, m):
    chat = m.chat.id
    status = Cast(chat).join()
    if status:
        m.reply("--**Chương trình đã bắt đầu**--")
        m.delete()
    else:
        st = m.reply("Không thể bắt đầu phát sóng", quote=True)
        time.sleep(10)
        st.delete()
        
@Client.on_message(filters.command("quit") & filters.create(on_channel))
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
        mid = os.getenv(str(m.chat.id))
        c.delete_messages(m.chat.id, int(mid))
        del os.environ[str(m.chat.id)]
