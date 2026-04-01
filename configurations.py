import os
import json
from constants import *

if not os.path.exists(dirs.CONFIGS):
    os.mkdir(dirs.CONFIGS)

if not os.path.exists(files.CONTROL_SCHEMES):
    with open(files.CONTROL_SCHEMES, 'w') as schemesFile:
        CONTROL_SCHEMES = {
            "Gameboy": {
                'combo_buttons':{},
                'controls': {},
                'presets': {},
                },
            "NES": {
                'combo_buttons':{},
                'controls': {}
                },
            "SNES": {
                'combo_buttons':{},
                'controls': {}
                },
            "Gamecube": {
                'combo_buttons':{},
                'controls': {}
                },
            "PC": {
                'combo_buttons':{},
                'controls': {}
                },
            "N64": {
                'combo_buttons':{},
                'controls': {}
                }
        }
        schemesFile.write(json.dumps(CONTROL_SCHEMES))
else:
    with open(files.CONTROL_SCHEMES, 'r') as schemesFile:
        CONTROL_SCHEMES = json.loads(schemesFile.read())

if not os.path.exists(files.SETTINGS):
    with open(files.SETTINGS, 'w') as settingsFile:
        SETTINGS = {
            'twitch_channel': ''
        }
        settingsFile.write(json.dumps(SETTINGS))
else:
    with open(files.SETTINGS, 'r') as settingsFile:
        SETTINGS = json.loads(settingsFile.read())

with open(files.SETTINGS, 'r+') as settingsFile:
    contents = settingsFile.read()
    if not contents:
        SETTINGS = {
            'twitch_channel': ''
        }
        settingsFile.write(json.dumps(SETTINGS))
    else:
        SETTINGS = json.loads(contents)
    
