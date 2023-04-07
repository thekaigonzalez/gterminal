import requests
from gterm.gterm_filesystem import writefile, getsysroot
from gterm.gterm_argmg import ArgumentManage
import os
from gterm.gterm_colorama import print_with_name, print_error

print = lambda text: print_with_name(text, "wget")
error = lambda text: print_error(text, "wget")

def onExecute(args: list):
    argv = ArgumentManage(args)

    site = argv.arg(1)

    if (site == None):
        error("missing [SITE]")
        return
    print("getting `{}'".format(site))
    site_data = requests.get(site)
    if (site_data.status_code == 404):
        print("site returned 404")
    print("writing file")
    writefile(os.path.basename(site)[0:], site_data.text)
    print("done!")