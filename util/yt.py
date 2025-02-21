import io
import requests
import yt_dlp
from youtubesearchpython import VideosSearch
from pydantic import BaseModel


class Result(BaseModel):
    title: str
    url: str


def get_thumbnail(url):
    req = requests.get(url, timeout=10)
    img = io.BytesIO(req.content)
    img.name = "thumbnail.jpg"
    return img


def get_video(video_url):
    ydl_opts = {"format": "best"}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        url = info_dict["url"]
        title = info_dict["fulltitle"]
        thumbnail = info_dict["thumbnail"]
        thumbnail = get_thumbnail(thumbnail)
        return (
            Result(
                title=title,
                url=url,
            ),
            thumbnail,
        )


def get_audio(url):
    ydl_opts = {"format": "bestaudio/best"}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        url = info_dict["url"]
        title = info_dict["fulltitle"]
        thumbnail = info_dict["thumbnail"]
        thumbnail = get_thumbnail(thumbnail)
        return (
            Result(
                title=title,
                url=url,
            ),
            thumbnail,
        )


def ytsearch(query):
    videosSearch = VideosSearch(query, limit=1)
    result = videosSearch.result()
    link = result["result"][0]["link"]
    return link
