import yt_dlp
import json


def get_video(video_url):
    ydl_opts = {"format": "best"}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        return info_dict


link = get_video("https://youtu.be/92rkN4n-V20?si=AL9oDh98_FS7LNJm")
with open("test.json", "w") as f:
    json.dump(link, f)
print(link['thumbnail'])
