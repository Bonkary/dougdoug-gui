import os
import json
from constants import *

if not os.path.exists(dirs.CONFIGS):
    os.mkdir(dirs.CONFIGS)

with open(files.CONTROL_SCHEMES, 'r+') as schemeFile:
    contents = schemeFile.read()
    if not contents:
        CONTROL_SCHEMES = {
            "Gameboy": {},
            "NES": {},
            "SNES": {},
            "Gamecube": {},
            "PC": {},
            "N64": {}
        }
        json.dump(obj=CONTROL_SCHEMES, fp=schemeFile)
    else:
        CONTROL_SCHEMES = json.loads(contents)


with open(files.SETTINGS, 'r+') as settingsFile:
    contents = settingsFile.read()
    if not contents:
        SETTINGS = {
            'twitch_channel': ''
        }
        settingsFile.write(json.dumps(SETTINGS))
    else:
        SETTINGS = json.loads(contents)
    
