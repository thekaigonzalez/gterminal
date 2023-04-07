import os
import pathlib

class Directory:
    def __init__(self, path) -> None:
        self.path = path
    def protected(self):
        if pathlib.Path((self.path + "/.protected")).exists():
            return True
        else:
            return False