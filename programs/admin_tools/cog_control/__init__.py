"""
File: __init__.py \n
Author: Stanley Goodwin \n
Last Updated: 5/22/2022

Description:
The set of functions for manipulating cogs.

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
    from _disable import


# Reverts directory switch
sys.path.remove(PACKAGE_DIR)
