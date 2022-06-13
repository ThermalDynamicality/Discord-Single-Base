"""
File: list_directory.py \n
Author: Stanley Goodwin \n
Last Updated: 6/12/2022
"""
import logging
from os import listdir


def list_directory(folder_directory: str) -> list:
    """
    Lists the files and folders in the directory specified and returns the list.

    :param folder_directory: The directory to be listed.
    :return: file_list – List of files in the directory.
    """
    try:
        file_list = listdir(folder_directory)
        logging.info(f"{__name__}: Created list of files in \"{folder_directory}\"")
        return file_list
    except Exception as error:
        logging.error(f"{__name__}: {error}")
        return []  # Returns empty list on exception
