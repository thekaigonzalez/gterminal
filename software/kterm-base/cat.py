def onExecute(args: list):
    if args[0] == "--file":
        if args[1] == "--read":
            name = args[2]
            ufile = open(name, 'r+')
            a= ufile.readlines()
            for line in a:
                print(line)