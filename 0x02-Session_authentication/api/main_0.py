#!/usr/bin/env python3
""" Main 0
"""
import sys
import os

# Ensure the parent directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import base64
from api.v1.auth.basic_auth import BasicAuth
from models.user import User
from api.v1.auth.session_auth import SessionAuth

sa = SessionAuth()

print("{}: {}".format(type(sa.user_id_by_session_id), sa.user_id_by_session_id))

user_id = None
session = sa.create_session(user_id)
print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))

user_id = 89
session = sa.create_session(user_id)
print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))

user_id = "abcde"
session = sa.create_session(user_id)
print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))

user_id = "fghij"
session = sa.create_session(user_id)
print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))

user_id = "abcde"
session = sa.create_session(user_id)
print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))


# """ Create a user test """
# user_email = "bob@hbtn.io"
# user_clear_pwd = "H0lbertonSchool98!"

# user = User()
# user.email = user_email
# user.password = user_clear_pwd
# print("New user: {}".format(user.id))
# user.save()

# basic_clear = "{}:{}".format(user_email, user_clear_pwd)
# print("Basic Base64: {}".format(base64.b64encode(basic_clear.encode('utf-8')).decode("utf-8")))

