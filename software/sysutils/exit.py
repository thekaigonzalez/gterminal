from gterm.gterm_helpers import get_arg
def onExecute(args: list):
    if (get_arg(args, 1) == "--help"):
        print("""
this program exits the shell using Python's exit() function.

you can [optionally] add an argument for the return value of the exit.

examples:

* exit -1
* exit 3
* exit
""")
        return
    code = int(get_arg(args, 1, 0))
    exit(code)