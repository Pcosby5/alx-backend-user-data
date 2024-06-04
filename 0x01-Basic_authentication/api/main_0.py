#!/usr/bin/env python3
""" Main 0
"""
import sys
import os

# Ensure the parent directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api.v1.auth.basic_auth import BasicAuth

a = BasicAuth()

print(a.extract_user_credentials(None))
print(a.extract_user_credentials(89))
print(a.extract_user_credentials("Holberton School"))
print(a.extract_user_credentials("Holberton:School"))
print(a.extract_user_credentials("bob@gmail.com:toto1234"))

# print(a.decode_base64_authorization_header(None))
# print(a.decode_base64_authorization_header(89))
# print(a.decode_base64_authorization_header("Holberton School"))
# print(a.decode_base64_authorization_header("SG9sYmVydG9u"))
# print(a.decode_base64_authorization_header("SG9sYmVydG9uIFNjaG9vbA=="))
# print(a.decode_base64_authorization_header(a.extract_base64_authorization_header("Basic SG9sYmVydG9uIFNjaG9vbA==")))


# print(a.extract_base64_authorization_header(None))
# print(a.extract_base64_authorization_header(89))
# print(a.extract_base64_authorization_header("Holberton School"))
# print(a.extract_base64_authorization_header("Basic Holberton"))
# print(a.extract_base64_authorization_header("Basic SG9sYmVydG9u"))
# print(a.extract_base64_authorization_header("Basic SG9sYmVydG9uIFNjaG9vbA=="))
# print(a.extract_base64_authorization_header("Basic1234"))

# from api.v1.auth.auth import Auth

# a = Auth()

# print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))
# print(a.authorization_header())
# print(a.current_user())


# print(a.require_auth(None, None))
# print(a.require_auth(None, []))
# print(a.require_auth("/api/v1/status/", []))
# print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))
# print(a.require_auth("/api/v1/status", ["/api/v1/status/"]))
# print(a.require_auth("/api/v1/users", ["/api/v1/status/"]))
# print(a.require_auth("/api/v1/users", ["/api/v1/status/", "/api/v1/stats"]))
