from dataclasses import dataclass
import os
from pathlib import Path

FONT_NAME = 'helvetica'

# WINDOW SIZES
MAIN_WINDOW_SIZE = '1500x900'
COMBINATIONS_WINDOW_SIZE = '1000x800'
KEYMAPPING_WINDOW_SIZE = '600x700'
BUTTON_COMBO_WINDOW_SIZE = '1300x800'
TUTORIAL_WINDOW_SIZE = '1500x800'

DISPLAY_KEYBOARD_MAPPING = [
    'Single characters (a, 4, -, etc.)',
    'F# (# = number)',
    'numpad# (# = number)',
    'left arrow',
    'right arrow',
    'up arrow',
    'down arrow',
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
    'alt',
    'right alt',
    'left alt'
    ]

MAX_MAPPING_DISPLAY_ROWS = (len(DISPLAY_KEYBOARD_MAPPING) // 2) + 2

GAMEBOY_BUTTON_ALIASES = {
            'A': 'A Button',
            'B': 'B Button',
            'L': 'Left Bumper',
            'R': 'Right Bumper',
            'dpad_up': 'D-Pad Up',
            'dpad_down': 'D-Pad Down',
            'dpad_right': 'D-Pad Right',
            'dpad_left': 'D-Pad Left',
            'select': "Select",
            'start': "Start"
        }

BUTTON_ALIASES = {
    'Gameboy': GAMEBOY_BUTTON_ALIASES,
}

# CONFIGS
FONT_NAME = 'helvetica'
ONLY_THESE_COLUMNS_EXIST = 1
EQUAL_SIZED_COLUMNS = 'column'
EQUAL_SIZED_ROWS = 'rows'

# CONSOLE NAMES
GAMEBOY = 'Gameboy'
SNES = 'SNES'
N64 = 'N64'
NES = 'NES'
GAMECUBE = 'Gamecube'
PC = 'PC'

# MISC
AVAILABLE_CONSOLES = ['Gameboy', 'N64', 'SNES', 'NES', 'Gamecube', 'PC']
MESSAGE_RATE = 0.5
MAX_QUEUE_LENGTH = 20
MAX_WORKERS = 100
BUTTON_HOLD_INTERVAL = 3

# LARGE STRINGS
TUTORIAL_TEXT = [
    "I'm going to tell you what you can do on the screen behind me.",
    "In the 'Keyboard' field, you're going to put the key you have bound to that button. You can see those by clicking the button on the top right.",
    "In the 'Press Command' field, you're going to put what you want your chat to type to press that button.",
    f"In the 'Hold Command' field, it's the same idea as the above one. Except it holds the button for {BUTTON_HOLD_INTERVAL} seconds.",
    "You can setup Button Combos by clicking the very obvious button for it after you select a console.",
    "Instructions will follow.",
    "Have fun. o7",
    "(You can close me now. I'm done. I appreciate the patience tho.)"
]

REWATCH_TUTORIAL_TEXT = [
    "I'm going to tell you what you can do on the screen behind me.",
    "Please pay attention because I am not doing this again.",
    "In the 'Keyboard' field, you're going to put the key you have bound to that button. You can see those by clicking the button on the top right.",
    "In the 'Press Command' field, you're going to put what you want your chat to type to press that button.",
    f"In the 'Hold Command' field, it's the same idea as the above one. Except it holds the button for {BUTTON_HOLD_INTERVAL} seconds.",
    "Still following?",
    "You can setup Button Combos by clicking the very obvious button for it after you select a console.",
    "Instructions will follow.",
    "Bye."
]

COMBO_BUTTON_INSTRUCTIONS = '\n'.join([
    "I'm sure you see the button names under me.",
    "I need you to type the ones on the right into the 'Key #' box.",
    "Don't mess it up.",
])

@dataclass
class colors:
    TWITCH_PURPLE = '#6441A5'
    GREEN = 'green'
    RED = 'red'

@dataclass
class dirs:
    ROOT = Path(__file__).resolve().parent
    CONFIGS = os.path.join(ROOT, 'configs')
    TEMP = os.path.join(ROOT, 'temp')

@dataclass
class files:
    CONTROL_SCHEMES = os.path.join(dirs.ROOT, 'configs', 'control_schemes.json')
    SETTINGS = os.path.join(dirs.CONFIGS, 'settings.json')
    