import configparser

def get_local_config():

    c = configparser.ConfigParser()
    c.read("system/system.cfg")

    return c

def get_version():
    return get_local_config()["System"]["version"]

