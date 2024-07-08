from pytgcalls import PyTgCalls
from pyrogram import Client
from pytgcalls.types import MediaStream, AudioQuality, VideoQuality
from pytgcalls.media_devices import MediaDevices
from youtubesearchpython import VideosSearch
from api import ttl, get_video, get_audio
from environ import session
import os

client = Client("telecast", session_string=session, plugins=dict(root="plugins"))
app = PyTgCalls(client)

def stream(media):
    return MediaStream(
        media,
        AudioQuality.MEDIUM, 
        VideoQuality.HD_720p)

class Cast:
    def __init__(self, chat):
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
            elif "youtube" in media and "live" in media:
                media = get_video(media)
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
            
    def pause(self):
        try:
            app.pause_stream(self.chat,)
            return True
        except Exception as e:
            print(e)
            return False
            
    def resume(self):
        try:
            app.resume_stream(self.chat,)
            return True
        except Exception as e:
            print(e)
            return False
            
    def screen(self):
        try:
            app.change_stream(self.chat, MediaStream(MediaDevices.get_screen_devices()[0], audio_path=MediaDevices.get_audio_devices()[0]),)
            return True
        except Exception as e:
            print(e)
            return False
    
    def ytsearch(self, query):
       videosSearch = VideosSearch(query, limit=1)
       result = videosSearch.result()
       link = result["result"][0]["link"]
       media = get_audio(link)
       app.change_stream(self.chat, stream(media),)