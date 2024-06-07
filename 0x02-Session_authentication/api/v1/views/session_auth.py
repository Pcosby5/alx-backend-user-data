#!/usr/bin/env python3
"""
Session authentication views
"""
from flask import jsonify, request, abort
from models.user import User
from api.v1.views import app_views
from api.v1.auth.session_auth import SessionAuth


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """
    Handles user login and creates a session
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or email == "":
        return jsonify({"error": "email missing"}), 400

    if not password or password == "":
        return jsonify({"error": "password missing"}), 400

    try:
        user = User.search({"email": email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    user = user[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_auth = SessionAuth()
    session_id = session_auth.create_session(user.id)
    response = jsonify(user.to_dict())
    response.set_cookie("_my_session_id", session_id)
    return response
