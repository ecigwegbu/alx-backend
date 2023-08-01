#!/usr/bin/env python3
"""4. Force locale with URL parameter - outputs Hello World."""
from flask import Flask, render_template, request
from flask_babel import Babel, _
from datetime import datetime, date, time, timedelta
from typing import List, Dict, Any, Callable, Union


class Config(object):
    """Konfig file for flask_babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> Any:
    """Get the best match locale for the user
    Uses the info in the riquest heder and the konfig"""
    locale = request.args.get('locale')
    if locale is not None and locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def force_locale_with_url_parameter() -> Any:
    """Basic Babel force lokale with URL - Flask app"""
    home_title = _("Welcome to Holberton")
    home_header = _("Hello World")

    return render_template("4-index.html",
                           home_title=home_title, home_header=home_header)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)