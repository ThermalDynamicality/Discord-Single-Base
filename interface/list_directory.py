"""
File: list_directory.py \n
Author: Stanley Goodwin \n
Last Updated: 5/22/2022

Description:
A function for listing the files in a given directory.

Known Issues: N/A

To Do: N/A
"""
from error_handling import log_error
from os import listdir


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
