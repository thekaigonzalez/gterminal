import requests
from gterm.gterm_helpers import get_arg
def onExecute(args: list):
    site = get_arg(args, 1)
    if get_arg(args, 2) == "--rco":
        print(requests.get(site).status_code)
        return
    print(requests.get(site).text)