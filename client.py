from hydrogram import Client
from deta import Deta 
from app import app
from environ import api_id, api_hash, bot_token

bot = Client("Bot", api_id, api_hash, bot_token=bot_token, plugins=dict(root="plugins"), in_memory=True)
app.start()
bot.run()