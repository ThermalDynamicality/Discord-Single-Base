"""
File: write.py \n
Author: Stanley Goodwin \n
Last Updated: 5/22/2022

Description:
A function for writing to a file in the system.

Known Issues: N/A

To Do:
Consider a "replace in file" function.
"""
from error_handling import log_error
from json import dumps


def write(directory: str,
          input_data: str | dict,
          *,
          overwrite: bool = False
          ) -> None:
    """
    Writes text to a directory (append / overwrite).

    # Positional Arguments
    :param directory: The directory of the file.
    :param input_data: The data to store.

    # Keyword Arguments
    :param overwrite: Whether to overwrite the file.

    # Return
    :return None:
    """
    try:
        # Converts json data into plain-text
        if isinstance(input_data, dict):
            input_data = dumps(input_data)

        # Opens file in append or write mode and writes to file
        method = "w" if overwrite else "a+"
        with open(directory, method, encoding="utf8") as file:
            file.write(input_data)

    except Exception as error:
        log_error(__name__, error, directory, input_data)
