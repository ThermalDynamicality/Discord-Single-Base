"""
File: message.py\n
Author: Stanley Goodwin\n
Last Updated: 4/11/2022

Description:
    Provides the discord bot and programs with message-related functions.

Known Issues: N/A

To Do: N/A
"""
import nextcord
from error_handling import log_error


async def message(self,
                  output: nextcord.abc.Messageable | tuple[str, int],
                  content: str | list,
                  *,
                  duration: int = None,
                  multiline: bool = True,
                  replacement_dict: dict = None
                  ) -> nextcord.Message | None:
    """
    Sends a message given the input parameters with extra functions like
    converting a list of strings into a multiline comment, replace text,
    and sending to an ID rather than object.

    # Artificial Arguments
    :param self: Since function is part of a larger class, DiscordUtils, then
        self refers to other class things (required for ID conversion).

    # Positional Arguments
    :param output: Where the message will be sent to (user, channel, etc).
        Can be a tuple of type ("channel"/"user", ID HERE).
    :param content: The string or list to send to the output.
        If content is a list, it sends a multiline comment to output instead.

    # Keyword Arguments
    :param duration: The duration of how long the message sticks around.
        Defaults to None, meaning infinite duration.
    :param multiline: The boolean for whether the message is multiline.
        Default of True, since most lists are multiline comments.
    :param replacement_dict: A dictionary for converting between text brackets
        to text provided. Ex: {"user" : self.client}.

    # Return
    :return message: The nextcord message object.
    """

    ' TYPE CONVERSIONS '
    # If output is a tuple, convert to messageable object
    if isinstance(output, tuple) and list(map(type, output)) == [str, int]:
        _type, _id = output
        try:
            if _type == "channel":
                output = self.client.get_channel(_id)
            elif _type == "user":
                output = self.client.get_user(_id)
            else:
                raise Exception("Invalid output type (not \"channel\" or \"user\").")
        except Exception as error:
            log_error(__name__, error, output, content, duration, replacement_dict)

    # If message_content is a list, convert to multiline comment
    if isinstance(content, list) and multiline:
        content = _convert_to_multiline(content)

    # If there is a replacement dictionary, swap text
    if replacement_dict is not None:
        content = _replace_text(content, replacement_dict)

    ' EXECUTION '
    try:
        if duration in [-1, None]:
            return await output.send(content)
        else:
            return await output.send(content, delete_after=duration)
    except Exception as error:
        log_error(__name__, error, output, content, duration, replacement_dict)
        return None


def _convert_to_multiline(string_list: list) -> str:
    """
    Converts a list of strings into a multiline string with newlines after each
    entry in the list.

    :param string_list: The list of strings to be converted.
    :return multiline_string: The multiline string.
    """
    try:
        return "\n".join(string_list)
    except Exception as error:
        log_error(__name__, error, string_list)
        return str(string_list)  # Returns list if it cannot be converted


def _replace_text(string: str, replacement_dict: dict) -> str:
    """
    Takes a string and finds {KEYWORD}s and replaces them with key values.

    :param string: The input string.
    :param replacement_dict: The conversion dictionary (omitting {} in keys)
    :return string: The modified string.
    """
    try:
        for key, replacement in replacement_dict.items():
            _in_text = "{" + key + "}"
            string = string.replace(_in_text, str(replacement))
    except Exception as error:
        log_error(__name__, error, string, replacement_dict)
    finally:
        return string  # Always returns string regardless of success
