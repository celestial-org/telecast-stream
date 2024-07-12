from pyrogram import Client, idle
from telecast.client import start_telecast
from env import BOT_TOKEN

bot = Client(
    "telecast_manager",
    21021245,
    "7b32ea92719781c5e22ede319c5dbde5",
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins"),
)

bot.start()
start_telecast(bot)
idle()
