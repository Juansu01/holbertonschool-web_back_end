#!/usr/bin/env python3
"""
Module for i18n project.
"""


from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
from typing import Union
import pytz
from datetime import datetime

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Configuration for Babel.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.timezoneselector
def get_timezone() -> str:
    """
    Gets timezone using the following steps:
    - Find timezone parameter in URL parameters
    - Find time zone from user settings
    - Default to UTC
    """

    try:

        if request.args.get("timezone"):
            timezone = request.args.get("timezone")
            timezone_py = pytz.timezone(timezone)
        elif g.user and g.user.get("timezone"):
            timezone = g.user.get("timezone")
            timezone_py = pytz.timezone(timezone)
        else:
            timezone = app.config["BABEL_DEFAULT_TIMEZONE"]
            timezone_py = pytz.timezone(timezone)
    except pytz.exceptions.UnknownTimeZoneError:
        timezone = "UTC"

    return timezone


def get_user() -> Union[dict, None]:
    """
    Gets user by id and returns user if found.
    """

    try:
        user_id = request.args.get("login_as")
        user = users[int(user_id)]
    except Exception:
        user = None

    return user


@app.before_request
def before_request():
    """
    Gets user before every request.
    """
    user = get_user()
    g.user = user


@app.route('/', methods=['GET'], strict_slashes=False)
def home() -> str:
    """
    Home route rendering simple html.
    """
    timezone = get_timezone()
    pytz_object = pytz.timezone(timezone)
    current_time = format_datetime(datetime=datetime.now(pytz_object))
    return render_template("index.html", current_time=current_time)


@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match with our supported languages
    """

    locale = request.args.get("locale")

    if locale and locale in app.config['LANGUAGES']:
        return locale

    if g.user:
        locale = g.user.get("locale")
        if locale and locale in app.config['LANGUAGES']:
            return locale

    locale = request.headers.get('locale')

    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
