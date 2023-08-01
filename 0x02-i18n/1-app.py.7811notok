#!/usr/bin/env python3
"""0. Basic Flask app. Outputs Hello World."""
from flask import Flask, render_template
from flask_babel import Babel
from datetime import datetime, date, time, timedelta
from config import Config
# import requests
# from os import getenv


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def basic_babel_setup():
    """Basic Hello World Flask app"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
