from hydrogram import Client, filters
import random

emojis = ["👍", "❤️", "😍", "🔥", "🥰", "👏", "💔", "💘", "🆒"]

@Client.on_message(group=2)
def react_all(c, m):
    emo = random.choice(emojis)
    if not m.from_user.is_bot:
        c.read_chat_history(m.chat.id)
        m.react(emoji=emo, big=True)