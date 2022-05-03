"""
File: give_roles.py
Author: Stanley Goodwin
Last Updated: 5/3/2022

Description:
    Given a user, it gives them a role.

Known Issues: N/A

To Do: N/A
"""
import nextcord
from error_handling import log_error


async def give_role(self, user: nextcord.Member | int, role: nextcord.Role | int) -> None:
    """
    Gives a role to a selected user.

    # Artificial Arguments
    :param self: The discord bot class that will be accessed of ID conversion.

    # Arguments
    :param user: The user to get the role.
    :param role: The role to give to the user.

    # Return
    :return None:
    """
    try:
        # If user is an ID, convert to Member
        if isinstance(user, int):
            user = self.client.get_user(id=user)

        # If role is an ID, convert to Role
        if isinstance(role, int):
            role = nextcord.utils.get(user.guild.roles, id=role)

        # Give user the role
        await user.add_roles(role)

    except Exception as error:
        log_error(__name__, error, user, role)