import os

def onExecute(args: list):
    arr = []
    for fname in os.listdir("system/scripts"):
        if fname.endswith(".py"):
            if not fname.startswith("__"):
                arr.append(os.path.basename(fname))
    print("you have {} commands installed".format(str(len(arr))))