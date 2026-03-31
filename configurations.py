import os
import json
from constants import *

if not os.path.exists(dirs.CONFIGS):
    os.mkdir(dirs.CONFIGS)

with open(files.CONTROL_SCHEMES, 'w+') as schemeFile:
    try:
        CONTROL_SCHEMES = json.loads(schemeFile.read())
    except json.decoder.JSONDecodeError:
        CONTROL_SCHEMES = {
            "Gameboy": {},
            "NES": {},
            "SNES": {},
            "Gamecube": {},
            "PC": {},
            "N64": {}
        }
        schemeFile.write(json.dumps(CONTROL_SCHEMES))
    
with open(files.SETTINGS, 'w+') as settingsFile:
    try:
        SETTINGS = json.loads(settingsFile.read())
    except json.decoder.JSONDecodeError:
        SETTINGS = {}
    
