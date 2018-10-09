import os

import yaml

def read_yaml():
    filepath=os.getcwd()+os.sep+"Data"+os.sep+"login.yaml"
    with open(filepath, "r", encoding="utf-8") as f:
        return yaml.load(f)
print(read_yaml())
filepath=os.getcwd()+os.sep+"Data"+os.sep+"login.yaml"
print(filepath)