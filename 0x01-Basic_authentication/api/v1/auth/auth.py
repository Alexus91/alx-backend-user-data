#!/usr/bin/env python3
"""  Auth class """
from flask import request
from typing import List, TypeVar


class Auth:
    """  manage the API authentication """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Method for validating if endpoint requires authentication.
        Args:
        - path (str): The endpoint path to check.
        - excluded_paths (List[str]): List of paths exempted from authen.
        Returns:
        - bool: True if authentication is required, False otherwise.
        """
        if not path or not excluded_paths:
            return True

        if path in excluded_paths:
            return False

        for exc in excluded_paths:
            if exc.endswith('*') and path.startswith(exc[:-1]):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Method that handles extraction of authorization header from request.
        Args:
        - request (flask.Request): The Flask request object. Default is None.
        Returns:
        - str: The authorization header if found, otherwise None.
        """
        if request is None:
            return None

        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method that validates the current user based on the request.

        Args:
        - request (flask.Request): The Flask request object. Default is None.

        Returns:
        - TypeVar('User'): The current user if authenticated, otherwise None.
        """
        return None
