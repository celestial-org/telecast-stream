from hydrogram import Client, filters

@Client.on_message(group=2)
def react_all(c, m):
    c.read_chat_history(m.chat.id)
    m.react(emoji="❤️", big=True)