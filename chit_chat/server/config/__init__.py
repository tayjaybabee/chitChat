"""


Author: 
    Inspyre Softworks

Project:
    chitChat

File: 
    chit_chat/server/config/__init__.py
 

Description:
    

"""
from pathlib import Path
from chit_chat.server.config.defaults import CONFIG_FILEPATH, DATA_DIR
from configparser import ConfigParser
CACHE_FILEPATH = DATA_DIR + '/cache.ini'
from datetime import datetime


class Cache(ConfigParser):
    __filepath = Path(CACHE_FILEPATH)

    def __init__(self, config_filepath=None):
        super().__init__()
        if self.__filepath.exists():
            self.read(self.__filepath)

        self._config_filepath = config_filepath if config_filepath else CONFIG_FILEPATH

    @property
    def filepath(self):
        return self.__filepath

    @filepath.setter
    def filepath(self, new):
        if not isinstance(new, (Path, str)):
            raise TypeError(f"Expected Path or str, got {type(new)}")

        if isinstance(new, str):
            new = Path(new)

        self.__filepath = new

    def create(self):
        self.__filepath.touch()
        self.read(self.__filepath)
        self.add_section('CACHE')
        self.add_section('CONFIG')
        self.set('CACHE', 'created', datetime.now().isoformat())
        self.write(self.__filepath)

    def set_config_filepath(self, config_filepath):

        if 'CONFIG' not in self.sections():
            self.add_section('CONFIG')

        path = Path(config_filepath).expanduser().absolute()
        self.set('CONFIG', 'filepath', str(path))
        self.write(self.__filepath)

   def write(cls, filepath=None):
       with open(filepath, 'w') as file:
           super().write(file)
