"""


Author: 
    Inspyre Softworks

Project:
    chitChat

File: 
    chit_chat/server/resources/commands/__init__.py
 

Description:
    

"""


class Command:
    def __init__(
            self,
            keywords,
            description,

    ):
        self._keywords = keywords
        self._description = description

    @property
    def keywords(self):
        return self._keywords

    @property
    def description(self):
        return self._description
