#!/usr/bin/env python3
"""0. Basic Flask app. Outputs Hello World."""
from flask import Flask, render_template
from datetime import datetime, date, time, timedelta
# import requests
# from os import getenv


app = Flask(__name__)


@app.route("/")
def basic_flask_app():
    """Basic Hello World Flask app"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
