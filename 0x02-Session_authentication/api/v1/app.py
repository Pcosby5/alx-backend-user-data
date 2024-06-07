#!/usr/bin/env python3
"""
API entry point
"""
from flask import Flask, jsonify, abort, request
from os import getenv
from api.v1.views import app_views
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth
from api.v1.auth.session_auth import SessionAuth
import os

app = Flask(__name__)
app.register_blueprint(app_views)

auth = None
if os.getenv("AUTH_TYPE") == "session_auth":
    auth = SessionAuth()
else:
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()


@app.before_request
def before_request():
    """Before request handler"""
    if auth:
        excluded_paths = [
            "/api/v1/status/",
            "/api/v1/unauthorized/",
            "/api/v1/forbidden/",
            "/api/v1/auth_session/login/"
        ]
        if not auth.require_auth(request.path, excluded_paths):
            return

        if (auth.authorization_header(request) is None and
                auth.session_cookie(request) is None):
            abort(401)

        request.current_user = auth.current_user(request)


@app.errorhandler(404)
def not_found(error) -> str:
    """Handler for 404 errors"""
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """Handler for 401 errors"""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """Handler for 403 errors"""
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
