# the hello world prompt!

def onExecute(arg: list):
    if (len(arg) == 1):
        print("hello, world!")
    elif (arg[1] == ".help"):
        print("""
hello! hi! welcome! this is the basic hello command
used as a base for the gterminal system.

you can use the basic form like so:

* hello

or you could add arguments.

* hello Kai
""")
    else:
        print("hello, {}!".format(" ".join(arg[1:])))