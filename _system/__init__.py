"""
File: __init__.py \n
Author: Stanley Goodwin \n
Description: Library of common interfacing interactions between program and _system.
"""
import os
import sys


# Temporary directory switch
PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(PACKAGE_DIR)


# SystemIO class
class SystemIO:
    from read import read
    from write import write
    from json_to_string import json_to_string
    from string_to_json import string_to_json
    from list_directory import list_directory


# Reverts directory switch
sys.path.remove(PACKAGE_DIR)
