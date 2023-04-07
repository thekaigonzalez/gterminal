def onExecute(args: list):
    if args[1] == "--file":
        if args[2] == "--read":
            name = args[3]
            ufile = open(name, 'r+')
            a= ufile.readlines()
            for line in a:
                print(line)