"""
File: read.py \n
Author: Stanley Goodwin \n
Description: Reads the file of the directory given and returns the contents of the file.
"""
import logging
from random import choice
from json import load


def read(directory: str, *,
         read_as_json: bool = False,
         line_number: int = None,
         choose_random: bool = False,
         ) -> list | dict | str | None:
    """
    :param directory: The directory of the file.

    :param read_as_json: [Optional]
        Whether to read the file like JSON (default False).
    :param line_number: [Optional]
        The line of the text being read from the file.
    :param choose_random: [Optional]
        Chooses a random line from the file (default False).

    :return: file_contents – The contents of the file (after modification).
    """
    try:
        # Open file and read contents
        with open(directory, "r", encoding="utf8") as file:
            if read_as_json:
                _output = load(file)
            else:
                _output = file.read().splitlines()
            logging.debug(f"{__name__}: Read data from [File \"{directory}\"]")

        # If a line number is specified, return the line at that line number
        if isinstance(line_number, int) and line_number is not None:
            _output = _output[line_number]

        # If line is chosen at random, return a random line
        if choose_random:
            _output = choice(_output)
            logging.debug(f"{__name__}: Chose random line from file")

        # If nothing is done to the file, return entire file data
        return _output

    except Exception as error:
        logging.error(f"{__name__}: {error}")
        return None
