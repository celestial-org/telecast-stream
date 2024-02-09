from pytgcalls import PyTgCalls
from pyrogram import Client
from pytgcalls.types import MediaStream, AudioQuality, VideoQuality
from api import ttl
from environ import session
import os

app = PyTgCalls(Client("telecast", session_string=session))

def stream(media):
    return MediaStream(
        media,
        AudioQuality.MEDIUM, 
        VideoQuality.HD_720p)

class Cast:
    def __init___(self, chat):
        self.chat = chat
    def join(self):
        try:
            app.join_group_call(self.chat,)
            return True 
        except Exception as e:
            print(e)
            return False
            
    def end(self):
        app.leave_group_call(self.chat,)
        
    def play(self, media):
        try:
            if "tiktok" in media:
                media = ttl(media)
            else:
                raise
        except Exception as e:
            media = media
            print(e)
        try:
            app.change_stream(self.chat, stream(media),)
            return True
        except Exception as e:
            print(e)
            return False