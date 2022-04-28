"""
File: systemIO.py
Author: Stanley Goodwin
Last Updated: 4/11/2022

Description:
    A library for reading, writing, and appending text to files in the system.

Known Issues: N/A

To Do: N/A
"""
from error_handling import log_error
from random import choice
from json import load, dumps


def read(directory: str, *,
         read_as_json: bool = False,
         line_number: int = None,
         choose_random: bool = False,
         ) -> list | dict | str | None:
    """
    Reads the file of the directory given and returns the contents of the file.

    # Positional Arguments
    :param directory: The directory of the file.

    # Keyword Arguments
    :param read_as_json: Whether to read the file like JSON.
    :param line_number: The line of the text being read from the file.
    :param choose_random: Chooses a random line from the file.

    # Return
    :return contents: The contents of the file (after modification).
    """
    try:
        # Open file and read
        with open(directory, "r", encoding="utf8") as file:
            if read_as_json:
                _output = load(file)
            else:
                _output = file.read().splitlines()

        # If line number is not none, return the line
        if line_number is not None:
            return _output[line_number]

        # If choosing random, return random line
        if choose_random:
            return choice(_output)

    except Exception as error:
        log_error(__name__, error, directory, read_as_json, line_number, choose_random)
        return None


def write(directory: str,
          input_data: str | dict,
          *,
          overwrite_file: bool = False
          ) -> None:
    """
    Writes text to a directory (append / overwrite).

    # Positional Arguments
    :param directory: The directory of the file.
    :param input_data: The data to store.

    # Keyword Arguments
    :param overwrite_file: Whether to overwrite the file.

    # Return
    :return None:
    """
    try:
        # Converts json data into plain-text
        if isinstance(input_data, dict):
            input_data = dumps(input_data)

        # Opens file in append or write mode and writes to file
        method = "w" if overwrite_file else "a+"
        with open(directory, method, encoding="utf8") as file:
            file.write(input_data)

    except Exception as error:
        log_error(__name__, error, directory, input_data)
