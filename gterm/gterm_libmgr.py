import os
import importlib

def include(libname: str):
    c = importlib.import_module("system.lib.lib" + libname)
    return c