"""
File: json_to_string.py \n
Author: Stanley Goodwin \n
Description: Converts a JSON dictionary to a string and returns the string.
"""
import logging
from json import dumps


def json_to_string(json_dictionary: dict) -> str:
    """
    :param json_dictionary: The dictionary to convert to string.
    :return: dictionary_string – The string of the dictionary.
    """
    try:
        dictionary_string = dumps(json_dictionary)
        logging.debug(f"{__name__}: Converted JSON to String")
        return dictionary_string
    except Exception as error:
        logging.error(f"{__name__}: {error}")
        return ""  # Returns an empty string on exception
