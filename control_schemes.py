import customtkinter as ctk
import widgets as wdgts
import time
import threading
import json
from constants import *
import configurations as cfg

class ControlAssignmentPanel(wdgts.CustomFrame):
    def __init__(self, app):
        super().__init__(master=app)
        self._app = app
        
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.grid_columnconfigure(index=0, weight=ONLY_THESE_COLUMNS_EXIST)
        self._activeScheme = None
        
        self._gameboyScheme = GameboyControls(panel=self)
        self._gameboyScheme.grid(row=0, column=0)
        self._gameboyScheme.hide()

        
    def set_console(self, console: str) -> None:
        if self._activeScheme:
            self._activeScheme.hide()
        match console:
            case 'Gameboy':
                self._activeScheme = self._gameboyScheme
                self._gameboyScheme.show()
            case 'NES':
                pass
            case 'N64':
                pass
            case 'SNES':
                pass
            case 'Gamecube':
                pass
            case 'PC':
                pass
    
    def save_control_scheme(self) -> None:
        cfg.SETTINGS['twitch_channel'] = self._app.get_channel_name()
        self._activeScheme.save_control_scheme()

    def load_control_scheme(self) -> None:
        self._gameboyScheme.load_control_scheme()

class ControlAssignment(wdgts.CustomFrame):
    def __init__(self, master, action: str, **kwargs):
        super().__init__(master, **kwargs)
        self._action = action
        self.grid_columnconfigure(index=(0), weight=ONLY_THESE_COLUMNS_EXIST, uniform=EQUAL_SIZED_COLUMNS)
        
        self._keyLabel = ctk.CTkLabel(master=self, text=action, width=90,
                                      font=ctk.CTkFont(family=FONT_NAME, size=30, underline=True))
        self._keyLabel.grid(row=0, column=0, padx=(20,0))
        
        self._keyboardEntry = wdgts.NamedEntry(master=self, name="Keyboard", name_placement='side')
        self._keyboardEntry.grid(row=1, column=0, pady=2, sticky='ew')
        
        self._pressEntry = wdgts.NamedEntry(master=self, name="Press Command", name_placement='side')
        self._pressEntry.grid(row=2, column=0, pady=2, sticky='ew')
        
        self._holdEntry = wdgts.NamedEntry(master=self, name="Hold Command", name_placement='side')
        self._holdEntry.grid(row=3, column=0, pady=2, sticky='ew')
         
    def get_controls(self) -> dict:
        return {
            'action': self._action,
            'key': self._keyboardEntry.get(),
            'press': self._pressEntry.get(),
            'hold': self._holdEntry.get()
        }
        
    def set_controls(self, controls: dict) -> None:
        self._keyboardEntry.set(controls['key'])
        self._pressEntry.set(controls['press'])
        self._holdEntry.set(controls['hold'])

class GameboyControls(wdgts.CustomFrame):
    def __init__(self, panel: ControlAssignmentPanel, **kwargs):
        super().__init__(master=panel, **kwargs)
        self._panel = panel
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.grid_columnconfigure((0,1,2,3), weight=ONLY_THESE_COLUMNS_EXIST)
        
        self._AButton = ControlAssignment(master=self, action="A Button")
        self._AButton.grid(row=0, column=0, padx=20, pady=20)
        
        self._BButton = ControlAssignment(master=self, action="B Button")
        self._BButton.grid(row=0, column=1, padx=20, pady=20)
        
        self._LButton = ControlAssignment(master=self, action="L Bumper")
        self._LButton.grid(row=0, column=2, padx=20, pady=20)
        
        self._RButton = ControlAssignment(master=self, action="R Bumper")
        self._RButton.grid(row=0, column=3, padx=20, pady=20)
        
        self._DPadLeft = ControlAssignment(master=self, action="D-Pad Left")
        self._DPadLeft.grid(row=1, column=0, padx=20, pady=20)
        
        self._DPadUp = ControlAssignment(master=self, action="D-Pad Up")
        self._DPadUp.grid(row=1, column=1, padx=20, pady=20)
        
        self._DPadRight = ControlAssignment(master=self, action="D-Pad Right")
        self._DPadRight.grid(row=1, column=2, padx=20, pady=20)
        
        self._DPadDown = ControlAssignment(master=self, action='D-Pad Down')
        self._DPadDown.grid(row=1, column=3, padx=20, pady=20)
        
        self._selectButton = ControlAssignment(master=self, action="Select")
        self._selectButton.grid(row=2, column=1, padx=20, pady=20)
        
        self._startButton = ControlAssignment(master=self, action="Start")
        self._startButton.grid(row=2, column=2, padx=20, pady=20)
        
        self._combosButton = wdgts.CustomButton(master=self, text='Open Button Combos', command=lambda: ComboButtonConfig(master=self, console=GAMEBOY),
                                                width=200, height=40, font=(FONT_NAME, 20))
        self._combosButton.grid(row=3, column=1, columnspan=2)

        self.load_control_scheme()

    def save_control_scheme(self) -> None:
        cfg.CONTROL_SCHEMES['Gameboy'] = {
            'A': self._AButton.get_controls(),
            'B': self._BButton.get_controls(),
            'L': self._LButton.get_controls(),
            'R': self._RButton.get_controls(),
            'dpad_left': self._DPadLeft.get_controls(),
            'dpad_up': self._DPadUp.get_controls(),
            'dpad_right': self._DPadRight.get_controls(),
            'dpad_down': self._DPadDown.get_controls(),
            'select': self._selectButton.get_controls(),
            'start': self._startButton.get_controls()
        }
        with open(files.CONTROL_SCHEMES, 'w') as controlSchemeFile:
            controlSchemeFile.write(json.dump(cfg.CONTROL_SCHEMES))

    def load_control_scheme(self) -> None:
        try:
            self._AButton.set_controls(cfg.CONTROL_SCHEMES['Gameboy']['A'])
            self._BButton.set_controls(cfg.CONTROL_SCHEMES['Gameboy']['B'])
            self._LButton.set_controls(cfg.CONTROL_SCHEMES['Gameboy']['L'])
            self._RButton.set_controls(cfg.CONTROL_SCHEMES['Gameboy']['R'])
            self._DPadLeft.set_controls(cfg.CONTROL_SCHEMES['Gameboy']['dpad_left'])
            self._DPadUp.set_controls(cfg.CONTROL_SCHEMES['Gameboy']['dpad_up'])
            self._DPadRight.set_controls(cfg.CONTROL_SCHEMES['Gameboy']['dpad_right'])
            self._DPadDown.set_controls(cfg.CONTROL_SCHEMES['Gameboy']['dpad_down'])
            self._selectButton.set_controls(cfg.CONTROL_SCHEMES['Gameboy']['select'])
            self._startButton.set_controls(cfg.CONTROL_SCHEMES['Gameboy']['start'])
        except KeyError:
            pass

class ComboButtonConfig(wdgts.CustomToplevel):
    def __init__(self, *, master, console: str, **kwargs):
        super().__init__(master, **kwargs)
        self._appRoot = master
        self._console = console
        self._nextComboRow = 0
        self._nextComboColumn = 0
        
        self.geometry(BUTTON_COMBO_WINDOW_SIZE)
        self.grid_columnconfigure(index=(0,1), weight=ONLY_THESE_COLUMNS_EXIST)
        
        # CREATE COMBOS
        self._createCombosFrame = wdgts.CustomFrame(master=self, border_width=2, border_color='black')
        self._createCombosFrame.grid_columnconfigure(index=(0,1), weight=ONLY_THESE_COLUMNS_EXIST)
        self._createCombosFrame.grid(row=0, column=0, sticky='news', pady=70, padx=20)
        
        self._title = wdgts.CustomLabel(master=self._createCombosFrame, text='Create Button Combos', font=(FONT_NAME,30))
        self._title.grid(row=0, column=0, columnspan=2)
        
        self._key1Entry = wdgts.NamedEntry(master=self._createCombosFrame, name="Key 1", name_placement='top')
        self._key1Entry.grid(row=2, column=0, pady=5, sticky='e')
        
        self._key2Entry = wdgts.NamedEntry(master=self._createCombosFrame, name='Key 2', name_placement='top')
        self._key2Entry.grid(row=2, column=1, pady=5, sticky='w')
        
        self._pressEntry = wdgts.NamedEntry(master=self._createCombosFrame, name='Press Command', name_placement='side')
        self._pressEntry.grid(row=3, column=0, pady=10, columnspan=2)
        
        self._holdEntry = wdgts.NamedEntry(master=self._createCombosFrame, name="Hold Command", name_placement='side')
        self._holdEntry.grid(row=4, column=0, columnspan=2)
        
        self._addButton = wdgts.CustomButton(master=self._createCombosFrame, text='Add', 
                                             command=self.add, font=(FONT_NAME,20))
        self._addButton.grid(row=5, column=0, columnspan=2, pady=20)
        
        # MY BUTTON COMBOS
        self._myCombosFrame = wdgts.CustomFrame(master=self)
        self._myCombosFrame.grid_columnconfigure(index=0, weight=ONLY_THESE_COLUMNS_EXIST, uniform=EQUAL_SIZED_COLUMNS)
        self._myCombosFrame.grid(row=1, column=0)
        
        self._myCombosLabel = wdgts.CustomLabel(master=self._myCombosFrame, text='My Combos', font=(FONT_NAME,25))
        self._myCombosLabel.grid(row=0, column=0, sticky='n', pady=(0,20))
        
        self._comboNamesFrame = wdgts.CustomFrame(master=self._myCombosFrame)
        self._comboNamesFrame.grid_columnconfigure(index=(0,1), weight=ONLY_THESE_COLUMNS_EXIST, uniform=EQUAL_SIZED_COLUMNS)
        self._comboNamesFrame.grid(row=1, column=0, sticky='news')
        
        for comboID in cfg.CONTROL_SCHEMES[self._console]['combo_buttons']:
            combo = cfg.CONTROL_SCHEMES[self._console]['combo_buttons'][comboID]
            ComboInfo(master=self._comboNamesFrame, combo=combo, console=self._console)\
                .grid(row=self._nextComboRow, 
                      column=self._nextComboColumn, 
                      pady=10, padx=60, sticky='w')
                
            self._nextComboRow += 1
            if self._nextComboRow == 3:
                self._nextComboRow = 0
                self._nextComboColumn = 1
        
        # INSTRUCTIONS
        self._instructionsFrame = wdgts.CustomFrame(master=self)
        self._instructionsFrame.grid_columnconfigure(index=0, weight=ONLY_THESE_COLUMNS_EXIST)
        self._instructionsFrame.grid(row=0, column=1, sticky='news', pady=60, padx=20, rowspan=2)
        
        self._instructions = wdgts.CustomLabel(master=self._instructionsFrame, font=(FONT_NAME, 20),
                                               text=COMBO_BUTTON_INSTRUCTIONS)
        self._instructions.grid(row=0, column=0)
        
        self._keyMappingFrame = wdgts.CustomFrame(master=self._instructionsFrame)
        self._keyMappingFrame.grid_columnconfigure(index=(0,1,2), weight=ONLY_THESE_COLUMNS_EXIST)
        self._keyMappingFrame.grid(row=1, column=0, pady=50)
        
        buttonNamesRow = 0
        for buttonID in BUTTON_ALIASES[self._console]:
            wdgts.CustomLabel(master=self._keyMappingFrame, text=BUTTON_ALIASES[self._console][buttonID], font=(FONT_NAME,20))\
                .grid(row=buttonNamesRow, column=0, sticky='w', padx=10, pady=5)
            wdgts.CustomLabel(master=self._keyMappingFrame, text='-------------------->', font=(FONT_NAME,20))\
                .grid(row=buttonNamesRow, column=1, padx=10)
            wdgts.CustomLabel(master=self._keyMappingFrame, text=buttonID, font=(FONT_NAME,20))\
                .grid(row=buttonNamesRow, column=2, sticky='w', padx=10)
            buttonNamesRow += 1
        
    def add(self) -> None:
        key1 = self._key1Entry.get()
        key2 = self._key2Entry.get()
        press = self._pressEntry.get()
        hold = self._pressEntry.get()
        
        newID = len(cfg.CONTROL_SCHEMES[self._console]['combo_buttons']) + 1
        cfg.CONTROL_SCHEMES[self._console]['combo_buttons'][newID] = {
            "key1": key1,
            "key2": key2,
            "press": press,
            "hold": hold
        }
        with open(files.CONTROL_SCHEMES, 'w') as schemesFile:
            schemesFile.write(json.dumps(cfg.CONTROL_SCHEMES))
        self._key1Entry.clear()
        self._key2Entry.clear()
        self._pressEntry.clear()
        self._holdEntry.clear()
        
        newFrame = wdgts.CustomFrame(master=self._comboNamesFrame)
        newFrame.grid_columnconfigure(index=0, weight=ONLY_THESE_COLUMNS_EXIST)
        # newFrame.grid(row=self._nextComboRow, column=self._nextComboColumn, padx=5, pady=5, sticky='w')

class ComboInfo(wdgts.CustomFrame):
    def __init__(self, master, combo: dict, console: str):
        super().__init__(master)
        self.grid_columnconfigure(index=0, weight=ONLY_THESE_COLUMNS_EXIST)
        
        comboFont = ctk.CTkFont(family=FONT_NAME, weight='bold', size=20)
        button1Name = BUTTON_ALIASES[console][combo['key1']]
        button2Name = BUTTON_ALIASES[console][combo['key2']] 
        self._comboName = wdgts.CustomLabel(master=self, text=f'{button1Name} + {button2Name}', font=comboFont)
        self._comboName.grid(row=0, column=0)
        
        self._pressCmd = wdgts.CustomLabel(master=self, text=f'Press: {combo["press"]}', font=(FONT_NAME,15))
        self._pressCmd.grid(row=1, column=0, padx=(20,0), sticky='w')
        
        self._holdCmd = wdgts.CustomLabel(master=self, text=f'Hold: {combo["hold"]}', font=(FONT_NAME,15))
        self._holdCmd.grid(row=2, column=0, padx=(20,0), sticky='w')
        


