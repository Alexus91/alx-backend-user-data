#!/usr/bin/env python3
"""Module for authentication.
"""


import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from uuid import uuid4
from user import User


def _hash_password(password: str) -> bytes:
    """
    Hashes a password and returns bytes.
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generates a uuid """
    return str(uuid4())


class Auth:
    """
    the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a new user with the given email and password
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            pass
        hashed_pass = _hash_password(password)
        user = self._db.add_user(email, hashed_pass)
        return user

    def valid_login(self, email: str, password: str) -> bool:
        """Checks if a user's email and password are valid."""
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                password_bytes = password.encode('utf-8')
                hashed_password = user.hashed_password
                if bcrypt.checkpw(password_bytes, hashed_password):
                    return True
        except NoResultFound:
            return False
        return False

    def create_session(self, email: str) -> str:
        """
        Creates a session and returns the session ID as a string.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        if user is None:
            return None
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id
