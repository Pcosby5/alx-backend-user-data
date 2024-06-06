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
from flask import Flask, request
from api.v1.auth.auth import Auth

auth = Auth()

app = Flask(__name__)

@app.route('/', methods=['GET'], strict_slashes=False)
def root_path():
    """ Root path
    """
    return "Cookie value: {}\n".format(auth.session_cookie(request))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

# sa = SessionAuth()

# user_id_1 = "abcde"
# session_1 = sa.create_session(user_id_1)
# print("{} => {}: {}".format(user_id_1, session_1, sa.user_id_by_session_id))

# user_id_2 = "fghij"
# session_2 = sa.create_session(user_id_2)
# print("{} => {}: {}".format(user_id_2, session_2, sa.user_id_by_session_id))

# print("---")

# tmp_session_id = None
# tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
# print("{} => {}".format(tmp_session_id, tmp_user_id))

# tmp_session_id = 89
# tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
# print("{} => {}".format(tmp_session_id, tmp_user_id))

# tmp_session_id = "doesntexist"
# tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
# print("{} => {}".format(tmp_session_id, tmp_user_id))

# print("---")

# tmp_session_id = session_1
# tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
# print("{} => {}".format(tmp_session_id, tmp_user_id))

# tmp_session_id = session_2
# tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
# print("{} => {}".format(tmp_session_id, tmp_user_id))

# print("---")

# session_1_bis = sa.create_session(user_id_1)
# print("{} => {}: {}".format(user_id_1, session_1_bis, sa.user_id_by_session_id))

# tmp_user_id = sa.user_id_for_session_id(session_1_bis)
# print("{} => {}".format(session_1_bis, tmp_user_id))

# tmp_user_id = sa.user_id_for_session_id(session_1)
# print("{} => {}".format(session_1, tmp_user_id))


# print("{}: {}".format(type(sa.user_id_by_session_id), sa.user_id_by_session_id))

# user_id = None
# session = sa.create_session(user_id)
# print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))

# user_id = 89
# session = sa.create_session(user_id)
# print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))

# user_id = "abcde"
# session = sa.create_session(user_id)
# print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))

# user_id = "fghij"
# session = sa.create_session(user_id)
# print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))

# user_id = "abcde"
# session = sa.create_session(user_id)
# print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))


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

