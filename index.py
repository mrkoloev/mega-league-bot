from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    return "<h2>Flask!!!!!</h2>"

@app.route("/mega")
def mega():
    return "<h2>mega</h2>"
