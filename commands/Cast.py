from pyrogram import Client, filters
from app import join, play, leave
from util import albums, album, add_media, del_media, get_media
from custom import on_channel
from gtts import gTTS
import time

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
    
@Client.on_message(filters.command("end") & filters.create(on_channel))
def leave_chat_call(c, m):
    leave(m.chat.id)
    m.reply("--**Chương trình đã kết thúc**--")
    
@Client.on_message(filters.command("play"))
def play_media_queue(c, m):
    chat = m.chat.id
    link = m.command[1]
    m.delete()
    if not link.startswith("http") and m.from_user:
        name = m.from_user.first_name
        link = get_media(f"Bộ sưu tập của {name}", link)
        st = m.reply(f"Bắt đầu phát {link} từ bộ sưu tập của {name}")
        play(chat, link)
        st.delete()
    else:
        try:
            user = m.from_user.first_name
        except:
            user = m.sender_chat.title
        st = m.reply(f"--**{user}**-- đã gửi yêu cầu phát __{link}__\nNội dung sẽ được phát sau 1 phút nữa.\nThêm vào bộ sưu tập sẽ có thể phát nhanh hơn")
        time.sleep(60)
        st.delete()
        play(chat, link)
    
@Client.on_message(filters.command('myalbum'))
def get_album(c, m):
    if m.sender_chat:
        m.reply("Album chỉ khả dụng cho tài khoản người dùng")
        return
    name = m.from_user.first_name
    try:
        album = album(name)
        m.reply(f"Bộ sưu tập của --**{name}**--", quote=True, reply_markup=album)
        m.delete()
    except:
        m.reply(f"--**{name}**-- không có bộ sưu tập, hãy bắt đầu bằng lệnh /addlist + tiêu đề + link đa phương tiện", quote=True)
    
@Client.on_message(filters.command("albums"))
def all_albums(c, m):
    m.reply("Tất cả bộ sưu tập", reply_markup=albums())
    
@Client.on_message(filters.command("addlist"))
def add_to_album(c, m):
    if m.sender_chat:
        m.reply("Album chỉ khả dụng cho tài khoản người dùng")
        return
    name = m.from_user.first_name
    pre = m.command[1]
    link = m.command[2]
    if not link.startswith("http"):
        m.reply("Liên kết không hợp lệ", quote=True)
        return
    if m.from_user.id == 5665225938:
        add_media("Telecast", [pre,link])
        m.reply(f"Đã thêm __{pre}__")
    else:
        add_media(f"Bộ sưu tập của {name}", [pre,link])
        m.reply(f"Đã thêm __{pre}__ vào bộ sưu tập của --**{name}**--")
    m.delete()
    
@Client.on_message(filters.command("dellist"))
def delete_from_album(c, m):
    if m.sender_chat:
        m.reply("Album chỉ khả dụng cho tài khoản người dùng")
        return
    name = m.from_user.first_name
    pre = m.command[1]
    if m.from_user.id == 5665225938:
        del_media("Telecast", pre)
        m.reply(f"Đã xoá {pre}")
    else:
        del_media(f"Bộ sưu tập của {name}", pre)
        m.reply(f"Đã xoá {pre} khỏi bộ sưu tập của {name}")
    m.delete()
    
@Client.on_message(filters.command("playlist") & filters.create(on_channel))
def get_album_of(c, m):
    name = m.reply_to_message.from_user.first_name
    try:
        album = album(name)
        m.reply(f"Bộ sưu tập của --**{name}**--", quote=True, reply_markup=album)
        m.delete()
    except:
        m.reply(f"--**{name}**-- không có bộ sưu tập", quote=True)
        
@Client.on_message(filters.text, group=2)
def Telecast_all(c, m):
    try:
        user = m.from_user.first_name
        last_name = m.from_user.last_name
        if last_name:
            user = user + last_name
    except:
        user = m.sender_chat.title
    text = f"{user}. {m.text}"
    chat = m.chat.id
    tts = gTTS(text=text, lang='vi', slow=True)
    tts.save(f'/tmp/{user}.mp3')
    try:
        play(chat, f"/tmp/{user}.mp3")
    except:
        join(chat)
        play(chat, f"/tmp/{user}.mp3")
    