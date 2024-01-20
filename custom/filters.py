from pyrogram import filters

def on_channel(_, __, m):
    return m.from_user.id == 5665225938 if m.from_user else (m.sender_chat.id == -1001559828576)