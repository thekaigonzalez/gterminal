# features to add
# * interface from gkux
# * command installation features (from KTerminal)
# * Safety (from KTerminal)
# * ALL COMMANDS FROM KUX AND KTERMINAL THAT ARENT IN BOTH
# * simple and easy to use
# * no boot system (from KTerminal)
# * basic user data structure
# * a combination of a good package manager from both apps

import os
import readline
import bashlex
import gterm.colorshell as gshc
import importlib
import json
import requests

# ripped from gkux terminal
cprint = lambda text: gshc.print_with_name(text, "gsh")

def start_shell():
    cprint("welcome to gterminal!")
    while True:
        try:
            raw_command = input(":-$ ")
            if (raw_command.startswith("#")): continue
            argv = list(bashlex.split(raw_command))
            c = importlib.import_module("system.scripts." + argv[0])
            c.onExecute(argv)
        except KeyboardInterrupt: # ^C
            cprint("press ^D to exit.")
        except EOFError: # ^D
            exit(0)
        except ModuleNotFoundError:
            missing = requests.get("https://raw.githubusercontent.com/thekaigonzalez/gterminal/master/software/MISSING_SOFTWARE.json")
            js = (missing.json())
            if (js.get(argv[0]) != None):
                cprint("that command can be found in the package '{}'.".format(js.get(argv[0])))
                cprint("to install it: `pkg get " + js[argv[0]] + "'")
            else:
                cprint("that command, {}, does not exist. sorry".format(argv[0]))
        except Exception as e:
            cprint("there was an error running your program.")
            cprint("error: " + str(e))