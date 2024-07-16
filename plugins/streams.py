import shelve
from pyrogram import Client, filters
from pyrogram.enums import ChatAction
from telecast import Telecast
from util import ytsearch, getlive, get_audio, get_video

streamer = Telecast()
owner = [5665225938, 7317791383]
kv = shelve.open("streamer.status")


def on_channel(_, __, m):
    return (
        m.from_user.id in owner if m.from_user else (m.sender_chat.id == -1001559828576)
    )


def filter_len(_, __, m):
    return len(m.command) > 1


@Client.on_message(filters.command("join"))
def join_chat(c, m):
    m.reply_chat_action(ChatAction.TYPING)
    chat = m.chat.id
    if chat in owner:
        chat = -1001559828576
    status = streamer.join(chat)
    if status:
        m.reply("**Chương trình đã bắt đầu**")
    else:
        m.reply("**Không thể bắt đầu phát sóng**", quote=True)


@Client.on_message(filters.command("leave") & filters.create(on_channel))
def leave_chat_call(c, m):
    m.reply_chat_action(ChatAction.TYPING)
    chat = m.chat.id
    if chat in owner:
        chat = -1001559828576
    played_time = streamer.played_time(chat)
    streamer.leave(chat)
    m.reply(
        f"**Chương trình đã kết thúc** ```\nplayed time: {played_time}```", quote=True
    )
    m.delete()


@Client.on_message(filters.command("play"))
def play_media(c, m):
    m.reply_chat_action(ChatAction.TYPING)
    chat = m.chat.id
    if chat in owner:
        chat = -1001559828576
    if len(m.command) == 1:
        m.reply("Vui lòng cung cấp link hoặc nội dung để phát", quote=True)
    link = m.text.split(m.command[0])[1]
    if not any(i in link for i in ["https://", "http://"]):
        link = ytsearch(link)
    else:
        link = [part for part in m.command if part.startswith("http")][0]
    if "tiktok" in link:
        live_link = getlive(link)
        if live_link:
            link = live_link
            title = " TikTok Livestream"
            m.reply(f"**Bắt đầu phát sóng:**\n ```\n{title}```", quote=True)
    else:
        result, thumbnail = get_video(link)
        link = result.url
        title = result.title
        m.reply_photo(
            thumbnail, caption=f"**Bắt đầu phát sóng:**\n ```\n{title}```", quote=True
        )
    m.delete()
    streamer.play(chat, link)


@Client.on_message(filters.command("playmusic") & filters.create(filter_len))
def play_music(c, m):
    m.reply_chat_action(ChatAction.TYPING)
    chat = m.chat.id
    if chat in owner:
        chat = -1001559828576
    link = m.text.split(m.command[0])[1]
    if not any(i in link for i in ["https://", "http://"]):
        link = ytsearch(link)
    else:
        link = [part for part in m.command if part.startswith("http")][0]
    result, thumbnail = get_audio(link)
    link = result.url
    title = result.title
    m.reply_photo(
        thumbnail, caption=f"**Bắt đầu phát sóng:**\n ```\n{title}```", quote=True
    )
    m.delete()
    streamer.play(chat, link)


@Client.on_message(filters.command("screen"))
def screen_record(c, m):
    m.reply_chat_action(ChatAction.TYPING)
    chat = m.chat.id
    if chat in owner:
        chat = -1001559828576
    status = streamer.screen(chat)
    if status:
        m.reply("Bắt đầu ghi màn hình", quote=True)
    else:
        m.reply("Máy chủ không có màn hình", quote=True)


@Client.on_message(filters.command("pause"))
def pause_cast(c, m):
    m.reply_chat_action(ChatAction.TYPING)
    chat = m.chat.id
    if chat in owner:
        chat = -1001559828576
    if not kv.get(str(chat)) or kv[str(chat)][0] != "paused":
        st = m.reply("Đang tạm dừng", quote=True)
        kv[str(chat)] = ["paused", st.id]


@Client.on_message(filters.command("resume"))
def resume_cast(c, m):
    m.reply_chat_action(ChatAction.TYPING)
    chat = m.chat.id
    if chat in owner:
        chat = -1001559828576
    if kv.get(str(chat)) and kv[str(chat)][0] == "paused":
        streamer.resume(chat)
        mid = kv[str(chat)][1]
        c.delete_messages(m.chat.id, int(mid))
        kv[str(chat)] = ["playing", mid]
