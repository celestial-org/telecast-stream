from deta import Deta 

deta = Deta(os.getenv("DETA"))
db = deta.Base("telegram-sessions")
api_id = db.get("API_ID")["value"]
api_hash = db.get("API_HASH")["value"]
bot_token = db.get("TD_TOKEN")["value"]
session = db.get("ContentCast")["value"]