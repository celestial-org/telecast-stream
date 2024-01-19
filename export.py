from pyrogram import Client
import os

api_id = input("API ID: ")
api_hash = input("API HASH: ")
client = Client("telestream", api_id, api_hash, in_memory=True, takeout=True, device_model="telestream", system_version="Ubuntu", app_version="1.0")

with client:
    session_string = client.export_session_string()
    os.system(f"echo {session_string}")