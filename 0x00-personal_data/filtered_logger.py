#!/usr/bin/env python3
"""
filter_datum function that returns an obfuscated log message
"""
from typing import List
import re


def filter_datum(fields_to_obfuscate: List[str], obfuscation_string: str,
                 log_message: str, field_separator: str) -> str:
    """
    Returns an obfuscated log message.

    Args:
        fields_to_obfuscate (list): List of strings to obfuscate.
        obfuscation_string (str): String to which the field will be obfuscated.
        log_message (str): The log line to obfuscate.
        field_separator (str): The character separating the fields.
    """
    for field in fields_to_obfuscate:
        log = re.sub(
            field + '=.*?' + field_separator,
            field + '=' + obfuscation_string + field_separator,
            log_message
        )
    return log
