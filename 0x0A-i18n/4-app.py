#!/usr/bin/env python3
"""
Module for i18n project.
"""

from flask import Flask, render_template, request
from flask_babel import Babel

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


@app.route('/', methods=['GET'], strict_slashes=False)
def home() -> str:
    """
    Home route rendering simple html.
    """
    return render_template("4-index.html")


@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match with our supported languages
    """

    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == "__main__":
    app.run()
