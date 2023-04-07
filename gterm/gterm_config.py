import configparser

def get_local_config():

    c = configparser.ConfigParser()
    c.read("system/system.cfg")

    return c
def get_account():

    c = configparser.ConfigParser()
    c.read("system/credentials.cfg")

    return c["account"]

def get_version():
    return get_local_config()["System"]["version"]

class Account:
    def __init__(self) -> None:
        self.profile = get_account()
        pass
    def get_name(self):
        return self.profile["name"]
    def has_bios_access(self):
        return self.profile["bios"]
    