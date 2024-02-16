from hydrogram import Client, filters

@Client.on_message(group=2)
def react_all(c, m):
    if not m.from_user.is_bot:
        c.read_chat_history(m.chat.id)
        m.react(emoji="❤️", big=True)