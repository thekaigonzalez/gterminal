def onExecute(arg: list):
    b = ' '.join(format(ord(x), 'b') for x in ' '.join(arg[1:]))
    print(str(b))