import os

def onExecute(arg: list[str]):
    if arg[0].startswith(arg[1]):
        print("yes")
    else:
        print('no')