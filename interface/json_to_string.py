"""
File: json_to_string.py \n
Author: Stanley Goodwin \n
Last Updated: 6/12/2022
"""
import logging
from json import dumps


def json_to_string(json_dictionary: dict) -> str:
    """
    Converts a JSON dictionary to a string and returns the string.

    :param json_dictionary: The input dictionary to convert to a string.
    :return: dictionary_string – The string of the dictionary.
    """
    try:
        dictionary_string = dumps(json_dictionary)
        logging.info(f"{__name__}: Converted JSON to String")
        return dictionary_string
    except Exception as error:
        logging.error(f"{__name__}: {error}")
        return ""  # Returns an empty string on exception
