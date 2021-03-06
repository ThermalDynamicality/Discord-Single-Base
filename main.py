"""
File: main.py \n
Author: Stanley Goodwin \n
Description: The main file for executing the _discord bot.
"""
import logging
import os
import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from dotenv import dotenv_values
from _system import SystemIO

# Bot logging settings
logging.basicConfig(filename="log.txt", encoding='utf-8', level=logging.INFO)


# Programs loader
def load_cogs(client):
    # For programs in the program folder
    for program in SystemIO.list_directory("./programs"):

        # Create list of all files in the program directory
        program_files = SystemIO.list_directory(f"./programs/{program}")

        # If file "NORUN" in program's folder, skip program
        if "NORUN" in program_files: continue

        # Load program if it has a settings file
        if "program.json" in program_files:
            try:
                cog_file = SystemIO.read(f"./programs/{program}/program.json", read_as_json=True)["cog_file"]
                client.load_extension(f"programs.{program}.{cog_file[:-3]}")
                logging.info(f"{__name__}: Loaded {program}!")
                print(f"Loaded {program}!")

            except Exception as error:
                logging.error(f"{__name__}: Failed to load program {program}!\n{error}\n")
                print(f"Failed to load program {program}!\n{error}\n")
        else:
            logging.error(f"{__name__}: File program.json is missing from {program}")
            print(f"Program {program} is missing its program.json")


# Main executable
def main():
    # Initialization
    config = dotenv_values(".env")
    prefix = config["PREFIX"]
    intents = nextcord.Intents.all()
    intents.members = True

    # Clear log file
    SystemIO.write("log.txt", "", overwrite=True)

    # Create client
    client = commands.Bot(
        command_prefix=prefix,
        intents=intents,
        test_guilds=config["SERVER_ID"],
        sync_commands_debug=True
    )

    # Load programs
    load_cogs(client)

    @client.event
    async def on_ready():
        logging.info(f"{client.user} has connected to Discord!\n")
        print(f"\n{client.user} has connected to Discord!\n")

    @client.event
    async def on_command_error(ctx, error):
        await ctx.send(f"Error Occurred. Try {prefix}help for a list of commands:\n{error}.")
        logging.debug(error)
        print(error)

    @client.slash_command(name="shutdown", description="Shuts down the bot.")
    async def shutdown(interaction: Interaction) -> None:
        await interaction.response.send_message("Shutting down...")
        logging.info("Bot is shutting down...")
        print("Shutting down...")
        os._exit(0)

    # Run instance
    client.run(config["TOKEN"])


# Main guard
if __name__ == "__main__":
    main()
