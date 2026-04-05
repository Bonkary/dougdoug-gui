from dataclasses import dataclass
import os
from pathlib import Path
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QBoxLayout
from platform_connection import Twitch
# from pydirectinput import KEYBOARD_MAPPING

class DefaultFont(QFont):
    def __init__(self):
        super().__init__()
        
        self.setPixelSize(17)

TWITCH_MANAGER = Twitch()

# COMMON STRINGS
GAMEBOY = 'Gameboy'
SNES = 'SNES'
N64 = 'N64'
NES = 'NES'
GAMECUBE = 'Gamecube'
PC = 'PC'
COMBO_BUTTONS = 'combo_buttons'
PRESETS = 'presets'
CONTROLS = 'controls'
TWITCH_CHANNEL = 'twitch_channel'



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

MESSAGE_RATE = 0.5
MAX_QUEUE_LENGTH = 20
MAX_WORKERS = 100
BUTTON_HOLD_INTERVAL = 3



# Stacked Layout Indexes
START_PLAYING_BUTTON_INDEX = 0
STOP_PLAYING_BUTTON_INDEX = 1
GAMEBOY_INDEX = 0

AVAILABLE_CONSOLES = [GAMEBOY, N64, SNES, NES, GAMECUBE, PC] 

@dataclass
class empty:
    CONSOLES = {
        GAMEBOY: {
            PRESETS: {}
        }
    }
    SETTINGS = {
        'twitch_channel': '',
        'seen_tutorial': False
    }
    PRESET = {
        CONTROLS: {},
        COMBO_BUTTONS: []
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
    @dataclass
    class dialog:
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

    DEFAULT_FONT = DefaultFont()
    
    ALIGN_LEFT = Qt.AlignmentFlag.AlignLeft
    ALIGN_RIGHT = Qt.AlignmentFlag.AlignRight
    ALIGN_CENTER = Qt.AlignmentFlag.AlignCenter
    ALIGN_BOTTOM = Qt.AlignmentFlag.AlignBottom
    ALIGN_TOP = Qt.AlignmentFlag.AlignTop
    
    LEFT_TO_RIGHT = QBoxLayout.Direction.LeftToRight
    RIGHT_TO_LEFT = QBoxLayout.Direction.RightToLeft
    TOP_TO_BOTTOM = QBoxLayout.Direction.TopToBottom
    BOTTOM_TO_TOP = QBoxLayout.Direction.BottomToTop
    
    MAIN_WINDOW_WIDTH = 1600
    MAIN_WINDOW_HEIGHT = 1000
    
    KEYMAP_WINDOW_WIDTH = 800
    KEYMAP_WINDOW_HEIGHT = 200
   
    COMBO_WINDOW_WIDTH = 1200
    COMBO_WINDOW_HEIGHT = 500

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
    CONSOLE_CONFIGS = os.path.join(dirs.ROOT, 'configs', 'console_configs.json')
    SETTINGS = os.path.join(dirs.CONFIGS, 'settings.json')
    