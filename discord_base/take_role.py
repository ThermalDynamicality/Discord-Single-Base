"""
File: take_role.py \n
Author: Stanley Goodwin \n
Last Updated: 6/12/2022
"""
import logging
import nextcord


async def take_role(self, user: nextcord.Member | int, role: nextcord.Role | int) -> None:
    """
    Takes a role away from a selected user.

    :param self: [Artificial] Self bot class.
    :param user: The user to take the role from.
    :param role: The role to take from the user.

    :returns: None
    """
    try:
        # If user is a discord ID number, convert user to nextcord Member object
        if isinstance(user, int):
            user = self.client.get_user(id=user)
            logging.info(f"{__name__}: Converted [User ID: {user.id}] => [Member: \"{user}\"]")

        # If role is a discord ID number, convert role to nextcord Role object
        if isinstance(role, int):
            role = nextcord.utils.get(user.guild.roles, id=role)
            logging.info(f"{__name__}: Converted [Role ID: {role.id}] => [Role: \"{role}\"]")

        # Give user the role
        await user.remove_roles(role)
        logging.info(f"{__name__}: Removed [Role \"{role}\" ({role.id})] to [Member {str(user)} ({user.id})]")

    except Exception as error:
        logging.error(f"{__name__}: {error}")
