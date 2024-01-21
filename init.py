from deta import Deta 
import os

deta = Deta(os.getenv("DETA"))
db = deta.Base("tokens")
api_id = db.get("api_id")["value"]
api_hash = db.get("api_hash")["value"]
bot_token = db.get("td_token")["value"]
cd_token = db.get("cd_token")["value"]
session = db.get("telecast")["value"]