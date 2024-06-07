#!/usr/bin/env python3
"""
Auth class
"""

from flask import request
from typing import List, TypeVar
import os

# Define a type variable for user type
User = TypeVar('User')


class Auth:
    """
    Auth class to manage API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required

        Args:
            path (str): The path to check
            excluded_paths (List[str]): A list of
            paths that do not require authentication

        Returns:
            bool: True if authentication is required, False otherwise
        """
        if path is None or not excluded_paths:
            return True

        if path[-1] != '/':
            path = path + '/'

        for excl_path in excluded_paths:
            if excl_path.endswith('*'):
                if path.startswith(excl_path[:-1]):
                    return False
            elif excl_path == path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from the request

        Args:
            request (flask.Request, optional): The Flask
            request object. Defaults to None.

        Returns:
            str: The authorization header value, or None if not present
        """
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None):
        """
        Retrieves the current user from the request

        Args:
            request (flask.Request, optional): The Flask
            request object. Defaults to None.

        Returns:
            User: None, indicating no user is retrieved
        """
        if request is None:
            return None

        session_id = self.session_cookie(request)
        if not session_id:
            return None

        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return None

        try:
            from models.user import User
            user = User.get(user_id)
        except Exception:
            return None

        return user

    def session_cookie(self, request=None):
        """Return a cookie value from a request"""
        if request is None:
            return None
        session_name = os.getenv('SESSION_NAME', '_my_session_id')
        return request.cookies.get(session_name)
