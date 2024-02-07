from pytgcalls import PyTgCalls
from pyrogram import Client
from pytgcalls.types import MediaStream
from pytgcalls.types.raw import AudioParameters, VideoParameters
from init import session
from api import get_video, get_audio, ttlive
from util import get_media
import os

app = PyTgCalls(Client("telecast", session_string=session))

def stream(media):
    aq = os.getenv("AUDIO_QUAL")
    vq = os.getenv("VIDEO_QUAL")
    aq = tuple(map(int, aq.split(',')))
    vq = tuple(map(int, vq.split(',')))
    ffmpeg = os.getenv("FFMPEG")
    return MediaStream(
        media,
        audio_parameters=AudioParameters(*aq), 
        video_parameters=VideoParameters(*vq), 
        additional_ffmpeg_parameters=ffmpeg)

def join(chat):
    media = get_video("https://youtu.be/5zsBVm4qK_A?si=YeNGaxega00-NmEu")
    app.join_group_call(chat, stream(media))
    
def leave(chat):
    app.leave_group_call(chat,)
    
def play(chat, media):
    if any(pre in media for pre in ["youtube", "youtu.be", "soundcloud", "bilibili", "tiktok", "zing"]):
        if media.startswith("music:"):
            media = media.replace("music:", "")
            media = get_audio(media)
        else:
            try:
                if "tiktok" in media:
                    media = ttlive(media)
                else:
                    raise
            except:
                media = get_video(media)
    app.change_stream(chat, stream(media))