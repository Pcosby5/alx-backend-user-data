from flask import request
from typing import List, TypeVar

# Define a type variable for user type
User = TypeVar('User')


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determines if authentication is required """
        return False

    def authorization_header(self, request=None) -> str:
        """ Retrieves the authorization header """
        return None

    def current_user(self, request=None) -> User:
        """ Retrieves the current user """
        return None
