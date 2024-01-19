from flask import Flask, request, Response
import subprocess

app = Flask("__telestream__")

def executor(chat, url):
    process = subprocess.Popen(["python3", "-u", "client.py", f"{chat}", f"{url}"], stdout=subprocess.PIPE, universal_newlines=True)
    for line in process.stdout:
        yield str(line + "\n")
    process.wait()

@app.route("/")
def telestream__():
    chat = request.args.get("chat")
    url = request.args.get("url")
    if not chat:
        return "Cần tham số chat=(username hoặc id của nhóm, channel)"
    if not url:
        return "Cần tham số url=(Liên kết video/âm thanh để phát trực tiếp)"
    return Response(executor(chat, url), content_type="text/plain")