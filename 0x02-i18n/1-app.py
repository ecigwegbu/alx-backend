#!/usr/bin/env python3
"""0. Basic Flask app. Outputs Hello World."""
from flask import Flask, render_template
from flask_babel import Babel
from datetime import datetime, date, time, timedelta
# import requests
# from os import getenv


babel = Babel()


class Config(object):
    """Config file for flask_babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = ["en"]
    BABEL_DEFAULT_TIMEZONE = ["UTC"]


def create_app(config_class=Config):
    """craete app object for the application"""
    app = Flask(__name__)
    app.config.from_object(config_class)

    babel.init_app(app)

    return app


app = create_app()


@app.route("/")
def basic_babel_setup():
    """Basic Babel Flask app"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
