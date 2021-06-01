from configparser import ConfigParser
from psycopg2 import connect


def config_reader(section):
    """Initiate class ConfigParser and read init file"""
    config = ConfigParser()
    config.read('config.ini')
    # Get a key:value from provided section
    configuration = {}
    for item in config[section]:
        configuration[item] = config[section][item]
    return configuration


def db_details(db):
    """Return connection to DB"""
    params = config_reader(db)
    connection = connect(**params)
    return connection
