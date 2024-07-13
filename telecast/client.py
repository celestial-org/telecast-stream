from pytgcalls import PyTgCalls
from pyrogram import Client
from pytgcalls.types import MediaStream, AudioQuality, VideoQuality, GroupCallConfig
from pytgcalls.media_devices import MediaDevices
from env import SESSION

client_app = Client("telecast", session_string=SESSION, device_model="Telecast")
telecast_app = PyTgCalls(client_app)

with client_app as c:
    channel_peer = c.resolve_peer("contentdownload")
call_config = GroupCallConfig(join_as=channel_peer)


def start_telecast(bot):
    return telecast_app.start()


class Telecast:

    def __init__(self):
        self.config = call_config
        self.app = telecast_app

    def stream(self, media):
        return MediaStream(media, AudioQuality.STUDIO, VideoQuality.FHD_1080p)

    def join(self, chat):
        try:
            self.app.play(chat, config=self.config)
            return True
        except Exception as e:
            print(e)
            return False

    def leave(self, chat):
        self.app.leave_call(
            chat,
        )

    def play(self, chat, media_link):
        self.app.play(chat, self.stream(media_link), config=self.config)

    def pause(self, chat):
        try:
            self.app.pause_stream(
                chat,
            )
            return True
        except Exception as e:
            print(e)
            return False

    def resume(self, chat):
        try:
            self.app.resume_stream(
                chat,
            )
            return True
        except Exception as e:
            print(e)
            return False

    def screen(self, chat):
        try:
            self.app.play(
                chat,
                MediaStream(
                    MediaDevices.get_screen_devices()[0],
                    audio_path=MediaDevices.get_audio_devices()[0],
                ),
                config=self.config,
            )
            return True
        except Exception as e:
            print(e)
            return False

    def played_time(self, chat):
        return self.app.played_time(chat)
