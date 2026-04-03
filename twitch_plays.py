import customtkinter as ctk
import widgets as wdgts
import time
from constants import *
from control_schemes import *
from configurations import *

class TwitchPlays(wdgts.CustomFrame):
    def __init__(self, app_root):
        super().__init__(master=app_root)
        self._appRoot = app_root
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.grid_columnconfigure(index=0, weight=gui.ONLY_THESE_COLUMNS_EXIST)
        
        self._selectorsFrame = wdgts.CustomFrame(master=self)
        self._selectorsFrame.grid_columnconfigure(index=(0,1,2), weight=gui.ONLY_THESE_COLUMNS_EXIST,
                                                  uniform=gui.EQUAL_SIZED_COLUMNS)
        self._selectorsFrame.grid(row=0, column=0, sticky='ew', pady=(0,20))
        
        self._consoleSelector = ConsoleSelector(master=self._selectorsFrame, app=self)
        self._consoleSelector.grid(row=0, column=1, sticky='ew')
        
        self.presetSelector = PresetSelector(master=self._selectorsFrame, app=self)
        self.presetSelector.grid(row=0, column=2, sticky='w', padx=20)
        self.presetSelector.hide()
        
        self._controlAssignmentFrame = ControlAssignmentFrame(app=self)
        self._controlAssignmentFrame.grid(row=2, column=0)
        
        self._alertLabel = wdgts.CustomLabel(master=self, text='', text_color='red', font=(gui.FONT_NAME, 20))
        self._alertLabel.grid(row=3, column=0, pady=(5,0))
        
        self._startButton = wdgts.ToggleableButton(master=self, text='Start Playing!', command=self.start_playing,
                                                          width=500, height=50, font=(gui.FONT_NAME,25))
        self._startButton.grid(row=4, column=0, pady=(10,0))
        self._startButton.hide()
        
        self._pauseButton = wdgts.ToggleableButton(master=self, text='Pause Playing...', command=self.stop_playing,
                                                         width=500, height=50, font=(gui.FONT_NAME,25), 
                                                         fg_color='red')
        self._pauseButton.grid(row=4, column=0, pady=(10,0))
        self._pauseButton.hide()
    
    def set_alert(self, message: str, is_persistant: bool = True) -> None:
        self._alertLabel.configure(text=message)
        if not is_persistant:
            time.sleep(2)
            self.clear_alert()
    
    def clear_alert(self) -> None:
        self._alertLabel.configure(text='')
    
    def assign_controls(self) -> None:
        pass
    
    def start_playing(self) -> None:
        # TODO: check that all controls are inputted
        if not self._appRoot.get_channel_name():
            self.set_alert("You need to enter your channel name!")
        else:
            self.clear_alert()
            self._controlAssignmentFrame.save_control_scheme()
            self._pauseButton.show()
            self._startButton.hide()
        
    def stop_playing(self) -> None:
        self._pauseButton.hide()
        self._startButton.show()
    
    def change_console(self, console: str) -> None:
        if self._startButton.isHidden:
            self._startButton.show()
        if self.presetSelector.isHidden:
            self.presetSelector.show()
        self._controlAssignmentFrame.set_console(console)
        
    def change_preset(self, preset: str) -> None:
        self._controlAssignmentFrame.load_preset(preset)


class PresetSelector(wdgts.CustomFrame):
    def __init__(self, master, app: TwitchPlays, **kwargs):
        super().__init__(master=master, **kwargs)
        self._app = app
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.grid_columnconfigure(index=0, weight=gui.ONLY_THESE_COLUMNS_EXIST)
        self._label = wdgts.CustomLabel(master=self, text="Select Preset", font=(gui.FONT_NAME, 20))
        self._label.grid(row=0, column=0, pady=(0,10))
        
        self._dropdown = wdgts.CustomComboBox(master=self, values=[], 
                                              width=230, height=40, font=(gui.FONT_NAME, 20), 
                                              state='readonly', command=self._app.change_preset)
        self._dropdown.grid(row=1, column=0)
        
    def set_console(self, console: str) -> None:
        values = cfg.CONTROL_SCHEMES[console][PRESETS]
        self._dropdown.fill(values)
    
    def add(self, value: str) -> None:
        self._dropdown.add(value)
        

class ConsoleSelector(wdgts.CustomFrame):
    def __init__(self, master, app: TwitchPlays):
        super().__init__(master=master)
        self._app = app
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.grid_columnconfigure(index=0, weight=gui.ONLY_THESE_COLUMNS_EXIST)
        self._label = wdgts.CustomLabel(master=self, text="Select Console", font=(gui.FONT_NAME, 20))
        self._label.grid(row=0, column=0, pady=(0,10))
        
        self._dropdown = wdgts.CustomComboBox(master=self, values=consoles.AVAILABLE_CONSOLES, 
                                              width=230, height=40, font=(gui.FONT_NAME, 20), 
                                              state='readonly', command=self._app.change_console)
        self._dropdown.grid(row=1, column=0)
        

