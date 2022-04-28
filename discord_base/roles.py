"""
File: roles.py
Author: Stanley Goodwin
Last Updated: 4/11/2022

Description:
    Provides the discord bot and programs with role-related functions.

Known Issues: N/A

To Do: N/A
"""
import nextcord
from error_handling import log_error


def has_role(self, user: nextcord.Member | int, role: nextcord.Role | int) -> bool:
    """
    Tests if a user has a role provided.

    # Artificial Arguments
    :param self: The discord bot class that will be accessed of ID conversion.

    # Arguments
    :param user: The user in question.
    :param role: The role to find in user.

    # Return
    :return bool: True/False if user has role.
    """
    try:
        # If user is an ID, convert to Member
        if isinstance(user, int):
            user = self.client.get_user(id=user)

        # If role isn't an ID, convert to ID
        if isinstance(role, nextcord.Role):
            role = role.id

        # Test if user has role
        if role in [r.id for r in user.roles]:
            return True
        else:
            return False

    except Exception as error:
        log_error(__name__, error, user, role)
        return False


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
