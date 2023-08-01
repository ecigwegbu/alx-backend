#!/usr/bin/env python3
"""3. Parameterize templates - outputs Hello World."""
from flask import Flask, render_template, request
from flask_babel import Babel, _
from datetime import datetime, date, time, timedelta
import typing
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
def get_locale() -> typing.Any:
    """Get the best match locale for the user
    Uses the info in the request header and the config"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def parameterize_template() -> typing.Any:
    """Basic Basic Babel Flask app"""
    home_title = 'Welcome to Holberton'
    home_header = 'Hello World'

    return render_template('3-index.html',
                           home_title=_("%(home_title)s",
                                        home_title=home_title),
                           home_header=_("%(home_header)s",
                                         home_header=home_header))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
