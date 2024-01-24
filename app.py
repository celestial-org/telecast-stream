from pytgcalls import PyTgCalls
from pyrogram import Client
from pytgcalls.types import MediaStream, AudioParameters, VideoParameters
from init import session
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
    media = "https://youtu.be/5zsBVm4qK_A?si=YeNGaxega00-NmEu"
    app.join_group_call(chat, stream(media))
    
def leave(chat):
    app.leave_group_call(chat,)
    
def play(chat, media):
    app.change_stream(chat, stream(media))