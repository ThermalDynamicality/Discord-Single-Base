"""
File: __init__.py
Author: Stanley Goodwin
Last Updated: 5/22/2022

Description:
    Library of common interfacing interactions between program and system.

Known Issues: N/A

To Do: N/A
"""
import os
import sys


# Temporary directory switch
PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(PACKAGE_DIR)


# DiscordUtils class
class SystemIO:
    from read import read
    from write import write
    from json_to_string import json_to_string
    from string_to_json import string_to_json
    from list_directory import list_directory


# Reverts directory switch
sys.path.remove(PACKAGE_DIR)
