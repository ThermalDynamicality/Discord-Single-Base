"""
File: misc.py
Author: Stanley Goodwin
Last Updated: 4/11/2022

Description:
    A library for random shit that can be used as system interface.

Known Issues: N/A

To Do: N/A
"""
from error_handling import log_error
from json import loads, dumps
from os import listdir


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


def list_directory(folder_directory: str) -> list:
    """
    Lists the files/folders in the directory specified and returns the list.

    :param folder_directory: The directory to be listed.
    :return list: List of files in the directory.
    """
    try:
        return listdir(folder_directory)
    except Exception as error:
        log_error(__name__, error, folder_directory)
        return []
