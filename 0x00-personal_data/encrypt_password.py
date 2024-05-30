#!/usr/bin/env python3
"""
Module for password encryption using bcrypt.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt with a randomly generated salt.

    Args:
        password (str): The password to be hashed.

    Returns:
        bytes: The salted, hashed password.
    """
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password with the generated salt
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed
