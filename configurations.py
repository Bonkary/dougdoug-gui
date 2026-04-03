import os
import json
import sys
from constants import *

def write_empty_schemes_file() -> None:
    with open(files.CONTROL_SCHEMES, 'w') as newFile:
        newFile.write(json.dumps(schemes.EMPTY_CONTROL_SCHEMES))

def write_empty_settings_file() -> None:
    with open(files.SETTINGS, 'w') as newFile:
        newFile.write(json.dumps(EMPTY_SETTINGS))

def update_settings_file() -> None:
    with open(files.SETTINGS, 'w') as settingsFile:
        settingsFile.write(json.dumps(SETTINGS))

def update_control_schemes_file() -> None:
    with open(files.CONTROL_SCHEMES, 'w') as controlSchemeFile:
        controlSchemeFile.write(json.dumps(CONTROL_SCHEMES))


if not os.path.exists(dirs.CONFIGS):
    os.mkdir(dirs.CONFIGS)

try:
    with open(files.CONTROL_SCHEMES, 'r') as schemesFile:
        contents = schemesFile.read()
        if not contents:
            CONTROL_SCHEMES = schemes.EMPTY_CONTROL_SCHEMES
            write_empty_schemes_file()
        else:
            CONTROL_SCHEMES = json.loads(contents)
except FileNotFoundError:
    CONTROL_SCHEMES = schemes.EMPTY_CONTROL_SCHEMES
    write_empty_schemes_file()

try:
    with open(files.SETTINGS, 'r') as settingsFile:
        contents = settingsFile.read()
        if not contents:
            SETTINGS = EMPTY_SETTINGS
            write_empty_settings_file()
        else:
            SETTINGS = json.loads(contents)
except FileNotFoundError:
    SETTINGS = EMPTY_SETTINGS
    write_empty_settings_file()



