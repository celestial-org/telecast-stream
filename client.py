from pyrogram import Client
from pytgcalls import PyTgCalls, idle
from pytgcalls.types import MediaStream
import os, sys

chat = sys.argv[1]
url = sys.argv[2]

session_string = "BQFOvq8AcSBo2sPYo3JpvmyuKAgW1-7mWxPbKfyLCccfpKRfLscllXG10AfVLxjoI3Yxhhuu7535NT0BZuB6icBbiUFcsoaXHpIy8mF7pQWcfjwMJmm6rXn-PsXO5EhBBAGKQNceZFAv8rczrqbN7Q3RH4DRAbbHDYQqIbcbwCQshd_3SPLNHMzOrkWEmiownTaZkkcWV9hF_7DfjO8KHOQRJbDJMn1VVNKqDxb9srdOZoxd6ZG3pHCucc_0lHQn1FeZRpG2ShmB8EnIUoywJLoPhpU0a3Tras8j7gfXn5VT7ApwQ1VVJwE1VRbQojFgYuN8xkemDqLzn8-00QqqIA1usYdc-QAAAAFsA-uxAA"
client = Client("telex", session_string=session_string)
app = PyTgCalls(client)

app.start()
app.join_group_call(chat, MediaStream(url,))
os.system("echo Đã kết nối")
idle()
