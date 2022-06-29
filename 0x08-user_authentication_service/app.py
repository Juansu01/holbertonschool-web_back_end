#!/usr/bin/env python3
"""
This module defines the routes for our API.
"""


from flask import Flask, jsonify, request, abort
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=["GET"])
def welcome_message() -> str:
    """
    First route for API.
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def register_user() -> str:
    """
    This function registers a new user to the DB.
    """

    try:
        email = request.form.get("email")
        pws = request.form.get("password")
        AUTH.register_user(email, pws)

        return jsonify({"email": email, "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """
    API login endpoint.
    """

    try:
        email, pws = request.form["email"], request.form["password"]
    except KeyError:
        abort(400)

    if AUTH.valid_login(email, pws):
        sess_id = AUTH.create_session(email)
        res = jsonify({
            "email": email,
            "message": "logged in"
        })
        res.set_cookie("session_id", sess_id)
        return res

    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
