"""


Author: 
    Inspyre Softworks

Project:
    chitChat

File: 
    chit_chat/server/database/__init__.py
 

Description:
    

"""
import sqlite3
import os
from inspy_logger import InspyLogger

logger = InspyLogger('chit_chat.server.database')
logger.replay_and_setup_handlers()


def ensure_database_exists(db_path):
    """Ensures the database file exists at the given path."""
    log = logger.get_child('ensure_database_exists')
    log.replay_and_setup_handlers()

    if not os.path.exists(db_path):
        log.warning(f'Database file not found at {db_path}!')
        log.info('Creating database file....')
        with open(db_path, 'w') as f:
            f.write('')
        log.info('Database file created!')


def provision_database(db_path):
    """Creates the database and the users table if they don't already exist."""

    log = logger.get_child('create_database')
    log.replay_and_setup_handlers()

    ensure_databse_exists(db_path)

    conn = sqlite3.connect('chat_server.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            wrap TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


provision_database()
