import os
import sys

from gterm.gterm_all import GTLang
from gterm.gterm_argmg import ArgumentManage


sysDict = {"SYS": "GTerminal"}
def interpreter():
    print("welcome to gt")
    while True:
        code = input("> ").strip()
        GTLang.runGTM(code, sysDict)

def onExecute(arg: list):
    args = ArgumentManage(arg)

    if (args.arg(1) == None):
        interpreter()
    else:
        f = open(args.arg(1), "r")
        text = f.read()
        f.close()
        GTLang.runGTM(text, sysDict)
