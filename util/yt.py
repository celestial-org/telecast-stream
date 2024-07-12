import yt_dlp
from youtubesearchpython import VideosSearch


def get_video(video_url):
    ydl_opts = {"format": "best"}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        return info_dict["url"]


def get_audio(url):
    ydl_opts = {"format": "bestaudio/best"}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        return info_dict["url"]


def ytsearch(query):
    videosSearch = VideosSearch(query, limit=1)
    result = videosSearch.result()
    return result["result"][0]["link"]
