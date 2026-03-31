import customtkinter as ctk
import widgets as wdgts
import ctypes
import pynput
import time
from constants import *
from keyboard_control import *

class TwitchPlays(wdgts.HideableFrame):
    def __init__(self, master):
        super().__init__(master=master)
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.grid_columnconfigure(0, weight=EQUAL_WEIGHT)
        
        self._consoleSelector = ConsoleSelector(master=self)
        self._consoleSelector.grid(row=0, column=0, pady=(0,20))
        
        self._instructions = ctk.CTkLabel(master=self, text="In the text box, enter the phrase for chat to use for that key", font=(FONT_NAME,20))
        self._instructions.grid(row=1, column=0)
        
        self._controlAssignmentPanel = ControlAssignmentPanel(master=self)
        self._controlAssignmentPanel.grid(row=2, column=0)
        
        self._startPlayingButton = wdgts.ToggleableButton(master=self, text='Start Playing!', command=self.start_playing,
                                                          width=500, height=50, font=(FONT_NAME,25))
        self._startPlayingButton.grid(row=3, column=0, pady=(50,0))
        
        self._stopPlayingButton = wdgts.ToggleableButton(master=self, text='Stop Playing...', command=self.stop_playing,
                                                         width=500, height=50, font=(FONT_NAME,25), fg_color='red')
        self._stopPlayingButton.grid(row=3, column=0, pady=(50,0))
        self._stopPlayingButton.hide()
        
        self._status = ctk.CTkLabel(master=self, text=f"Status: Not Playing", font=(FONT_NAME, 30), text_color='red')
        # self._status.grid(row=4, column=0)
        
    def assign_controls(self) -> None:
        pass
    
    def start_playing(self) -> None:
        self._status.configure(text='Status: Playing!', text_color='green')
        self._stopPlayingButton.show()
        self._startPlayingButton.hide()
        
    def stop_playing(self) -> None:
        self._status.configure(text='Status: Not Playing...', text_color='red')
        self._stopPlayingButton.hide()
        self._startPlayingButton.show()


class ConsoleSelector(wdgts.HideableFrame):
    def __init__(self, master):
        super().__init__(master=master)
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.grid_columnconfigure(index=0, weight=EQUAL_WEIGHT)
        self._label = ctk.CTkLabel(master=self, text="Select Console", font=(FONT_NAME, 20))
        self._label.grid(row=0, column=0, pady=(0,10))
        
        self._dropdown = ctk.CTkComboBox(master=self, values=AVAILABLE_CONSOLES, 
                                         width=230, height=40, font=(FONT_NAME, 20))
        self._dropdown.grid(row=1, column=0)

class ControlAssignmentPanel(wdgts.HideableFrame):
    def __init__(self, master):
        super().__init__(master=master)
        self.configure(fg_color=colors.TWITCH_PURPLE)
        
        self.gameboyControls = GameboyControls(master=self)
        self.gameboyControls.grid(row=0, column=0)

class ControlAssignment(wdgts.HideableFrame):
    def __init__(self, master, action: str, **kwargs):
        super().__init__(master, **kwargs)
        self._action = action
        self.configure(fg_color=colors.TWITCH_PURPLE)
        
        self.grid_columnconfigure(index=(0,1), weight=EQUAL_WEIGHT)
        
        self._keyLabel = ctk.CTkLabel(master=self, text=action, font=(FONT_NAME, 30), width=80)
        self._keyLabel.grid(row=0, column=0, sticky='w', padx=10)
        
        self._entry = wdgts.ClearableEntry(master=self)
        self._entry.grid(row=0, column=1, sticky='e', padx=10)

class GameboyControls(wdgts.HideableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color=colors.TWITCH_PURPLE)
        self.grid_columnconfigure((0,1,2,3), weight=EQUAL_WEIGHT)
        
        self._AButton = wdgts.ControlAssignment(master=self, action="A")
        self._AButton.grid(row=0, column=0, padx=20, pady=20)
        
        self._BButton = wdgts.ControlAssignment(master=self, action="B")
        self._BButton.grid(row=0, column=1, padx=20, pady=20)
        
        self._LButton = wdgts.ControlAssignment(master=self, action="L")
        self._LButton.grid(row=0, column=2, padx=20, pady=20)
        
        self._RButton = wdgts.ControlAssignment(master=self, action="R")
        self._RButton.grid(row=0, column=3, padx=20, pady=20)
        
        self._DPadLeft = wdgts.ControlAssignment(master=self, action="Left")
        self._DPadLeft.grid(row=1, column=0, padx=20, pady=20)
        
        self._DPadUp = wdgts.ControlAssignment(master=self, action="Up")
        self._DPadUp.grid(row=1, column=1, padx=20, pady=20)
        
        self._DPadRight = wdgts.ControlAssignment(master=self, action="Right")
        self._DPadRight.grid(row=1, column=2, padx=20, pady=20)
        
        self._DPadDown = wdgts.ControlAssignment(master=self, action='Down')
        self._DPadDown.grid(row=1, column=3, padx=20, pady=20)
        
        self._selectButton = wdgts.ControlAssignment(master=self, action="Select")
        self._selectButton.grid(row=2, column=1, padx=20, pady=20)
        
        self._startButton =wdgts.ControlAssignment(master=self, action="Start")
        self._startButton.grid(row=2, column=2, padx=20, pady=20)


