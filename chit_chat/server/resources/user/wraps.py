"""


Author: 
    Inspyre Softworks

Project:
    chitChat

File: 
    chit_chat/server/resources/user/wraps.py
 

Description:
    

"""

class Wrap:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    @start.setter
    def start(self, start):
        self._start = start

    @end.setter
    def end(self, end):
        self._end = end

    def __str__(self):
        return f"{self.start}{self.end}"

    def decorate_string(self, string):
        return f"{self.start}{string}{self.end}"
