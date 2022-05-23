"""
File: list_directory.py
Author: Stanley Goodwin
Last Updated: 5/22/2022

Description:
    A function for converting json to a string.

Known Issues: N/A

To Do: N/A
"""
from error_handling import log_error
from json import dumps


def json_to_string(json_dictionary: dict) -> str:
    """
    Converts a JSON dictionary to a single-line string and returns the string.

    :param json_dictionary: The input dictionary.
    :return string: String of dictionary.
    """
    try:
        return dumps(json_dictionary)
    except Exception as error:
        log_error(__name__, error, json_dictionary)
        return ""
