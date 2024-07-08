from pyrogram import Client, filters
import os, requests

@Client.on_message(filters.command("add_proxy"))
def add_proxy(c, m):
    if len(m.command) > 1:
        proxy = m.command[1]
        if os.path.exists("lite"):
            os.system("pkill -9 lite &")
        else:
            content = requests.get("https://github.com/xxf098/LiteSpeedTest/releases/download/v0.15.0/lite-linux-amd64-v0.15.0.gz").content
            with open("lite.gz", "wb") as f:
                f.write(content)
            os.system("gzip -d lite.gz && chmod +x lite")
        os.system(f"./lite {proxy} &")
        os.environ["http_proxy"]="http://127.0.0.1:8090"
        os.environ["https_proxy"]="http://127.0.0.1:8090"
        m.reply("Đã thiết lập proxy", quote=True)
        m.delete()
        
@Client.on_message(filters.command("remove_proxy"))
def remove_proxy(c, m):
    os.system("pkill -9 lite &")
    del os.environ["http_proxy"]
    del os.environ["https_proxy"]
    m.reply("Đã loại bỏ proxy", quote=True)