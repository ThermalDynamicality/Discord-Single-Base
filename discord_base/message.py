"""
File: message.py
Author: Stanley Goodwin
Last Updated: 6/12/2022

Description:
    Provides the discord bot and programs with message-related functions.
"""
import logging
import nextcord


async def message(self,
                  output: nextcord.abc.Messageable | tuple[str, int],
                  content: str | list,
                  *,
                  duration: int = None,
                  multiline: bool = True,
                  replacement_dict: dict = None
                  ) -> nextcord.Message | None:
    """
    Sends a message to a given output channel / channel-id, with extra
    functions allowing for multiline text output, in-place text replacement,
    and a duration of text lifespan.

    :param self: [Artificial] Self bot class.
    :param output: Where the message will be sent to (ex: user, channel, etc).
        Parameter can be a tuple of type ("channel" or "user", DISCORD_ID).
    :param content: The string or list to send to the output.
        If content is a list, it sends a multiline comment to output instead.

    :param duration: [Optional] A duration of how long the message sticks around.
        Defaults to None, allowing for infinite message duration.
        Setting duration to -1 also allows for infinite duration.
    :param multiline: [Optional] A boolean for whether the message is multiline.
        Default of True, since most lists are multiline comments.
        If set to false, the message with print a list without formatting.
    :param replacement_dict: [Optional] A dictionary for converting between text brackets
        to text provided. Ex: {"user" : self.client}.
        Allows for in-place replacement of text from a script file.

    :return: message – A nextcord Message object of the created message.
    """

    ' TYPE CONVERSIONS '
    # If the output is a tuple of type ("channel"/"user", ID)
    # convert the output into a nextcord Messageable object
    if isinstance(output, tuple) and list(map(type, output)) == [str, int]:
        _type, _id = output
        try:
            if _type == "channel":
                output = self.client.get_channel(_id)
                logging.info(f"{__name__}: Converted [Channel ID: {_id}] => [Channel: \"{str(output)}\"]")
            elif _type == "user":
                output = self.client.get_user(_id)
                logging.info(f"{__name__}: Converted [User ID: {_id}] => [User: \"{str(output)}\"]")
            else:
                raise ValueError("Invalid output type (not \"channel\" or \"user\").")
        except Exception as error:
            logging.error(f"{__name__}: {error}")

    # If the content is a list and multiline is True, create a multiline string message
    if isinstance(content, list) and multiline:
        content = _convert_to_multiline(content)

    # If there is a replacement dictionary, complete the replacements
    if replacement_dict is not None:
        content = _replace_text(content, replacement_dict)

    ' EXECUTION '
    try:
        if duration in {-1, None}:
            msg = await output.send(content)
        else:
            msg = await output.send(content, delete_after=duration)
        logging.info(f"{__name__}: Sent [Message \"{msg.content}\" ({msg.id})] to [Channel \"{msg.channel}\" ({msg.channel.id})]")
        return msg

    except Exception as error:
        logging.error(f"{__name__}: {error}")
        return None


def _convert_to_multiline(string_list: list) -> str:
    """
    Converts a list of strings into a multiline string with newlines after each
    entry in the list.

    :param string_list: The list of strings to be converted into a multiline string.
    :return: multiline_string – The multiline string output.
    """
    try:
        multiline_string = "\n".join(string_list)
        logging.info(f"{__name__}: Converted [List[str] to String")
        return multiline_string
    except Exception as error:
        logging.error(f"{__name__}: {error}")
        return str(string_list)  # Returns list as a string if it cannot be converted


def _replace_text(string: str, replacement_dict: dict) -> str:
    """
    Takes a string and finds {KEYWORD} and replaces them with key values.

    :param string: The input string to be converted.
    :param replacement_dict: The conversion dictionary (omitting {} in key names)
    :return string: The dictionary-converted string.
    """
    try:
        for key, replacement in replacement_dict.items():
            string = string.replace(f"{{{key}}}", str(replacement))
        logging.info(f"{__name__}: Replaced Strings by Dictionary reference")
    except Exception as error:
        logging.error(f"{__name__}: {error}")
    finally:
        return string  # Always returns string regardless of success
