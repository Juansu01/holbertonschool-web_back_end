#!/usr/bin/env python3
"""
This module defines the routes for our API.
"""

from flask import Flask, jsonify

app = Flask()


@app.route('/', methods=["GET"])
def welcome_message() -> str:
    """
    First route for API.
    """

    return jsonify({"message": "Bienvenue"})
