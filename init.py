from deta import Deta 
import os

deta = Deta(os.getenv("DETA"))
db = deta.Base("telegram-sessions")
api_id = db.get("API_ID")["value"]
api_hash = db.get("API_HASH")["value"]
bot_token = db.get("TD_TOKEN")["value"]
cd_token = db.get("CD_TOKEN")["value"]
session = db.get("ContentCast")["value"]