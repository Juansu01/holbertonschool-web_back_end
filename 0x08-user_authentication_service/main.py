#!/usr/bin/env python3
"""
Main for advanced task
"""

import requests

EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"
URL = "http://localhost:5000"


def create_data(email: str = None,
                password: str = None,
                new_pass: str = None) -> dict:
    """
    This method creates a dictionary with the
    data that was requested.
    """
    data = {}

    if email:
        data["email"] = email
    if password:
        data["password"] = password
    if new_pass:
        data["new_password"] = new_pass

    return data


def register_user(email: str, password: str) -> None:
    """
    Test method for user registration
    """

    data = create_data(email, password)
    print(data)
    res = requests.post(f"{URL}/users", data=data)
    expected = {"email": email, "message": "user created"}

    assert res.status_code == 200 and res.json() == expected


def log_in_wrong_password(email: str, password: str) -> None:
    """
    Testing wrong password case.
    """
    data = create_data(email, password)

    res = requests.post(f"{URL}/sessions", data=data)

    assert res.status_code == 401


def log_in(email: str, password: str) -> str:
    """
    Testing successful login case.
    """
    data = create_data(email, password)
    res = requests.post(f'{URL}/sessions', data=data)
    expected = {
        "email": email,
        "message": "logged in"
    }

    sess_id = res.cookies.get("session_id")

    assert res.status_code == 200
    assert expected == res.json()

    return sess_id


def profile_unlogged() -> None:
    """
    Testing valitation for profile request without
    logging in.
    """
    res = requests.get(f"{URL}/profile", cookies={"session_id": ""})
    assert res.status_code == 403


def profile_logged(session_id: str) -> None:
    """
    Testing valitation for profile request
    when logged in.
    """

    res = requests.get(f"{URL}/profile", cookies={"session_id": session_id})

    expected = {"email": EMAIL}

    assert res.status_code == 200 and expected == res.json()


def log_out(session_id: str) -> str:
    """
    Testing logout endpoint.
    """

    res = requests.delete(f'{URL}/sessions',
                          cookies={"session_id": session_id})

    assert res.status_code == 200
    assert {"message": "Bienvenue"} == res.json()


def reset_password_token(email: str) -> str:
    """
    Validating password reset_token.
    """

    data = create_data(email)

    res = requests.post(f"{URL}/reset_password", data=data)
    reset_token = res.json().get("reset_token")

    expected = {
        "email": email,
        "reset_token": reset_token
    }

    assert res.status_code == 200 and res.json() == expected

    return reset_token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """
    Test for password reset.
    """

    data = {
        "email": email,
        "new_password": new_password,
        "reset_token": reset_token
    }

    res = requests.put(f"{URL}/reset_password", data=data)

    expected = {
        "email": email,
        "message": "Password updated"
    }

    assert res.json() == expected and res.status_code == 200


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
