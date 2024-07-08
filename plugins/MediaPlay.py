from pyrogram import Client, filters
from app import Cast

def filter_len(_, __, m):
    return len(m.command) > 1
    
@Client.on_message(filters.command("play") & filters.regex("http://|https://") & filters.create(filter_len))
def play_media_queue(c, m):
    chat = m.chat.id
    link = [i for i in m.command if i.startswith("http")][0]
    st = m.reply("Ok", quote=True)
    Cast(chat).play(link)
    st.delete()
    m.delete()
    
@Client.on_message(filters.command("screen"))
def screen_record(c, m):
    status = Cast(m.chat.id).screen()
    if status:
        m.reply("Bắt đầu ghi màn hình", quote=True)
    else:
        m.reply("Máy chủ không có màn hình", quote=True)
        
@Client.on_message(filters.command("search"))
def search_youtube(c ,m):
    query = m.text.split(m.command[0])[1]
    m.reply("Ok", quote=True)
    Cast(m.chat.id).ytsearch(query)