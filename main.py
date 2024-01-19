from flask import Flask, request, Response
import subprocess

web = Flask("__telestream__")

def executor(chat, url):
    process = subprocess.Popen(["python3", "-u", "client.py", f"{chat}", f"{url}"], stdout=subprocess.PIPE, universal_newlines=True)
    for line in process.stdout:
        yield line + "\n"
    process.wait()

@web.route("/")
def telestream__():
    chat = request.args.get("chat")
    url = request.args.get("url")
    return Response(executor(chat, url), content_type="text/plain")