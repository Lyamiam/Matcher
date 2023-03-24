#!/bin/python

from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/")
def titleScreen():
    return render_template("titleScreen.html")

@app.route("/", methods=["POST"])
def loggedInTitleScreen():
    return render_template("titleScreen.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
