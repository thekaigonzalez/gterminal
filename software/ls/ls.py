import os

# basic ls :)

def onExecute(arg: list):
    if (len(arg[0])):
        print("\n".join(os.listdir(".")))
    else:
        print("\n".join(os.listdir(arg[1])))
