"""
File: __init__.py
Author: Stanley Goodwin
Last Updated: 4/11/2022

Description:
    Creates a subclass for discord cogs in order to speed up programming.

Known Issues: N/A

To Do: N/A
"""
import os
import sys


# Temporary directory switch
PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(PACKAGE_DIR)


# DiscordUtils class
class DiscordUtils:
    from message import message
    from roles import has_role, give_role, take_role


# Reverts directory switch
sys.path.remove(PACKAGE_DIR)
