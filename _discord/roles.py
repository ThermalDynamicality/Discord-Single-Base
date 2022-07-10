"""
File: roles.py \n
Author: Stanley Goodwin \n
Description: Provides the _discord bot and programs with role-related functions.
"""
import logging
import nextcord


def has_role(self, user: nextcord.Member | int, role: nextcord.Role | int) -> bool:
    """
    Checks if user has role.

    :param self: [Artificial] Self bot class.
    :param user: The user.
    :param role: The role to find.
    :returns: user_has_role_boolean
    """
    try:
        # If user is an id, convert user to a nextcord Member object
        if isinstance(user, int):
            user = self.client.get_user(id=user)
            logging.info(f"{__name__}: Converted [User ID: {user.id}] => [Member: \"{user}\"]")

        # If role is a nextcord Role object, convert role to an id
        if isinstance(role, nextcord.Role):
            role = role.id
            logging.info(f"{__name__}: Converted [Role: \"{role}\"] => [Role ID: {role.id}]")

        # Checks if user has role
        role_object = nextcord.utils.get(user.guild.roles, id=role)
        user_has_role_boolean = role in [r.id for r in user.roles]
        logging.info(f"{__name__}: Tested if [Member {str(user)} ({user.id})] has [Role \"{role_object}\" ({role})]: {user_has_role_boolean}")
        return user_has_role_boolean

    except Exception as error:
        logging.error(f"{__name__}: {error}")
        return False  # Returns False on exception


async def give_role(self, user: nextcord.Member | int, role: nextcord.Role | int) -> None:
    """
    Give role to user.

    :param self: [Artificial] Self bot class.
    :param user: The user.
    :param role: The role to give.
    :returns: None
    """
    try:
        # If user is an id, convert user to a nextcord Member object
        if isinstance(user, int):
            user = self.client.get_user(id=user)
            logging.info(f"{__name__}: Converted [User ID: {user.id}] => [Member: \"{user}\"]")

        # If role is an id, convert role to a nextcord Role object
        if isinstance(role, int):
            role = nextcord.utils.get(user.guild.roles, id=role)
            logging.info(f"{__name__}: Converted [Role ID: {role.id}] => [Role: \"{role}\"]")

        # Give role to user
        await user.add_roles(role)
        logging.info(f"{__name__}: Gave [Role \"{role}\" ({role.id})] to [Member {str(user)} ({user.id})]")

    except Exception as error:
        logging.error(f"{__name__}: {error}")


async def remove_role(self, user: nextcord.Member | int, role: nextcord.Role | int) -> None:
    """
    Remove role from user.

    :param self: [Artificial] Self bot class.
    :param user: The user.
    :param role: The role to take.
    :returns: None
    """
    try:
        # If user is an id, convert user to a nextcord Member object
        if isinstance(user, int):
            user = self.client.get_user(id=user)
            logging.info(f"{__name__}: Converted [User ID: {user.id}] => [Member: \"{user}\"]")

        # If role is an id, convert role to a nextcord Role object
        if isinstance(role, int):
            role = nextcord.utils.get(user.guild.roles, id=role)
            logging.info(f"{__name__}: Converted [Role ID: {role.id}] => [Role: \"{role}\"]")

        # Remove role from user
        await user.remove_roles(role)
        logging.info(f"{__name__}: Removed [Role \"{role}\" ({role.id})] from [Member {str(user)} ({user.id})]")

    except Exception as error:
        logging.error(f"{__name__}: {error}")
