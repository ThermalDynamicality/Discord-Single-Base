"""
File: write.py \n
Author: Stanley Goodwin \n
Last Updated: 6/12/2022
"""
import logging
from json import dumps
# TODO Info on execution


def write(directory: str,
          input_data: str | dict,
          *,
          overwrite: bool = False
          ) -> None:
    """
    Writes the input data to a given directory with option for replacing or appending text.

    :param directory: The directory of the file to write to.
    :param input_data: The data to store to the file.
    :param overwrite: Whether the text should overwrite the file.
    :return: None
    """
    try:
        # Converts json data into plain-text for storage
        if isinstance(input_data, dict):
            input_data = dumps(input_data)
            logging.info(f"{__name__}: Converted JSON data to String")

        # Determines whether overwriting or appending to the file
        method = "w" if overwrite else "a+"

        # Open file and writes the input_data to it
        with open(directory, method, encoding="utf8") as file:
            file.write(input_data)
            logging.info(f"{__name__}: Wrote data to [File \"{directory}\"]")

    except Exception as error:
        logging.error(f"{__name__}: {error}")
