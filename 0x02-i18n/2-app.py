#!/usr/bin/env python3
"""2. Get locale from request - Outputs Hello World."""
from flask import Flask, render_template, request
from flask_babel import Babel
from datetime import datetime, date, time, timedelta
# import requests
# from os import getenv


class Config(object):
    """Config file for flask_babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get the best match locale for the user
    Uses the info in the request header and the config"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def get_locale_from_request():
    """Basic Basic Babel Flask app"""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
