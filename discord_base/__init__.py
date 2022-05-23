"""
File: __init__.py \n
Author: Stanley Goodwin \n
Last Updated: 5/22/2022

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
    from has_role import has_role
    from give_role import give_role
    from take_role import take_role


# Reverts directory switch
sys.path.remove(PACKAGE_DIR)
