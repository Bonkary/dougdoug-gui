import customtkinter as ctk
import widgets as wdgts
import time
import threading
import json
import popups
from constants import *
import configurations as cfg


class Console(wdgts.CustomFrame):
    def __init__(self, app, **kwargs):
        super().__init__(master=app, **kwargs)
        self._app = app
        self._activeControls = None
        
        self.grid_columnconfigure(index=0, weight=gui.ONLY_THESE_COLUMNS_EXIST)
        
        self._selectorsFrame = wdgts.CustomFrame(master=self)
        self._selectorsFrame.grid_columnconfigure(index=(0,1,2), weight=gui.ONLY_THESE_COLUMNS_EXIST, uniform=gui.EQUAL_SIZED_COLUMNS)
        self._selectorsFrame.grid(row=0, column=0, sticky='ew')
        
        self._consoleSelector = ConsoleSelector(master=self._selectorsFrame, console=self)
        self._consoleSelector.grid(row=0, column=1)
        
        self._presetSelector = PresetSelector(master=self._selectorsFrame, console=self)
        self._presetSelector.grid(row=0, column=2, sticky='w')
        self._presetSelector.hide()
        
        self._gameboyControls = GameboyControls(console=self)
        self._gameboyControls.grid(row=1, column=0)
        self._gameboyControls.hide()
        
        self._n64Controls = N64Controls(console=self)
        self._n64Controls.grid(row=1, column=0)
        self._n64Controls.hide()
        
        self._snesControls = SuperNintendoControls(console=self)
        self._snesControls.grid(row=1, column=0)
        self._snesControls.hide()
        
        self._gamecubeControls = GamecubeControls(console=self)
        self._gamecubeControls.grid(row=1, column=0)
        self._gamecubeControls.hide()
        
        self._nesControls = NintendoControls(console=self)
        self._nesControls.grid(row=1, column=0)
        self._nesControls.hide()
        
        self._pcControls = ComputerControls(console=self)
        self._pcControls.grid(row=1, column=0)
        self._pcControls.hide()
        
        self._buttonsFrame = wdgts.CustomFrame(master=self)
        self._buttonsFrame.grid_columnconfigure(index=(0,1,2), weight=gui.ONLY_THESE_COLUMNS_EXIST, uniform=gui.EQUAL_SIZED_COLUMNS)
        self._buttonsFrame.grid(row=2, column=0, sticky='s')
        self._buttonsFrame.hide()
        
        self._savePresetButton = wdgts.CustomButton(master=self._buttonsFrame, text="Save Preset",
                                                    command=self.save_preset, width=200, height=40, font=(gui.FONT_NAME, 20))
        self._savePresetButton.grid(row=0, column=0)
        
        self._presetEntry = wdgts.NamedEntry(master=self._buttonsFrame, name='Preset', name_placement='top')
        self._presetEntry.grid(row=0, column=1, padx=50)
        
        self._combosButton = wdgts.CustomButton(master=self._buttonsFrame, text='Open Button Combos',
                                                command=lambda: popups.ButtonComboConfigPopup(master=self, console=GAMEBOY, preset=''),
                                                width=200, height=40, font=(gui.FONT_NAME, 20))
        self._combosButton.grid(row=0, column=2)
        
    def save_preset(self) -> None:
        pass
    
    def change_console(self, console: str) -> None:
        if self._app.startButton.isHidden:
            self._app.startButton.show()
        if self._activeControls:
            self._activeControls.hide()
        if self._presetSelector.isHidden:
            self._presetSelector.show()
        if self._buttonsFrame.isHidden:
            self._buttonsFrame.show()
            
        match console:
            case 'Gameboy':
                self._activeControls = self._gameboyControls
            case 'N64':
                self._activeControls = self._n64Controls
            case 'SNES':
                self._activeControls = self._snesControls
            case 'PC':
                self._activeControls = self._pcControls
            case 'NES':
                self._activeControls = self._nesControls
            case 'Gamecube':
                self._activeControls = self._gamecubeControls
        
        self._presetSelector.set_console(console)
        self._activeControls.show()
    
    def change_preset(self, preset: str) -> None:
        self._activeControls.load_preset(preset)
  
    def get_controls(self) -> dict:
        return self._activeControls.get_inputs()
  
class PresetSelector(wdgts.CustomFrame):
    def __init__(self, master, console: Console, **kwargs):
        super().__init__(master=master, **kwargs)
        self._console = console
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.grid_columnconfigure(index=0, weight=gui.ONLY_THESE_COLUMNS_EXIST)
        self._label = wdgts.CustomLabel(master=self, text="Select Preset", font=(gui.FONT_NAME, 20))
        self._label.grid(row=0, column=0, pady=(0,10))
        
        self._dropdown = wdgts.CustomComboBox(master=self, values=[], 
                                              width=230, height=40, font=(gui.FONT_NAME, 20), 
                                              state='readonly', command=self._console.change_preset)
        self._dropdown.grid(row=1, column=0)
        
    def set_console(self, console: str) -> None:
        values = cfg.CONTROL_SCHEMES[console][PRESETS]
        self._dropdown.fill(values)
    
    def add(self, value: str) -> None:
        self._dropdown.add(value)

class ConsoleSelector(wdgts.CustomFrame):
    def __init__(self, master, console: Console):
        super().__init__(master=master)
        self._console = console
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.grid_columnconfigure(index=0, weight=gui.ONLY_THESE_COLUMNS_EXIST)
        self._label = wdgts.CustomLabel(master=self, text="Select Console", font=(gui.FONT_NAME, 20))
        self._label.grid(row=0, column=0, pady=(0,10))
        
        self._dropdown = wdgts.CustomComboBox(master=self, values=consoles.AVAILABLE_CONSOLES, 
                                              width=230, height=40, font=(gui.FONT_NAME, 20), 
                                              state='readonly', command=self._console.change_console)
        self._dropdown.grid(row=1, column=0)
    
class ControlInputs(wdgts.CustomFrame):
    def __init__(self, master, name: str, **kwargs):
        super().__init__(master, **kwargs)
        self._name = name
        self.grid_columnconfigure(index=(0), weight=gui.ONLY_THESE_COLUMNS_EXIST, uniform=gui.EQUAL_SIZED_COLUMNS)
        
        self._keyLabel = wdgts.CustomLabel(master=self, text=name, width=90,
                                      font=ctk.CTkFont(family=gui.FONT_NAME, size=30, underline=True))
        self._keyLabel.grid(row=0, column=0, padx=(20,0))
        
        self._keyboardEntry = wdgts.NamedEntry(master=self, name="Keyboard", name_placement='side')
        self._keyboardEntry.grid(row=1, column=0, pady=2, sticky='ew')
        
        self._pressEntry = wdgts.NamedEntry(master=self, name="Press Command", name_placement='side')
        self._pressEntry.grid(row=2, column=0, pady=2, sticky='ew')
        
        self._holdEntry = wdgts.NamedEntry(master=self, name="Hold Command", name_placement='side')
        self._holdEntry.grid(row=3, column=0, pady=2, sticky='ew')
    
    def get_controls(self) -> dict:
        key = self._keyboardEntry.get().lower()
        if key in keys.AVAILABLE_KEYS:
            pass
        elif key in keys.NEEDED_MAPPING_TRANSLATIONS:
            key = keys.NEEDED_MAPPING_TRANSLATIONS[key]
        else:
            print(f"{key} is not a valid keyboard key!")
        
        return {
            'action': self._name,
            'key': key,
            'press': self._pressEntry.get(),
            'hold': self._holdEntry.get()
        }
        
    def set_controls(self, controls: dict) -> None:
        self._keyboardEntry.set(controls['key'])
        self._pressEntry.set(controls['press'])
        self._holdEntry.set(controls['hold'])

  


class GameboyControls(wdgts.CustomFrame):
    def __init__(self, console: Console, **kwargs):
        super().__init__(master=console, **kwargs)
        self._console = console
        self.loadedPreset = ''
        
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.grid_columnconfigure((0,1,2,3), weight=gui.ONLY_THESE_COLUMNS_EXIST)
        
        self._AButton = ControlInputs(master=self, name="A Button")
        self._AButton.grid(row=0, column=0, padx=20, pady=20)
        
        self._BButton = ControlInputs(master=self, name="B Button")
        self._BButton.grid(row=0, column=1, padx=20, pady=20)
        
        self._LButton = ControlInputs(master=self, name="L Bumper")
        self._LButton.grid(row=0, column=2, padx=20, pady=20)
        
        self._RButton = ControlInputs(master=self, name="R Bumper")
        self._RButton.grid(row=0, column=3, padx=20, pady=20)
        
        self._DPadLeft = ControlInputs(master=self, name="D-Pad Left")
        self._DPadLeft.grid(row=1, column=0, padx=20, pady=20)
        
        self._DPadUp = ControlInputs(master=self, name="D-Pad Up")
        self._DPadUp.grid(row=1, column=1, padx=20, pady=20)
        
        self._DPadRight = ControlInputs(master=self, name="D-Pad Right")
        self._DPadRight.grid(row=1, column=2, padx=20, pady=20)
        
        self._DPadDown = ControlInputs(master=self, name='D-Pad Down')
        self._DPadDown.grid(row=1, column=3, padx=20, pady=20)
        
        self._selectButton = ControlInputs(master=self, name="Select")
        self._selectButton.grid(row=2, column=1, padx=20, pady=20)
        
        self._startButton = ControlInputs(master=self, name="Start")
        self._startButton.grid(row=2, column=2, padx=20, pady=20)

    def get_inputs(self) -> dict[str, dict]:
        return {
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

    def save_preset(self) -> None:
        presetName = self._presetEntry.get()
        if not presetName:
            return
        self.loadedPreset = presetName
        
        cfg.CONTROL_SCHEMES[GAMEBOY][PRESETS][presetName] = {
            'A': self._AButton.get_controls(),
            'B': self._BButton.get_controls(),
            'L': self._LButton.get_controls(),
            'R': self._RButton.get_controls(),
            'dpad_left': self._DPadLeft.get_controls(),
            'dpad_up': self._DPadUp.get_controls(),
            'dpad_right': self._DPadRight.get_controls(),
            'dpad_down': self._DPadDown.get_controls(),
            'select': self._selectButton.get_controls(),
            'start': self._startButton.get_controls(),
            'combo_buttons': self.loadedCombos
        }
        cfg.update_control_schemes_file()
        self._app.presetSelector.add(presetName)

    def load_preset(self, preset: str) -> None:
        self.loadedPreset = preset
        
        presetControls = cfg.CONTROL_SCHEMES[GAMEBOY][PRESETS][preset]
        self._AButton.set_controls(presetControls['A'])
        self._BButton.set_controls(presetControls['B'])
        self._LButton.set_controls(presetControls['L'])
        self._RButton.set_controls(presetControls['R'])
        self._DPadLeft.set_controls(presetControls['dpad_left'])
        self._DPadUp.set_controls(presetControls['dpad_up'])
        self._DPadRight.set_controls(presetControls['dpad_right'])
        self._DPadDown.set_controls(presetControls['dpad_down'])
        self._selectButton.set_controls(presetControls['select'])
        self._startButton.set_controls(presetControls['start'])

class N64Controls(wdgts.CustomFrame):
    def __init__(self, console: Console, **kwargs):
        super().__init__(master=console, **kwargs)
        
class GamecubeControls(wdgts.CustomFrame):
    def __init__(self, console: Console, **kwargs):
        super().__init__(master=console, **kwargs)

class SuperNintendoControls(wdgts.CustomFrame):
    def __init__(self, console: Console, **kwargs):
        super().__init__(master=console, **kwargs)
  
class NintendoControls(wdgts.CustomFrame):
    def __init__(self, console: Console, **kwargs):
        super().__init__(master=console, **kwargs)

class ComputerControls(wdgts.CustomFrame):
    def __init__(self, console: Console, **kwargs):
        super().__init__(master=console, **kwargs)