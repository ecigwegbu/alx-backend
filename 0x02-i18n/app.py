#!/usr/bin/env python3
"""8. Display The Current Time in The user's Locale -outputs Hello World."""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from datetime import datetime
from typing import Dict, Optional, Union, Any
from pytz import timezone
import pytz


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


users: Dict = {
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
    if g.user:
        for user_id, user in users.items():
            if user["name"] == g.user:
                locale = user["locale"]
                break
        if locale in app.config["LANGUAGES"]:
            return locale
    if request.headers.get('Accept-Language') and \
            str(request.headers.get('Accept-Language'))[:1] in \
            app.config["LANGUAGES"]:
        return str(request.headers.get('Accept-Language'))[:1]
    return app.config["BABEL_DEFAULT_LOCALE"]


@babel.timezoneselector
def get_timezone() -> str:
    """get time zone for user locale"""
    tzone = request.args.get('timezone')
    if tzone is not None and is_valid_timezone(tzone):
        return tzone
    if g.user:
        for user_id, user in users.items():
            if user["name"] == g.user:
                tzone = user["timezone"]
                break
        if tzone and is_valid_timezone(tzone):
            return tzone
    return "UTC"


def is_valid_timezone(tzone: str) -> bool:
    """validate a timezone string"""
    try:
        pytz.timezone(tzone)
        return True
    except pytz.exceptions.UnknownTimeZoneError:
        return False


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

    tzone = timezone(str(get_timezone()))  # local timezone object

    utc_now = datetime.utcnow()
    curr_time = utc_now.astimezone(tzone).strftime("%c")
    current_time_display = _("The current time is %(current_time)s.",
                             current_time=curr_time)
    return render_template("index.html", home_title=home_title,
                           home_header=home_header,
                           status_message=status_message,
                           current_time=current_time_display)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
