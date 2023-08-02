#!/usr/bin/env python3
"""3. Parameterize templates - outputs Hello World.
This module parametises the title and header to different
locales"""
from flask import Flask, render_template, request
from flask_babel import Babel, _
from datetime import datetime, date, time, timedelta
from typing import Dict, Any, Union


class Config(object):
    """Config file for flask_babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.secret_key = ("The_Eagle_Has_Landed_8")
app.url_map.strict_slashes = False
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> Union[str, None]:
    """Get the best match locale for the user
    Uses the info in the request header and the config. If locale not
    found then return None"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def parameterize_template() -> str:
    """Basic Basic Babel Flask app. Returns the index page containing
    The title and header translated to the locale of choice"""
    home_title = _("Welcome to Holberton")
    home_header = _("Hello world!")
    return render_template("3-index.html", home_title=home_title,
                           home_header=home_header)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
