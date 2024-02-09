#!/usr/bin/env python3
"""
Module for encrypting passwords.
"""
import bcrypt
from bcrypt import hashpw


def hash_password(password: str) -> bytes:
    """
    Hashes the provided password using bcrypt
    """
    b = password.encode()
    h = hashpw(b, bcrypt.gensalt())
    return h
