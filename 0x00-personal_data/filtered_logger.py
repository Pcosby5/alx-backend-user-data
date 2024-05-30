#!/usr/bin/env python3
"""
This module contains a function to obfuscate specified fields in log messages.
"""

import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """
    Returns the log message with specified fields obfuscated.

    Args:
        fields (List[str]): List of field names to obfuscate.
        redaction (str): String to replace the field values with.
        message (str): The log message to be processed.
        separator (str): Character that separates
        the fields in the log message.

    Returns:
        str: The log message with specified fields obfuscated.
    """
    pattern = '|'.join([f"{field}=[^{separator}]*" for field in fields])
    return re.sub(pattern,
                  lambda m: f"{m.group(0).split('=')[0]}={redaction}", message)
