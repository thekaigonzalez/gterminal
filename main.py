import os
import sys
import readline

import gterm.shell as gsh
from gtacc.Info import check_and_ask
from gtacc.Send import stringify

# this is where it begins

import pathlib

if (pathlib.Path("system/bin").exists == False):
    os.mkdir("system/bin")

response = check_and_ask()

if (stringify(response) == 'F_OK'):
    gsh.start_shell()
else:
    print("login to gsh failed.")