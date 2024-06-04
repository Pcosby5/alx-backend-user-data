#!/usr/bin/env python3
"""
BasicAuth class that inherits from Auth
"""

import base64
from api.v1.auth.auth import Auth
from typing import TypeVar, List
from models.user import User


class BasicAuth(Auth):
    """ BasicAuth class for basic authentication """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extracts the Base64 part of the
        Authorization header for Basic Authentication.

        Args:
            authorization_header (str): The Authorization header.

        Returns:
            str: The Base64 part of the
            Authorization header, or None if invalid.
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        # Split the string after "Basic " and return the second part
        return authorization_header.split(" ", 1)[1]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """
        Decodes the Base64 string.

        Args:
            base64_authorization_header (str): The Base64 string.

        Returns:
            str: The decoded value as a UTF-8 string, or None if invalid.
        """
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """
        Extracts user email and password from Base64 decoded value.

        Args:
            decoded_base64_authorization_header
            (str): The Base64 decoded value.

        Returns:
            (str, str): The user
            email and password, or (None, None) if invalid.
        """
        if decoded_base64_authorization_header is None or not isinstance(
            decoded_base64_authorization_header, str
        ):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar('User'):
        """
        Returns the User instance based on his email and password.

        Args:
            user_email (str): The user's email.
            user_pwd (str): The user's password.

        Returns:
            User: The User instance if credentials are correct, None otherwise.
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        # Search for the user by email
        user_list = User.search({'email': user_email})
        if not user_list:
            return None

        user = user_list[0]
        if not user.is_valid_password(user_pwd):
            return None

        return user
