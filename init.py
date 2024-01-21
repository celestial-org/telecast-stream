from deta import Deta 
import os

deta = Deta(os.getenv("DETA"))
db = deta.Base("tokens")
api_id = db.get("api")["id"]
api_hash = db.get("api")["hash"]
bot_token = db.get("bot")["td"]
cd_token = db.get("bot")["cd"]
session = db.get("telecast")["ss"]