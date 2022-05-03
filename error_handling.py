"""
File: error_handling.py
Author: Stanley Goodwin
Last Updated: 5/2/2022

Description:
    Provides error handling and printing for functions.

Known Issues:
    May print to log weirdly and not to the right directory.

To Do: N/A
"""
import logging
logging.basicConfig(filename="log.txt", encoding='utf-8', level=logging.ERROR)


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
    text = f"""{DIVIDER}
    Function: {function}()
    Error: {error}
    Parameters:\n"""
    for i in params:  # Add parameters
        text += f"\t{i=}\n"

    # Closing divider
    # text += DIVIDER  # Not currently needed

    # Log Error
    logging.error(text)
