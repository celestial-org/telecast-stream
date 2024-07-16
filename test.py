from util import ytsearch
import json

from util.yt import ytsearch

link = ytsearch('nguoi la oi')
with open("test.json", "w") as f:
    json.dump(link, f)
print(link)
