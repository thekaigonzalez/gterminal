import os

# basic ls :)

def get_arg(listf: list, num: int):
    if (len(listf) > num): return listf[num]
    else: return "."

def onExecute(arg: list):
    print("\n".join(os.listdir(get_arg(arg, 1))))
