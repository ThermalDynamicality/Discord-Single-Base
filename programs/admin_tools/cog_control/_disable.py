"""
File: _disable.py \n
Author: Stanley Goodwin \n
Last Updated: 5/22/2022

Description:
A function for disabling a cog.

Known Issues: N/A

To Do: N/A
"""


async def disable(self, ctx, program):
    if program == "admin_tools":  # Can't Reload Control Cog
        await ctx.send("Cannot unload control cog. Please reboot bot manually.")
    else:  # If Not Control Cog, Attempt Unload
        try:
            self.client.unload_extension(f"modules.{program}.cog")
            await ctx.send("Unloaded " + program)
            print(f"Unloaded {program}!")
        except Exception as error:
            print(f"Failed To Unload {program}!")
            print(error)
