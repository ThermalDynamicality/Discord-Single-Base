"""
File: take_roles.py \n
Author: Stanley Goodwin \n
Last Updated: 5/22/2022

Description:
Given a user, it takes away a role.

Known Issues: N/A

To Do: N/A
"""
import nextcord
from error_handling import log_error


async def take_role(self, user: nextcord.Member | int, role: nextcord.Role | int) -> None:
    """
    Takes a role away from a selected user.

    # Artificial Arguments
    :param self: The discord bot class that will be accessed of ID conversion.

    # Arguments
    :param user: The user to remove the role from.
    :param role: The role to remove from the user.

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

        # Removes the role from the user
        await user.remove_roles(role)

    except Exception as error:
        log_error(__name__, error, user, role)
