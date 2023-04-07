import gterm.gterm_config as gtcfg

def onExecute(args: list):
    print("You are running GTerminal version " + gtcfg.get_version())
    print("the codename for this version is " + gtcfg.get_local_config()["System"]["codename"] + "")