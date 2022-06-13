"""
File: main.py \n
Author: Stanley Goodwin \n
Last Updated: 5/22/2022

Description:
Program 2

Known Issues: N/A

To Do: N/A
"""
import logging
from nextcord.ext import commands
from discord_base import DiscordUtils


class Test2(commands.Cog, DiscordUtils):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping2(self, ctx):
        await ctx.send(f'My ping is 2 {commands.latency}!')

    @commands.command()
    async def test(self, ctx):
        await self.give_role(ctx.author, 9708956305222615222284)


# Setup function
def setup(client):
    client.add_cog(Test2(client))
