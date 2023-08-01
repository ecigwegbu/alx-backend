#!/usr/bin/env python3
""" Config file for my flask app """


class Config(object):
    """Config file for flask_babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = ["en"]
    BABEL_DEFAULT_TIMEZONE = ["UTC"]
