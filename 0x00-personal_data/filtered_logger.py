#!/usr/bin/env python3
"""
Definition of filter_datum function that returns an obfuscated log message
"""
import re
from typing import List
import logging


PII_FIELDS = ("name", "email", "phone", "ssn", "credit_card")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Return an obfuscated log message
    Args:
        fields (list): list of strings indicating fields to obfuscate
        redaction (str): what the field will be obfuscated to
        message (str): the log line to obfuscate
        separator (str): the character separating the fields
    """
    for field in fields:
        message = re.sub(field+'=.*?'+separator,
                         field+'='+redaction+separator, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the RedactingFormatter with a
        list of fields to redact.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Filter values in incoming log records using filter_datum.
        Values for fields in fields should be filtered.
        """
        msg = super(RedactingFormatter, self).format(record)
        redacted = filter_datum(self.fields, self.REDACTION,
                                msg, self.SEPARATOR)
        return redacted


def get_logger() -> logging.Logger:
    """
    Returns a logging.Logger object named "user_data" configured as specified.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler()
    logger.propagate = False
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(stream_handler)
    return logger
