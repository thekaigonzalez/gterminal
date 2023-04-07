import os
from pathlib import Path
from gterm.gterm_helpers import get_arg
def onExecute(args: list):
    if (Path(get_arg(args, 1)).exists()):
        print("mkdir: could not create directory: dir exists")
        return -1
    os.mkdir(get_arg(args, 1))