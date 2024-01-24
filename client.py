from pyrogram import Client, filters, idle
from pytgcalls import PyTgCalls
from pytgcalls.types import MediaStream, AudioParameters, VideoParameters, AudioQuality, VideoQuality
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os, sys
from init import api_id, api_hash, bot_token, session
from custom import on_channel
from api import get_video, get_audio, ttlive
from app import app
from more_itertools import chunked
import shelve
import time
import json

bot = Client("Bot", api_id, api_hash, bot_token=bot_token, in_memory=True)
app.start()
bot.run()