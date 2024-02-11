"""


Author: 
    Inspyre Softworks

Project:
    chitChat

File: 
    chit_chat/server/resources/user.py
 

Description:
    

"""
from chit_chat.server.resources.user.errors import WrapValidationError


class User:
    """Represents a chat user.

    Attributes:
"""
    __default_wrap = ['[', ']']

    def __init__(self, name, socket, wrap=__default_wrap,):
        """Initializes a User with a name, custom wrap, and socket."""
        self.name = name
        self.wrap = wrap
        self.socket = socket
        self.__allowed_wraps = None

    @property
    def allowed_wraps(self):
        """Returns the allowed wraps for the user."""
        pass

    def get_allowed_wraps(self):
        """Returns the allowed wraps for the user."""
        wraps = {'default': self.__default_wrap}


    def set_wrap(self, wrap):
        """Sets the user's custom wrap."""
        self.wrap = wrap if wrap in self.allowed_wraps else raise WrapValidationError(wrap, self.allowed_wraps)

    def format_message(self, message):
        """Formats a message with the user's custom wrap."""
        return f"{self.wrap}{self.name}{self.wrap}: {message}"
