from urllib import response
import requests
import os

secret = os.getenv("SECRET")
req = requests.get(secret, timeout=10)
response = req.json()
SESSION = response["telegram"]["session"]
BOT_TOKEN = response["bot"]["tiktokdouyin"]
