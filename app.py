from pytgcalls import PyTgCalls
from pyrogram import Client
from pytgcalls.types import MediaStream, AudioQuality, VideoQuality
from api import ttl
import os

session = os.getenv("SESSION")

def stream(media):
    return MediaStream(
        media,
        AudioQuality.MEDIUM, 
        VideoQuality.HD_720p)

class Cast:
    def __init___(self, chat):
        self.app = PyTgCalls(Client("telecast", session_string=session))
    def join(self):
        try:
            self.app.join_group_call(self.chat,)
            return True 
        except Exception as e:
            print(e)
            return False
            
    def end(self):
        self.app.leave_group_call(self.chat,)
        
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
            self.app.change_stream(self.chat, stream(media),)
            return True
        except Exception as e:
            print(e)
            return False