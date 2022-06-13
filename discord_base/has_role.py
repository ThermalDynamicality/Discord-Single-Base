"""
File: has_role.py \n
Author: Stanley Goodwin \n
Last Updated: 6/12/2022
"""
import logging
import nextcord


def has_role(self, user: nextcord.Member | int, role: nextcord.Role | int) -> bool:
    """
    Tests if a selected user has a role.

    :param self: [Artificial] Self bot class.
    :param user: The user to have tested.
    :param role: The role to be found.

    :returns: user_has_role_boolean
    """
    try:
        # If user is a discord ID number, convert user to nextcord Member object
        if isinstance(user, int):
            user = self.client.get_user(id=user)
            logging.info(f"{__name__}: Converted [User ID: {user.id}] => [Member: \"{user}\"]")

        # If role is a nextcord Role object, convert role to discord role id
        if isinstance(role, nextcord.Role):
            role = role.id
            logging.info(f"{__name__}: Converted [Role: \"{role}\"] => [Role ID: {role.id}]")

        # Test if the user has the role
        # TODO add INFO for the result of this function
        return role in [r.id for r in user.roles]

    except Exception as error:
        logging.error(f"{__name__}: {error}")
        return False  # Returns False on exception
