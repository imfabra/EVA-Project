import configparser
from pathlib import Path
import os


def getValueConfig(header,param):
    path = Path(__file__)
    ROOT_DIR = path.parent.absolute()
    config_path = os.path.join(ROOT_DIR, "config.properties")
    config = configparser.RawConfigParser()
    config.read(config_path)
    return config.get(header,param)



