from gterm.gterm_libmgr import include

def onExecute(args):
    L = include("hello")

    L.hello()