import os
import time
import toml
import requests
import random

def get_arg(listf: list, num: int):
    if (len(listf) > num): return listf[num]
    else: return ""

def pkg_install(prog: str):
    prog = prog.strip()
    if (len(prog) == 0):
        print("need package to install ?")
        return
    print("pkg: installing {} . . .".format(prog))
    url = "https://raw.githubusercontent.com/thekaigonzalez/gterminal/master/software/" + prog
    pkg_file = requests.get(url + "/package.toml")
    
    if (pkg_file.status_code != 200):
        print("error: package was not found in repo")
        return -1
    loader = toml.loads(pkg_file.text)

    # https://raw.githubusercontent.com/thekaigonzalez/hello/master/hello.py
    time.sleep(2)

    print("pkg: name: " + loader["main"]["name"])
    print("pkg: version: " + loader["main"]["version"])

    for file in loader["main"]["files"]:
        print("file: " + file + " !")
        fileinstall = requests.get(url + file)
        with open("system/scripts" + file, "w") as f:
            f.write(fileinstall.text)
        time.sleep(random.uniform(0.5, 0.01))
    print("---------")
    time.sleep(1)
    print("package installed :D ! enjoy.")
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