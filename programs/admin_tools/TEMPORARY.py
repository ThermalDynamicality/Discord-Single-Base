"""
File: main.py \n
Author: Stanley Goodwin \n
Last Updated: 5/22/2022

Description:
Provides admins with tools such as enable, disable, reload, and shutdown.

Known Issues: N/A

To Do: N/A
"""
from nextcord.ext import commands
from discord_base import DiscordUtils


class Control(commands.Cog, DiscordUtils):
    def __init__(self, client):
        self.client = client


# Setup function
def setup(client):
    client.add_cog(Control(client))
