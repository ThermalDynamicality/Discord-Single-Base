"""
File: string_to_json.py \n
Author: Stanley Goodwin \n
Description: Converts a string into a JSON dictionary and returns the dictionary.
"""
import logging
from json import loads


def string_to_json(json_string: str) -> dict:
    """
    :param json_string: The string to convert to dictionary.
    :return: string_dictionary – The dictionary of the string.
    """
    try:
        string_dictionary = loads(json_string)
        logging.debug(f"{__name__}: Converted String to JSON")
        return string_dictionary
    except Exception as error:
        logging.error(f"{__name__}: {error}")
        return {}  # Returns an empty dictionary on exception
