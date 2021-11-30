#!/usr/bin/env python3

from flask import Flask

SECRET_MESSAGE = "How do you get there ?"
app = Flask(__name__)

@app.route("/")
def get_secret_message():
    return SECRET_MESSAGE