from hydrogram import Client, filters
from app import Cast

def filter_len(_, __, m):
    return m.command > 1
    
@Client.on_message(filters.command("play") & filters.regex("http://|https://") & filters.create(filter_len))
def play_media_queue(c, m):
    chat = m.chat.id
    link = [i for i in m.command if i.startswith("http")][0]
    st = m.reply("Ok", quote=True)
    Cast(chat).play(link)
    st.delete()