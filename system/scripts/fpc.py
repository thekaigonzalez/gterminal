# the hello world prompt!
import os
import shutil
import time


def onExecute(arg: list):
    print("cleaning your system's pycache!")

    for (root, dirs, files) in os.walk('.', topdown=True):
        if (root.find("__pycache__") != -1):
            shutil.rmtree(root)

    time.sleep(1)

    print("cleaned system cache!")