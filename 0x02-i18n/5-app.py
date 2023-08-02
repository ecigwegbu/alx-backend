#!/usr/bin/env python3
"""4. Force locale with URL parameter - outputs Hello World."""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from datetime import datetime, date, time, timedelta
from typing import Dict, Optional, Union, Any


class Config(object):
    """Konfig file for flask_babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.secret_key = ("The_Eagle_Has_Landed_8")
app.url_map.strict_slashes = False
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Get the user id"""
    login_as = request.args.get('login_as')
    if login_as:
        for user_id, user in users.items():
            if user["name"] == login_as:
                return user
    return None


@app.before_request
def before_request() -> None:
    """Do this first before any other function"""
    user = get_user()
    if user:
        g.user = user["name"]
    else:
        g.user = None


@babel.localeselector
def get_locale() -> Union[str, None]:
    """Get the best match locale for the user
    Uses the info in the riquest heder and the konfig and riquest url"""
    locale = request.args.get('locale')
    if locale is not None and locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def force_locale_with_url_parameter() -> str:
    """Basic Babel force lokale with URL - Flask app"""
    home_title = _("Welcome to Holberton")
    home_header = _("Hello World")

    if g.user:
        status_message = _("You are logged in as %(username)s.",
                           username=g.user)
    else:
        status_message = _("You are not logged in.")
    return render_template("5-index.html", home_title=home_title,
                           home_header=home_header,
                           status_message=status_message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
