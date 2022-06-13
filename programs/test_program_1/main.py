"""
File: main.py \n
Author: Stanley Goodwin \n
Last Updated: 5/22/2022

Description:
Program 1

Known Issues: N/A

To Do: N/A
"""
from discord.ext import commands
from discord_base import DiscordUtils


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


# Setup function
def setup(client):
    client.add_cog(Test1(client))
