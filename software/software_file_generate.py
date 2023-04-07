import os
import pathlib
import toml
import json


# generate a file with connection from commands to packages in a json file

final_dict = {}

for i in os.listdir("."):
    if pathlib.Path(i).is_dir():
        packagetoml = open(i + "/package.toml")
        tomlpac = toml.load(packagetoml)
        for ic in tomlpac["main"]["scripts"]:
            name = pathlib.Path(ic).stem
            final_dict[name] = pathlib.Path(i).stem
        try:
            for ic in tomlpac["main"]["binaries"]:
                name = pathlib.Path(ic).stem
                final_dict[name] = pathlib.Path(i).stem
        except KeyError:
            pass
        packagetoml.close()

di = json.dumps(final_dict)

with open("MISSING_SOFTWARE.json", "w") as f:
    f.write(di)