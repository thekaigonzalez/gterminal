import os
import time
import toml
import requests

def get_arg(listf: list, num: int):
    if (len(listf) > num): return listf[num]
    else: return ""

def pkg_install(prog: str):
    prog = prog.strip()
    if (len(prog) == 0):
        print("need package to install ?")
        return
    print("pkg: installing {} . . .".format(prog))
    pkg_file = requests.get("https://raw.githubusercontent.com/thekaigonzalez/gterminal/master/software/" + prog + "/package.toml")
    
    loader = toml.loads(pkg_file.text)

    # https://raw.githubusercontent.com/thekaigonzalez/hello/master/hello.py
    time.sleep(2)

    print("pkg: name: " + loader["main"]["name"])
    print("pkg: version: " + loader["main"]["version"])

    for file in loader["main"]["files"]:
        print(file)
def onExecute(args: list):
    if (len(args) == 1):
        print(
"""
pkg - install packages

pkg is a program to install programs from online. it is very simple and based on both get-apt/dpkg from KTERMINAL
and pkg/dup from Kux
"""
        )
    else:
        if (get_arg(args, 1) == "get"):
            package = get_arg(args, 2)
            pkg_install(package)