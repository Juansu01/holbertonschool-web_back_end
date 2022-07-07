#!/usr/bin/env python3
"""
Module for i18n project.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def home() -> str:
    """
    Home route rendering simple html.
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
