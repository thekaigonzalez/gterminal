import os
from pathlib import Path

def rootify(path: str):
    new_path = path
    if not (new_path.startswith("/")):
        new_path = "/" + new_path
    return new_path

def getsysroot(path: str):
    return "system" + rootify(path)

def exists(path: str):
    return Path(getsysroot(path)).exists()

def writefile(path: str, text: str):
    with open(path, "w") as f:
        f.write(text)

