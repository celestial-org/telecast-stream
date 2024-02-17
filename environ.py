import requests
import os

secret = os.getenv("SECRET")
r = requests.get(secret)
session = r.text