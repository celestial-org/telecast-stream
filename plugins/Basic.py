from hydrogram import Client, filters

@Client.on_message(group=2)
def react_all(c, m):
    m.react(emoji="❤️", big=True)