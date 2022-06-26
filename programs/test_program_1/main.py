"""
File: main.py \n
Author: Stanley Goodwin \n
Last Updated: 6/12/2022

Description:

"""
import logging
from nextcord.ext import commands
from discord_base import DiscordUtils
from interface import SystemIO


class Test1(commands.Cog, DiscordUtils):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def bruh(self, ctx):
        await self.message(ctx, "{USER} has logged on", duration=10, replacement_dict={"USER": ctx.author.name})



# Setup function
def setup(client):
    client.add_cog(Test1(client))
