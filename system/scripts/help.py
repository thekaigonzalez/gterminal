# all commands should implement help, if not, this will provide some insights using external manuals.

# the hello world prompt!
import os
def onExecute(arg: list):
    if (len(arg) >= 2):
        os.system("man system/help/" + arg[1] + ".1")