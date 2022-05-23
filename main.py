"""
File: main.py
Author: Stanley Goodwin
Last Updated: 5/2/2022

Description:
    Runs the bot straight from the console off the bat.

Known Issues: N/A

To Do:
    Send print statements to log.txt
"""
import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from dotenv import dotenv_values


# Load cogs
def load_cogs(client):
    pass


# Instance loop
def instance():

    # Initial variables
    config = dotenv_values(".env")
    token = config["TOKEN"]
    prefix = config["PREFIX"]
    server_id = config["SERVER_ID"]
    intents = nextcord.Intents.all()
    intents.members = True

    # Create client
    client = commands.Bot(
        command_prefix=prefix,
        intents=intents,
        test_guilds=[server_id],
        sync_commands_debug=True
    )

    @client.event
    async def on_ready():
        print(f"\n{client.user} has connected to Discord!\n")

    @client.event
    async def on_command_error(ctx, error):
        await ctx.send(error)
        print(error)

    @client.slash_command(name="shutdown", description="Shuts down the bot.")
    async def shutdown(interaction: Interaction) -> None:
        await interaction.response.send_message("Shutting down...")
        print("Shutting down...")
        exit()

    # Run instance
    client.run(token)


# Main executable
def main() -> None:
    instance()


# Main guard
if __name__ == "__main__":
    main()
