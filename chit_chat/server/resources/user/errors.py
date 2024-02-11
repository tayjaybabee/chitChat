"""


Author: 
    Inspyre Softworks

Project:
    chitChat

File: 
    chit_chat/server/resources/user/errors.py
 

Description:
    

"""
from chit_chat.server.errors import ServerError


class UserError(ServerError):
    """Base class for user errors."""
    pass


class WrapValidationError(UserError):
    """Raised when an invalid wrap is attempted to be set."""
    def __init__(self, wrap, allowed_wraps=None):
        allowed_wraps_message = f'Allowed wraps: {allowed_wraps}' if allowed_wraps else 'No allowed wraps provided.'
        self.message = f"The wrap '{wrap}' is invalid for this user. {allowed_wraps_message}"
        super().__init__(self.message)
