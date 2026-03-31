from dataclasses import dataclass
import os
from pathlib import Path

MAIN_WINDOW_SIZE = '1500x800'
COMBINATIONS_WINDOW_SIZE = '1000x800'
EQUAL_WEIGHT = 1
FONT_NAME = 'helvetica'
AVAILABLE_CONSOLES = ['Gameboy', 'N64', 'SNES', 'NES', 'Gamecube', 'PC']
MESSAGE_RATE = 0.5
MAX_QUEUE_LENGTH = 20
MAX_WORKERS = 100

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
    