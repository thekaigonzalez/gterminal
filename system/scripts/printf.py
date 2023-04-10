import shlex

def onExecute(arg: list[str]):
    for i in arg[1:]:
        print(i.encode().decode("unicode_escape"))