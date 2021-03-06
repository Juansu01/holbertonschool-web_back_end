#!/usr/bin/env python3
"""
This module defines the routes for our API.
"""

from flask import Flask, jsonify, request, abort
from auth import Auth
from flask import redirect

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


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """
    API logout endpoint.
    """

    session_id = request.cookies.get("session_id")

    if session_id:
        user = AUTH.get_user_from_session_id(session_id=session_id)

        if user:
            AUTH.destroy_session(user.id)
        else:
            abort(403)
    else:
        abort(403)

    return redirect('/')


@app.route('/profile', methods=['GET'], strict_slashes=False)
def user_profile() -> str:
    """
    Responds with 200 status if user exists.
    """

    session_id = request.cookies.get("session_id")

    if session_id:
        user = AUTH.get_user_from_session_id(session_id=session_id)

        if user:
            return jsonify({"email": user.email}), 200
        else:
            abort(403)
    else:
        abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def reset_password() -> str:
    """
    Generates a token for a password
    reset if account is found.
    """
    email = request.form.get("email")
    try:

        reset_token = AUTH.get_reset_password_token(email)
        my_dict = {"email": email, "reset_token": reset_token}
        return jsonify(my_dict), 200
    except Exception:
        abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password() -> str:
    """
    This API route updates password if data from
    request body is correct.
    """

    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")

    try:
        AUTH.update_password(reset_token, new_password)
    except ValueError:
        abort(403)

    my_dict = {"email": email, "message": "Password updated"}

    return jsonify(my_dict), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
