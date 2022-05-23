"""
File: list_directory.py \n
Author: Stanley Goodwin \n
Last Updated: 5/22/2022

Description:
A function for converting string to a json dictionary.

Known Issues: N/A

To Do: N/A
"""
from error_handling import log_error
from json import loads


def string_to_json(json_string: str) -> dict:
    """
    Converts a string of JSON into a JSON dictionary and returns the dictionary.

    :param json_string: The input string.
    :return dictionary: The dictionary of the string.
    """
    try:
        return loads(json_string)
    except Exception as error:
        log_error(__name__, error, json_string)
        return {}
