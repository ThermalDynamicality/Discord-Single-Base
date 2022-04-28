"""
File: __init__.py
Author: Stanley Goodwin
Last Updated: 4/11/2022

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
    from systemIO import read, write
    from misc import json_to_string, string_to_json, list_directory


# Reverts directory switch
sys.path.remove(PACKAGE_DIR)
