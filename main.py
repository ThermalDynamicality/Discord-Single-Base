"""
File: main.py \n
Author: Stanley Goodwin \n
Last Updated: 6/12/2022

Description:
The main file for executing the discord bot.
"""
import os
import logging
import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from dotenv import dotenv_values
from interface import SystemIO

# Bot logging settings
logging.basicConfig(filename="log.txt", encoding='utf-8', level=logging.INFO)


# Load cogs
def load_cogs(client):

    # List of available programs
    programs = SystemIO.list_directory("./programs")

    # For programs in the program folder
    for program in programs:

        # Set program's variable values
        program_dir = f"./programs/{program}"
        files = SystemIO.list_directory(program_dir)

        # If file "NORUN" in program's folder, skip program
        if "NORUN" in files:
            continue

        # If program settings file exists, load program
        if "program.json" in files:

            # Try to load program
            try:
                cog_file = SystemIO.read(f"{program_dir}/program.json", read_as_json=True)["cog_file"]
                client.load_extension(f"programs.{program}.{cog_file[:-3]}")
                print(f"Loaded {program}!")
            except Exception as error:
                print(f"Failed to load program {program}!\n{error}\n")
                logging.error(f"Failed to load program {program}!\n{error}\n")

        else:
            print(f"File program.json is missing from {program}")
            logging.error(f"File program.json is missing from {program}")


# Main executable
def main():

    # Initial variables
    config = dotenv_values(".env")
    token = config["TOKEN"]
    prefix = config["PREFIX"]
    server_id = config["SERVER_ID"]

    # Intents
    intents = nextcord.Intents.all()
    intents.members = True

    # Create client
    client = commands.Bot(
        command_prefix=prefix,
        intents=intents,
        test_guilds=[server_id],
        sync_commands_debug=True
    )

    # Load cogs
    load_cogs(client)

    @client.event
    async def on_ready():
        print(f"\n{client.user} has connected to Discord!\n")

    @client.event
    async def on_command_error(ctx, error):
        await ctx.send(f"Error Occurred. Try {prefix}help for a list of commands:\n{error}.")
        print(error)

    @client.slash_command(name="shutdown", description="Shuts down the bot.")
    async def shutdown(interaction: Interaction) -> None:
        await interaction.response.send_message("Shutting down...")
        print("Shutting down...")
        os._exit(0)

    # Run instance
    client.run(token)


# Main guard
if __name__ == "__main__":
    main()
