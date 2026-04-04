from dataclasses import dataclass
import os
from pathlib import Path
from PySide6.QtGui import QFont
# from pydirectinput import KEYBOARD_MAPPING

class DefaultFont(QFont):
    def __init__(self):
        super().__init__()
        
        self.setPixelSize(17)


# COMMON STRINGS
GAMEBOY = 'Gameboy'
SNES = 'SNES'
N64 = 'N64'
NES = 'NES'
GAMECUBE = 'Gamecube'
PC = 'PC'
COMBO_BUTTONS = 'combo_buttons'
PRESETS = 'presets'

IRC_CMDS_TO_IGNORE = ['JOIN', '001', '002', '003', '004', '375', '372', '376', '353', '366']

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

ALL_BUTTON_ALIASES = {
    'Gameboy': GAMEBOY_BUTTON_ALIASES,
}

MESSAGE_RATE = 0.5
MAX_QUEUE_LENGTH = 20
MAX_WORKERS = 100
BUTTON_HOLD_INTERVAL = 3

EMPTY_SETTINGS = {
    'twitch_channel': '',
    'seen_tutorial': False
}





@dataclass
class keys:
    # AVAILABLE_KEYS = KEYBOARD_MAPPING
    USER_FRIENDLY_KEYBOARD_MAPPINGS = [
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
    
    # Some were renamed so that the user better understands that the key is. These are those keywords
    # Some may see 'prntscrn' and get confused. 
    # "Think about how stupid the average person is, and remember half the world is stupider than that" -George Carlin
    NEEDED_MAPPING_TRANSLATIONS = {
        'right arrow': 'right',
        'up arrow': 'up',
        'left arrow': 'left',
        'down arrow': 'down',
        'scroll lock': 'scrolllock',
        'right shift': 'shiftright',
        'left shift': 'shiftleft',
        'right ctrl': 'ctrlright',
        'left ctrl': 'ctrlleft',
        'windows key': 'win',
        'print screen': 'prntscrn'
    }
    HOLD_KEY_DURATION = 2
    PRESS_TIME_DURATION = 0.4

@dataclass
class gui:
    DEFAULT_FONT = DefaultFont()
    
    # These are just to explain what the grid_columnconfigure aimed to do
    ONLY_THESE_COLUMNS_EXIST = 1
    FIXED_SIZE = 1

@dataclass
class consoles:
    AVAILABLE_CONSOLES = [GAMEBOY, N64, SNES, NES, GAMECUBE, PC]
    
@dataclass
class schemes:
    EMPTY_SCHEME = {
        PRESETS: {}
        }
    
    EMPTY_CONTROL_SCHEMES = {
        GAMEBOY: EMPTY_SCHEME,
        N64: EMPTY_SCHEME,
        PC: EMPTY_SCHEME,
        SNES: EMPTY_SCHEME,
        NES: EMPTY_SCHEME,
        GAMECUBE: EMPTY_SCHEME
    }    

@dataclass
class text:
    COMBO_BUTTON_INSTRUCTIONS = '\n'.join([
        "I'm sure you see the button names under me.\n",
        "I need you to type the ones on the right into the 'Key #' box.\n",
        "Don't mess it up.\n",
    ])
    
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
    
    TUTORIAL_TEXT = [
        "I'm going to tell you what you can do on the screen behind me.",
        "On the top left, put in your Twitch username. Correct capitalization matters."
        "In the 'Keyboard' field, you're going to put the key you have bound to that button. You can see those by clicking the button on the top right.",
        "In the 'Press Command' field, you're going to put what you want your chat to type to press that button.",
        f"In the 'Hold Command' field, it's the same idea as the above one. Except it holds the button for {BUTTON_HOLD_INTERVAL} seconds.",
        "You can setup Button Combos by clicking the very obvious button for it after you select a console.",
        "Instructions will follow.",
        "Have fun. o7",
        "(You can close me now. I'm done. I appreciate the patience tho.)"
    ]

@dataclass
class colors:
    DEFAULT_TEXT = 'white' # also maybe #F9F871'
    TWITCH_PURPLE = '#6441A5'
    DARK_PURPLE = '#4c3080'
    GREEN = 'green'
    RED = 'red'
    BLACK = 'black'
    
@dataclass
class dirs:
    ROOT = Path(__file__).resolve().parent
    CONFIGS = os.path.join(ROOT, 'configs')
    TEMP = os.path.join(ROOT, 'temp')

@dataclass
class files:
    CONTROL_SCHEMES = os.path.join(dirs.ROOT, 'configs', 'control_schemes.json')
    SETTINGS = os.path.join(dirs.CONFIGS, 'settings.json')
    