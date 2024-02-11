"""


Author: 
    Inspyre Softworks

Project:
    chitChat

File: 
    chit_chat/server/config/defaults.py
 

Description:
    

"""
from chit_chat.__about__ import __PROG__, __AUTHOR__
from appdirs import user_data_dir, user_config_dir, user_log_dir, user_cache_dir

HOST = 'localhost'
PORT = 6627
MAX_CONNECTIONS = 50
DATA_DIR = user_data_dir(__PROG__, __AUTHOR__)
CONFIG_FILEPATH = DATA_DIR + '/config.ini'
