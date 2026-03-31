import os
import json
from constants import *

if not os.path.exists(dirs.CONFIGS):
    os.mkdir(dirs.CONFIGS)

with open(files.CONTROL_SCHEMES, 'w+') as schemeFile:
    CONTROL_SCHEMES = json.loads(schemeFile.read())
    
with open(files.SETTINGS, 'w+') as settingsFile:
    SETTINGS = json.loads(settingsFile.read())
    
