import yt_dlp

def get_video(video_url):
  ydl_opts = {'format': 'best'}
  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(video_url, download=False)
    return info_dict["url"]
    
def get_audio(url):
  ydl_opts = {'format': 'worstaudio'}
  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(url, download=False)
    return info_dict["url"]
    
    