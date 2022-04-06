"""
File: error_handling.py\n
Author: Stanley Goodwin\n
Last Updated: 4/6/2022

Description:
    Provides error handling and printing for functions.

Known Issues: N/A

To Do: N/A
"""
import logging
logging.basicConfig(filename="../$store/log.txt", encoding='utf-8', level=logging.ERROR)


def log_error(function: str, error: str, *params) -> None:
    """
    Logs an error to the $store file when a function fails.

    :param function: The name of the function that errored.
    :param error:    The string that explains the error that occurred.
    :param params:   All the parameters of the function that errored.
    :return None:
    """

    # Constants
    DIVIDER = "--------------------------------------------------"

    # Text string
    text = f"""{DIVIDER}\n
    Function: {function}()\n
    Error: {error}\n
    Parameters: {error}\n"""

    # Add parameters
    for i in params:
        text += f"\t{i=}\n"

    # Close divider
    text += DIVIDER

    # Log Error
    logging.error(text)
