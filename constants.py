from dataclasses import dataclass
import os
from pathlib import Path

# UI
FONT_NAME = 'helvetica'
MAIN_WINDOW_SIZE = '1500x900'
COMBINATIONS_WINDOW_SIZE = '1000x800'
KEYMAPPING_WINDOW_SIZE = '450x900'

# CONFIGS
ONLY_THESE_COLUMNS_EXIST = 1
EQUAL_SIZED_COLUMNS = 'column'
EQUAL_SIZED_ROWS = 'rows'

# MISC
AVAILABLE_CONSOLES = ['Gameboy', 'N64', 'SNES', 'NES', 'Gamecube', 'PC']
MESSAGE_RATE = 0.5
MAX_QUEUE_LENGTH = 20
MAX_WORKERS = 100
DISPLAY_KEYBOARD_MAPPING = ['Any single character key (a, b, 1, ?, -, :, etc.)',
                            'F# (# = number)',
                            'numpad# (# = number)'
                            'escape',
                            'print screen',
                            'scroll lock',
                            'backspace',
                            'insert',
                            'home',
                            'pageup',
                            'pagedown',
                            'numlock',
                            'clear',
                            'tab',
                            'space',
                            'delete',
                            'end',
                            'capslock',
                            'enter',
                            'return',
                            'shift',
                            'right shift',
                            'left shift',
                            'ctrl',
                            'right ctrl',
                            'left ctrl',
                            'windows key',
                            'right alt',
                            'left alt',]
MAX_MAPPING_DISPLAY_ROWS = 28

@dataclass
class colors:
    TWITCH_PURPLE = '#6441A5'

@dataclass
class dirs:
    ROOT = Path(__file__).resolve().parent
    CONFIGS = os.path.join(ROOT, 'configs')
    TEMP = os.path.join(ROOT, 'temp')

@dataclass
class files:
    CONTROL_SCHEMES = os.path.join(dirs.ROOT, 'configs', 'control_schemes.json')
    SETTINGS = os.path.join(dirs.CONFIGS, 'settings.json')
    