"""
File: has_role.py \n
Author: Stanley Goodwin \n
Last Updated: 5/22/2022

Description:
Tests if a user has a role.

Known Issues: N/A

To Do: N/A
"""
import nextcord
from error_handling import log_error


def has_role(self, user: nextcord.Member | int, role: nextcord.Role | int) -> bool:
    """
    Tests if a user has a role.

    # Artificial Arguments
    :param self: The discord bot class that will be accessed of ID conversion.

    # Arguments
    :param user: The user in question.
    :param role: The role to find in user.

    # Return
    :return bool: If the user has the role.
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
