import os
import sys
import readline

import gterm.shell as gsh

# this is where it begins

import pathlib

if (pathlib.Path("system/bin").exists == False):
    os.mkdir("system/bin")

gsh.start_shell()
