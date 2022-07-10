"""
File: __init__.py \n
Author: Stanley Goodwin \n
Description: Creates a subclass for _discord programs in order to speed up programming.
"""
import os
import sys


# Temporary directory switch
PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(PACKAGE_DIR)


# DiscordUtils class
class DiscordUtils:
    from message import message
    from roles import has_role, give_role, remove_role


# Reverts directory switch
sys.path.remove(PACKAGE_DIR)
