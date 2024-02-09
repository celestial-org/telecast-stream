from flask import Flask

app = Flask("__telestream__")

@app.route("/")
def telestream__():
    return "OK"